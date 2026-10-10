// Usage: node tools/build-part.mjs N   -> parts/partN/ (HyperFrames project built from scenes/partN.json + timing)
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
const N = process.argv[2] || '1';
const spec = JSON.parse(fs.readFileSync(`scenes/part${N}.json`, 'utf8'));
const timing = JSON.parse(fs.readFileSync(`scenes/part${N}.timing.json`, 'utf8'));
const out = `parts/part${N}`;
fs.rmSync(out, { recursive: true, force: true });
for (const d of ['pictures', 'fonts', 'vendor', 'audio', 'broll']) fs.mkdirSync(`${out}/assets/${d}`, { recursive: true });
fs.copyFileSync('assets/vendor/gsap.min.js', `${out}/assets/vendor/gsap.min.js`);
for (const f of ['montserrat-latin-800-normal.woff2', 'bebas-neue-latin-400-normal.woff2']) fs.copyFileSync(`assets/fonts/${f}`, `${out}/assets/fonts/${f}`);
fs.copyFileSync(timing.audio, `${out}/assets/audio/voice.wav`);
fs.writeFileSync(`${out}/hyperframes.json`, JSON.stringify({ $schema: 'https://hyperframes.heygen.com/schema/hyperframes.json', paths: { blocks: 'compositions', components: 'compositions/components', assets: 'assets' } }, null, 2));

const D = timing.duration;
const FADE = 0.4, PAD = FADE / 2;
const C = { paper: '#FAF7F0', ink: '#1A1A1A', orange: '#F2A65A', green: '#2F6B2F', mustard: '#F2C230', red: '#D64545' };
const t3 = (x) => +x.toFixed(3);
let html = '', js = '';
const need = new Set();
spec.scenes.forEach((s, i) => {
  const tm = timing.scenes[i];
  const start = tm.start, end = tm.end, len = end - start;
  const cut = s.transition === 'cut' || i === 0;
  const cs = cut ? start : start - PAD, ce = i === spec.scenes.length - 1 ? end : end + PAD;
  const id = s.id;
  need.add(s.picture); if (s.pictureB) need.add(s.pictureB);
  let inner = `<img class="pic" id="${id}-a" src="assets/pictures/${s.picture}.svg" alt="">`;
  if (s.pictureB) inner += `<img class="pic" id="${id}-b" src="assets/pictures/${s.pictureB}.svg" alt="" style="opacity:0">`;
  (s.overlays || []).forEach((o, oi) => { inner += overlayHtml(o, `${id}-o${oi}`); });
  html += `<div id="${id}" class="clip scene" data-start="${t3(cs)}" data-duration="${t3(ce - cs)}" data-track-index="${1 + (i % 2)}" style="z-index:${10 + i}"><div class="fade" id="${id}-f"><div class="cam" id="${id}-c">${inner}</div></div></div>\n`;
  // camera
  const d = ce - cs, mv = s.camera;
  const g = `#${id}-c`;
  if (mv === 'zoom-in') js += `tl.fromTo("${g}",{scale:1},{scale:1.06,duration:${t3(d)},ease:"sine.inOut"},${t3(cs)});\n`;
  else if (mv === 'zoom-out') js += `tl.fromTo("${g}",{scale:1.06},{scale:1,duration:${t3(d)},ease:"sine.inOut"},${t3(cs)});\n`;
  else if (mv === 'pan-right') js += `tl.fromTo("${g}",{scale:1.04,x:30},{x:-30,duration:${t3(d)},ease:"sine.inOut"},${t3(cs)});\n`;
  else if (mv === 'pan-left') js += `tl.fromTo("${g}",{scale:1.04,x:-30},{x:30,duration:${t3(d)},ease:"sine.inOut"},${t3(cs)});\n`;
  if (!cut) js += `tl.fromTo("#${id}-f",{opacity:0},{opacity:1,duration:${FADE},ease:"none"},${t3(cs)});\n`;
  if (s.pictureB) js += `tl.fromTo("#${id}-b",{opacity:0},{opacity:1,duration:0.3,ease:"none"},${t3(tm.cues.swap)});\n`;
  // overlays
  (s.overlays || []).forEach((o, oi) => {
    const oid = `#${id}-o${oi}`, at = tm.cues[`o${oi}`];
    if (o.type === 'bubbles') o.items.forEach((_, k) => (js += `tl.fromTo("${oid}-${k}",{scale:0.2,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"back.out(1.4)"},${t3(at + k * (o.gap || 0.4))});\n`));
    else js += `tl.fromTo("${oid}",{opacity:0},{opacity:1,duration:0.3,ease:"none"},${t3(at)});\n`;
  });
  // b-roll (own clip, muted, graded)
  if (s.broll && fs.existsSync(`broll/${id}.mp4`)) {
    const bl = s.broll.len, bs = s.broll.from === 'end' ? end - bl : start;
    const bsT = Math.max(start, bs), bd = Math.min(bl, len) + 0;
    const dst = `${out}/assets/broll/${id}.mp4`;
    execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-ss', '1.5', '-i', `broll/${id}.mp4`, '-t', String(Math.ceil(bd + 1)), '-an', '-vf', 'eq=saturation=0.85:contrast=0.95,colorbalance=rs=0.05:gs=0.01:bs=-0.05:rm=0.04:bm=-0.04,fps=30', '-c:v', 'libx264', '-crf', '20', '-preset', 'fast', '-pix_fmt', 'yuv420p', dst]);
    html += `<video id="${id}-br" class="clip broll" src="assets/broll/${id}.mp4" data-start="${t3(bsT)}" data-duration="${t3(bd)}" data-track-index="3" muted playsinline style="z-index:${10 + i}"></video>\n`;
    js += `tl.fromTo("#${id}-br",{opacity:0,scale:1},{opacity:1,scale:1.04,duration:${FADE},ease:"none"},${t3(bsT)});\n`;
    js += `tl.to("#${id}-br",{scale:1.08,duration:${t3(bd - FADE)},ease:"sine.inOut"},${t3(bsT + FADE)});\n`;
    js += `tl.to("#${id}-br",{opacity:0,duration:${FADE},ease:"none"},${t3(bsT + bd - FADE)});\n`;
  }
});
for (const p of need) fs.copyFileSync(`assets/pictures/${p}.svg`, `${out}/assets/pictures/${p}.svg`);

function overlayHtml(o, oid) {
  if (o.type === 'titlecard') {
    return `<div id="${oid}" class="card" style="opacity:0"><div class="pill">LESSON</div><div class="h1">ONE OF THE MOST <span style="color:${C.orange}">USEFUL</span></div><div class="h1">LESSONS I LEARNED</div></div>`;
  }
  if (o.type === 'text') {
    const lines = o.lines.map((l) => `<div style="color:${l.c === 'orange' ? C.orange : l.c === 'green' ? C.green : C.ink}">${l.t}</div>`).join('');
    return `<div id="${oid}" class="txt" style="opacity:0;left:${o.x - o.w / 2}px;top:${o.y - 150}px;width:${o.w}px;font-size:${o.size}px">${lines}</div>`;
  }
  if (o.type === 'bubbles') {
    return o.items.map((b, k) => {
      const icon = b.icon === 'laugh'
        ? `<circle cx="100" cy="82" r="42" fill="${C.mustard}" stroke="${C.ink}" stroke-width="4.5"/><path d="M78 72 q8 -10 16 0 M106 72 q8 -10 16 0" stroke="${C.ink}" stroke-width="4.5" fill="none" stroke-linecap="round"/><path d="M76 92 Q100 126 124 92Z" fill="${C.ink}"/>`
        : `<text x="100" y="${b.icon === '!' ? 112 : 112}" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="96" fill="${b.icon === '!' ? C.red : C.ink}">${b.icon}</text>`;
      return `<svg id="${oid}-${k}" class="bub" style="opacity:0;left:${b.x - 110}px;top:${b.y - 100}px" width="220" height="250" viewBox="0 0 220 250"><g transform="translate(10 0)"><ellipse cx="100" cy="82" rx="96" ry="76" fill="${C.paper}" stroke="${C.ink}" stroke-width="4.5"/>${icon}<circle cx="96" cy="184" r="14" fill="${C.paper}" stroke="${C.ink}" stroke-width="4.5"/><circle cx="92" cy="220" r="9" fill="${C.paper}" stroke="${C.ink}" stroke-width="4.5"/></g></svg>`;
    }).join('');
  }
  return '';
}

const page = `<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=1920, height=1080"><title>SimpleMindMotivation Part ${N}</title>
<script src="assets/vendor/gsap.min.js"></script>
<style>
@font-face{font-family:"Montserrat";font-weight:800;src:url("assets/fonts/montserrat-latin-800-normal.woff2") format("woff2")}
@font-face{font-family:"Bebas Neue";font-weight:400;src:url("assets/fonts/bebas-neue-latin-400-normal.woff2") format("woff2")}
body{margin:0;background:${C.paper}}
#root{position:relative;width:100%;height:100%;overflow:hidden;background:${C.paper}}
.clip{position:absolute;inset:0}
.fade,.cam{position:absolute;inset:0;transform-origin:50% 50%}
.pic{position:absolute;inset:0;width:100%;height:100%;display:block}
.broll{width:100%;height:100%;object-fit:cover;transform-origin:50% 50%}
.card{position:absolute;inset:0;background:${C.paper};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px;font-family:"Montserrat"}
.pill{background:${C.green};color:#fff;font-weight:800;font-size:50px;letter-spacing:4px;padding:10px 46px;border-radius:60px;margin-bottom:22px}
.h1{font-weight:800;font-size:112px;line-height:1.05;color:${C.ink};text-align:center}
.txt{position:absolute;font-family:"Montserrat";font-weight:800;text-align:center;line-height:1.18}
.bub{position:absolute;transform-origin:50% 90%;overflow:visible}
</style></head><body>
<div id="root" data-composition-id="part${N}" data-start="0" data-width="1920" data-height="1080" data-duration="${t3(D)}">
<audio id="voice" src="assets/audio/voice.wav" data-start="0" data-duration="${t3(D)}" data-track-index="0"></audio>
${html}</div>
<script>
const tl = gsap.timeline({ paused: true });
${js}window.__timelines["part${N}"] = tl;
</script></body></html>`;
fs.writeFileSync(`${out}/index.html`, page);
console.log(`built ${out}/index.html  (${spec.scenes.length} scenes, ${D.toFixed(1)}s)`);
