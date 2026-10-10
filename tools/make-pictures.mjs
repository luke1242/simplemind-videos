// Draws one illustration per scene -> assets/pictures/<id>.svg  (1920x1080). Usage: node tools/make-pictures.mjs S01 S02 ...  (no args = all)
import fs from 'node:fs';
import { figure, place, DEFS, C } from './characters.mjs';
const W = 1920, H = 1080, RIM = '#C98B6B';
const svg = (inner, bg = C.paper) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}">${DEFS}<rect width="${W}" height="${H}" fill="${bg}"/>${inner}</svg>`;
const L = (x1, y1, x2, y2, c = C.ink, w = 4) => `<path d="M${x1} ${y1} L${x2} ${y2}" stroke="${c}" stroke-width="${w}" stroke-linecap="round" fill="none"/>`;
const R = (x, y, w, h, fill, rx = 0, sw = 4, st = C.ink) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" fill="${fill}" stroke="${fill === 'none' || sw === 0 ? 'none' : st}" stroke-width="${sw}" stroke-linejoin="round"/>`;
const E = (cx, cy, rx, ry, fill, op = 1, sw = 0, st = C.ink) => `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="${fill}" opacity="${op}" stroke="${sw ? st : 'none'}" stroke-width="${sw}"/>`;
const rng = (seed) => () => (seed = (seed * 16807) % 2147483647) / 2147483647;
const N = (pose, expr, o = {}) => figure('narrator', pose, expr, o);
const Pn = (pose, expr, x, y, s, o = {}, flip = false) => place(N(pose, expr, o), x, y, s, flip);
const Pp = (v, pose, expr, x, y, s, o = {}, flip = false) => place(figure('person', pose, expr, { variant: v, ...o }), x, y, s, flip);
const ground = (y = 900, x1 = 100, x2 = 1820) => L(x1, y, x2, y);

// ---- props ----
function lockers(y0 = 270, y1 = 860) {
  let s = '';
  for (let i = 0; i < 16; i++) {
    const x = i * 120;
    s += R(x + 2, y0, 116, y1 - y0, C.sky, 0, 4);
    s += R(x + 14, y0 + 40, 92, 18, 'none', 3, 3) + L(x + 28, y0 + 49, x + 92, y0 + 49, C.ink, 3);
    s += `<circle cx="${x + 94}" cy="${y0 + 280}" r="6" fill="${C.ink}"/>` + L(x + 2, y0 + 210, x + 118, y0 + 210, C.ink, 3);
  }
  return s;
}
const hallway = () => R(0, 860, W, 220, C.shadow, 0, 0) + lockers() + L(0, 860, W, 860, C.ink, 5);
const spot = (cx, cy, rx = 170, ry = 34, op = 0.5) => E(cx, cy, rx, ry, C.orange, op);
function gymDoor(x, y0 = 900) {
  const w = 400, h = 580, top = y0 - h;
  let s = R(x, top, w, h, C.shadow, 0, 0);
  s += L(x + 20, y0 - 150, x + w - 20, y0 - 150, C.ink, 5) + L(x + 20, y0 - 300, x + w - 20, y0 - 300, C.ink, 5);
  for (let i = 0; i < 4; i++) { const dx = x + 70 + i * 86, cy = y0 - 160 - 10; s += `<g>${L(dx - 22, cy, dx + 22, cy, C.ink, 6)}<rect x="${dx - 36}" y="${cy - 13}" width="14" height="26" rx="4" fill="${[C.terracotta, C.mustard, C.sage, C.pink][i]}" stroke="${C.ink}" stroke-width="4"/><rect x="${dx + 22}" y="${cy - 13}" width="14" height="26" rx="4" fill="${[C.terracotta, C.mustard, C.sage, C.pink][i]}" stroke="${C.ink}" stroke-width="4"/></g>`; }
  for (let i = 0; i < 4; i++) { const dx = x + 60 + i * 80; s += `<g>${L(dx - 24, y0 - 310, dx + 24, y0 - 310, C.ink, 7)}<circle cx="${dx - 30}" cy="${y0 - 310}" r="14" fill="${C.sky}" stroke="${C.ink}" stroke-width="4"/><circle cx="${dx + 30}" cy="${y0 - 310}" r="14" fill="${C.sky}" stroke="${C.ink}" stroke-width="4"/></g>`; }
  s += R(x, top, w, h, 'none', 0, 12) + R(x - 16, top - 16, w + 32, 22, C.paper, 4, 6);
  return s;
}
const bulb = (x, y, r = 50) => E(x, y, r * 2, r * 2, C.orange, 0.28) + [...Array(8)].map((_, i) => { const a = (i * Math.PI) / 4; return L(x + Math.cos(a) * (r + 22), y + Math.sin(a) * (r + 22), x + Math.cos(a) * (r + 46), y + Math.sin(a) * (r + 46), C.orange, 6); }).join('') +
  `<path d="M${x - r * 0.5} ${y + r * 0.85} Q${x - r * 1.15} ${y + r * 0.1} ${x - r * 0.95} ${y - r * 0.35} A${r} ${r} 0 1 1 ${x + r * 0.95} ${y - r * 0.35} Q${x + r * 1.15} ${y + r * 0.1} ${x + r * 0.5} ${y + r * 0.85}Z" fill="${C.mustard}" stroke="${C.ink}" stroke-width="4.5" stroke-linejoin="round"/>` +
  R(x - r * 0.5, y + r * 0.85, r, r * 0.38, C.shadow, 5, 4.5) + R(x - r * 0.38, y + r * 1.22, r * 0.76, r * 0.2, C.ink, 6, 3);
function tshirt(x, y, s = 1) {
  return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M-72 -64 L-30 -86 Q0 -66 30 -86 L72 -64 L104 -8 L70 10 L54 -14 L54 104 L-54 104 L-54 -14 L-70 10 L-104 -8 Z" fill="${C.mustard}" stroke="${C.ink}" stroke-width="5" stroke-linejoin="round"/>
  <circle cx="-24" cy="-6" r="19" fill="#fff" stroke="${C.ink}" stroke-width="4"/><circle cx="26" cy="-10" r="15" fill="#fff" stroke="${C.ink}" stroke-width="4"/><circle cx="-20" cy="-4" r="7" fill="${C.ink}"/><circle cx="30" cy="-8" r="6" fill="${C.ink}"/>
  <path d="M-34 32 Q0 76 38 28 Z" fill="${C.ink}" stroke="${C.ink}" stroke-width="4" stroke-linejoin="round"/><path d="M-8 46 Q8 70 22 42 Q8 36 -8 46Z" fill="${C.red}"/></g>`;
}
function stage(spotX, withCone = true) {
  let s = R(0, 760, W, 100, C.hoodie, 0, 0) + R(0, 860, W, 50, C.night, 0, 0) + L(0, 860, W, 860, '#5a4a40', 4);
  if (withCone) s += `<path d="M${spotX - 40} 0 L${spotX + 40} 0 L${spotX + 300} 790 L${spotX - 300} 790Z" fill="${C.orange}" opacity="0.28"/>` + E(spotX, 800, 300, 46, C.orange, 0.42);
  return s;
}
function crowd(seed = 7) {
  const r = rng(seed); let s = '';
  for (let row = 0; row < 7; row++) {
    const y = 925 + row * 24, sc = 0.9 + row * 0.2, n = 18 - row;
    for (let i = 0; i < n; i++) {
      const x = (i + 0.2 + r() * 0.6) * (W / n); const g = 11 * sc;
      s += E(x - g, y, 5.2 * sc, 8 * sc, '#fff', 0.92) + E(x + g, y, 5.2 * sc, 8 * sc, '#fff', 0.92);
    }
  }
  return s;
}
function bubble(x, y, w, h, tail = [x, y + h]) {
  return `<g fill="${C.paper}" stroke="${C.ink}" stroke-width="4.5"><ellipse cx="${x}" cy="${y}" rx="${w / 2}" ry="${h / 2}"/><circle cx="${tail[0] + (x - tail[0]) * 0.25}" cy="${y + h / 2 + 22}" r="14"/><circle cx="${tail[0]}" cy="${y + h / 2 + 60}" r="9"/></g><ellipse cx="${x}" cy="${y}" rx="${w / 2 - 2}" ry="${h / 2 - 2}" fill="${C.paper}"/>`;
}
function bedroom(withBubble, expr) {
  const M = 700, sc = 1.1;
  let s = R(0, 840, W, 240, C.stage, 0, 0) + L(0, 840, W, 840, '#5a4a40', 4);
  s += R(1250, 150, 360, 330, C.stage, 0, 0, C.paper).replace(`stroke="${C.ink}"`, `stroke="${C.paper}"`).replace('stroke-width="4"', 'stroke-width="9"');
  s += L(1430, 150, 1430, 480, C.paper, 7) + L(1250, 315, 1610, 315, C.paper, 7);
  s += `<circle cx="1340" cy="240" r="40" fill="${C.mustard}"/><circle cx="1358" cy="228" r="36" fill="${C.stage}"/>`;
  [[1500, 220], [1540, 400], [1320, 400], [1570, 300]].forEach(([a, b]) => (s += `<circle cx="${a}" cy="${b}" r="4" fill="${C.paper}"/>`));
  s += R(250, 760, 770, 56, C.terracotta, 8) + R(262, 816, 26, 24, C.terracotta, 4) + R(982, 816, 26, 24, C.terracotta, 4);
  s += R(250, M, 770, 66, C.sky, 14) + R(262, 625, 190, 78, C.paper, 30);
  s += place(figure('narrator', 'lie-bed', expr, { rim: RIM, shadow: false }), 690, M + 150 * sc, sc);
  s += R(740, M - 74, 290, 140, C.sage, 22);
  s += L(740, M - 18, 1030, M - 18, C.ink, 3);
  if (withBubble) s += bubble(470, 330, 380, 230, [470, 560]) + Pn('stumble', 'cringe', 480, 440, 0.3);
  return svg(s, C.night);
}

const P = {};
P.S01 = () => svg(ground() + gymDoor(1190) + Pn('stand-strap', 'worried', 700, 900, 1.15, { backpack: true }));
P.S02 = () => svg(Pn('stand', 'worried', 960, 1720, 3.1, { sweat: true, shadow: false }));
P.S03 = () => svg(stage(960) + Pn('stand', 'worried', 960, 810, 0.62, { rim: RIM }) + crowd(), C.stage);
P.S04 = () => svg(stage(960) + L(960, 0, 960, 330, C.paper, 4) + `<g stroke="${C.paper}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M960 330 Q960 300 985 296 Q1006 292 1004 270"/><path d="M880 440 L960 372 L1040 440"/></g>` + tshirt(960, 560, 1.7), C.stage);
P.S05 = () => svg(ground() + Pn('think', 'thinking', 800, 900, 1.15) + bulb(840, 215));
P.S06 = () => svg(hallway() + spot(760, 940) + Pn('walk', 'neutral', 760, 940, 1.15));
P.S07 = () => svg(hallway() + Pp('a', 'stand', 'neutral', 330, 950, 0.95) + Pp('c', 'stand', 'neutral', 1500, 950, 0.95) + Pp('d', 'stand', 'neutral', 1740, 940, 0.9) + Pn('stumble', 'cringe', 960, 960, 1.2));
P.S08 = () => bedroom(true, 'worried');
P.S09b = () => bedroom(false, 'relieved');
P.S10 = () => svg(ground() +
  R(1060, 170, 740, 560, '#fff', 8, 8) + R(1100, 730, 660, 20, C.shadow, 6, 4) + L(1170, 750, 1130, 900) + L(1690, 750, 1730, 900) +
  Pn('present', 'happy', 640, 900, 1.15));

const ids = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(P);
fs.mkdirSync('assets/pictures', { recursive: true });
for (const id of ids) { if (!P[id]) throw new Error('no picture ' + id); fs.writeFileSync(`assets/pictures/${id}.svg`, P[id]()); }
console.log('pictures:', ids.join(' '));
