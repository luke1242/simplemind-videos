// Builds assets/characters/*.svg (master + every pose) and review/character-sheet.png
import fs from 'node:fs';
import { execFileSync } from 'node:child_process';
import { figure, place, POSES, EXPRESSIONS, VARIANTS, DEFS, C } from './characters.mjs';
const dir = 'assets/characters';
fs.mkdirSync(dir, { recursive: true }); fs.mkdirSync('review', { recursive: true });
const wrap = (inner, vb = '-260 -470 520 500', bg = '') => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}">${DEFS}${bg}${inner}</svg>`;
const wide = '-330 -490 660 520';
const head = `<!-- narrator colors: brain ${C.peach} / folds ${C.fold} / glow ${C.peach}@35% / hoodie+pants+hands ${C.hoodie} / outline ${C.ink} / shoes #FFFFFF + stripe ${C.red} / eyes #FFFFFF -->\n`;
const n = (pose, expr = 'neutral', o = {}) => figure('narrator', pose, expr, o).svg;
fs.writeFileSync(`${dir}/narrator.svg`, head + wrap(n('stand'), '-200 -470 400 490'));
for (const p of Object.keys(POSES)) {
  fs.writeFileSync(`${dir}/narrator-${p}.svg`, head + wrap(p === 'lie-bed' ? figure('narrator', p, 'neutral', { shadow: false }).svg.replace('<g>', '<g transform="translate(0 ' + 150 + ')">') : n(p), wide));
  for (const v of Object.keys(VARIANTS)) fs.writeFileSync(`${dir}/person-${v}-${p}.svg`, wrap(figure('person', p, 'neutral', { variant: v }).svg, wide));
}
// ---- review sheet ----
const cell = (svg, label, w = 300, h = 340) => `<div style="width:${w}px;text-align:center"><svg width="${w}" height="${h}" viewBox="-190 -470 380 490">${DEFS}${svg}</svg><div style="font:700 15px Montserrat,sans-serif">${label}</div></div>`;
const poses8 = ['wave', 'think', 'present', 'explain', 'point-left', 'shrug', 'facepalm', 'walk'];
const poses2 = Object.keys(POSES).filter((p) => !poses8.includes(p) && p !== 'stand');
const row = (a) => `<div style="display:flex;flex-wrap:wrap;gap:6px">${a.join('')}</div>`;
const html = `<html><body style="margin:0;background:#FAF7F0;width:2400px;font-family:sans-serif">
<div style="display:flex;gap:10px;align-items:flex-end;background:#2a2a2e;padding:8px"><img src="../reference/characters/narrator.png" style="height:420px"><div style="background:#FAF7F0;padding:6px">${cell(n('stand'), 'MINE: stand (front)', 300, 420)}</div></div>
${row(poses8.map((p) => cell(n(p, 'neutral'), p)))}
${row(EXPRESSIONS.map((e) => cell(n('stand', e), e, 230, 270).replace('viewBox="-190 -470 380 490"', 'viewBox="-110 -480 220 200"')))}
${row(poses2.map((p) => cell(p === 'lie-bed' ? figure('narrator', p, 'worried', { shadow: false }).svg.replace('<g>', '<g transform="translate(0 150)">') : n(p, 'neutral', {}), p, 300, 340)))}
${row(Object.keys(VARIANTS).flatMap((v) => EXPRESSIONS.slice(0, 2).map((e) => cell(figure('person', 'stand', e, { variant: v }).svg, `person-${v} ${e}`))))}
${row(['happy', 'surprised', 'worried', 'cringe', 'relieved', 'laugh', 'thinking', 'wink'].map((e) => cell(figure('person', 'stand', e, { variant: e.length % 4 === 0 ? 'c' : 'a' }).svg, e, 230, 270).replace('viewBox="-190 -470 380 490"', 'viewBox="-110 -480 220 200"')))}
${row(['sit-chair', 'kneel', 'stumble', 'lift', 'hold-front', 'raise-hand', 'walk', 'thumbs-up'].map((p) => cell(figure('person', p, 'happy', { variant: 'b' }).svg, `person ${p}`)))}
</body></html>`;
fs.writeFileSync('review/character-sheet.html', html);
const chrome = process.env.HYPERFRAMES_BROWSER_PATH;
execFileSync(chrome, ['--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars', '--window-size=2400,3300', `--screenshot=${process.cwd()}/review/character-sheet.png`, `file://${process.cwd()}/review/character-sheet.html`], { stdio: 'ignore' });
console.log('ok');
