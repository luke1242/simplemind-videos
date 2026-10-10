// scenes spec + word timing -> HyperFrames project parts/partN/   usage: node tools/build-part.mjs N
// Every scene is tiled into shots of at most 4s whose cuts land on word starts (see ROUND 2 in CLAUDE.md).
import fs from "node:fs";
const N = process.argv[2]; const R = (p) => JSON.parse(fs.readFileSync(p, "utf8"));
const cfg = R(`scenes/part${N}.json`), tim = R(`scenes/part${N}.timing.json`), FOC = R(`scenes/part${N}.foci.json`);
const out = `parts/part${N}`;
for (const d of ["pictures", "icons", "narrator", "fonts"]) fs.mkdirSync(`${out}/assets/${d}`, { recursive: true });
const dur = tim.duration, XF = 0.25, MAXSHOT = 4.0, f3 = (x) => +x.toFixed(3);
const INK = "#1A1A1A", PAPER = "#FAF7F0", YEL = "#F2C230", RED = "#D64545", ORG = "#F2A65A", GREEN = "#2F6B2F";
const tl = [], html = [], warn = [], sfx = [], cutRows = [], planOut = [];
const usedPics = new Set(), usedIcons = new Set(), usedPoses = new Set();
const norm = (w) => w.toLowerCase().replace(/[^a-z0-9']/g, "");

// ---------- html helpers ----------
const pieSvg = (cx, cy, r, pct) => {
  const a = (pct / 100) * 2 * Math.PI, x = cx + r * Math.sin(a), y = cy - r * Math.cos(a);
  const slice = pct >= 100 ? `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${ORG}" stroke="${INK}" stroke-width="9"/>` : `<path d="M${cx} ${cy} L${cx} ${cy - r} A${r} ${r} 0 ${a > Math.PI ? 1 : 0} 1 ${f3(x)} ${f3(y)} Z" fill="${ORG}" stroke="${INK}" stroke-width="9" stroke-linejoin="round"/>`;
  return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="#E6E1D6" stroke="${INK}" stroke-width="9"/>${slice}`;
};
const svgWrap = (inner) => `<svg viewBox="0 0 1920 1080" width="1920" height="1080" style="position:absolute;inset:0">${inner}</svg>`;
function scaleSvg() {
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
const linesHtml = (parts, cls = "ln") => parts.map((p) => `<div class="${cls}">${p.badge ? `<span class="badge ${p.badge}">${p.t}</span>` : p.t}</div>`).join("");
function diagramHtml(d) {
  if (d.kind === "pie") return `<div class="fill diag">${svgWrap(pieSvg(960, 440, 310, d.pct))}<div class="dlabel"><span>${d.label}</span><span class="badge ${d.badge}">${d.value}</span></div></div>`;
  if (d.kind === "card") return `<div class="fill diag cardc"><div class="cardtxt">${linesHtml(d.parts)}</div></div>`;
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
const SCREEN = new Set(["label", "pill", "step"]);
function screenOv(id, o) {
  if (o.type === "step") return `<div id="${id}" class="scr" data-layout-allow-overlap><div class="pill big">${o.step}</div><div class="spill2">${o.text}</div></div>`;
  if (o.type === "pill") return `<div id="${id}" class="scr" data-layout-allow-overlap><div class="pill big">${o.text}</div></div>`;
  return `<div id="${id}" class="scr" data-layout-allow-overlap><div class="spill2">${o.text}</div></div>`;
}
function picOv(id, o) {
  const b = o.box, kind = o.type || "board", pos = `left:${f3(b.x * 1920)}px;top:${f3(b.y * 1080)}px;width:${f3(b.w * 1920)}px;height:${f3(b.h * 1080)}px`;
  if (kind === "bubble") return `<div id="${id}" class="bubble" data-layout-allow-overlap style="${pos}"><svg viewBox="0 0 100 100" width="100%" height="100%">${ICONS[o.icon]}</svg></div>`;
  if (kind === "badge") return `<div id="${id}" class="tagbox" data-layout-allow-overlap style="${pos};font-size:84px"><span class="badge ${o.badge}">${o.text}</span></div>`;
  return `<div id="${id}" class="board" data-layout-allow-overlap style="${pos}${o.color ? `;color:${o.color}` : ""}${o.bg ? `;background:${o.bg};border-radius:36px` : ""}">${o.text.map((l) => `<div class="bl${l === "SPOTLIGHT" ? " org" : ""}" data-layout-allow-overlap>${l}</div>`).join("")}</div>`;
}

// ---------- planning ----------
const scenes = cfg.scenes.map((sc, i) => ({ ...sc, t: tim.scenes[i] }));
const ALT = { "zoom-in": "zoom-out", "zoom-out": "zoom-in", "pan-left": "pan-right", "pan-right": "pan-left", hold: "zoom-in" };
const CAM = { "zoom-in": [1, 1.05, 0, 0], "zoom-out": [1.05, 1, 0, 0], "pan-right": [1.04, 1.04, 25, -25], "pan-left": [1.04, 1.04, -25, 25], hold: null };
const LIM = { icon: [1.5, 3.0], card: [1.5, 2.5], pop: [2.0, 4.0] };

function planScene(sc, i) {
  const t = sc.t, S = t.start, E = t.end, ws = t.words;
  const W = (word, occ = 1) => { const n = norm(word); let c = 0; for (let k = 0; k < ws.length; k++) if (ws[k].w === n && ++c === occ) return k; throw new Error(`${sc.id}: word not found: ${word}`); };
  const cutAt = (k) => { if (k <= 0) return S; if (k >= ws.length) return E; const w = ws[k], p = ws[k - 1]; let c = w.s - 0.04; if (c < p.e) c = Math.min(p.e + 0.005, w.s); return c; };
  const gapBefore = (k) => (k <= 0 ? 1 : ws[k].s - ws[k - 1].e);
  // events
  let evs = [];
  for (const e of sc.events || []) {
    if (e.kind === "title") { evs.push({ ...e, a: E - e.dur, e: E }); continue; }
    const k = W(e.word, e.occ || 1), [mn, mx] = LIM[e.kind];
    let a = cutAt(k); if (a - S < 1.0) a = S;
    const tt = (sc.events || []).find((x) => x.kind === "title"), limit = tt ? E - tt.dur : E;
    let best = null;
    for (let j = k + 1; j <= ws.length; j++) { const d = cutAt(j) - a; if (cutAt(j) <= limit + 0.01 && d >= mn && d <= mx && (!best || Math.abs(d - e.dur) < Math.abs(best.d - e.dur))) best = { j, d }; }
    let end;
    if (best) end = cutAt(best.j);
    else { let j = k + 1; while (j <= ws.length && cutAt(j) - a < mn) j++; end = j <= ws.length ? cutAt(j) : E; if (end - a > mx + 1.5) end = Math.min(E, a + e.dur); }
    if (end > limit) end = limit; else if (limit - end < 0.9) end = limit;
    evs.push({ ...e, a, e: end, k });
  }
  evs.sort((x, y) => x.a - y.a);
  const kept = [];
  for (const ev of evs) {
    const prev = kept[kept.length - 1];
    if (prev && ev.a < prev.e + (ev.kind === "title" ? 0 : 0.8)) {
      if (ev.kind === "title") { kept.pop(); warn.push(`${sc.id}: dropped ${prev.kind} (${prev.word}) for title`); }
      else { warn.push(`${sc.id}: dropped ${ev.kind} "${ev.word}" (too close to ${prev.kind})`); continue; }
    }
    kept.push(ev);
  }
  evs = kept;
  // swap time
  let T = Infinity;
  if (sc.swap) { T = cutAt(W(sc.swap.word, sc.swap.occ || 1)); const inside = evs.find((e) => T > e.a && T < e.e); if (inside) T = inside.e; }
  // gaps
  const gaps = []; let cur = S;
  for (const ev of evs) { if (ev.a - cur > 0.05) gaps.push([cur, ev.a]); cur = ev.e; }
  const tailStart = cur;
  const splitGap = (g0, g1) => {
    const res = []; let c = g0;
    while (g1 - c > MAXSHOT - 0.05) {
      let cands = [];
      for (let j = 1; j < ws.length; j++) { const x = cutAt(j); if (x >= c + 1.8 && x <= c + 3.8 && g1 - x >= 1.0) cands.push({ x, sc: gapBefore(j) * 2 - Math.abs(x - (c + 3.2)) * 0.6 }); }
      if (!cands.length) for (let j = 1; j < ws.length; j++) { const x = cutAt(j); if (x >= c + 1.0 && x <= c + 3.9 && g1 - x >= 0.8) cands.push({ x, sc: gapBefore(j) * 2 - Math.abs(x - (c + 3.2)) * 0.6 }); }
      let x;
      if (cands.length) { cands.sort((p, q) => q.sc - p.sc); x = cands[0].x; } else { x = c + 3.5; warn.push(`${sc.id}: cut in silence at ${f3(x)}`); }
      res.push([c, x]); c = x;
    }
    res.push([c, g1]); return res;
  };
  let hold = null;
  if (sc.holdEnd) { const lastEnd = ws[ws.length - 1].e + 0.3; if (E - lastEnd > 1) { hold = [lastEnd, E]; } }
  if (E - tailStart > 0.05) { const g1 = hold ? hold[0] : E; if (g1 - tailStart > 0.05) gaps.push([tailStart, g1]); }
  const shotsOut = []; let gi = 0, ci = 0;
  const foci = (pic) => (sc.foci ? FOC["__" + sc.id] : FOC[pic] || []);
  const picAt = (a) => (a >= T - 0.01 && (sc.pictureB || sc.diagramB) ? "B" : "A");
  const picName = (side) => (side === "B" ? sc.pictureB : sc.picture);
  const crops = {};
  const pushGap = (g0, g1) => {
    let parts = [[g0, g1]];
    if (T > g0 + 0.6 && T < g1 - 0.6) parts = [[g0, T], [T, g1]];
    for (const [p0, p1] of parts) for (const [a, e] of splitGap(p0, p1)) {
      const side = picAt(a), pn = picName(side), fl = foci(pn);
      let type = "main";
      if (ci % 2 === 1 && fl.length) type = "crop";
      ci++;
      const sh = { a, e, type, side, pic: pn };
      if (type === "crop") { const key = side + pn; crops[key] = (crops[key] || 0); sh.fi = crops[key] % fl.length; crops[key]++; }
      shotsOut.push(sh);
    }
  };
  const all = [];
  for (const g of gaps) all.push({ g });
  for (const ev of evs) all.push({ ev });
  all.sort((x, y) => (x.g ? x.g[0] : x.ev.a) - (y.g ? y.g[0] : y.ev.a));
  for (const it of all) {
    if (it.g) pushGap(...it.g);
    else shotsOut.push({ a: it.ev.a, e: it.ev.e, type: it.ev.kind, ev: it.ev });
  }
  if (hold) shotsOut.push({ a: hold[0], e: hold[1], type: "main", side: picAt(hold[0]), pic: picName(picAt(hold[0])), hold: true, exempt: true });
  shotsOut.sort((x, y) => x.a - y.a);
  // tiling check
  shotsOut[0].a = S; for (let k = 1; k < shotsOut.length; k++) { shotsOut[k].a = shotsOut[k - 1].e; }
  shotsOut[shotsOut.length - 1].e = E;
  return { shots: shotsOut, ws, W };
}

// ---------- build ----------
let z = 10, shotNo = 0;
scenes.forEach((sc, i) => {
  const { shots, ws, W } = planScene(sc, i);
  const S = sc.t.start, E = sc.t.end, id = sc.id.toLowerCase();
  const PICK = new Set(["main", "crop"]);
  const prevLast = i > 0 ? scenes[i - 1].lastKind : null;
  const hard = i === 0 || sc.continues || sc.transition === "cut" || !PICK.has(shots[0].type) || (prevLast && !PICK.has(prevLast));
  sc.lastKind = shots[shots.length - 1].type;
  const ovs = sc.overlays || [];
  let mainIdx = 0;
  shots.forEach((sh, si) => {
    const sid = `${id}-s${si}`, a = sh.a, e = sh.e, d = e - a;
    const first = si === 0, cs = first && !hard ? a - XF : a, cd = e - cs;
    if (d > MAXSHOT + 0.02 && !sh.exempt && sh.type !== "title") warn.push(`${sc.id}: shot ${f3(a)}-${f3(e)} is ${f3(d)}s`);
    if (sh.type === "icon" && d > 3.05 || sh.type === "card" && d > 2.55) warn.push(`${sc.id}: ${sh.type} lasts ${f3(d)}s`);
    // cut table
    if (!(i === 0 && first)) {
      let bi = 0; ws.forEach((w, k) => { if (Math.abs(w.s - a) < Math.abs(ws[bi].s - a)) bi = k; });
      const prevScene = scenes[i - 1]; let bd = Math.abs(ws[bi].s - a), bw = ws[bi].w;
      if (first && prevScene) { /* scene boundary: the first word of this scene */ bw = ws[0].w; bd = Math.abs(ws[0].s - a); }
      cutRows.push({ t: a, word: bw, delta: bd, kind: sh.type, scene: sc.id });
      if (bd > 0.1) warn.push(`${sc.id}: cut ${f3(a)} is ${f3(bd)}s from word "${bw}"`);
    }
    const zi = ++z;
    if (sh.type === "main" || sh.type === "crop") {
      const isDiag = !!(sc.diagram), side = sh.side;
      let inner, rect = null;
      if (sh.type === "crop") rect = isDiag ? (FOC["__" + sc.id] || [])[sh.fi] : (FOC[sh.pic] || [])[sh.fi];
      const dg = isDiag ? (side === "B" && sc.diagramB ? sc.diagramB : sc.diagram) : null;
      const picOvs = ovs.map((o, k) => [o, k]).filter(([o]) => !SCREEN.has(o.type));
      const scrOvs = ovs.map((o, k) => [o, k]).filter(([o]) => SCREEN.has(o.type));
      const picOvHtml = picOvs.map(([o, k]) => picOv(`${sid}-ov${k}`, o)).join("");
      if (sh.type === "crop") {
        const [x0, y0, iw] = rect, zz = 1 / iw;
        if (isDiag) inner = `<div class="mapov" style="transform:translate(${f3(-x0 * 1920 * zz)}px,${f3(-y0 * 1080 * zz)}px) scale(${f3(zz)})">${diagramHtml(dg)}${picOvHtml}</div>`;
        else { usedPics.add(`${sh.pic}-f${sh.fi}`); inner = `<img src="assets/pictures/${sh.pic}-f${sh.fi}.jpg" class="pic" alt=""><div class="mapov" style="transform:translate(${f3(-x0 * 1920 * zz)}px,${f3(-y0 * 1080 * zz)}px) scale(${f3(zz)})">${picOvHtml}</div>`; }
      } else if (isDiag) inner = diagramHtml(dg) + picOvHtml;
      else { usedPics.add(sh.pic); inner = `<img src="assets/pictures/${sh.pic}.jpg" class="pic" alt="">${picOvHtml}`; }
      const scrHtml = scrOvs.map(([o, k]) => screenOv(`${sid}-so${k}`, o)).join("");
      html.push(`<div id="${sid}" class="clip" data-start="${f3(cs)}" data-duration="${f3(cd)}" style="z-index:${zi}"><div id="${sid}-fade" class="fill"><div id="${sid}-cam" class="fill">${inner}</div>${scrHtml}</div></div>`);
      if (first && !hard) tl.push(`tl.fromTo("#${sid}-fade",{opacity:0},{opacity:1,duration:${XF},ease:"none"},${f3(cs)});`);
      // camera
      if (sh.type === "crop") tl.push(`tl.fromTo("#${sid}-cam",{scale:1},{scale:1.03,duration:${f3(cd)},ease:"sine.inOut"},${f3(cs)});`);
      else if (!sh.hold) {
        const base = sc.camera, kind = mainIdx % 2 === 0 ? base : ALT[base]; mainIdx++;
        let c = CAM[kind];
        if (sc.zoomTo && kind === "zoom-in") c = [1, sc.zoomTo, 0, 0];
        if (c) tl.push(`tl.fromTo("#${sid}-cam",{scale:${c[0]},x:${c[2]}${sc.camOrigin ? `,transformOrigin:"${sc.camOrigin}"` : ""}},{scale:${c[1]},x:${c[3]},duration:${f3(cd)},ease:"sine.inOut"},${f3(cs)});`);
      }
      for (const [o, k] of picOvs) { const w = ws[W(o.word, o.occ || 1)]; tl.push(`tl.fromTo("#${sid}-ov${k}",{opacity:0},{opacity:1,duration:0.5,ease:"power1.out"},${f3(w.s - 0.05)});`); }
      for (const [o, k] of scrOvs) { const w = ws[W(o.word, o.occ || 1)]; tl.push(`tl.fromTo("#${sid}-so${k}",{opacity:0},{opacity:1,duration:0.4,ease:"power1.out"},${f3(w.s - 0.05)});`); }
    } else if (sh.type === "icon") {
      usedIcons.add(sh.ev.icon);
      html.push(`<div id="${sid}" class="clip iconshot" data-start="${f3(cs)}" data-duration="${f3(cd)}" style="z-index:${zi}"><img id="${sid}-img" src="assets/icons/${sh.ev.icon}.jpg" class="pic" alt=""></div>`);
      tl.push(`tl.fromTo("#${sid}-img",{scale:0.92},{scale:1,duration:0.2,ease:"power2.out"},${f3(a)});`);
      sfx.push({ t: f3(a), kind: "pop" });
    } else if (sh.type === "card") {
      html.push(`<div id="${sid}" class="clip card" data-start="${f3(cs)}" data-duration="${f3(cd)}" style="z-index:${zi}"><div id="${sid}-in" class="cardtxt">${linesHtml(sh.ev.parts)}</div></div>`);
      tl.push(`tl.fromTo("#${sid}-in",{scale:0.94},{scale:1,duration:0.25,ease:"back.out(1.4)"},${f3(a)});`);
      sfx.push({ t: f3(a), kind: "click" });
    } else if (sh.type === "title") {
      html.push(`<div id="${sid}" class="clip card" data-start="${f3(cs)}" data-duration="${f3(cd)}" style="z-index:${zi}"><div id="${sid}-in" class="cardtxt"><div class="pill">LESSON</div><div class="ln big">ONE OF THE MOST <span class="org">USEFUL</span></div><div class="ln big">LESSONS I LEARNED</div></div></div>`);
      tl.push(`tl.fromTo("#${sid}-in",{scale:0.94},{scale:1,duration:0.3,ease:"back.out(1.4)"},${f3(a)});`);
      sfx.push({ t: f3(a), kind: "click" });
    } else if (sh.type === "pop") {
      const c = sh.ev.content, pose = sh.ev.pose; usedPoses.add(pose);
      let content;
      if (c.type === "icon") { usedIcons.add(c.icon); content = `<img src="assets/icons/${c.icon}.jpg" class="popicon" alt="">`; }
      else content = `<div class="popcard">${linesHtml(c.parts, "ln sm")}</div>`;
      html.push(`<div id="${sid}" class="clip card" data-start="${f3(cs)}" data-duration="${f3(cd)}" style="z-index:${zi}${c.type === "icon" ? ";background:#F8F5EE" : ""}"><div id="${sid}-c" class="popwrap">${content}</div><img id="${sid}-n" class="narr" src="assets/narrator/${pose}.png" alt=""></div>`);
      tl.push(`tl.fromTo("#${sid}-n",{x:-460},{x:0,duration:0.25,ease:"power2.out"},${f3(a)});`);
      tl.push(`tl.to("#${sid}-n",{x:-460,duration:0.2,ease:"power2.in"},${f3(e - 0.22)});`);
      tl.push(`tl.fromTo("#${sid}-c",{scale:0.94},{scale:1,duration:0.25,ease:"back.out(1.4)"},${f3(a + 0.1)});`);
      sfx.push({ t: f3(a), kind: "swoosh" });
    }
    planOut.push({ scene: sc.id, kind: sh.type, a: f3(a), e: f3(e) });
  });
  if (sc.swap) sfx.push({ t: f3(ws[W(sc.swap.word, sc.swap.occ || 1)].s), kind: "ding" });
  ovs.forEach((o) => sfx.push({ t: f3(ws[W(o.word, o.occ || 1)].s - 0.05), kind: "pop" }));
});

// ---------- files ----------
for (const n of usedPics) fs.copyFileSync(`assets/pictures/${n}.jpg`, `${out}/assets/pictures/${n}.jpg`);
for (const n of usedIcons) fs.copyFileSync(`assets/icons/${n}.jpg`, `${out}/assets/icons/${n}.jpg`);
for (const n of usedPoses) fs.copyFileSync(`assets/narrator/${n}.png`, `${out}/assets/narrator/${n}.png`);
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
.iconshot{background:#F8F5EE}
.card{background:${PAPER};display:flex;align-items:center;justify-content:center}
.cardtxt{display:flex;flex-direction:column;align-items:center;gap:26px;text-align:center}
.ln{font-size:170px;line-height:1.05;letter-spacing:1px;white-space:nowrap}
.ln.big{font-size:118px}
.ln.sm{font-size:112px}
.badge{display:inline-block;padding:4px 40px 12px;border:9px solid ${INK};border-radius:34px;box-shadow:8px 8px 0 ${INK}}
.badge.yellow{background:${YEL};color:${INK}} .badge.red{background:${RED};color:#fff}
.pill{background:${GREEN};color:#fff;border:7px solid ${INK};border-radius:60px;font-size:64px;padding:2px 54px 8px;letter-spacing:4px;margin-bottom:18px}
.pill.big{margin:0;border-width:6px;font-size:64px;padding:2px 50px 8px}
.org{color:${ORG};-webkit-text-stroke:6px ${INK};paint-order:stroke fill}
.mapov{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0}
.board{position:absolute;display:flex;flex-direction:column;align-items:center;justify-content:center;color:${INK};font-size:112px;line-height:1.08;text-align:center}
.diag{background:${PAPER}}
.cardc{display:flex;align-items:center;justify-content:center}
.dlabel{position:absolute;left:0;right:0;top:830px;display:flex;justify-content:center;align-items:center;gap:36px;font-size:130px;white-space:nowrap}
.spillrow{position:absolute;left:0;right:0;top:70px;display:flex;justify-content:center}
.stitle{position:absolute;left:0;right:0;top:190px;text-align:center;font-size:140px;line-height:1}
.bigval{position:absolute;left:1000px;right:0;top:560px;display:flex;justify-content:center;font-size:240px}
.sclab{position:absolute;width:500px;display:flex;justify-content:center;font-size:84px}
.tagbox{position:absolute;display:flex;align-items:center;justify-content:center;white-space:nowrap}
.bubble{position:absolute;background:#fff;border:6px solid ${INK};border-radius:50%;box-sizing:border-box;padding:14px}
.scr{position:absolute;left:0;right:0;top:24px;display:flex;flex-direction:column;align-items:center;gap:14px;z-index:5}
.spill2{background:${PAPER};border:6px solid ${INK};border-radius:44px;font-size:60px;line-height:1.05;padding:4px 40px 10px;white-space:nowrap}
.popwrap{position:absolute;left:760px;right:50px;top:0;bottom:0;display:flex;align-items:center;justify-content:center}
.popcard{display:flex;flex-direction:column;align-items:center;gap:22px;text-align:center}
.popicon{width:1180px;height:664px}
.narr{position:absolute;left:70px;bottom:0;height:700px}
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
fs.writeFileSync(`scenes/part${N}.sfx.json`, JSON.stringify(sfx.sort((a, b) => a.t - b.t)));
fs.writeFileSync(`scenes/part${N}.plan.json`, JSON.stringify(planOut, null, 1));
const rows = cutRows.sort((a, b) => a.t - b.t).map((r) => `${r.t.toFixed(2).padStart(7)}s  ${r.scene}  ${r.kind.padEnd(5)}  word "${r.word}"  Δ${(r.delta * 1000).toFixed(0)}ms`);
fs.writeFileSync(`scenes/part${N}.cuts.txt`, rows.join("\n"));
const lens = planOut.map((p) => p.e - p.a), over = planOut.filter((p) => p.e - p.a > 4.02);
console.log(`shots ${planOut.length}, avg ${(lens.reduce((x, y) => x + y, 0) / lens.length).toFixed(2)}s, max ${Math.max(...lens).toFixed(2)}s, over 4s: ${over.length}`);
console.log(warn.length ? "WARNINGS:\n" + warn.join("\n") : "no warnings"); console.log("built", out);
