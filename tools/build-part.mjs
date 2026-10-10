// scenes JSON + word timing -> HyperFrames project in parts/partN/   usage: node tools/build-part.mjs N
import fs from "node:fs"; import path from "node:path";
const N = process.argv[2]; const R = (p) => JSON.parse(fs.readFileSync(p, "utf8"));
const cfg = R(`scenes/part${N}.resolved.json`), tim = R(`scenes/part${N}.timing.json`);
const out = `parts/part${N}`; fs.mkdirSync(`${out}/assets/pictures`, { recursive: true }); fs.mkdirSync(`${out}/assets/fonts`, { recursive: true });
const dur = tim.duration, XF = 0.4, f3 = (x) => +x.toFixed(3);
const INK = "#1A1A1A", PAPER = "#FAF7F0", YEL = "#F2C230", RED = "#D64545", ORG = "#F2A65A", GREEN = "#2F6B2F";
const tl = []; const html = []; const warn = []; const sfx = [];
const used = new Set();
const pic = (n) => { used.add(n); return `assets/pictures/${n}.jpg`; };
const findWord = (t, w, occ = 1) => { let c = 0; for (const x of t.words) if (x.w === w && ++c === occ) return x; throw new Error("word not found: " + w); };

const pieSvg = (cx, cy, r, pct) => {
  const a = (pct / 100) * 2 * Math.PI, x = cx + r * Math.sin(a), y = cy - r * Math.cos(a);
  const slice = pct >= 100 ? `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${ORG}" stroke="${INK}" stroke-width="9"/>` : `<path d="M${cx} ${cy} L${cx} ${cy - r} A${r} ${r} 0 ${a > Math.PI ? 1 : 0} 1 ${f3(x)} ${f3(y)} Z" fill="${ORG}" stroke="${INK}" stroke-width="9" stroke-linejoin="round"/>`;
  return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="#E6E1D6" stroke="${INK}" stroke-width="9"/>${slice}`;
};
const svgWrap = (inner) => `<svg viewBox="0 0 1920 1080" width="1920" height="1080" style="position:absolute;inset:0">${inner}</svg>`;
function scaleSvg(labels) {
  const c = Math.cos(12 * Math.PI / 180), sn = Math.sin(12 * Math.PI / 180), px = 960, py = 270;
  const L = [px - 500 * c, py + 500 * sn], Rr = [px + 500 * c, py - 500 * sn];
  const pan = (p, fill) => `<line x1="${f3(p[0])}" y1="${f3(p[1])}" x2="${f3(p[0] - 140)}" y2="${f3(p[1] + 300)}" stroke="${INK}" stroke-width="7"/><line x1="${f3(p[0])}" y1="${f3(p[1])}" x2="${f3(p[0] + 140)}" y2="${f3(p[1] + 300)}" stroke="${INK}" stroke-width="7"/><path d="M${f3(p[0] - 160)} ${f3(p[1] + 300)} H${f3(p[0] + 160)} Q${f3(p[0] + 160)} ${f3(p[1] + 370)} ${f3(p[0])} ${f3(p[1] + 370)} Q${f3(p[0] - 160)} ${f3(p[1] + 370)} ${f3(p[0] - 160)} ${f3(p[1] + 300)} Z" fill="${fill}" stroke="${INK}" stroke-width="8" stroke-linejoin="round"/>`;
  const blk = (x, y, w, h) => `<rect x="${f3(x)}" y="${f3(y)}" width="${w}" height="${h}" rx="12" fill="#2B2B2B" stroke="${INK}" stroke-width="7"/>`;
  let g = `<path d="M700 930 L760 860 H1160 L1220 930 Z" fill="#E6E1D6" stroke="${INK}" stroke-width="9" stroke-linejoin="round"/><line x1="960" y1="270" x2="960" y2="860" stroke="${INK}" stroke-width="16" stroke-linecap="round"/>`;
  g += `<line x1="${f3(L[0])}" y1="${f3(L[1])}" x2="${f3(Rr[0])}" y2="${f3(Rr[1])}" stroke="${INK}" stroke-width="18" stroke-linecap="round"/><circle cx="960" cy="270" r="28" fill="${YEL}" stroke="${INK}" stroke-width="8"/>`;
  g += pan(L, ORG) + pan(Rr, "#9CC08B") + blk(L[0] - 100, L[1] + 220, 200, 80) + blk(L[0] - 65, L[1] + 140, 130, 80);
  g += `<circle cx="${f3(Rr[0])}" cy="${f3(Rr[1] + 270)}" r="30" fill="#F7C4AE" stroke="${INK}" stroke-width="7"/>`;
  return svgWrap(g);
}
function diagramHtml(d) {
  if (d.kind === "pie") return `<div class="fill diag">${svgWrap(pieSvg(960, 440, 310, d.pct))}<div class="dlabel"><span>${d.label}</span><span class="badge ${d.badge}">${d.value}</span></div></div>`;
  if (d.kind === "card") return `<div class="fill diag cardc"><div class="cardtxt">${d.parts.map((p) => `<div class="ln">${p.badge ? `<span class="badge ${p.badge}">${p.t}</span>` : p.t}</div>`).join("")}</div></div>`;
  if (d.kind === "stepPie") return `<div class="fill diag">${svgWrap(pieSvg(640, 700, 250, d.pct))}<div class="spillrow"><div class="pill">${d.step}</div></div><div class="stitle">${d.title}</div><div class="bigval"><span class="badge ${d.badge}">${d.value}</span></div></div>`;
  if (d.kind === "scale") return `<div class="fill diag">${scaleSvg()}${d.labels ? `<div class="sclab" style="left:${471 - 250}px;top:790px"><span class="badge red">EXPECTED</span></div><div class="sclab" style="left:${1449 - 250}px;top:580px"><span class="badge yellow">REALITY</span></div>` : ""}</div>`;
  throw new Error("diagram " + d.kind);
}
const ICONS = {
  sheet: `<rect x="26" y="14" width="48" height="72" rx="5" fill="#fff" stroke="${INK}" stroke-width="5"/><path d="M36 34H64M36 48H64M36 62H56" stroke="${INK}" stroke-width="5" stroke-linecap="round"/>`,
  hand: `<g fill="#F7C4AE" stroke="${INK}" stroke-width="4" stroke-linejoin="round"><rect x="30" y="50" width="42" height="38" rx="14"/><rect x="30" y="14" width="10" height="44" rx="5"/><rect x="41" y="8" width="10" height="50" rx="5"/><rect x="52" y="12" width="10" height="46" rx="5"/><rect x="63" y="20" width="10" height="38" rx="5"/><rect x="14" y="48" width="10" height="32" rx="5" transform="rotate(-25 19 64)"/></g>`,
  phone: `<rect x="31" y="10" width="38" height="80" rx="9" fill="#2B2B2B" stroke="${INK}" stroke-width="5"/><rect x="36" y="20" width="28" height="54" rx="3" fill="#8EC5E8"/><circle cx="50" cy="82" r="3" fill="#fff"/>`,
  wave: `<circle cx="50" cy="26" r="12" fill="#fff" stroke="${INK}" stroke-width="5"/><path d="M50 38V68M50 68L36 92M50 68L64 92M50 48L74 24M50 48L30 62" stroke="${INK}" stroke-width="6" stroke-linecap="round" fill="none"/>`
};
function boardHtml(id, o) {
  const b = o.box, kind = o.type || "board", pos = `left:${f3(b.x * 1920)}px;top:${f3(b.y * 1080)}px;width:${f3(b.w * 1920)}px;height:${f3(b.h * 1080)}px`;
  if (kind === "step") return `<div id="${id}" class="stepbox" data-layout-allow-overlap style="${pos}"><div class="pill sm">${o.step}</div><div class="stxt">${o.text}</div></div>`;
  if (kind === "bubble") return `<div id="${id}" class="bubble" data-layout-allow-overlap style="${pos}"><svg viewBox="0 0 100 100" width="100%" height="100%">${ICONS[o.icon]}</svg></div>`;
  if (kind === "badge") return `<div id="${id}" class="tagbox" data-layout-allow-overlap style="${pos};font-size:84px"><span class="badge ${o.badge}">${o.text}</span></div>`;
  if (kind !== "board") return `<div id="${id}" class="tagbox ${kind}" data-layout-allow-overlap style="${pos}">${o.text.join(" ")}</div>`;
  return `<div id="${id}" class="board" data-layout-allow-overlap style="${pos}${o.color ? `;color:${o.color}` : ""}${o.bg ? `;background:${o.bg};border-radius:36px` : ""}">${o.text.map((l) => `<div class="bl${l === "SPOTLIGHT" ? " org" : ""}" data-layout-allow-overlap>${l}</div>`).join("")}</div>`;
}
const scenes = cfg.scenes.map((sc, i) => ({ ...sc, t: tim.scenes[i] }));
scenes.forEach((sc, i) => {
  const t = sc.t, S = t.start, E = t.end, prev = scenes[i - 1];
  const hard = i === 0 || sc.continues || sc.transition === "cut" || (prev.beats || []).some((b) => b.type === "title") || sc.diagram?.kind === "card" || prev?.diagram?.kind === "card";
  const cs = hard ? S : S - XF, ce = E, z = (i + 1) * 10, id = sc.id.toLowerCase();
  const bound = (k) => (k <= 0 ? S : Math.max(t.sentenceStarts[k] - 0.15, t.sentenceEnds[k - 1] + 0.02));
  // beats
  const beats = [];
  for (const [bi, b] of (sc.beats || []).entries()) {
    if (b.type === "crop") { const a = bound(b.sentences[0]), e = b.sentences[1] + 1 >= t.sentenceStarts.length ? E : bound(b.sentences[1] + 1); beats.push({ ...b, a, e, bi }); }
    else if (b.type === "card") {
      const w = findWord(t, b.word); let a = w.s - (b.back || 0), e = a + b.dur;
      const limit = E - 0.55; if (e > limit) { e = limit; a = e - b.dur; }
      beats.push({ ...b, a, e, bi });
    } else if (b.type === "title") { const e = E, a = E - b.dur; if (a < t.narrationEnd + b.afterNarration) warn.push(`${sc.id}: title card starts ${f3(a)}, too close to narration end ${f3(t.narrationEnd)}`); beats.push({ ...b, a, e, bi }); }
  }
  beats.sort((x, y) => x.a - y.a);
  for (let k = 1; k < beats.length; k++) if (beats[k].a < beats[k - 1].e) warn.push(`${sc.id}: beats overlap`);
  sc.resolvedBeats = beats;
  for (const b of beats) sfx.push({ t: f3(b.a), kind: b.type === "crop" ? "swoosh" : "click" });
  if (sc.swapWord) sfx.push({ t: f3(findWord(t, sc.swapWord).s), kind: "ding" });
  (sc.overlays || []).forEach((o) => sfx.push({ t: f3(findWord(t, o.word, o.occ || 1).s - 0.05), kind: "pop" }));
  // base picture clip
  let inner = sc.diagram ? `<div id="${id}-picA" class="fill">${diagramHtml(sc.diagram)}</div>` : `<img src="${pic(sc.picture)}" class="pic" alt="">`;
  if (sc.pictureB) inner += `<img id="${id}-picB" src="${pic(sc.pictureB)}" class="pic" style="opacity:0" alt="">`;
  if (sc.diagramB) inner += `<div id="${id}-picB" class="fill" style="opacity:0">${diagramHtml(sc.diagramB)}</div>`;
  const ov = (sc.overlays || []).map((o, k) => boardHtml(`${id}-ov${k}`, o)).join("");
  html.push(`<div id="${id}" class="clip" data-start="${f3(cs)}" data-duration="${f3(ce - cs)}" style="z-index:${z}"><div id="${id}-fade" class="fill"><div id="${id}-cam" class="fill">${inner}${ov}</div></div></div>`);
  if (!hard) tl.push(`tl.fromTo("#${id}-fade",{opacity:0},{opacity:1,duration:${XF},ease:"none"},${f3(cs)});`);
  const hasSwap = sc.pictureB || sc.diagramB;
  const camStart = sc.cameraStart === "swap" ? findWord(t, sc.swapWord).s : cs;
  const cam = { "zoom-in": [1, sc.zoomTo || 1.06, 0, 0], "zoom-out": [sc.zoomTo || 1.06, 1, 0, 0], "pan-right": [1.04, 1.04, 30, -30], "pan-left": [1.04, 1.04, -30, 30] }[sc.camera];
  if (cam) tl.push(`tl.fromTo("#${id}-cam",{scale:${cam[0]},x:${cam[2]}${sc.camOrigin ? `,transformOrigin:"${sc.camOrigin}"` : ""}},{scale:${cam[1]},x:${cam[3]},duration:${f3(ce - camStart)},ease:"sine.inOut"},${f3(camStart)});`);
  if (hasSwap) { const w = findWord(t, sc.swapWord); tl.push(`tl.to("#${id}-picB",{opacity:1,duration:0.3,ease:"none"},${f3(w.s)});`); if (sc.diagramB) tl.push(`tl.set("#${id}-picA",{opacity:0},${f3(w.s + 0.3)});`); }
  (sc.overlays || []).forEach((o, k) => { const w = findWord(t, o.word, o.occ || 1); tl.push(`tl.fromTo("#${id}-ov${k}",{opacity:0},{opacity:1,duration:0.5,ease:"power1.out"},${f3(w.s - 0.05)});`); if (beats.some((b) => b.type === "crop")) tl.push(`tl.fromTo("#${id}-cov${k}",{opacity:0},{opacity:1,duration:0.5,ease:"power1.out"},${f3(w.s - 0.05)});`); });
  // beat clips
  for (const b of beats) {
    const bid = `${id}-b${b.bi}`;
    if (b.type === "crop") {
      const [x0, y0, iz] = b.rect, zz = 1 / iz;
      const ovc = (sc.overlays || []).map((o, k) => `<div class="mapov" style="transform:translate(${f3(-x0 * 1920 * zz)}px,${f3(-y0 * 1080 * zz)}px) scale(${f3(zz)})">${boardHtml(`${id}-cov${k}`, o)}</div>`).join("");
      html.push(`<div id="${bid}" class="clip" data-start="${f3(b.a)}" data-duration="${f3(b.e - b.a)}" style="z-index:${z + 1}"><div id="${bid}-cam" class="fill"><img src="assets/pictures/${sc.id}-crop${b.bi}.jpg" class="pic" alt="">${ovc}</div></div>`);
      tl.push(`tl.fromTo("#${bid}-cam",{scale:1},{scale:1.04,duration:${f3(b.e - b.a)},ease:"sine.inOut"},${f3(b.a)});`);
    } else if (b.type === "card") {
      html.push(`<div id="${bid}" class="clip card" data-start="${f3(b.a)}" data-duration="${f3(b.e - b.a)}" style="z-index:${z + 2}"><div id="${bid}-in" class="cardtxt">${b.parts.map((p) => `<div class="ln">${p.badge ? `<span class="badge ${p.badge}">${p.t}</span>` : p.t}</div>`).join("")}</div></div>`);
      tl.push(`tl.fromTo("#${bid}-in",{scale:0.94},{scale:1,duration:0.25,ease:"back.out(1.4)"},${f3(b.a)});`);
    } else {
      html.push(`<div id="${bid}" class="clip card" data-start="${f3(b.a)}" data-duration="${f3(b.e - b.a)}" style="z-index:${z + 2}"><div id="${bid}-in" class="cardtxt"><div class="pill">LESSON</div><div class="ln big">ONE OF THE MOST <span class="org">USEFUL</span></div><div class="ln big">LESSONS I LEARNED</div></div></div>`);
      tl.push(`tl.fromTo("#${bid}-in",{scale:0.94},{scale:1,duration:0.3,ease:"back.out(1.4)"},${f3(b.a)});`);
    }
  }
});
for (const n of used) fs.copyFileSync(`assets/pictures/${n}.jpg`, `${out}/assets/pictures/${n}.jpg`);
for (const sc of scenes) for (const b of sc.resolvedBeats) if (b.type === "crop") fs.copyFileSync(`assets/pictures/${sc.id}-crop${b.bi}.jpg`, `${out}/assets/pictures/${sc.id}-crop${b.bi}.jpg`);
fs.copyFileSync("node_modules/@fontsource/nunito/files/nunito-latin-800-normal.woff2", `${out}/assets/fonts/nunito-800.woff2`);
fs.copyFileSync("assets/vendor/gsap.min.js", `${out}/assets/gsap.min.js`);
fs.copyFileSync(cfg.audio, `${out}/assets/part${N}.wav`);
for (const f of ["hyperframes.json", "package.json"]) if (fs.existsSync(`tools/template/${f}`)) fs.copyFileSync(`tools/template/${f}`, `${out}/${f}`);
fs.writeFileSync(`${out}/meta.json`, JSON.stringify({ id: `part${N}`, name: `SimpleMindMotivation Part ${N}`, createdAt: "2026-10-10T00:00:00.000Z" }, null, 2));
const page = `<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=1920, height=1080"><title>Part ${N}</title>
<script src="assets/gsap.min.js"></script>
<style>
@font-face{font-family:"Nunito";font-weight:800;src:url("assets/fonts/nunito-800.woff2") format("woff2")}
html,body{margin:0;background:${PAPER}}
#root{position:relative;width:100%;height:100%;overflow:hidden;background:${PAPER};font-family:"Nunito",sans-serif;font-weight:800;color:${INK}}
.clip{position:absolute;inset:0;overflow:hidden}
.fill{position:absolute;inset:0}
.pic{position:absolute;inset:0;width:100%;height:100%;display:block}
.card{background:${PAPER};display:flex;align-items:center;justify-content:center}
.cardtxt{display:flex;flex-direction:column;align-items:center;gap:26px;text-align:center}
.ln{font-size:170px;line-height:1.05;letter-spacing:1px;white-space:nowrap}
.ln.big{font-size:118px}
.badge{display:inline-block;padding:4px 40px 12px;border:9px solid ${INK};border-radius:34px;box-shadow:8px 8px 0 ${INK}}
.badge.yellow{background:${YEL};color:${INK}} .badge.red{background:${RED};color:#fff}
.pill{background:${GREEN};color:#fff;border:7px solid ${INK};border-radius:60px;font-size:64px;padding:2px 54px 8px;letter-spacing:4px;margin-bottom:18px}
.org{color:${ORG};-webkit-text-stroke:6px ${INK};paint-order:stroke fill}
.mapov{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0}
.board{position:absolute;display:flex;flex-direction:column;align-items:center;justify-content:center;color:${INK};font-size:112px;line-height:1.08;text-align:center}
.diag{background:${PAPER}}
.dlabel{position:absolute;left:0;right:0;top:830px;display:flex;justify-content:center;align-items:center;gap:36px;font-size:130px;white-space:nowrap}
.tagbox{position:absolute;display:flex;align-items:center;justify-content:center;white-space:nowrap}
.tagbox.label{background:${PAPER};border:5px solid ${INK};border-radius:40px;font-size:40px}
.tagbox.pill{background:${GREEN};color:#fff;border:6px solid ${INK};border-radius:60px;font-size:54px;letter-spacing:3px}
.cardc{display:flex;align-items:center;justify-content:center}
.spillrow{position:absolute;left:0;right:0;top:70px;display:flex;justify-content:center}
.stitle{position:absolute;left:0;right:0;top:190px;text-align:center;font-size:140px;line-height:1}
.bigval{position:absolute;left:1000px;right:0;top:560px;display:flex;justify-content:center;font-size:240px}
.sclab{position:absolute;width:500px;display:flex;justify-content:center;font-size:84px}
.stepbox{position:absolute;background:${PAPER};border:6px solid ${INK};border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;text-align:center;box-sizing:border-box;padding:8px 18px}
.stepbox .pill.sm{font-size:42px;padding:0 34px 4px;margin:0;border-width:5px}
.stxt{font-size:50px;line-height:1.05}
.bubble{position:absolute;background:#fff;border:6px solid ${INK};border-radius:50%;box-sizing:border-box;padding:14px}
.board .bl.org{-webkit-text-stroke:4px ${INK}}
</style></head><body>
<div id="root" data-composition-id="part${N}" data-start="0" data-width="1920" data-height="1080" data-duration="${f3(dur)}">
${html.join("\n")}
<audio id="vo" src="assets/part${N}.wav" data-start="0" data-duration="${f3(dur)}" data-track-index="0"></audio>
</div>
<script>
const tl = gsap.timeline({ paused: true });
${tl.join("\n")}
window.__timelines["part${N}"] = tl;
</script></body></html>`;
fs.writeFileSync(`${out}/index.html`, page);
const plan = scenes.map((s) => ({ id: s.id, start: f3(s.t.start), end: f3(s.t.end), beats: s.resolvedBeats.map((b) => ({ type: b.type, a: f3(b.a), e: f3(b.e) })) }));
fs.writeFileSync(`scenes/part${N}.sfx.json`, JSON.stringify(sfx.sort((a, b) => a.t - b.t)));
fs.writeFileSync(`scenes/part${N}.plan.json`, JSON.stringify(plan, null, 1));
console.log(warn.length ? "WARNINGS:\n" + warn.join("\n") : "no warnings"); console.log("built", out);
