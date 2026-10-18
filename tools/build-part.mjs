// scenes spec + word timing -> HyperFrames project parts/partN/   usage: node tools/build-part.mjs N
// Every scene is tiled into shots of at most 4s whose cuts land on word starts. Host mode (narrator at the side),
// motivated camera moves (snap zoom / whip slide), coded diagrams, callouts, count-ups: see CLAUDE.md sections 4-9.
import fs from "node:fs";
const N = process.argv[2]; const R = (p) => JSON.parse(fs.readFileSync(p, "utf8"));
const cfg = R(`scenes/part${N}.json`), tim = R(`scenes/part${N}.timing.json`), FOC = R(`scenes/part${N}.foci.json`);
const out = `parts/part${N}`;
for (const d of ["pictures", "icons", "narrator", "fonts"]) fs.mkdirSync(`${out}/assets/${d}`, { recursive: true });
const dur = tim.duration, MAXSHOT = 4.0, f3 = (x) => +x.toFixed(3);
const INK = "#1A1A1A", PAPER = "#FAF7F0", YEL = "#F2C230", RED = "#D64545", ORG = "#F2A65A", GREEN = "#2F6B2F", TERRA = "#D9805F", GREY = "#E6E1D6", SKY = "#8EC5E8", SAGE = "#9CC08B";
const tl = [], html = [], warn = [], sfx = [], cutRows = [], planOut = [], leaks = [];
const vid = (s) => s.replace(/[^a-zA-Z0-9]/g, "_");
const usedPics = new Set(), usedIcons = new Set(), usedPoses = new Set();
const norm = (w) => w.toLowerCase().replace(/[^a-z0-9']/g, "");
const HS = 0.74, FW = 1920 * HS, FH = 1080 * HS, FL = 1920 - FW - 44, FT = 140; // host frame geometry
const NH = 648, NSCALE = NH / 680;
const pngW = (p) => fs.readFileSync(p).readUInt32BE(16);
const POSEW = {}; for (let i = 1; i <= 12; i++) { const n = "N" + String(i).padStart(2, "0"); POSEW[n] = Math.round(pngW(`assets/narrator/${n}.png`) * NSCALE); }
const FULL = [0.5, 0.5, 1];
const trSt = (f, drift = 1, clamp = true) => { let [cx, cy, z] = f; z *= drift; const hw = 0.5 / z; if (clamp) { cx = Math.min(Math.max(cx, hw), 1 - hw); cy = Math.min(Math.max(cy, hw), 1 - hw); } return `x:${f3(960 - cx * 1920 * z)},y:${f3(540 - cy * 1080 * z)},scale:${f3(z)}`; };

// ---------- html helpers ----------
const svgWrap = (inner, extra = "") => `<svg viewBox="0 0 1920 1080" width="1920" height="1080" style="position:absolute;inset:0" ${extra}>${inner}</svg>`;
const pieSvg = (id, cx, cy, r, pct) => {
  const a = (pct / 100) * 2 * Math.PI, x = cx + r * Math.sin(a), y = cy - r * Math.cos(a);
  return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${GREY}" stroke="${INK}" stroke-width="9"/><path id="${id}" d="M${cx} ${cy} L${cx} ${cy - r} A${r} ${r} 0 ${a > Math.PI ? 1 : 0} 1 ${f3(x)} ${f3(y)} Z" fill="${ORG}" stroke="${INK}" stroke-width="9" stroke-linejoin="round"/>`;
};
const piePath = (cx, cy, r, pct) => { const p = Math.min(Math.max(pct, 0.01), 99.99), a = (p / 100) * 2 * Math.PI; return `M${cx} ${cy} L${cx} ${cy - r} A${r} ${r} 0 ${a > Math.PI ? 1 : 0} 1 ${f3(cx + r * Math.sin(a))} ${f3(cy - r * Math.cos(a))} Z`; };
const partHtml = (p, extra = "") => {
  if (p.mk) return `<span class="mk"><i id="${extra}-mk"></i><b>${p.t}</b></span>`;
  if (p.circ) return `<span class="circw"><span class="badge ${p.badge || "yellow"}" id="${extra}-cw">${p.t}</span><svg class="circ" viewBox="0 0 400 200" preserveAspectRatio="none"><ellipse id="${extra}-ci" cx="200" cy="100" rx="185" ry="88" fill="none" stroke="${RED}" stroke-width="9" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg></span>${p.after || ""}`;
  const inner = p.badge ? `<span class="badge ${p.badge}" id="${extra}-bd">${p.t}</span>` : p.t;
  return p.ul ? `<span class="ulw">${inner}<svg class="ul" viewBox="0 0 400 30" preserveAspectRatio="none"><path id="${extra}-ul" d="M6 18 C60 6 110 26 170 14 S300 8 394 16" fill="none" stroke="${RED}" stroke-width="9" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg></span>` : inner;
};
const linesHtml = (parts, pre, cls = "ln") => parts.map((p, i) => `<div class="${cls}${p.small ? " small" : ""}${p.sz === "big" ? " big" : ""}${p.sz === "mid" ? " mid" : ""}" id="${pre}-l${i}">${partHtml(p, `${pre}-p${i}`)}</div>`).join("");
const partTweens = (parts, pre, t0) => { const r = []; parts.forEach((p, i) => {
  if (p.mk) r.push(`tl.fromTo("#${pre}-p${i}-mk",{scaleX:0},{scaleX:1,duration:0.45,ease:"power2.out"},${f3(t0 + 0.2)});`);
  if (p.circ) r.push(`tl.to("#${pre}-p${i}-ci",{strokeDashoffset:0,duration:0.5,ease:"power2.out"},${f3(t0 + 0.35)});`);
  if (p.ul) r.push(`tl.to("#${pre}-p${i}-ul",{strokeDashoffset:0,duration:0.5,ease:"power2.out"},${f3(t0 + 0.4)});`);
}); return r; };
const countTw = (id, obj, to, t, d, fmt) => `tl.fromTo(${obj},{v:0},{v:${to},duration:${d},ease:"power2.out",onUpdate:function(){var e=document.getElementById("${id}");if(e)e.textContent=${fmt};}},${f3(t)});`;
let cuid = 0;
const person = (x, y, id, fill) => `<g id="${id}" transform="translate(${x} ${y}) scale(1.2)"><circle cx="0" cy="-34" r="21" class="pp" fill="${fill}" stroke="${INK}" stroke-width="6"/><path class="pp" d="M-27 40 V0 Q-27 -12 -15 -12 H15 Q27 -12 27 0 V40 Z" fill="${fill}" stroke="${INK}" stroke-width="6" stroke-linejoin="round"/></g>`;
const ICONS = {};
const SCREEN = new Set(["label", "pill", "step", "sbadge"]);

// diagram -> {html, tw}. t = absolute trigger times (already resolved by the caller via d.at)
function diagram(d, pre, T, S0 = 0) {
  const tw = [];
  const at = (k, dflt = 0) => (d.at && d.at[k] !== undefined ? T(d.at[k]) : dflt);
  if (d.kind === "card") {
    const h = `<div class="fill diag cardc"><div class="cardtxt" id="${pre}-ct">${linesHtml(d.parts, pre)}</div>${d.sweep ? `<div class="sweep" id="${pre}-sw" style="left:760px;top:240px;width:400px;height:600px;border-radius:0;transform:skewX(-20deg)"></div>` : ""}</div>`;
    tw.push(...partTweens(d.parts, pre, d.rise !== undefined ? d.rise : S0));
    d.parts.forEach((p, i) => {
      if (p.at && d.rise === undefined) tw.push(`tl.set("#${pre}-l${i}",{opacity:0},0);`, `tl.fromTo("#${pre}-l${i}",{opacity:0,scale:0.8},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.5)"},${f3(T(p.at))});`);
      if (p.slam) tw.push(`tl.fromTo("#${pre}-p${i}-bd",{scale:1.5,rotation:-9},{scale:1,rotation:-3,duration:0.28,ease:"back.out(1.7)"},${f3((d.rise !== undefined ? d.rise : S0) + 0.3)});`);
    });
    if (d.sweep) tw.push(`tl.set("#${pre}-sw",{opacity:0},0);`, `tl.fromTo("#${pre}-sw",{opacity:1,x:-1300},{x:1300,duration:0.8,ease:"power1.inOut"},${f3((d.rise !== undefined ? d.rise : S0) + 0.45)});`, `tl.set("#${pre}-sw",{opacity:0},${f3((d.rise !== undefined ? d.rise : S0) + 1.3)});`);
    if (d.rise !== undefined) tw.push(`tl.fromTo("#${pre}-ct .ln",{y:70,opacity:0},{y:0,opacity:1,duration:0.34,ease:"back.out(1.6)",stagger:0.07},${f3(d.rise)});`);
    return { html: h, tw };
  }
  if (d.kind === "pie") {
    const t0 = at("fill", 0), cx = 960, cy = 440, r = 310;
    let h = `<div class="fill diag">${svgWrap(pieSvg(pre + "-pp", cx, cy, r, d.from !== undefined ? d.from : d.pct))}<div class="dlabel" style="font-size:${d.fs || 130}px"><span>${d.label}</span><span class="badge ${d.badge}" id="${pre}-val">${d.from !== undefined ? d.from + "%" : d.value}</span></div>${d.small ? `<div class="dsmall">${d.small}</div>` : ""}</div>`;
    if (d.from !== undefined) {
      const o = vid(`${pre}_o`); tw.push(`const ${o}={v:0};`);
      tw.push(`tl.fromTo(${o},{v:${d.from}},{v:${d.pct},duration:1.1,ease:"power2.out",onUpdate:function(){var e=document.getElementById("${pre}-pp");if(e)e.setAttribute("d",${JSON.stringify("")}+pp(${cx},${cy},${r},${o}.v));var l=document.getElementById("${pre}-val");if(l)l.textContent=Math.round(${o}.v)+"%";}},${f3(t0)});`);
    }
    return { html: h, tw };
  }
  if (d.kind === "grid") {
    let g = ""; const nred = d.fill || 0;
    for (let r = 0; r < 6; r++) for (let c = 0; c < 10; c++) g += person(960 + (c - 4.5) * 150, 175 + r * 120, `${pre}-g${r * 10 + c}`, "#fff");
    const h = `<div class="fill diag">${svgWrap(g)}<div class="dlabel" id="${pre}-lab" style="top:810px">${d.label}</div></div>`;
    // draw in row by row
    if (d.draw) for (let r = 0; r < 6; r++) tw.push(`tl.fromTo("#${pre}-g${r * 10}, #${pre}-g${r * 10 + 1}, #${pre}-g${r * 10 + 2}, #${pre}-g${r * 10 + 3}, #${pre}-g${r * 10 + 4}, #${pre}-g${r * 10 + 5}, #${pre}-g${r * 10 + 6}, #${pre}-g${r * 10 + 7}, #${pre}-g${r * 10 + 8}, #${pre}-g${r * 10 + 9}",{opacity:0,scale:0.6},{opacity:1,scale:1,duration:0.22,ease:"back.out(1.7)"},${f3(S0 + r * 0.2)});`);
    if (nred) { const t0 = at("red", 0); for (let i = 0; i < nred; i++) tw.push(`tl.to("#${pre}-g${i} .pp",{fill:"${RED}",duration:0.12,ease:"none"},${f3(t0 + (i / nred) * 0.6)});`); }
    if (d.count) { const c = d.count, t0 = at("count", 0), o = vid(`${pre}_c`); tw.push(`const ${o}={v:0};`, `tl.set("#${pre}-lab",{opacity:0},0);`, `tl.set("#${pre}-lab",{opacity:1},${f3(t0)});`,
      `tl.fromTo(${o},{v:0},{v:${c.to},duration:0.6,ease:"power2.out",onUpdate:function(){var e=document.getElementById("${pre}-cv");if(e)e.textContent=Math.round(${o}.v)+${JSON.stringify(c.suffix || "")};}},${f3(t0)});`); }
    return { html: h.replace(`id="${pre}-lab" style="top:810px">${d.label}`, `id="${pre}-lab" style="top:810px">${d.count ? `<span class="badge ${d.count.badge}" id="${pre}-cv">0${d.count.suffix || ""}</span><span>${d.count.text}</span>` : d.label}`), tw };
  }
  if (d.kind === "bars") {
    const t0 = at("grow", 0), base = 830, MAXH = 560, xs = [610, 1310], BW = 380;
    let h = `<div class="fill diag">`;
    d.bars.forEach((b, i) => {
      const o = vid(`${pre}_b${i}`);
      h += `<div class="bar" id="${pre}-b${i}" style="left:${xs[i] - BW / 2}px;top:${base}px;width:${BW}px;height:0px;background:${i === 0 ? RED : GREY}"><div class="btag"><span class="badge ${i === 0 ? "red" : "yellow"}" id="${pre}-v${i}" style="${i === 0 ? "" : "background:#fff"}">0%</span></div></div><div class="blab" id="${pre}-bl${i}" style="left:${xs[i] - 330}px;top:${base + 30}px;width:660px">${b.label}</div>`;
      const hh = MAXH * b.pct / 100;
      tw.push(`const ${o}={v:0};`, `tl.fromTo("#${pre}-b${i}",{top:${base},height:0},{top:${f3(base - hh)},height:${f3(hh)},duration:0.7,ease:"power2.out"},${f3(t0)});`,
        `tl.fromTo(${o},{v:0},{v:${b.pct},duration:0.7,ease:"power2.out",onUpdate:function(){var e=document.getElementById("${pre}-v${i}");if(e)e.textContent=Math.round(${o}.v)+"%";}},${f3(t0)});`);
      tw.push(`tl.set("#${pre}-v${i}",{opacity:0},0);`, `tl.set("#${pre}-v${i}",{opacity:1},${f3(t0)});`);
    });
    if (d.rack) { const tr = at("rack", 0); const f0 = d.rackFirst || 0, f1 = 1 - f0; tw.push(`tl.set("#${pre}-bl${f0}",{filter:"blur(0px)",opacity:1},0);`, `tl.set("#${pre}-bl${f1}",{filter:"blur(12px)",opacity:0.45},0);`, `tl.to("#${pre}-bl${f0}",{filter:"blur(12px)",opacity:0.45,duration:0.35,ease:"power2.inOut"},${f3(tr)});`, `tl.to("#${pre}-bl${f1}",{filter:"blur(0px)",opacity:1,duration:0.35,ease:"power2.inOut"},${f3(tr)});`); }
    if (d.badge) { const tb = at("badge", 0); h += `<div class="topbadge" id="${pre}-tb">${d.badge.map((p) => (p.b ? `<span class="badge ${p.b}">${p.t}</span>` : `<span>${p.t}</span>`)).join("")}</div>`; tw.push(`tl.set("#${pre}-tb",{opacity:0},0);`, `tl.fromTo("#${pre}-tb",{opacity:0,scale:0.8},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.4)"},${f3(tb)});`); }
    return { html: h + `</div>`, tw };
  }
  if (d.kind === "lines") {
    const X0 = 260, X1 = 1660, A = `M${X0} 270 C 620 300, 900 640, ${X1} 720`, B = `M${X0} 750 C 760 730, 1100 300, ${X1} 235`;
    const t0 = at("draw", 0);
    const bez = (p, t) => { const m = 1 - t; return [m ** 3 * p[0][0] + 3 * m * m * t * p[1][0] + 3 * m * t * t * p[2][0] + t ** 3 * p[3][0], m ** 3 * p[0][1] + 3 * m * m * t * p[1][1] + 3 * m * t * t * p[2][1] + t ** 3 * p[3][1]]; };
    const pa = [[X0, 270], [620, 300], [900, 640], [X1, 720]], pb = [[X0, 750], [760, 730], [1100, 300], [X1, 235]];
    let cross = [1000, 500], best = 1e9; for (let i = 0; i <= 400; i++) { const a = bez(pa, i / 400); for (let j = 0; j <= 400; j++) { const b = bez(pb, j / 400); const dd = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2; if (dd < best) { best = dd; cross = a; } } }
    const h = `<div class="fill diag">${svgWrap(`<line x1="200" y1="900" x2="1720" y2="900" stroke="${INK}" stroke-width="9" stroke-linecap="round"/><path d="M1700 876 L1735 900 L1700 924" fill="none" stroke="${INK}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><line x1="200" y1="150" x2="200" y2="900" stroke="${INK}" stroke-width="9" stroke-linecap="round"/>
    <path id="${pre}-A" d="${A}" fill="none" stroke="${TERRA}" stroke-width="16" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/><path id="${pre}-B" d="${B}" fill="none" stroke="${RED}" stroke-width="16" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>`)}
    <div class="ctitle">REGRET OVER TIME</div><div class="axl" style="left:200px;top:925px">TODAY</div><div class="axl" style="left:1220px;top:925px;width:500px;text-align:right">YEARS LATER</div>
    <div class="llab" id="${pre}-LA" style="left:300px;top:180px;color:${TERRA}">THINGS I DID</div><div class="llab" id="${pre}-LB" style="left:300px;top:790px;color:${RED}">THINGS I DIDN'T DO</div>
    <div class="tag" id="${pre}-fade" style="left:1400px;top:760px"><span class="badge yellow">FADE</span></div><div class="tag" id="${pre}-grow" style="left:1380px;top:90px"><span class="badge red">GROW</span></div>
    <div class="sweep" id="${pre}-sw" style="left:${f3(cross[0] - 150)}px;top:${f3(cross[1] - 150)}px"></div></div>`;
    const dd = d.drawDur || 1.5;
    tw.push(`tl.to("#${pre}-A",{strokeDashoffset:0,duration:${dd},ease:"power1.inOut"},${f3(t0)});`, `tl.to("#${pre}-B",{strokeDashoffset:0,duration:${dd},ease:"power1.inOut"},${f3(t0)});`);
    tw.push(`tl.set("#${pre}-LA,#${pre}-LB",{opacity:0},0);`, `tl.to("#${pre}-LA,#${pre}-LB",{opacity:1,duration:0.4},${f3(t0)});`);
    for (const k of ["fade", "grow"]) { const tg = at(k, 0); tw.push(`tl.set("#${pre}-${k}",{opacity:0},0);`, `tl.fromTo("#${pre}-${k}",{opacity:0,scale:0.6},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.6)"},${f3(tg)});`); }
    if (d.sweep) tw.push(`tl.set("#${pre}-sw",{opacity:0},0);`, `tl.fromTo("#${pre}-sw",{opacity:1,x:-420,rotation:25},{x:420,duration:0.9,ease:"power1.inOut"},${f3(t0 + dd * 0.4)});`, `tl.set("#${pre}-sw",{opacity:0},${f3(t0 + dd * 0.4 + 0.9)});`);
    return { html: h, tw };
  }
  if (d.kind === "split") {
    const tl0 = at("left", 0), tr0 = at("right", 0), tr = at("rack", tr0);
    const h = `<div class="fill diag"><div class="half" id="${pre}-L" style="left:0"><div class="ln" style="font-size:${d.fs || 128}px">${d.left[0]}</div><div class="ln" style="font-size:${d.fs || 128}px"><span class="badge yellow">${d.left[1]}</span></div></div><div class="vdiv"></div><div class="half" id="${pre}-R" style="left:960px"><div class="ln" style="font-size:${d.fs || 128}px">${d.right[0]}</div><div class="ln" style="font-size:${d.fs || 128}px"><span class="badge red">${d.right[1]}</span></div></div>${d.at.sign ? `<div class="splsign" id="${pre}-sg" style="font-size:${d.fs ? 100 : 170}px;top:${d.fs ? 450 : 420}px"><span class="badge yellow">≈</span></div>` : ""}</div>`;
    tw.push(`tl.set("#${pre}-L",{opacity:0},0);`, `tl.set("#${pre}-R",{opacity:0},0);`, `tl.fromTo("#${pre}-L",{opacity:0,scale:0.9},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.4)"},${f3(tl0)});`,
      `tl.fromTo("#${pre}-R",{opacity:0,scale:0.9},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.4)"},${f3(tr0)});`,
      ...(d.norack ? [] : [`tl.to("#${pre}-L",{filter:"blur(10px)",opacity:0.5,duration:0.35,ease:"power2.inOut"},${f3(tr + 0.3)});`]));
    if (d.at.sign) { const ts = at("sign", 0); tw.push(`tl.set("#${pre}-sg",{opacity:0},0);`, `tl.fromTo("#${pre}-sg",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.8)"},${f3(ts)});`); sfx.push({ t: f3(ts), kind: "ding" }); }
    return { html: h, tw };
  }
  if (d.kind === "irow") {
    d.items.forEach((it) => usedIcons.add(it.icon));
    let h = `<div class="fill diag"><div class="irow2">${d.items.map((it, k) => `<div class="icol" id="${pre}-ic${k}"><div class="itile"><img src="assets/icons/${it.icon}.jpg" alt=""></div>${it.label ? `<div class="ilab">${it.label}</div>` : ""}</div>`).join("")}</div>${d.under ? `<div class="under" id="${pre}-un">${d.under.html}</div>` : ""}</div>`;
    d.items.forEach((it, k) => { const t0 = T(it.word); tw.push(`tl.set("#${pre}-ic${k}",{opacity:0},0);`, `tl.fromTo("#${pre}-ic${k}",{opacity:0,scale:0.92},{opacity:1,scale:1,duration:0.25,ease:"back.out(1.4)"},${f3(t0)});`); sfx.push({ t: f3(t0), kind: "pop" }); });
    if (d.under) { const t0 = T(d.under.word); tw.push(`tl.set("#${pre}-un",{opacity:0},0);`, `tl.fromTo("#${pre}-un",{opacity:0,y:30},{opacity:1,y:0,duration:0.3,ease:"back.out(1.4)"},${f3(t0)});`); }
    return { html: h, tw };
  }
  if (d.kind === "quad") {
    const COL = [SKY, SAGE, YEL, ORG]; let h = `<div class="fill diag">`;
    d.tiles.forEach((tt, i) => { usedIcons.add(tt.icon); const x = 110 + (i % 2) * 900, y = 130 + Math.floor(i / 2) * 460;
      h += `<div class="qtile" id="${pre}-q${i}" style="left:${x}px;top:${y}px;background:${COL[i]}"><div class="qic"><img src="assets/icons/${tt.icon}.jpg" alt=""></div><div class="qlab">${tt.label}</div></div>`; });
    d.tiles.forEach((tt, i) => { if (!tt.word) return; const t0 = T(tt.word); tw.push(`tl.set("#${pre}-q${i}",{opacity:0},0);`, `tl.fromTo("#${pre}-q${i}",{opacity:0,scale:0.8},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.6)"},${f3(t0)});`); sfx.push({ t: f3(t0), kind: "pop" }); });
    if (d.active) { const t0 = T(d.active.word); d.tiles.forEach((tt, i) => tw.push(`tl.fromTo("#${pre}-q${i}",{opacity:1,scale:1},{opacity:${i === d.active.idx ? 1 : 0.4},scale:${i === d.active.idx ? 1.05 : 1},duration:0.3,ease:"power2.out"},${f3(t0)});`)); sfx.push({ t: f3(t0), kind: "pop" }); }
    if (d.pulse) { const t0 = T(d.pulse); d.tiles.forEach((tt, i) => tw.push(`tl.fromTo("#${pre}-q${i}",{scale:1},{scale:1.07,duration:0.16,ease:"power2.out"},${f3(t0)});`, `tl.to("#${pre}-q${i}",{scale:1,duration:0.24,ease:"power2.in"},${f3(t0 + 0.16)});`)); sfx.push({ t: f3(t0), kind: "pop" }); }
    return { html: h + `</div>`, tw };
  }
  if (d.kind === "list") {
    const COL = [YEL, SKY, ORG, SAGE]; let h = `<div class="fill diag">`;
    d.items.forEach((it, i) => { h += `<div class="lrow" id="${pre}-r${i}" style="top:${110 + i * 190}px"><span class="lpill" style="background:${COL[i % 4]}">${it.t}</span></div>`; });
    d.items.forEach((it, i) => { const t0 = T(it.word); tw.push(`tl.set("#${pre}-r${i}",{opacity:0},0);`, `tl.fromTo("#${pre}-r${i}",{opacity:0,x:-120},{opacity:1,x:0,duration:0.3,ease:"back.out(1.5)"},${f3(t0)});`); sfx.push({ t: f3(t0), kind: "click" }); });
    if (d.stamp) { const t0 = T(d.stamp.word); h += `<div class="stamp" id="${pre}-st">${d.stamp.text}</div>`; tw.push(`tl.set("#${pre}-st",{opacity:0},0);`, `tl.fromTo("#${pre}-st",{opacity:0,scale:1.7,rotation:-2},{opacity:1,scale:1,rotation:-8,duration:0.26,ease:"back.out(1.5)"},${f3(t0)});`); sfx.push({ t: f3(t0), kind: "ding" }); }
    return { html: h + `</div>`, tw };
  }
  if (d.kind === "bars2") {
    const base = 860, MAXH = 520, xs = [620, 1300], BW = 400, hs = [MAXH, 200], cols = [RED, SAGE], t0 = at("grow", 0);
    let h = `<div class="fill diag"><div class="topbadge" id="${pre}-hd">HARVARD DIARY STUDY</div><div class="topbadge" id="${pre}-tb"><span class="badge yellow" id="${pre}-cnt">0</span><span>DIARY ENTRIES</span></div>`;
    d.bars.forEach((b, i) => { h += `<div class="bar" id="${pre}-b${i}" style="left:${xs[i] - BW / 2}px;top:${base}px;width:${BW}px;height:0px;background:${cols[i]}"></div><div class="blab" id="${pre}-bl${i}" style="left:${xs[i] - 330}px;top:${base + 28}px;width:660px">${b}</div>`;
      tw.push(`tl.set("#${pre}-b${i},#${pre}-bl${i}",{opacity:0},0);`, `tl.set("#${pre}-b${i},#${pre}-bl${i}",{opacity:1},${f3(t0)});`, `tl.fromTo("#${pre}-b${i}",{top:${base},height:0},{top:${base - hs[i]},height:${hs[i]},duration:0.7,ease:"power2.out"},${f3(t0)});`); });
    h += `<div class="ratio" id="${pre}-ra"><span class="badge yellow">2–3×</span></div>${d.small ? `<div class="dsmall">${d.small}</div>` : ""}</div>`;
    const tc = at("count", 0), o = vid(`${pre}_c`);
    tw.push(`const ${o}={v:0};`, `tl.to("#${pre}-hd",{opacity:0,duration:0.15},${f3(tc - 0.05)});`, `tl.set("#${pre}-tb",{opacity:0},0);`, `tl.fromTo("#${pre}-tb",{opacity:0,scale:0.85},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.4)"},${f3(tc)});`,
      `tl.fromTo(${o},{v:0},{v:12000,duration:1.3,ease:"power2.out",onUpdate:function(){var e=document.getElementById("${pre}-cnt");if(e)e.textContent=Math.round(${o}.v).toLocaleString("en-US");}},${f3(tc)});`);
    const tb = at("badge", 0); tw.push(`tl.set("#${pre}-ra",{opacity:0},0);`, `tl.fromTo("#${pre}-ra",{opacity:0,scale:1.6,rotation:-2},{opacity:1,scale:1,rotation:-7,duration:0.26,ease:"back.out(1.6)"},${f3(tb)});`);
    sfx.push({ t: f3(tc), kind: "pop" }, { t: f3(t0), kind: "swoosh" });
    return { html: h, tw };
  }
  if (d.kind === "quote") {
    const wordsHtml = d.html;
    const h = `<div class="fill diag"><div class="qmark">&ldquo;</div><div class="qtext" id="${pre}-q">${wordsHtml}</div><div class="qby">${d.by}</div></div>`;
    d.times.forEach((t, i) => tw.push(`tl.fromTo("#${pre}-w${i}",{y:44,opacity:0},{y:0,opacity:1,duration:0.32,ease:"power2.out"},${f3(t - 0.04)});`));
    return { html: h, tw };
  }
  throw new Error("diagram " + d.kind);
}
function screenOv(id, o, host) {
  const ul = o.ul ? `<svg class="ulp" viewBox="0 0 400 30" preserveAspectRatio="none"><path id="${id}-ul" d="M6 18 C60 6 110 26 170 14 S300 8 394 16" fill="none" stroke="${RED}" stroke-width="9" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>` : "";
  if (o.type === "step") return `<div id="${id}" class="scr${host ? " row" : ""}" data-layout-allow-overlap><div class="pill big">${o.step}</div><div class="spill2">${o.text}</div></div>`;
  if (o.type === "sbadge") return `<div id="${id}" class="scr" data-layout-allow-overlap><span class="badge yellow" style="font-size:78px;padding:0 38px 8px">${o.text}</span></div>`;
  if (o.type === "pill") return `<div id="${id}" class="scr${host ? " row" : ""}" data-layout-allow-overlap><div class="pill big">${o.text}</div></div>`;
  return `<div id="${id}" class="scr" data-layout-allow-overlap><div class="spill2">${o.text}${ul}</div></div>`;
}
function picOv(id, o) {
  const b = o.box, pos = b ? `left:${f3(b.x * 1920)}px;top:${f3(b.y * 1080)}px;width:${f3(b.w * 1920)}px;height:${f3(b.h * 1080)}px` : "";
  if (o.type === "bubble") return `<div id="${id}" class="sbub" data-layout-allow-overlap style="${pos}"><span>${o.text}</span><i></i></div>`;
  if (o.type === "sign") return `<div id="${id}" class="sign" data-layout-allow-overlap style="${pos};transform:rotate(${o.rot || 0}deg);font-size:${o.fs || 64}px">${o.text}</div>`;
  if (o.type === "sweep") return `<div id="${id}" class="sweepbox" data-layout-allow-overlap style="${pos}"><div id="${id}-b" class="sweepband"></div></div>`;
  if (o.type === "badge") return `<div id="${id}" class="tagbox" data-layout-allow-overlap style="${pos};font-size:${o.fs || 110}px"><span class="badge ${o.badge}" id="${id}-t">${o.text}</span></div>`;
  if (o.type === "wheel") return `<div id="${id}" class="tagbox" data-layout-allow-overlap style="${pos};font-size:230px"><span class="badge yellow wheel" id="${id}-t" style="display:flex">${[0, 1, 2].map((k) => `<span class="dig"><span class="col" id="${id}-c${k}">${[0, 1, 2, 3, 4, 5, 6, 7, 8, 9].map((x) => `<span>${x}</span>`).join("")}</span></span>`).join("")}</span></div>`;
  if (o.type === "circle") return `<svg id="${id}" class="ovsvg" data-layout-allow-overlap viewBox="0 0 1920 1080"><ellipse id="${id}-e" cx="${f3(o.cx * 1920)}" cy="${f3(o.cy * 1080)}" rx="${f3(o.rx * 1920)}" ry="${f3(o.ry * 1080)}" transform="rotate(-4 ${f3(o.cx * 1920)} ${f3(o.cy * 1080)})" fill="none" stroke="${RED}" stroke-width="12" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>${o.label ? `<div id="${id}-lab" class="clab" data-layout-allow-overlap style="left:${f3((o.lx ?? o.cx) * 1920)}px;top:${f3((o.ly ?? o.cy + o.ry + 0.03) * 1080)}px"><span class="badge yellow" style="font-size:68px;padding:0 28px 8px">${o.label}</span></div>` : ""}`;
  if (o.type === "arrow") { const x0 = o.x0 * 1920, y0 = o.y0 * 1080, x1 = o.x1 * 1920, y1 = o.y1 * 1080, a = Math.atan2(y1 - y0, x1 - x0), hl = 60; const hx = (s) => f3(x1 - hl * Math.cos(a + s)), hy = (s) => f3(y1 - hl * Math.sin(a + s));
    return `<svg id="${id}" class="ovsvg" data-layout-allow-overlap viewBox="0 0 1920 1080"><path id="${id}-e" d="M${f3(x0)} ${f3(y0)} Q${f3((x0 + x1) / 2 + 40)} ${f3((y0 + y1) / 2 - 60)} ${f3(x1)} ${f3(y1)} M${hx(0.5)} ${hy(0.5)} L${f3(x1)} ${f3(y1)} L${hx(-0.5)} ${hy(-0.5)}" fill="none" stroke="${RED}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>`; }
  throw new Error("pic overlay " + o.type);
}

// ---------- planning ----------
const scenes = cfg.scenes.map((sc, i) => ({ ...sc, t: tim.scenes[i] }));
const LIM = { icon: [1.5, 3.0], card: [1.5, 2.5], pop: [2.0, 4.0], crop: [1.5, 3.5], iconrow: [1.5, 4.0] };

function planScene(sc, i) {
  const t = sc.t, S = t.start, E = t.end, ws = t.words;
  const W = (word, occ = 1) => { const n = norm(word); let c = 0; for (let k = 0; k < ws.length; k++) if (ws[k].w === n && ++c === occ) return k; throw new Error(`${sc.id}: word not found: ${word} #${occ}`); };
  const cutAt = (k) => { if (k <= 0) return S; if (k >= ws.length) return E; const w = ws[k], p = ws[k - 1]; let c = w.s - 0.04; if (c < p.e) c = Math.min(p.e + 0.005, w.s); return c; };
  const gapBefore = (k) => (k <= 0 ? 1 : ws[k].s - ws[k - 1].e);
  const nocut = (sc.moves || []).map((m) => { const x = cutAt(W(m.word, m.occ || 1)); return [x + 0.01, x + 0.4]; }); // a cut exactly at a move start is fine
  const okCut = (x) => !nocut.some(([a, b]) => x > a && x < b);
  const tt = (sc.events || []).find((x) => x.kind === "title"), limit = tt ? E - tt.dur : E;
  const order = (sc.events || []).map((e) => ({ e, k: e.kind === "title" ? 1e9 : e.kind === "quote" ? W(e.word, e.occ || 1) - 1 : W(e.word, e.occ || 1) })).sort((x, y) => x.k - y.k);
  const evs = [];
  for (const { e, k } of order) {
    if (e.kind === "title") { const prev = evs[evs.length - 1]; if (prev && prev.e > E - e.dur) { warn.push(`${sc.id}: dropped ${prev.kind} (${prev.word}) for title`); evs.pop(); } evs.push({ ...e, a: E - e.dur, e: E }); continue; }
    if (e.kind === "quote") { evs.push({ ...e, a: cutAt(k), e: cutAt(W(e.until, e.untilOcc || 1)), k }); continue; }
    const [mn, mx] = LIM[e.kind];
    let a = cutAt(k); if (a - S < 1.0) a = S;
    const prev = evs[evs.length - 1];
    if (prev) {
      const cls = (x) => (x.kind === "card" || (x.kind === "pop" && x.content.type === "card") ? "card" : x.kind === "icon" || x.kind === "iconrow" || (x.kind === "pop" && x.content.type === "icon") ? "icon" : x.kind);
      const sameKind = cls(prev) === cls(e) && (cls(e) === "card" || cls(e) === "icon"); // never two icons / two text cards in a row
      const need = prev.e + (sameKind ? (cls(e) === "icon" ? 0.3 : 0.4) : 0);
      if (a < need - 0.001) {
        let j = k; while (j < ws.length && cutAt(j) < need - 0.001) j++;
        if (j >= ws.length || cutAt(j) - a > 1.0) { warn.push(`${sc.id}: dropped ${e.kind} "${e.word}" (too close to ${prev.kind} ${prev.word})`); continue; }
        warn.push(`${sc.id}: ${e.kind} "${e.word}" delayed ${f3(cutAt(j) - a)}s after ${prev.kind} ${prev.word}`); a = cutAt(j);
      }
    }
    let best = null;
    if (e.kind === "iconrow") { const kl = W(e.items[e.items.length - 1].word); let j = Math.min(kl + 2, ws.length); best = { j, d: cutAt(j) - a }; }
    else for (let j = 1; j <= ws.length; j++) { const d = cutAt(j) - a; if (cutAt(j) > a && cutAt(j) <= limit + 0.01 && d >= mn && d <= mx && (!best || Math.abs(d - e.dur) < Math.abs(best.d - e.dur))) best = { j, d }; }
    let end;
    if (best) end = cutAt(best.j);
    else { let j = 1; while (j <= ws.length && (cutAt(j) <= a || cutAt(j) - a < mn)) j++; end = j <= ws.length ? cutAt(j) : E; if (end - a > mx + 0.05) end = Math.min(E, a + Math.min(mx, e.dur + 0.3)); }
    if (end > limit) end = limit;
    else if (limit - end < 0.9) { if (limit - a <= mx + 0.3) end = limit; else { let b = null; for (let j = 1; j <= ws.length; j++) { const x = cutAt(j); if (x > a + mn - 0.001 && x <= limit - 0.9) b = x; } if (b) end = b; } }
    evs.push({ ...e, a, e: end, k });
  }
  let T = Infinity;
  if (sc.swap) { T = cutAt(W(sc.swap.word, sc.swap.occ || 1)); const inside = evs.find((e) => T > e.a && T < e.e); if (inside) T = inside.e; }
  const gaps = []; let cur = S;
  for (const ev of evs) { if (ev.a - cur > 0.05) gaps.push([cur, ev.a]); cur = ev.e; }
  const tailStart = cur;
  const splitGap = (g0, g1) => {
    const res = []; let c = g0;
    while (g1 - c > MAXSHOT - 0.05) {
      let cands = [];
      for (let j = 1; j < ws.length; j++) { const x = cutAt(j); if (okCut(x) && x >= c + 1.8 && x <= c + 3.8 && g1 - x >= 1.0) cands.push({ x, sc: gapBefore(j) * 2 - Math.abs(x - (c + 3.2)) * 0.6 }); }
      if (!cands.length) for (let j = 1; j < ws.length; j++) { const x = cutAt(j); if (okCut(x) && x >= c + 1.0 && x <= c + 3.9 && g1 - x >= 0.8) cands.push({ x, sc: gapBefore(j) * 2 - Math.abs(x - (c + 3.2)) * 0.6 }); }
      let x;
      if (cands.length) { cands.sort((p, q) => q.sc - p.sc); x = cands[0].x; } else { x = c + 3.5; warn.push(`${sc.id}: cut in silence at ${f3(x)}`); }
      res.push([c, x]); c = x;
    }
    res.push([c, g1]); return res;
  };
  let hold = null;
  if (sc.holdEnd) { const lastEnd = ws[ws.length - 1].e + 0.3; if (E - lastEnd > 1) hold = [lastEnd, E]; }
  if (E - tailStart > 0.05) { const g1 = hold ? hold[0] : E; if (g1 - tailStart > 0.05) gaps.push([tailStart, g1]); }
  const shotsOut = [];
  const picAt = (a) => (a >= T - 0.01 && (sc.pictureB || sc.diagramB) ? "B" : "A");
  const picName = (side) => (side === "B" ? sc.pictureB : sc.picture);
  const pushGap = (g0, g1) => {
    let parts = [[g0, g1]];
    if (T > g0 + 0.6 && T < g1 - 0.6) parts = [[g0, T], [T, g1]];
    for (const [p0, p1] of parts) for (const [a, e] of splitGap(p0, p1)) { const side = picAt(a); shotsOut.push({ a, e, type: "main", side, pic: picName(side) }); }
  };
  const all = [];
  for (const g of gaps) all.push({ g });
  for (const ev of evs) all.push({ ev });
  all.sort((x, y) => (x.g ? x.g[0] : x.ev.a) - (y.g ? y.g[0] : y.ev.a));
  for (const it of all) {
    if (it.g) pushGap(...it.g);
    else { const ev = it.ev, side = picAt(ev.a); shotsOut.push({ a: ev.a, e: ev.e, type: ev.kind, ev, side, pic: picName(side) }); }
  }
  if (hold) shotsOut.push({ a: hold[0], e: hold[1], type: "main", side: picAt(hold[0]), pic: picName(picAt(hold[0])), hold: true, exempt: true });
  shotsOut.sort((x, y) => x.a - y.a);
  shotsOut[0].a = S; for (let k = 1; k < shotsOut.length; k++) shotsOut[k].a = shotsOut[k - 1].e;
  shotsOut[shotsOut.length - 1].e = E;
  return { shots: shotsOut, ws, W, cutAt, T };
}

// ---------- build ----------
const planned = scenes.map((sc, i) => ({ sc, ...planScene(sc, i) }));
const G = []; // global shot list
planned.forEach((P, i) => P.shots.forEach((sh, si) => { sh.si = si; sh.P = P; sh.i = i; sh.sid = `${P.sc.id.toLowerCase()}-s${si}`; G.push(sh); }));
// transitions
const TRANS = { push: 0.4, whip: 0.3, fade: 0.25, iris: 0.5 };
G.forEach((sh, gi) => {
  const sc = sh.P.sc; let tr = null;
  if (sh.si === 0 && gi > 0 && sc.trans && sc.trans !== "cut") tr = { kind: sc.trans, dur: TRANS[sc.trans], pt: sc.irisAt || [0.5, 0.5] };
  if (sc.swap && sc.swap.kind === "iris" && sh.side === "B" && sh.si > 0 && G[gi - 1].side === "A" && G[gi - 1].P === sh.P) tr = { kind: "iris", dur: TRANS.iris, pt: sc.swap.pt || [0.5, 0.5] };
  sh.trans = tr;
  if (tr && gi > 0) G[gi - 1].ext = Math.max(G[gi - 1].ext || 0, tr.dur);
});
// iris reveal into a scene start from a given word (R61): scene.irisWord => the first main shot after that word iris-reveals
G.forEach((sh, gi) => { const sc = sh.P.sc; if (sc.irisWord && sh.type === "main" && !sh.trans && gi > 0) { const k = sh.P.W(sc.irisWord.word, sc.irisWord.occ || 1), x = sh.P.cutAt(k); if (Math.abs(sh.a - x) < 0.05) { sh.trans = { kind: "iris", dur: TRANS.iris, pt: sc.irisWord.pt || [0.5, 0.5] }; G[gi - 1].ext = Math.max(G[gi - 1].ext || 0, 0.5); } } });

let z = 10;
const impacts = [], narrSeg = [];
const overlayWin = (sc, ws, W, o) => { const k = W(o.word, o.occ || 1); const t0 = ws[k].s - 0.05; let t1 = o.until ? ws[W(o.until, o.untilOcc || 1)].s : t0 + (o.dur || (sc.host ? 99 : 6)); return [t0, Math.min(t1, sc.t.end)]; };

// camera script for a scene: returns per-shot list of keyframes
function cameraPlan(P) {
  const sc = P.sc, { ws, W, cutAt } = P, shots = P.shots;
  const foci = sc.foci || (sc.picture ? FOC[sc.picture] : null) || [];
  const explicit = (sc.moves || []).map((m) => ({ t: m.kind === "slow" ? ws[W(m.word, m.occ || 1)].s : cutAt(W(m.word, m.occ || 1)), kind: m.kind, f: m.f, dur: m.dur, blur: m.blur }));
  const kfs = []; let st = FULL, prev = null, autoIdx = 0, mainRun = 0;
  const drift = sc.camera || "zoom-in";
  shots.forEach((sh, si) => {
    const plan = { kfs: [], start: st };
    if (sh.type === "main" || sh.type === "crop") {
      if (prev && prev.side !== sh.side) { st = FULL; plan.start = FULL; }
      const mine = explicit.filter((m) => m.t >= sh.a - 0.001 && m.t < sh.e - 0.05);
      if (sh.type === "crop") { plan.kfs.push({ t: sh.a, kind: "snap", f: sh.ev.focus }); st = sh.ev.focus; plan.start = FULL; }
      else if (!explicit.length) {
        const afterEvent = prev && prev.type !== "main" && prev.type !== "crop";
        if (afterEvent || !prev) { if (st !== FULL) { plan.start = FULL; st = FULL; } mainRun = 0; }
        else if (!sh.hold && sc.picture && foci.length) { mainRun++; if (st === FULL) { const f = foci[autoIdx++ % foci.length]; plan.kfs.push({ t: sh.a, kind: "snap", f }); st = f; } else { plan.kfs.push({ t: sh.a, kind: "zoom", f: FULL }); st = FULL; } }
      }
      for (const m of mine) { plan.kfs.push(m); if (m.f) st = m.f; }
      plan.end = st;
    }
    else for (const m of explicit) if (m.t >= sh.a - 0.001 && m.t < sh.e && m.f) st = m.f;
    sh.cam = plan; prev = sh;
  });
}
planned.forEach(cameraPlan);

// ---- emit shots
const allSfxSwap = [];
G.forEach((sh, gi) => {
  const P = sh.P, sc = P.sc, { ws, W } = P, i = sh.i, id = sh.sid, a = sh.a, e = sh.e, d = e - a, host = !!sc.host && sh.type !== "title";
  const first = sh.si === 0, zi = ++z;
  const tr = sh.trans, ext = sh.ext || 0, cd = d + ext;
  const prevSh = gi > 0 ? G[gi - 1] : null;
  if (d > MAXSHOT + 0.02 && !sh.exempt && sh.type !== "title" && sh.type !== "iconrow" && !(sh.type === "quote" && d <= 7.05)) warn.push(`${sc.id}: shot ${f3(a)}-${f3(e)} (${sh.type}) is ${f3(d)}s`);
  if (sh.type === "icon" && d > 3.05 || sh.type === "card" && d > 2.55) warn.push(`${sc.id}: ${sh.type} lasts ${f3(d)}s`);
  if (gi > 0) {
    let bi = 0; ws.forEach((w, k) => { if (Math.abs(w.s - a) < Math.abs(ws[bi].s - a)) bi = k; });
    let bd = Math.abs(ws[bi].s - a), bw = ws[bi].w;
    if (first) { bw = ws[0].w; bd = Math.abs(ws[0].s - a); if (sc.lead) bd = 0; }
    cutRows.push({ t: a, word: bw, delta: bd, kind: sh.type, scene: sc.id });
    if (bd > 0.1) warn.push(`${sc.id}: cut ${f3(a)} is ${f3(bd)}s from word "${bw}" (${sh.type})`);
  }
  // ---- content
  let content = "", extra = "";
  const pre = id;
  const T = (w) => { if (typeof w === "number") return w; const k = W(w.word, w.occ || 1); return ws[k].s - (w.off ?? 0.03); };
  const mapAt = (dg) => { if (!dg.at) return dg; const r = { ...dg, at: {} }; for (const [k, v] of Object.entries(dg.at)) r.at[k] = T(v); return r; };
  if (sh.type === "main" || sh.type === "crop") {
    const isDiag = !!sc.diagram && !(sh.side === "B" && sc.pictureB && !sc.diagramB), dg = isDiag ? (sh.side === "B" && sc.diagramB ? sc.diagramB : sc.diagram) : null;
    const ovs = (sc.overlays || []).map((o, k) => [o, k]);
    const picOvs = ovs.filter(([o]) => !SCREEN.has(o.type)), scrOvs = ovs.filter(([o]) => SCREEN.has(o.type));
    let inner;
    const picHtml = picOvs.map(([o, k]) => picOv(`${id}-ov${k}`, o)).join("");
    if (isDiag) { const dr = diagram(mapAt({ ...dg, rise: sh.side === "B" ? P.T : undefined }), `${id}-dg`, T, sc.t.start); inner = dr.html + picHtml; dr.tw.forEach((x) => tl.push(x)); }
    else { usedPics.add(sh.pic); inner = `<img src="assets/pictures/${sh.pic}.jpg" class="pic" alt="">${picHtml}`; }
    content = `<div id="${id}-cam" class="cam">${sc.bleed ? `<div class="bleed" style="background:${sc.bleed}"></div>` : ""}${inner}</div>`;
    extra = scrOvs.map(([o, k]) => screenOv(`${id}-so${k}`, o, host)).join("");
    // camera tweens
    if (!isDiag || sc.camMove) {
      const cp = sh.cam; let cur = cp.start, tcur = a; const drv = sc.camera || "zoom-in";
      tl.push(`tl.set("#${id}-cam",{${trSt(cp.start, 1, !sc.bleed)}},${f3(a)});`);
      let lastEnd = a;
      for (const kf of cp.kfs) {
        const dd = kf.kind === "snap" ? 0.25 : kf.kind === "whip" ? (kf.dur || 0.26) : kf.kind === "zoom" ? 0.4 : kf.kind === "slow" ? (kf.dur || 2) : 0.0001;
        const ease = kf.kind === "snap" ? "expo.out" : kf.kind === "whip" ? "power3.inOut" : kf.kind === "slow" ? "power1.inOut" : "power2.out";
        const start = Math.max(kf.t, a);
        if (kf.kind === "cut") tl.push(`tl.set("#${id}-cam",{${trSt(kf.f, 1, !sc.bleed)}},${f3(start)});`);
        else tl.push(`tl.fromTo("#${id}-cam",{${trSt(cur, 1, !sc.bleed)}},{${trSt(kf.f, 1, !sc.bleed)},duration:${dd},ease:"${ease}"},${f3(start)});`);
        if (kf.kind === "whip" && kf.blur !== false) {
          tl.push(`tl.set("#${id}-cam",{filter:"url(#mb)"},${f3(start)});`, `tl.fromTo("#mbb",{attr:{stdDeviation:"0 0"}},{attr:{stdDeviation:"38 0"},duration:${f3(dd / 2)},ease:"power2.in"},${f3(start)});`, `tl.to("#mbb",{attr:{stdDeviation:"0 0"},duration:${f3(dd / 2)},ease:"power2.out"},${f3(start + dd / 2)});`, `tl.set("#${id}-cam",{filter:"none"},${f3(start + dd + 0.02)});`);
        }
        if (kf.kind === "whip" || (kf.kind === "snap")) sfx.push({ t: f3(start), kind: kf.kind === "whip" ? "swoosh" : "pop" });
        cur = kf.f; lastEnd = start + dd;
      }
      if (cp.kfs.length === 0 && !sh.hold && !(cur === FULL && drv.startsWith("pan"))) { /* plain drift below */ }
      if (!sh.hold && e - lastEnd > 0.4) {
        const zf = drv === "zoom-out" && cur === FULL ? [1.015, 1] : [1, 1.015];
        if (drv.startsWith("pan") && cur === FULL) tl.push(`tl.fromTo("#${id}-cam",{x:${drv === "pan-right" ? -2 : -26},y:${trSt(FULL, 1.015).match(/y:(-?[\d.]+)/)[1]},scale:1.015},{x:${drv === "pan-right" ? -26 : -2},duration:${f3(e - lastEnd)},ease:"none"},${f3(lastEnd)});`);
        else tl.push(`tl.fromTo("#${id}-cam",{${trSt(cur, zf[0], !sc.bleed)}},{${trSt(cur, zf[1], !sc.bleed)},duration:${f3(e - lastEnd)},ease:"none"},${f3(lastEnd)});`);
      }
    }
    if (sc.unroll) { const tu = ws[W(sc.unroll.word, sc.unroll.occ || 1)].s; tl.push(`tl.fromTo("#${id}-cam",{clipPath:"inset(0% 0% ${sc.unroll.from || 62}% 0%)"},{clipPath:"inset(0% 0% 0% 0%)",duration:0.6,ease:"power2.out"},${f3(tu)});`); if (tu >= a && tu < e) sfx.push({ t: f3(tu), kind: "swoosh" }); }
    // overlays timing
    for (const [o, k] of picOvs) {
      let w0 = ws[W(o.word, o.occ || 1)].s - 0.05; const oid = `${id}-ov${k}`;
      const cov = G.find((s2) => s2.P === P && s2.type !== "main" && s2.type !== "crop" && s2.type !== "title" && w0 >= s2.a - 0.001 && w0 < s2.e - 0.25); if (cov) w0 = cov.e + 0.05;
      if (o.type === "sweep") { tl.push(`tl.fromTo("#${oid}-b",{x:-900,opacity:1},{x:1300,duration:0.9,ease:"power1.inOut"},${f3(w0)});`, `tl.set("#${oid}-b",{opacity:0},${f3(w0 + 0.95)});`, `tl.set("#${oid}-b",{opacity:0},0);`); sfx.push({ t: f3(w0), kind: "swoosh" }); continue; }
      if (o.type === "circle" || o.type === "arrow") { tl.push(`tl.set("#${oid}",{opacity:0},0);`, `tl.set("#${oid}",{opacity:1},${f3(w0)});`, `tl.to("#${oid}-e",{strokeDashoffset:0,duration:0.55,ease:"power2.out"},${f3(w0)});`); if (o.label) tl.push(`tl.set("#${oid}-lab",{opacity:0},0);`, `tl.fromTo("#${oid}-lab",{opacity:0,scale:0.7},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.4)"},${f3(w0 + 0.35)});`); }
      else if (o.type === "wheel") {
        tl.push(`tl.set("#${oid}",{opacity:0},0);`, `tl.fromTo("#${oid}",{opacity:0,scale:0.8},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.4)"},${f3(w0)});`);
        String(o.value).split("").forEach((dgt, c) => tl.push(`tl.fromTo("#${oid}-c${c}",{y:0},{y:-${(+dgt) * 253},duration:${f3(0.9 + c * 0.2)},ease:"power3.out"},${f3(w0 + 0.05)});`));
      } else {
        tl.push(`tl.set("#${oid}",{opacity:0},0);`, `tl.fromTo("#${oid}",{opacity:0,scale:0.85},{opacity:1,scale:1,duration:0.3,ease:"back.out(1.4)"},${f3(w0)});`);
        if (o.count) { const ob = vid(`${oid}_o`); tl.push(`const ${ob}={v:0};`, `tl.fromTo(${ob},{v:0},{v:${o.count},duration:0.7,ease:"power2.out",onUpdate:function(){var e=document.getElementById("${oid}-t");if(e)e.textContent=Math.round(${ob}.v)+"%";}},${f3(w0)});`); }
      }
      if (o.dur) tl.push(`tl.to("#${oid}",{opacity:0,duration:0.2},${f3(w0 + o.dur)});`);
      if (["badge", "circle", "arrow", "wheel"].includes(o.type)) sfx.push({ t: f3(w0), kind: "pop" });
      else sfx.push({ t: f3(w0), kind: "pop" });
    }
    for (const [o, k] of scrOvs) {
      const [t0, t1] = overlayWin(sc, ws, W, o), oid = `${id}-so${k}`, vis = t1 > a && t0 < e;
      if (!vis) { tl.push(`tl.set("#${oid}",{opacity:0},0);`); continue; }
      if (t0 >= a - 0.001) { tl.push(`tl.set("#${oid}",{opacity:0},0);`, `tl.fromTo("#${oid}",{opacity:0,y:-20},{opacity:1,y:0,duration:0.3,ease:"back.out(1.4)"},${f3(t0)});`); if (o.ul) tl.push(`tl.to("#${oid}-ul",{strokeDashoffset:0,duration:0.5,ease:"power2.out"},${f3(t0 + 0.5)});`); }
      if (t1 < e - 0.01) tl.push(`tl.to("#${oid}",{opacity:0,duration:0.2},${f3(t1)});`);
    }
  } else if (sh.type === "quote") {
    const q = sh.ev, toks = q.text.split(" "), s0 = W(q.word, q.occ || 1) - 1; let html2 = "", ti = 0, times = [], inB = false;
    let bn = 0; const bt = []; for (const tk of toks) { let w = tk; if (w.startsWith("[[")) { inB = true; html2 += `<span class="badge yellow" id="${id}-dg-b${bn}">`; bt.push(ws[Math.min(s0 + ti, ws.length - 1)].s); bn++; w = w.slice(2); } let close = false; if (w.endsWith("]]")) { close = true; w = w.slice(0, -2); }
      html2 += `<span class="w" id="${id}-dg-w${ti}">${w}</span>${close ? "" : " "}`; times.push(ws[Math.min(s0 + ti, ws.length - 1)].s); ti++; if (close) { html2 += `</span> `; inB = false; } }
    const dr = diagram({ kind: "quote", html: html2, times, by: q.by }, `${id}-dg`, T); dr.tw.forEach((x) => tl.push(x)); bt.forEach((t0, bi) => tl.push(`tl.set("#${id}-dg-b${bi}",{opacity:0},0);`, `tl.fromTo("#${id}-dg-b${bi}",{opacity:0},{opacity:1,duration:0.2},${f3(t0 - 0.04)});`));
    content = dr.html; sfx.push({ t: f3(a), kind: "click" });
  } else if (sh.type === "icon") {
    usedIcons.add(sh.ev.icon);
    content = `<div class="fill iconbg"><img id="${id}-img" src="assets/icons/${sh.ev.icon}.jpg" class="pic" alt=""></div>`;
    tl.push(`tl.fromTo("#${id}-img",{scale:0.92},{scale:1,duration:0.2,ease:"power2.out"},${f3(a)});`);
    sfx.push({ t: f3(a), kind: "pop" });
  } else if (sh.type === "iconrow") {
    const items = sh.ev.items; items.forEach((it) => usedIcons.add(it.icon));
    content = `<div class="fill diag cardc"><div class="irow">${items.map((it, k) => `<div id="${id}-ic${k}" class="itile"><img src="assets/icons/${it.icon}.jpg" alt=""></div>`).join("")}</div></div>`;
    items.forEach((it, k) => { const t0 = ws[W(it.word)].s - 0.03; tl.push(`tl.set("#${id}-ic${k}",{opacity:0},0);`, `tl.fromTo("#${id}-ic${k}",{opacity:0,scale:0.92},{opacity:1,scale:1,duration:0.2,ease:"power2.out"},${f3(t0)});`); sfx.push({ t: f3(t0), kind: "pop" }); });
  } else if (sh.type === "card") {
    content = `<div class="fill card"><div id="${id}-in" class="cardtxt">${linesHtml(sh.ev.parts, id)}</div></div>`;
    tl.push(`tl.fromTo("#${id}-in",{scale:0.94},{scale:1,duration:0.25,ease:"back.out(1.4)"},${f3(a)});`, ...partTweens(sh.ev.parts, id, a));
    sfx.push({ t: f3(a), kind: "click" });
  } else if (sh.type === "title") {
    content = `<div class="fill card"><div id="${id}-in" class="cardtxt"><div class="pill">${sh.ev.pill || "LESSON"}</div><div class="ln big">${sh.ev.l1 || "PSYCHOLOGY OF"}</div><div class="ln big"><span class="org">${sh.ev.l2 || "REGRET"}</span></div></div></div>`;
    tl.push(`tl.fromTo("#${id}-in",{scale:0.94},{scale:1,duration:0.3,ease:"back.out(1.4)"},${f3(a)});`);
    sfx.push({ t: f3(a), kind: "click" });
  } else if (sh.type === "pop") {
    const c = sh.ev.content;
    if (c.type === "icon") { usedIcons.add(c.icon); content = `<div class="fill iconbg"><img src="assets/icons/${c.icon}.jpg" class="pic" alt=""></div>`; }
    else content = `<div class="fill card"><div id="${id}-in" class="cardtxt">${linesHtml(c.parts, id)}</div></div>`;
    if (c.type !== "icon") tl.push(`tl.fromTo("#${id}-in",{scale:0.94},{scale:1,duration:0.25,ease:"back.out(1.4)"},${f3(a + 0.1)});`, ...partTweens(c.parts, id, a));
    else tl.push(`tl.fromTo("#${id}-t .pic",{scale:0.94},{scale:1,duration:0.25,ease:"back.out(1.4)"},${f3(a + 0.1)});`);
    usedPoses.add(sh.ev.pose);
    sfx.push({ t: f3(a), kind: "swoosh" });
  }
  // ---- wrap
  const isPop = sh.type === "pop", hosted = host || isPop;
  let body;
  if (hosted) body = `<div class="hbg"></div><div class="frame"><div class="hs"><div id="${id}-fin" class="fin">${content}</div></div></div><div class="fborder"></div>`;
  else body = `<div id="${id}-fin" class="fin">${content}</div>`;
  let nar = "";
  if (isPop && !host) {
    const pose = sh.ev.pose, w = POSEW[pose], left = Math.max(10, FL + 36 - w);
    nar = `<div id="${id}-nw" class="nw"><div class="nshadow" style="left:${left - 10}px;width:${w + 40}px"></div><img class="narr" style="left:${left}px;height:${NH}px" src="assets/narrator/${pose}.png" alt=""></div>`;
    tl.push(`tl.fromTo("#${id}-nw",{x:-520},{x:0,duration:0.25,ease:"power2.out"},${f3(a)});`, `tl.to("#${id}-nw",{x:-520,duration:0.2,ease:"power2.in"},${f3(e - 0.22)});`);
  }
  html.push(`<div id="${id}" class="clip" data-start="${f3(a)}" data-duration="${f3(cd)}" style="z-index:${zi}"><div id="${id}-t" class="tt">${body}${extra}</div>${nar}</div>`);
  // transitions
  if (tr) {
    const dd = tr.dur, tid = `#${id}-t`, pt = prevSh ? `#${prevSh.sid}-t` : null;
    if (tr.kind === "push" || tr.kind === "whip") {
      const ease = tr.kind === "whip" ? "power3.inOut" : "power2.inOut";
      tl.push(`tl.fromTo("${tid}",{x:1920},{x:0,duration:${dd},ease:"${ease}"},${f3(a)});`, `tl.to("${pt}",{x:-1920,duration:${dd},ease:"${ease}"},${f3(a)});`);
      if (tr.kind === "whip") tl.push(`tl.set("${tid},${pt}",{filter:"url(#mb)"},${f3(a)});`, `tl.fromTo("#mbb",{attr:{stdDeviation:"0 0"}},{attr:{stdDeviation:"42 0"},duration:${f3(dd / 2)},ease:"power2.in"},${f3(a)});`, `tl.to("#mbb",{attr:{stdDeviation:"0 0"},duration:${f3(dd / 2)},ease:"power2.out"},${f3(a + dd / 2)});`, `tl.set("${tid},${pt}",{filter:"none"},${f3(a + dd + 0.02)});`);
      sfx.push({ t: f3(a), kind: "swoosh" });
    } else if (tr.kind === "fade") tl.push(`tl.fromTo("${tid}",{opacity:0},{opacity:1,duration:${dd},ease:"none"},${f3(a)});`);
    else if (tr.kind === "iris") { tl.push(`tl.fromTo("${tid}",{clipPath:"circle(0% at ${tr.pt[0] * 100}% ${tr.pt[1] * 100}%)"},{clipPath:"circle(150% at ${tr.pt[0] * 100}% ${tr.pt[1] * 100}%)",duration:${dd + 0.2},ease:"power2.out"},${f3(a)});`); sfx.push({ t: f3(a), kind: "ding" }); }
  } else if (sh.si > 0 && sh.P.sc.swap && sh.side === "B" && G[gi - 1].side === "A" && G[gi - 1].P === P) sfx.push({ t: f3(a), kind: "ding" });
  // narrator-related bookkeeping
  planOut.push({ scene: sc.id, kind: sh.type, a: f3(a), e: f3(e), host: hosted });
});

// ---- impact hits & fx
planned.forEach((P) => {
  const { sc, ws, W } = P;
  for (const fx of sc.fx || []) {
    const k = W(fx.word, fx.occ || 1), t = ws[k].s;
    if (fx.type === "impact") {
      const sh = G.find((s) => s.P === P && t >= s.a - 0.001 && t < s.e);
      if (!sh) continue;
      tl.push(`tl.fromTo("#${sh.sid}-fin",{scale:1.06},{scale:1,duration:0.2,ease:"power2.out"},${f3(t)});`, `tl.set("#${sh.sid}-fin",{x:5},${f3(t)});`, `tl.set("#${sh.sid}-fin",{x:-4},${f3(t + 0.033)});`, `tl.set("#${sh.sid}-fin",{x:3},${f3(t + 0.066)});`, `tl.set("#${sh.sid}-fin",{x:0},${f3(t + 0.1)});`);
      sfx.push({ t: f3(t), kind: "ding" });
    }
    if (fx.type === "riser") sfx.push({ t: f3(t - 0.65), kind: "riser" });
    if (fx.type === "leak") leaks.push({ t, d: fx.dur || 1.4 });
  }
});

// ---- narrator host track
const stretches = [];
planned.forEach((P, i) => {
  if (!P.sc.host) return;
  const last = stretches[stretches.length - 1];
  if (last && last.endI === i - 1) { last.endI = i; last.items.push(P); } else stretches.push({ startI: i, endI: i, items: [P] });
});
let nk = 0;
for (const stt of stretches) {
  const segs = [];
  for (const P of stt.items) {
    const sc = P.sc, { ws, W, cutAt } = P, S = sc.t.start, titleShot = P.shots.find((s) => s.type === "title"), E = titleShot ? titleShot.a : sc.t.end;
    const hostL = sc.host.map((h, k) => ({ pose: h[0], t: k === 0 ? S : cutAt(W(h[1], h[2] || 1)) }));
    hostL.forEach((h, k) => segs.push({ pose: h.pose, a: h.t, e: k + 1 < hostL.length ? hostL[k + 1].t : E }));
    // pop overrides
    for (const sh of P.shots) if (sh.type === "pop") {
      const pose = sh.ev.pose; const idx = segs.findIndex((s) => s.a <= sh.a + 0.001 && s.e > sh.a + 0.001);
      if (idx < 0 || segs[idx].pose === pose) continue;
      const sg = segs[idx], rest = { pose: sg.pose, a: sh.e, e: sg.e };
      sg.e = sh.a; segs.splice(idx + 1, 0, { pose, a: sh.a, e: sh.e });
      if (rest.e - rest.a > 0.05) segs.splice(idx + 2, 0, rest);
    }
  }
  const clean = segs.filter((s) => s.e - s.a > 0.05).sort((x, y) => x.a - y.a);
  // merge neighbours with same pose
  const mg = []; for (const s of clean) { const l = mg[mg.length - 1]; if (l && l.pose === s.pose && Math.abs(l.e - s.a) < 0.02) l.e = s.e; else mg.push({ ...s }); }
  mg.forEach((s, k) => {
    usedPoses.add(s.pose); const w = POSEW[s.pose], left = Math.max(10, FL + 36 - w), id = `nar${++nk}`;
    html.push(`<div id="${id}" class="clip" data-start="${f3(s.a)}" data-duration="${f3(s.e - s.a)}" style="z-index:900"><div id="${id}-w" class="nw"><div class="nshadow" style="left:${left - 10}px;width:${w + 40}px"></div><img class="narr" style="left:${left}px;height:${NH}px" src="assets/narrator/${s.pose}.png" alt=""></div></div>`);
    if (k === 0) { tl.push(`tl.fromTo("#${id}-w",{x:-520},{x:0,duration:0.25,ease:"power2.out"},${f3(s.a)});`); sfx.push({ t: f3(s.a), kind: "swoosh" }); }
    if (k === mg.length - 1) tl.push(`tl.to("#${id}-w",{x:-520,duration:0.2,ease:"power2.in"},${f3(s.e - 0.22)});`);
    planOut.push({ scene: "host", kind: "pose:" + s.pose, a: f3(s.a), e: f3(s.e) });
  });
}

// ---- light leaks / sweeps (top layer clips)
leaks.forEach((l, k) => {
  html.push(`<div id="leak${k}" class="clip" data-start="${f3(l.t - 0.2)}" data-duration="${f3(l.d + 0.4)}" style="z-index:950;pointer-events:none"><div id="leak${k}-i" class="leak"></div></div>`);
  tl.push(`tl.fromTo("#leak${k}-i",{opacity:0},{opacity:0.85,duration:${f3(l.d * 0.4)},ease:"power1.out"},${f3(l.t - 0.2)});`, `tl.to("#leak${k}-i",{opacity:0,duration:${f3(l.d * 0.6)},ease:"power1.in"},${f3(l.t - 0.2 + l.d * 0.4)});`);
});

// ---------- files ----------
for (const n of usedPics) fs.copyFileSync(`assets/pictures/${n}.jpg`, `${out}/assets/pictures/${n}.jpg`);
for (const n of usedIcons) fs.copyFileSync(`assets/icons/${n}.jpg`, `${out}/assets/icons/${n}.jpg`);
for (const n of usedPoses) fs.copyFileSync(`assets/narrator/${n}.png`, `${out}/assets/narrator/${n}.png`);
fs.copyFileSync("node_modules/@fontsource/nunito/files/nunito-latin-800-normal.woff2", `${out}/assets/fonts/nunito-800.woff2`);
fs.copyFileSync("assets/vendor/gsap.min.js", `${out}/assets/gsap.min.js`);
fs.copyFileSync(cfg.audio, `${out}/assets/part${N}.wav`);
for (const f of ["hyperframes.json", "package.json"]) if (fs.existsSync(`tools/template/${f}`)) fs.copyFileSync(`tools/template/${f}`, `${out}/${f}`);
fs.writeFileSync(`${out}/meta.json`, JSON.stringify({ id: `part${N}`, name: `SimpleMindMotivation Part ${N}`, createdAt: "2026-10-12T00:00:00.000Z" }, null, 2));
const page = `<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=1920, height=1080"><title>Part ${N}</title>
<script src="assets/gsap.min.js"></script>
<style>
@font-face{font-family:"Nunito";font-weight:800;src:url("assets/fonts/nunito-800.woff2") format("woff2")}
html,body{margin:0;background:${PAPER}}
#root{position:relative;width:100%;height:100%;overflow:hidden;background:${PAPER};font-family:"Nunito",sans-serif;font-weight:800;color:${INK}}
.clip{position:absolute;inset:0;overflow:hidden}
.tt,.fill{position:absolute;inset:0}
.tt{background:${PAPER}}
.fin{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:50% 50%}
.bleed{position:absolute;left:-1920px;top:-1080px;width:5760px;height:3240px}
.cam{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0}
.pic{position:absolute;left:0;top:0;width:1920px;height:1080px;display:block}
.iconbg{background:#F8F5EE}
.card{background:${PAPER};display:flex;align-items:center;justify-content:center}
.cardtxt{display:flex;flex-direction:column;align-items:center;gap:26px;text-align:center}
.ln{font-size:170px;line-height:1.05;letter-spacing:1px;white-space:nowrap;position:relative}
.ln.big{font-size:130px}.ln.small{font-size:84px}.ln.mid{font-size:112px}
.badge{display:inline-block;padding:4px 40px 12px;border:9px solid ${INK};border-radius:34px;box-shadow:8px 8px 0 ${INK}}
.badge.yellow{background:${YEL};color:${INK}} .badge.red{background:${RED};color:#fff}
.pill{background:${GREEN};color:#fff;border:7px solid ${INK};border-radius:60px;font-size:64px;padding:2px 54px 8px;letter-spacing:4px;margin-bottom:18px}
.pill.big{margin:0;border-width:6px;font-size:64px;padding:2px 50px 8px}
.org{color:${ORG};-webkit-text-stroke:6px ${INK};paint-order:stroke fill}
.mk{position:relative;display:inline-block}.mk i{position:absolute;left:-14px;right:-14px;top:22%;bottom:2%;background:${YEL};transform-origin:0 50%;z-index:0;border-radius:10px}.mk b{position:relative;z-index:1;font-weight:800}
.circw{position:relative;display:inline-block}.circ{position:absolute;left:-60px;top:-34px;width:calc(100% + 120px);height:calc(100% + 68px);overflow:visible}
.ulw{position:relative;display:inline-block}.ul{position:absolute;left:0;bottom:-26px;width:100%;height:30px;overflow:visible}
.ulp{position:absolute;left:0;bottom:-24px;width:100%;height:26px;overflow:visible}
.hbg{position:absolute;inset:0;background:${PAPER}}
.frame{position:absolute;left:${f3(FL)}px;top:${FT}px;width:${f3(FW)}px;height:${f3(FH)}px;border-radius:28px;overflow:hidden;background:${PAPER}}
.hs{position:absolute;left:0;top:0;width:1920px;height:1080px;transform:scale(${HS});transform-origin:0 0}
.fborder{position:absolute;left:${f3(FL)}px;top:${FT}px;width:${f3(FW)}px;height:${f3(FH)}px;box-sizing:border-box;border:6px solid ${INK};border-radius:28px;pointer-events:none}
.nw{position:absolute;inset:0;z-index:5}
.narr{position:absolute;bottom:48px;display:block}
.nshadow{position:absolute;bottom:26px;height:46px;background:radial-gradient(ellipse at center,rgba(26,26,26,.28),rgba(26,26,26,0) 70%)}
.diag{background:${PAPER}}
.cardc{display:flex;align-items:center;justify-content:center}
.dlabel{position:absolute;left:0;right:0;top:830px;display:flex;justify-content:center;align-items:center;gap:36px;font-size:130px;white-space:nowrap}
.sclab{position:absolute;width:500px;display:flex;justify-content:center;font-size:84px}
.tagbox{position:absolute;display:flex;align-items:center;justify-content:center;white-space:nowrap}
.scr{position:absolute;left:0;right:0;top:24px;display:flex;flex-direction:column;align-items:center;gap:14px;z-index:6}.scr.row{flex-direction:row;justify-content:center;gap:20px;top:22px}
.spill2{background:${PAPER};border:6px solid ${INK};border-radius:44px;font-size:60px;line-height:1.05;padding:4px 40px 10px;white-space:nowrap;position:relative}
.sbub{position:absolute;background:#fff;border:7px solid ${INK};border-radius:42px;box-sizing:border-box;display:flex;align-items:center;justify-content:center;text-align:center;font-size:64px;line-height:1.05;padding:6px 18px}
.sbub i{position:absolute;right:-34px;bottom:-30px;width:40px;height:40px;background:#fff;border:7px solid ${INK};border-radius:50%;box-sizing:border-box}
.sign{position:absolute;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1;color:${INK};white-space:nowrap}
.ovsvg{position:absolute;left:0;top:0;width:1920px;height:1080px;overflow:visible}
.clab{position:absolute;white-space:nowrap}
.wheel{padding:0 26px 4px;overflow:hidden}.dig{display:block;height:253px;overflow:hidden;width:130px}.col{display:flex;flex-direction:column;line-height:253px;text-align:center}
.bar{position:absolute;border:9px solid ${INK};border-radius:26px 26px 0 0;box-sizing:border-box;box-shadow:8px 8px 0 rgba(26,26,26,.18)}
.btag{position:absolute;left:-40px;right:-40px;top:-130px;text-align:center;font-size:100px;white-space:nowrap}
.blab{position:absolute;text-align:center;font-size:66px;line-height:1.05}
.topbadge{position:absolute;left:0;right:0;top:48px;display:flex;justify-content:center;align-items:center;gap:28px;font-size:94px;white-space:nowrap}
.ctitle{position:absolute;left:0;right:0;top:36px;text-align:center;font-size:100px;letter-spacing:3px}
.axl{position:absolute;font-size:62px}
.llab{position:absolute;font-size:62px;white-space:nowrap;-webkit-text-stroke:2px ${INK};paint-order:stroke fill}
.tag{position:absolute;font-size:70px}.tag .badge{padding:0 30px 8px}
.sweep{position:absolute;width:300px;height:300px;opacity:0;background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,247,200,.95),rgba(255,255,255,0));filter:blur(8px);border-radius:50%}
.half{position:absolute;top:0;width:960px;height:1080px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px}
.half .ln{font-size:128px}
.vdiv{position:absolute;left:956px;top:120px;width:8px;height:840px;background:${INK};border-radius:4px}
.qmark{position:absolute;left:210px;top:60px;font-size:420px;line-height:1;color:${ORG};-webkit-text-stroke:5px ${INK};paint-order:stroke fill}
.qtext{position:absolute;left:200px;top:250px;width:1540px;font-size:90px;line-height:1.42;text-align:left}
.qtext .w{display:inline-block;margin-right:16px}.qtext .badge{padding:0 20px 6px;box-shadow:6px 6px 0 ${INK};border-width:7px;border-radius:24px;margin-right:16px}.qtext .badge .w{margin-right:14px}.qtext .badge .w:last-child{margin-right:0}
.qby{position:absolute;left:0;right:0;top:880px;text-align:center;font-size:58px;color:#6a6454}
.irow2{position:absolute;left:0;right:0;top:190px;display:flex;gap:70px;justify-content:center;align-items:flex-start}.icol{display:flex;flex-direction:column;align-items:center;gap:26px;width:540px}.ilab{font-size:84px;line-height:1.05;text-align:center;width:560px}.under{position:absolute;left:0;right:0;top:840px;text-align:center;font-size:90px;white-space:nowrap}
.qtile{position:absolute;width:800px;height:400px;box-sizing:border-box;border:9px solid ${INK};border-radius:36px;display:flex;align-items:center;gap:30px;padding:0 30px;box-shadow:10px 10px 0 rgba(26,26,26,.2)}.qic{width:300px;height:300px;overflow:hidden;border-radius:24px;border:6px solid ${INK};background:#F8F5EE;flex:none;box-sizing:border-box}.qic img{height:288px;width:512px;margin-left:-112px;display:block}.qlab{font-size:64px;line-height:1.05;flex:1;text-align:left}
.lrow{position:absolute;left:0;right:0;text-align:center;font-size:100px;white-space:nowrap}.lpill{display:inline-block;padding:4px 56px 14px;border:9px solid ${INK};border-radius:46px;box-shadow:8px 8px 0 ${INK}}
.stamp{position:absolute;left:240px;right:240px;top:420px;text-align:center;font-size:170px;color:${RED};border:16px solid ${RED};border-radius:30px;background:rgba(250,247,240,.9);padding:0 20px 14px;white-space:nowrap;letter-spacing:4px}
.ratio{position:absolute;left:0;right:0;top:360px;text-align:center;font-size:150px}.dsmall{position:absolute;left:0;right:0;top:992px;text-align:center;font-size:44px;color:#6a6454}.splsign{position:absolute;left:0;right:0;top:420px;text-align:center;font-size:170px}
.irow{display:flex;gap:70px;align-items:center}
.itile{width:520px;height:520px;border:9px solid ${INK};border-radius:36px;overflow:hidden;background:#F8F5EE;box-shadow:10px 10px 0 rgba(26,26,26,.2)}.itile img{width:924px;height:520px;margin-left:-202px;display:block}
.sweepbox{position:absolute;overflow:hidden}.sweepband{position:absolute;left:0;top:-20%;width:35%;height:140%;transform:skewX(-18deg);background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,247,200,.9),rgba(255,255,255,0));opacity:0}
.leak{position:absolute;inset:0;mix-blend-mode:screen;background:radial-gradient(ellipse 60% 70% at 95% 10%,rgba(255,170,70,.95),rgba(255,120,40,0) 70%),radial-gradient(ellipse 50% 60% at 5% 95%,rgba(255,210,120,.75),rgba(255,160,60,0) 70%)}
</style></head><body>
<div id="root" data-composition-id="part${N}" data-start="0" data-width="1920" data-height="1080" data-duration="${f3(dur)}">
<svg width="0" height="0" style="position:absolute"><filter id="mb" x="-5%" y="-5%" width="110%" height="110%" color-interpolation-filters="sRGB"><feGaussianBlur id="mbb" stdDeviation="0 0"/></filter></svg>
${html.join("\n")}
<audio id="vo" src="assets/part${N}.wav" data-start="0" data-duration="${f3(dur)}" data-track-index="0"></audio>
</div>
<script>
const pp=(cx,cy,r,pct)=>{const p=Math.min(Math.max(pct,0.01),99.99),a=p/100*2*Math.PI;return "M"+cx+" "+cy+" L"+cx+" "+(cy-r)+" A"+r+" "+r+" 0 "+(a>Math.PI?1:0)+" 1 "+(cx+r*Math.sin(a)).toFixed(2)+" "+(cy-r*Math.cos(a)).toFixed(2)+" Z";};
const tl = gsap.timeline({ paused: true });
${tl.join("\n")}
window.__timelines["part${N}"] = tl;
</script></body></html>`;
fs.writeFileSync(`${out}/index.html`, page);
fs.writeFileSync(`scenes/part${N}.sfx.json`, JSON.stringify(sfx.sort((a, b) => a.t - b.t)));
fs.writeFileSync(`scenes/part${N}.plan.json`, JSON.stringify(planOut, null, 1));
const rows = cutRows.sort((a, b) => a.t - b.t).map((r) => `${r.t.toFixed(2).padStart(7)}s  ${r.scene}  ${r.kind.padEnd(7)}  word "${r.word}"  Δ${(r.delta * 1000).toFixed(0)}ms`);
fs.writeFileSync(`scenes/part${N}.cuts.txt`, rows.join("\n"));
const sh = planOut.filter((p) => p.scene !== "host"), lens = sh.map((p) => p.e - p.a), over = sh.filter((p) => p.e - p.a > 4.02);
console.log(`shots ${sh.length}, avg ${(lens.reduce((x, y) => x + y, 0) / lens.length).toFixed(2)}s, max ${Math.max(...lens).toFixed(2)}s, over 4s: ${over.length}`);
const hostT = planOut.filter((p) => p.scene !== "host" && p.host).reduce((s, p) => s + p.e - p.a, 0);
console.log(`host screen time ${(100 * hostT / dur).toFixed(0)}%`);
console.log(warn.length ? "WARNINGS:\n" + warn.join("\n") : "no warnings"); console.log("built", out);
