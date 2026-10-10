// Usage: node tools/timing.mjs N
// 1) lengthens pauses in audio/partN.mp3 -> audio/padded/partN.wav (speech is never stretched)
// 2) aligns scene narration to the word timestamps and writes scenes/partN.timing.json (padded times)
import fs from 'node:fs';
import { execFileSync, spawnSync } from 'node:child_process';

const N = process.argv[2] || '1';
const SHORT_PAD = Number(process.env.SHORT_PAD || 0.25);
const BEAT_PAD = 0.9, SCENE_PAD = 0.4;
const spec = JSON.parse(fs.readFileSync(`scenes/part${N}.json`, 'utf8'));
const rawAudio = `audio/part${N}.mp3`;
const outAudio = `audio/padded/part${N}.wav`;
const tpath = `scenes/part${N}.transcript.json`;

if (!fs.existsSync(tpath)) {
  fs.mkdirSync('scenes/_tr', { recursive: true });
  const out = execFileSync('npx', ['hyperframes', 'transcribe', rawAudio, '--dir', 'scenes/_tr', '--json'], { encoding: 'utf8', maxBuffer: 1 << 28 });
  const line = out.trim().split('\n').filter((l) => l.startsWith('{"ok"')).pop();
  fs.copyFileSync(JSON.parse(line).transcriptPath, tpath);
  fs.rmSync('scenes/_tr', { recursive: true, force: true });
}
const words = JSON.parse(fs.readFileSync(tpath, 'utf8'));
const norm = (w) => w.toLowerCase().replace(/[^a-z0-9]/g, '');
const rawDur = Number(execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', rawAudio], { encoding: 'utf8' }));

// ---- align scene tokens to transcript words (LCS) ----
const sceneTok = spec.scenes.map((s) => s.narration.split(/\s+/).map(norm).filter(Boolean));
const flat = sceneTok.flatMap((t, si) => t.map((w, wi) => ({ w, si, wi })));
const tw = words.map((x) => norm(x.text));
const n = flat.length, m = tw.length;
const dp = Array.from({ length: n + 1 }, () => new Int16Array(m + 1));
for (let i = n - 1; i >= 0; i--) for (let j = m - 1; j >= 0; j--)
  dp[i][j] = flat[i].w === tw[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
const map = new Array(n).fill(-1);
for (let i = 0, j = 0; i < n && j < m;) {
  if (flat[i].w === tw[j]) { map[i] = j; i++; j++; } else if (dp[i + 1][j] >= dp[i][j + 1]) i++; else j++;
}
console.log(`aligned ${map.filter((x) => x >= 0).length}/${n} script words (${m} spoken)`);
const idxOf = (si, wi) => { // nearest aligned transcript index for scene si token wi
  let base = flat.findIndex((f) => f.si === si && f.wi === 0);
  for (let d = 0; d < 40; d++) for (const k of [wi + d, wi - d]) {
    const g = base + k; if (k >= 0 && k < sceneTok[si].length && map[g] >= 0) return map[g];
  }
  return -1;
};
const sceneWords = spec.scenes.map((_, si) => {
  const a = idxOf(si, 0), b = idxOf(si, sceneTok[si].length - 1);
  return { a, b };
});
function cueIdx(si, phrase) {
  const p = phrase.split(/\s+/).map(norm);
  const t = sceneTok[si];
  for (let i = 0; i + p.length <= t.length; i++) if (p.every((x, k) => t[i + k] === x)) return idxOf(si, i);
  throw new Error(`cue "${phrase}" not found in ${spec.scenes[si].id}`);
}

// ---- pauses ----
const log = spawnSync('ffmpeg', ['-hide_banner', '-i', rawAudio, '-af', 'silencedetect=noise=-35dB:d=0.25', '-f', 'null', '-'], { encoding: 'utf8' }).stderr;
const starts = [...log.matchAll(/silence_start: ([\d.]+)/g)].map((x) => +x[1]);
const ends = [...log.matchAll(/silence_end: ([\d.]+)/g)].map((x) => +x[1]);
let pauses = starts.map((s, i) => ({ s, e: ends[i] ?? rawDur })).filter((p) => p.s > 0.1 && p.e < rawDur - 0.1);
for (const p of pauses) { p.dur = p.e - p.s; p.mid = (p.s + p.e) / 2; p.add = p.dur < 0.6 ? SHORT_PAD : BEAT_PAD; }

// scene boundaries -> pause (or synthetic cut)
const bounds = []; // between scene i and i+1
for (let i = 0; i < spec.scenes.length - 1; i++) {
  const endT = words[sceneWords[i].b].end, startT = words[sceneWords[i + 1].a].start;
  const mid = (endT + startT) / 2;
  let p = pauses.find((q) => q.s <= mid + 0.05 && q.e >= mid - 0.05);
  if (!p) { p = { s: endT, e: startT, dur: startT - endT, mid, add: SHORT_PAD, synthetic: true }; pauses.push(p); }
  p.add += SCENE_PAD + (spec.scenes[i].holdAfter || 0);
  p.boundary = i; p.hold = spec.scenes[i].holdAfter || 0;
  bounds.push(p);
}
// big reveals: >= 2.0s of silence after the scene
spec.scenes.forEach((s, i) => {
  if (!s.revealAfter || i >= bounds.length) return;
  const p = bounds[i]; const total = p.dur + p.add; if (total < 2.0) p.add += 2.0 - total;
});
pauses.sort((a, b) => a.mid - b.mid);

// ---- build padded audio ----
const info = execFileSync('ffprobe', ['-v', 'error', '-select_streams', 'a:0', '-show_entries', 'stream=sample_rate,channels', '-of', 'csv=p=0', rawAudio], { encoding: 'utf8' }).trim().split(',');
const sr = info[0], ch = Number(info[1]) === 1 ? 'mono' : 'stereo';
let cur = 0, shift = 0, parts = [], filt = [], k = 0;
const shifts = []; // [rawMid, cumulative shift after]
for (const p of pauses) {
  filt.push(`[0:a]atrim=${cur.toFixed(4)}:${p.mid.toFixed(4)},asetpts=PTS-STARTPTS[a${k}]`);
  filt.push(`anullsrc=r=${sr}:cl=${ch},atrim=0:${p.add.toFixed(4)},asetpts=PTS-STARTPTS[a${k + 1}]`);
  parts.push(`[a${k}]`, `[a${k + 1}]`); k += 2; cur = p.mid;
  p.padStart = p.mid + shift; shift += p.add; p.shiftAfter = shift; shifts.push(p);
}
filt.push(`[0:a]atrim=${cur.toFixed(4)},asetpts=PTS-STARTPTS[a${k}]`); parts.push(`[a${k}]`);
filt.push(`${parts.join('')}concat=n=${parts.length}:v=0:a=1[out]`);
fs.writeFileSync('scenes/_pad.filter', filt.join(';\n'));
execFileSync('ffmpeg', ['-y', '-hide_banner', '-loglevel', 'error', '-i', rawAudio, '-filter_complex_script', 'scenes/_pad.filter', '-map', '[out]', '-ar', sr, outAudio]);
fs.rmSync('scenes/_pad.filter');
const padDur = Number(execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', outAudio], { encoding: 'utf8' }));

const toPad = (t) => { let sh = 0; for (const p of shifts) if (t >= p.mid) sh = p.shiftAfter; else break; return t + sh; };
const T = (idx, edge) => +toPad(words[idx][edge]).toFixed(3);

// ---- scene times ----
const scenes = spec.scenes.map((s, i) => {
  const first = T(sceneWords[i].a, 'start'), last = T(sceneWords[i].b, 'end');
  return { id: s.id, first, last };
});
const tl_bounds = bounds.map((p) => +(p.hold ? p.padStart + p.add - 0.6 : p.padStart + p.add / 2).toFixed(3));
const out = spec.scenes.map((s, i) => {
  const start = i === 0 ? 0 : tl_bounds[i - 1];
  const end = i === spec.scenes.length - 1 ? +(padDur + (s.holdAfter || 0)).toFixed(3) : tl_bounds[i];
  const cues = {};
  if (s.swapAt) cues.swap = T(cueIdx(i, s.swapAt), 'start');
  (s.overlays || []).forEach((o, oi) => {
    if (o.at && o.at !== 'end') cues[`o${oi}`] = T(cueIdx(i, o.at), 'start');
    if (o.at === 'end') cues[`o${oi}`] = scenes[i].last + 0.15;
  });
  return { id: s.id, start, end: +end.toFixed(3), speechStart: scenes[i].first, speechEnd: scenes[i].last, cues };
});
const totalEnd = out[out.length - 1].end;
fs.writeFileSync(`scenes/part${N}.timing.json`, JSON.stringify({ part: +N, audio: outAudio, duration: +Math.max(padDur, totalEnd).toFixed(3), rawDuration: +rawDur.toFixed(3), scenes: out }, null, 2));
const f = (x) => `${Math.floor(x / 60)}:${(x % 60).toFixed(1).padStart(4, '0')}`;
console.log(`part ${N}: raw ${f(rawDur)} -> padded ${f(padDur)} (${pauses.length} pauses lengthened)`);
console.log('scene  start   end     len');
for (const o of out) console.log(`${o.id}   ${f(o.start)}  ${f(o.end)}  ${(o.end - o.start).toFixed(1)}s`);
