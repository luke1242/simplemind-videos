// Pads pauses (A11), estimates scene times, writes audio/padded/partN.wav + scenes/partN.timing.json
// usage: node tools/timing.mjs N [shortPad=0.25]
import { execFileSync, spawnSync } from 'node:child_process';
import fs from 'node:fs';
const N = process.argv[2] || '1';
const SHORT = parseFloat(process.argv[3] || '0.25'), BEAT = 0.9, SCENE = 0.4;
const src = `audio/part${N}.mp3`, out = `audio/padded/part${N}.wav`;
const scenes = JSON.parse(fs.readFileSync(`scenes/part${N}.json`, 'utf8')).scenes;
const rawDur = parseFloat(execFileSync('ffprobe', ['-v','error','-show_entries','format=duration','-of','csv=p=0',src]).toString());
const sd = spawnSync('ffmpeg', ['-i', src, '-af', 'silencedetect=noise=-35dB:d=0.25', '-f', 'null', '-']).stderr.toString();
const sil = []; let cur = null;
for (const l of sd.split('\n')) {
  let m = l.match(/silence_start: ([\d.]+)/); if (m) cur = { s: +m[1] };
  m = l.match(/silence_end: ([\d.]+) \| silence_duration: ([\d.]+)/); if (m && cur) { cur.e = +m[1]; cur.d = +m[2]; sil.push(cur); cur = null; }
}
sil.forEach(x => { x.mid = (x.s + x.e) / 2; x.pad = x.d < 0.6 ? SHORT : BEAT; });
// estimate scene boundaries by word share
const words = scenes.map(s => s.narration.split(/\s+/).length), tot = words.reduce((a,b)=>a+b,0);
let acc = 0; const bounds = [];
for (let i = 0; i < scenes.length - 1; i++) {
  acc += words[i]; const est = acc / tot * rawDur;
  let best = null;
  for (const x of sil) if (Math.abs(x.mid - est) <= 1.5 && (!best || Math.abs(x.mid - est) < Math.abs(best.mid - est))) best = x;
  if (best) { best.scene = true; best.hold = scenes[i].holdAfter || 0; bounds.push({ sil: best }); } else bounds.push({ raw: est });
}
for (const x of sil) { if (x.scene) x.pad += SCENE; if (x.hold) x.pad = Math.max(x.pad, x.hold + 0.4 - x.d); }
// raw -> padded map
const toPad = t => t + sil.filter(x => x.mid < t).reduce((a, x) => a + x.pad, 0);
const padDur = rawDur + sil.reduce((a, x) => a + x.pad, 0);
const bPad = bounds.map(b => b.sil ? toPad(b.sil.s) + (b.sil.hold ? b.sil.d + b.sil.pad - 0.3 : (b.sil.d + b.sil.pad) / 2) : toPad(b.raw));
// scene raw ranges for cue estimation
const rawB = [0, ...bounds.map(b => b.sil ? b.sil.mid : b.raw), rawDur];
const starts = [0, ...bPad], ends = [...bPad, padDur];
const timing = scenes.map((s, i) => ({ id: s.id, start: +starts[i].toFixed(2), end: +ends[i].toFixed(2), rawStart: +rawB[i].toFixed(2), rawEnd: +rawB[i+1].toFixed(2), words: words[i] }));
// build padded wav
const parts = []; let prev = 0, k = 0, fc = [];
const cuts = [...sil.map(x => ({ t: x.mid, pad: x.pad })), { t: rawDur, pad: 0 }];
for (const c of cuts) {
  fc.push(`[0:a]atrim=${prev}:${c.t},asetpts=PTS-STARTPTS[a${k}]`); parts.push(`[a${k}]`); k++;
  if (c.pad > 0) { fc.push(`anullsrc=r=44100:cl=mono,atrim=0:${c.pad}[s${k}]`); parts.push(`[s${k}]`); k++; }
  prev = c.t;
}
const filter = fc.join(';') + ';' + parts.join('') + `concat=n=${parts.length}:v=0:a=1[o]`;
execFileSync('ffmpeg', ['-v','error','-y','-i', src, '-filter_complex', filter, '-map', '[o]', '-ar', '44100', '-ac', '1', out]);
const real = parseFloat(execFileSync('ffprobe', ['-v','error','-show_entries','format=duration','-of','csv=p=0',out]).toString());
timing[timing.length-1].end = +real.toFixed(2);
fs.writeFileSync(`scenes/part${N}.timing.json`, JSON.stringify({ pads: sil.map(x => [+x.mid.toFixed(3), x.pad]), rawDuration: rawDur, paddedDuration: real, scenes: timing }, null, 1));
console.log(`part${N}: ${rawDur.toFixed(1)}s -> ${real.toFixed(1)}s (pauses: ${sil.length})`);
for (const t of timing) console.log(t.id, t.start.toFixed(2), t.end.toFixed(2), (t.end - t.start).toFixed(1) + 's');
