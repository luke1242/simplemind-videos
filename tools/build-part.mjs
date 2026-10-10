// scenes JSON + word timing -> HyperFrames project in parts/partN/   usage: node tools/build-part.mjs N
import fs from "node:fs"; import path from "node:path";
const N = process.argv[2]; const R = (p) => JSON.parse(fs.readFileSync(p, "utf8"));
const cfg = R(`scenes/part${N}.resolved.json`), tim = R(`scenes/part${N}.timing.json`);
const out = `parts/part${N}`; fs.mkdirSync(`${out}/assets/pictures`, { recursive: true }); fs.mkdirSync(`${out}/assets/fonts`, { recursive: true });
const dur = tim.duration, XF = 0.4, f3 = (x) => +x.toFixed(3);
const INK = "#1A1A1A", PAPER = "#FAF7F0", YEL = "#F2C230", RED = "#D64545", ORG = "#F2A65A", GREEN = "#2F6B2F";
const tl = []; const html = []; const warn = [];
const used = new Set();
const pic = (n) => { used.add(n); return `assets/pictures/${n}.jpg`; };
const findWord = (t, w, occ = 1) => { let c = 0; for (const x of t.words) if (x.w === w && ++c === occ) return x; throw new Error("word not found: " + w); };

const scenes = cfg.scenes.map((sc, i) => ({ ...sc, t: tim.scenes[i] }));
scenes.forEach((sc, i) => {
  const t = sc.t, S = t.start, E = t.end, prev = scenes[i - 1];
  const hard = i === 0 || sc.continues || sc.transition === "cut" || (prev.beats || []).some((b) => b.type === "title");
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
  // base picture clip
  let inner = `<img src="${pic(sc.picture)}" class="pic" alt="">`;
  if (sc.pictureB) inner += `<img id="${id}-picB" src="${pic(sc.pictureB)}" class="pic" style="opacity:0" alt="">`;
  const ov = (sc.overlays || []).map((o, k) => boardHtml(`${id}-ov${k}`, o)).join("");
  html.push(`<div id="${id}" class="clip" data-start="${f3(cs)}" data-duration="${f3(ce - cs)}" style="z-index:${z}"><div id="${id}-fade" class="fill"><div id="${id}-cam" class="fill">${inner}${ov}</div></div></div>`);
  if (!hard) tl.push(`tl.fromTo("#${id}-fade",{opacity:0},{opacity:1,duration:${XF},ease:"none"},${f3(cs)});`);
  const cam = { "zoom-in": [1, 1.06, 0, 0], "zoom-out": [1.06, 1, 0, 0], "pan-right": [1.04, 1.04, 30, -30], "pan-left": [1.04, 1.04, -30, 30] }[sc.camera];
  if (cam) tl.push(`tl.fromTo("#${id}-cam",{scale:${cam[0]},x:${cam[2]}},{scale:${cam[1]},x:${cam[3]},duration:${f3(ce - cs)},ease:"sine.inOut"},${f3(cs)});`);
  if (sc.pictureB) { const w = findWord(t, sc.swapWord); tl.push(`tl.to("#${id}-picB",{opacity:1,duration:0.3,ease:"none"},${f3(w.s)});`); }
  (sc.overlays || []).forEach((o, k) => { const w = findWord(t, o.word, o.occ || 1); tl.push(`tl.fromTo("#${id}-ov${k}",{opacity:0},{opacity:1,duration:0.5,ease:"power1.out"},${f3(w.s - 0.05)});`); tl.push(`tl.fromTo("#${id}-cov${k}",{opacity:0},{opacity:1,duration:0.5,ease:"power1.out"},${f3(w.s - 0.05)});`); });
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
function boardHtml(id, o) {
  const b = o.box;
  return `<div id="${id}" class="board" data-layout-allow-overlap style="left:${f3(b.x * 1920)}px;top:${f3(b.y * 1080)}px;width:${f3(b.w * 1920)}px;height:${f3(b.h * 1080)}px">${o.text.map((l) => `<div class="bl${l === "SPOTLIGHT" ? " org" : ""}" data-layout-allow-overlap>${l}</div>`).join("")}</div>`;
}
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
fs.writeFileSync(`scenes/part${N}.plan.json`, JSON.stringify(plan, null, 1));
console.log(warn.length ? "WARNINGS:\n" + warn.join("\n") : "no warnings"); console.log("built", out);
