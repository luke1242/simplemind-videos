// scenes/partN.json + timing -> parts/partN/ HyperFrames project. usage: node tools/build-part.mjs N
import fs from 'node:fs'; import path from 'node:path'; import { execFileSync } from 'node:child_process';
const N = process.argv[2] || '1';
const D = `parts/part${N}`;
const sc = JSON.parse(fs.readFileSync(`scenes/part${N}.json`, 'utf8')).scenes;
const tm = JSON.parse(fs.readFileSync(`scenes/part${N}.timing.json`, 'utf8'));
for (const d of ['pics', 'fonts', 'audio']) fs.mkdirSync(`${D}/${d}`, { recursive: true });
fs.copyFileSync('assets/vendor/gsap.min.js', `${D}/gsap.min.js`);
fs.copyFileSync('node_modules/@fontsource/nunito/files/nunito-latin-800-normal.woff2', `${D}/fonts/nunito-800.woff2`);
fs.copyFileSync(`audio/padded/part${N}.wav`, `${D}/audio/vo.wav`);
const total = tm.paddedDuration;
const toPad = t => t + tm.pads.filter(p => p[0] < t).reduce((a, p) => a + p[1], 0);
const picFile = id => { // id -> jpg/png scaled to 1920x1080 (lanczos, cover)
  const f = ['jpg', 'png'].map(e => `pictures/${id}.${e}`).find(fs.existsSync);
  const out = `${D}/pics/${id}.jpg`;
  if (f) { if (!fs.existsSync(out)) execFileSync('ffmpeg', ['-v','error','-y','-i',f,'-vf','scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080','-q:v','2',out]); return `pics/${id}.jpg`; }
  return null;
};
const missing = [];
const cueTime = (s, t, word) => {
  const ws = s.narration.split(/\s+/); const w = word.toLowerCase().split(' ');
  let i = ws.findIndex((_, k) => w.every((x, j) => (ws[k + j] || '').toLowerCase().replace(/[^a-z']/g, '') === x));
  if (i < 0) i = 0;
  return toPad(t.rawStart + (i / ws.length) * (t.rawEnd - t.rawStart));
};
const badge = txt => txt.replace(/\*(.+?)\*/g, '<b class="y">$1</b>').replace(/!(.+?)!/g, '<b class="r">$1</b>');
let html = '', js = '', n = 0; const gap = 0.2; // scene crossfade half-width
sc.forEach((s, si) => {
  const t = tm.scenes[si]; const start = t.start, end = t.end;
  // beat start times
  const bs = s.beats; const fixedEnd = bs.filter(b => b.dur).reduce((a, b) => a + b.dur, 0);
  const free = bs.filter(b => !b.dur); const times = new Array(bs.length);
  // cues pin beat starts; others split evenly in the gaps
  let tail = end - fixedEnd;
  const pins = bs.map((b, i) => b.cue ? cueTime(s, t, b.cue) : null);
  let i = 0; let cur = start;
  const segs = []; // [startIdx, endIdx, tStart, tEnd]
  const idxs = bs.map((_, k) => k); const pinIdx = idxs.filter(k => pins[k] !== null);
  let from = 0, tFrom = start;
  for (const pk of [...pinIdx, bs.length]) {
    const tTo = pk === bs.length ? tail : pins[pk];
    const grp = idxs.slice(from, pk); const fx = grp.filter(k => bs[k].dur).reduce((a, k) => a + bs[k].dur, 0);
    const nfree = grp.filter(k => !bs[k].dur).length; let c = tFrom;
    const span = (pk === bs.length ? tail : tTo) - tFrom;
    for (const k of grp) { times[k] = c; c += bs[k].dur || (span - (pk === bs.length ? 0 : fx)) / nfree; }
    from = pk; tFrom = tTo;
  }
  bs.forEach((b, k) => {
    let bst = times[k], ben = k + 1 < bs.length ? times[k + 1] : end;
    if (b.type === 'title') { ben = end; bst = end - b.dur; }
    if (k > 0 && bs[k - 1].type !== 'title' && bs[k-1].type === 'pic' && false) {}
    const first = k === 0, last = k === bs.length - 1;
    let a = bst - (first && s.transition !== 'cut' && si > 0 ? gap : 0), z = ben + (last && si < sc.length - 1 && sc[si + 1].transition !== 'cut' ? gap : 0);
    // title beat: shrink previous beat's end handled by times
    if (si === sc.length - 1 && last) z = Math.min(z, total);
    const id = `b${++n}`; const dur = +(z - a).toFixed(3);
    const pid = b.pic || s.pic; const img = b.type !== 'card' && b.type !== 'title' ? picFile(pid) : null;
    if (b.type !== 'card' && b.type !== 'title' && !img) { missing.push(pid); }
    let inner = '';
    if (b.type === 'card' || (b.type !== 'title' && !img)) {
      inner = `<div class="card"><div class="txt" id="${id}t">${badge(b.type === 'card' ? b.text : (s.narration.split('.')[0]).toUpperCase())}</div></div>`;
      js += `tl.fromTo('#${id}t',{scale:.88,opacity:0},{scale:1,opacity:1,duration:.3,ease:'back.out(1.4)'},${a.toFixed(3)});`;
    } else if (b.type === 'title') {
      inner = `<div class="card"><div class="pill" id="${id}p">LESSON</div><div class="txt big" id="${id}t">ONE OF THE MOST <b class="o">USEFUL</b><br>LESSONS I LEARNED</div></div>`;
      js += `tl.fromTo('#${id}p',{y:-30,opacity:0},{y:0,opacity:1,duration:.4,ease:'back.out(1.4)'},${a.toFixed(3)});tl.fromTo('#${id}t',{scale:.9,opacity:0},{scale:1,opacity:1,duration:.5,ease:'back.out(1.2)'},${(a+.2).toFixed(3)});`;
    } else {
      const ov = (s.overlays || []).map((o, oi) => `<div class="ov" id="${id}o${oi}" style="left:${o.x*100}%;top:${o.y*100}%;width:${o.w*100}%">${o.text}</div>`).join('');
      const crop = b.type === 'crop';
      inner = `<div class="pic" id="${id}c" style="transform-origin:${(crop ? b.fx : .5) * 100}% ${(crop ? b.fy : .5) * 100}%"><img src="${img}">${ov}</div>`;
      let f = 1, tt = 1, ox = 0;
      if (crop) { f = b.s; tt = b.s * 1.06; const cl = (v, lo, hi) => Math.min(hi, Math.max(lo, v)); const px = (S) => cl((.5 - b.fx) * 1920, (1 - b.fx) * 1920 * (1 - S), b.fx * 1920 * (S - 1)), py = (S) => cl((.5 - b.fy) * 1080, (1 - b.fy) * 1080 * (1 - S), b.fy * 1080 * (S - 1)); js += `tl.fromTo('#${id}c',{scale:${f},x:${px(f).toFixed(0)},y:${py(f).toFixed(0)}},{scale:${tt.toFixed(3)},x:${px(tt).toFixed(0)},y:${py(tt).toFixed(0)},duration:${dur},ease:'sine.inOut'},${a.toFixed(3)});`; f = tt; } else { const c = b.camera || s.camera; if (c === 'zoom-in') tt = 1.06; else if (c === 'zoom-out') { f = 1.06; tt = 1; } else if (c.startsWith('pan')) { f = tt = 1.04; ox = c === 'pan-right' ? [-30, 30] : [30, -30]; } }
      if (ox) js += `tl.fromTo('#${id}c',{scale:${f},x:${ox[0]}},{scale:${tt},x:${ox[1]},duration:${dur},ease:'sine.inOut'},${a.toFixed(3)});`;
      else if (f !== tt && !crop) js += `tl.fromTo('#${id}c',{scale:${f}},{scale:${tt},duration:${dur},ease:'sine.inOut'},${a.toFixed(3)});`;
      (s.overlays || []).forEach((o, oi) => { const ct = Math.max(cueTime(s, t, o.cue), a); if (ct < z) js += `tl.fromTo('#${id}o${oi}',{opacity:0,scale:.9},{opacity:1,scale:1,duration:.4,ease:'back.out(1.4)'},${ct.toFixed(3)});`; });
    }
    // 0.4s crossfade between scenes / 0.3s swap fade
    const fadeIn = first && s.transition !== 'cut' && si > 0 ? 0.4 : (b.cue ? 0.3 : 0);
    if (fadeIn) js += `tl.fromTo('#${id}',{opacity:0},{opacity:1,duration:${fadeIn},ease:'none'},${a.toFixed(3)});`;
    html += `<div id="${id}" class="clip beat" data-start="${a.toFixed(3)}" data-duration="${dur}" data-track-index="${n % 2}" style="z-index:${n}">${inner}</div>\n`;
  });
});
const page = `<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=1920, height=1080"><title>Part ${N}</title>
<script src="gsap.min.js"></script>
<style>
@font-face{font-family:'Nunito';font-weight:800;src:url(fonts/nunito-800.woff2) format('woff2')}
html,body{margin:0;background:#FAF7F0}
#root{position:relative;width:100%;height:100%;overflow:hidden;background:#FAF7F0;font-family:'Nunito',sans-serif;font-weight:800;color:#1A1A1A}
.beat{position:absolute;inset:0;overflow:hidden}
.pic{position:absolute;inset:0}.pic img{width:100%;height:100%;display:block}
.card{position:absolute;inset:0;background:#FAF7F0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px}
.txt{font-size:150px;line-height:1.25;text-align:center;max-width:1700px;color:#1A1A1A}
.txt.big{font-size:120px}
.txt b{display:inline-block;padding:0 28px;border:8px solid #1A1A1A;border-radius:28px;font-weight:800;line-height:1.15;margin:6px 0}
.txt b.y{background:#F2C230}.txt b.r{background:#D64545;color:#fff}.txt b.o{background:#F2A65A}
.pill{background:#2F6B2F;color:#fff;font-size:64px;letter-spacing:6px;padding:10px 56px;border:6px solid #1A1A1A;border-radius:60px}
.ov{position:absolute;transform:translate(-50%,-50%);text-align:center;font-size:62px;line-height:1.15;color:#1A1A1A;opacity:0}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-width="1920" data-height="1080" data-duration="${total.toFixed(3)}">
${html}<audio id="vo" src="audio/vo.wav" data-start="0" data-duration="${total.toFixed(3)}" data-track-index="5"></audio>
</div>
<script>const tl=gsap.timeline({paused:true});${js}window.__timelines["main"]=tl;</script></body></html>`;
fs.writeFileSync(`${D}/index.html`, page);
console.log(`built ${D} (${n} beats, ${total.toFixed(1)}s)` + (missing.length ? ' MISSING: ' + [...new Set(missing)].join(',') : ''));
