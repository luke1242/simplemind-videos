// Master characters (narrator + generic persons), poses and expressions.
// figure(kind, pose, expr, opts) -> { svg, joints }  (local coords: feet centre = 0,0, up = -y)
// Poses are hand/foot targets solved with two-bone IK, so every pose shares exactly the same parts.
export const C = {
  paper: '#FAF7F0', ink: '#1A1A1A', shadow: '#E6E1D6', mustard: '#F2C230', sky: '#8EC5E8', sage: '#9CC08B',
  terracotta: '#D9805F', orange: '#F2A65A', pink: '#F4A6B8', peach: '#F7C4AE', fold: '#E39A82', hoodie: '#2B2B2B',
  green: '#2F6B2F', night: '#2E3A52', stage: '#1C1C1C', red: '#D64545', white: '#FFFFFF',
};
const f = (n) => +n.toFixed(2);
const rad = (d) => (d * Math.PI) / 180;
const rot = ([x, y], a, [cx, cy] = [0, 0]) => {
  const c = Math.cos(rad(a)), s = Math.sin(rad(a));
  return [cx + (x - cx) * c - (y - cy) * s, cy + (x - cx) * s + (y - cy) * c];
};
const P = (pts) => pts.map(([x, y], i) => `${i ? 'L' : 'M'}${f(x)} ${f(y)}`).join(' ');

// body dimensions (shared skeleton)
const HIP = -196, TORSO = 125, THIGH = 93, SHIN = 90, UPPER = 85, LOWER = 80, ANKLE = -13;
export const LIE_Y = 150; // ground offset for the lying pose (hip height after rotating)

function ik(root, target, l1, l2, hint) {
  const dx = target[0] - root[0], dy = target[1] - root[1];
  let d = Math.hypot(dx, dy);
  const reach = l1 + l2 - 0.5;
  const ux = d ? dx / d : 0, uy = d ? dy / d : 1;
  d = Math.min(Math.max(d, Math.abs(l1 - l2) + 1), reach);
  const a = (d * d + l1 * l1 - l2 * l2) / (2 * d);
  const h = Math.sqrt(Math.max(l1 * l1 - a * a, 0));
  const bx = root[0] + ux * a, by = root[1] + uy * a;
  const c1 = [bx - uy * h, by + ux * h], c2 = [bx + uy * h, by - ux * h];
  const score = (c) => (c[0] - root[0]) * hint[0] + (c[1] - root[1]) * hint[1];
  const mid = score(c1) >= score(c2) ? c1 : c2;
  return [root, mid, [root[0] + ux * d, root[1] + uy * d]];
}

// ---------------- poses ----------------
// hL/hR: hand targets (screen left/right), hints are elbow/knee bend directions. fL/fR: ankle targets.
const stdFeet = { fL: [-20, ANKLE], fR: [20, ANKLE] };
const armsDown = { hL: [-52, -152], hR: [52, -152], eL: [-1, 0.2], eR: [1, 0.2] };
export const POSES = {
  stand: { ...armsDown, ...stdFeet },
  'stand-strap': { ...armsDown, hR: [36, -262], eR: [1, 1.6], ...stdFeet }, // stand, one hand gripping a backpack strap
  wave: { ...armsDown, hR: [92, -430], eR: [1, 0.3], ...stdFeet },
  think: { hL: [-62, -212], eL: [-1, 0.3], hR: [26, -338], eR: [0.6, 1], ...stdFeet, headTilt: 7 },
  present: { ...armsDown, hR: [172, -292], eR: [0.3, 1], ...stdFeet, palm: 'R' },
  explain: { hL: [-64, -214], eL: [-1, 0.3], hR: [78, -418], eR: [1, 0.6], ...stdFeet, finger: 'R' },
  'point-left': { hL: [-205, -334], eL: [-0.2, 1], hR: [52, -152], eR: [1, 0.2], ...stdFeet, finger: 'L' },
  'point-right': { hR: [205, -334], eR: [0.2, 1], hL: [-52, -152], eL: [-1, 0.2], ...stdFeet, finger: 'R' },
  shrug: { hL: [-112, -262], eL: [-1, 0.8], hR: [112, -262], eR: [1, 0.8], ...stdFeet, headTilt: -6, shoulderUp: 12 },
  facepalm: { hL: [-52, -152], eL: [-1, 0.2], hR: [20, -404], eR: [1, 0.5], ...stdFeet, headTilt: -6, tilt: 3 },
  walk: { hL: [58, -226], eL: [1, 0.4], hR: [-52, -208], eR: [-1, 0.4], fL: [-48, -24], fR: [52, ANKLE], tilt: 3, profile: true, hipDX: 4 },
  'sit-chair': { hipY: -103, hL: [74, -108], eL: [0, 1], hR: [96, -110], eR: [1, 1], fL: [92, ANKLE], fR: [112, ANKLE], profile: true, kneeHint: [0, -1], noShadowLegs: false },
  'sit-bench': { hipY: -103, hL: [70, -108], eL: [0, 1], hR: [92, -110], eR: [1, 1], fL: [92, ANKLE], fR: [112, ANKLE], profile: true, kneeHint: [0, -1] },
  'sit-curb': { hipY: -52, hL: [58, -118], eL: [-0.4, 1], hR: [80, -120], eR: [1, 0.5], fL: [78, ANKLE], fR: [98, ANKLE], profile: true, kneeHint: [0, -1], tilt: 6, headTilt: 6 },
  'lie-bed': { ...armsDown, hL: [-47, -140], hR: [47, -140], fL: [-20, ANKLE], fR: [22, ANKLE], lie: true, kneeHint: [1, 0] },
  'raise-hand': { ...armsDown, hR: [66, -482], eR: [1, 0], ...stdFeet },
  'thumbs-up': { ...armsDown, hR: [96, -318], eR: [1, 0.8], ...stdFeet, thumb: 'R' },
  'hold-front': { hL: [-22, -236], eL: [-1, 1], hR: [22, -236], eR: [1, 1], ...stdFeet },
  'hold-up': { hL: [-40, -462], eL: [-1, 0.3], hR: [40, -462], eR: [1, 0.3], ...stdFeet },
  kneel: { hipY: -108, hL: [76, -128], eL: [0, 1], hR: [-30, -150], eR: [-1, 0.5], fL: [88, ANKLE], fR: [-96, ANKLE], profile: true, kneeHint: [0, -1], rearKnee: true, tilt: 4 },
  stumble: { hL: [-104, -352], eL: [-1, -0.3], hR: [128, -296], eR: [0.4, 1], fL: [-74, -20], fR: [58, ANKLE], tilt: 15, headTilt: 8, profile: true, hipDX: 22 },
  lift: { hL: [-52, -152], eL: [-1, 0.2], hR: [66, -352], eR: [1, 0.9], ...stdFeet, hold: { R: 'dumbbell' } },
  'arms-relaxed': { hL: [-84, -208], eL: [-1, 0.6], hR: [84, -208], eR: [1, 0.6], ...stdFeet },
};
export const EXPRESSIONS = ['happy', 'neutral', 'surprised', 'worried', 'cringe', 'relieved', 'laugh', 'thinking', 'wink'];

// ---------------- narrator face ----------------
function narratorFace(expr) {
  const fold = '#C97B63';
  const oval = (x, y, rx, ry) => `<ellipse cx="${x}" cy="${y}" rx="${rx}" ry="${ry}" fill="#fff" stroke="${C.fold}" stroke-width="2"/>`;
  const arc = (x, y) => `<path d="M${x - 10} ${y + 5} Q${x} ${y - 9} ${x + 10} ${y + 5}" fill="none" stroke="${C.fold}" stroke-width="10" stroke-linecap="round"/><path d="M${x - 10} ${y + 5} Q${x} ${y - 9} ${x + 10} ${y + 5}" fill="none" stroke="#fff" stroke-width="5.5" stroke-linecap="round"/>`;
  const brow = (x1, y1, x2, y2) => `<path d="M${x1} ${y1} L${x2} ${y2}" stroke="${fold}" stroke-width="4.5" stroke-linecap="round"/>`;
  const Y = 8, X = 22;
  switch (expr) {
    case 'happy': case 'relieved': return arc(-X, Y) + arc(X, Y);
    case 'surprised': return oval(-X, Y, 11, 12) + oval(X, Y, 11, 12);
    case 'worried': return oval(-X, Y, 6, 8.5) + oval(X, Y, 6, 8.5) + brow(-34, -9, -14, -19) + brow(34, -9, 14, -19);
    case 'cringe': return oval(-X, Y + 1, 8, 4.5) + oval(X, Y + 1, 8, 4.5) + brow(-35, -6, -13, -20) + brow(35, -6, 13, -20);
    case 'thinking': return oval(-X, Y, 7, 10) + oval(X, Y + 3, 9, 3.5) + brow(10, -14, 34, -10);
    case 'laugh': return arc(-X, Y) + arc(X, Y) + `<path d="M-62 -34 l-9 -8 M-60 -22 l-12 -1 M62 -34 l9 -8 M60 -22 l12 -1" stroke="${C.orange}" stroke-width="3.5" stroke-linecap="round"/>`;
    case 'wink': return oval(-X, Y, 7, 10) + arc(X, Y);
    default: return oval(-X, Y, 7, 10) + oval(X, Y, 7, 10); // neutral
  }
}
function brainSvg(o) {
  const shapes = [[-30, -6, 38, 40], [30, -6, 38, 40], [-17, -26, 34, 26], [17, -26, 34, 26], [0, 20, 44, 26], [-50, 12, 20, 24], [50, 12, 20, 24]];
  const e = (s, extra) => `<ellipse cx="${s[0]}" cy="${s[1]}" rx="${s[2]}" ry="${s[3]}" ${extra}/>`;
  return `<g>
    ${o.glow ? `<ellipse cx="0" cy="0" rx="92" ry="80" fill="${C.peach}" opacity="0.35" filter="url(#hfBlur)"/>` : ''}
    ${shapes.map((s) => e(s, `fill="${C.peach}" stroke="${o.rim}" stroke-width="${o.line * 2 + 1}"`)).join('')}
    ${shapes.map((s) => e(s, `fill="${C.peach}"`)).join('')}
    <path d="M0 -48 Q-5 -14 0 42" stroke="${C.fold}" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M-52 -8 Q-38 -22 -24 -10 M-46 18 Q-34 8 -22 18 M-30 -32 Q-20 -40 -8 -30 M-58 14 Q-54 6 -48 8 M-10 14 Q-18 24 -12 34" stroke="${C.fold}" stroke-width="2.8" fill="none" stroke-linecap="round"/>
    <path d="M52 -8 Q38 -22 24 -10 M46 18 Q34 8 22 18 M30 -32 Q20 -40 8 -30 M58 14 Q54 6 48 8 M10 14 Q18 24 12 34" stroke="${C.fold}" stroke-width="2.8" fill="none" stroke-linecap="round"/>
    ${o.face}
  </g>`;
}

// ---------------- person face ----------------
function personFace(expr) {
  const eye = (x, y, ry = 9, dx = 0, dy = 0) => `<ellipse cx="${x + dx}" cy="${y + dy}" rx="5.5" ry="${ry}" fill="${C.ink}"/><circle cx="${x + dx + 1.8}" cy="${y + dy - 3}" r="2" fill="#fff"/>`;
  const closed = (x, y) => `<path d="M${x - 9} ${y + 4} Q${x} ${y - 8} ${x + 9} ${y + 4}" fill="none" stroke="${C.ink}" stroke-width="4.5" stroke-linecap="round"/>`;
  const brow = (x1, y1, x2, y2) => `<path d="M${x1} ${y1} L${x2} ${y2}" stroke="${C.ink}" stroke-width="4" stroke-linecap="round"/>`;
  const mouthOpen = (w, h, tongue = true) => `<path d="M${-w} 20 Q0 ${20 + h * 2} ${w} 20 Z" fill="${C.ink}" stroke="${C.ink}" stroke-width="3" stroke-linejoin="round"/>${tongue ? `<ellipse cx="0" cy="${20 + h * 1.15}" rx="${w * 0.5}" ry="${h * 0.3}" fill="${C.red}"/>` : ''}`;
  const ln = (d) => `<path d="${d}" fill="none" stroke="${C.ink}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>`;
  const E = 17, Y = -4;
  switch (expr) {
    case 'happy': return eye(-E, Y) + eye(E, Y) + mouthOpen(15, 15);
    case 'surprised': return eye(-E, Y - 1, 10) + eye(E, Y - 1, 10) + brow(-26, -26, -10, -28) + brow(10, -28, 26, -26) + `<ellipse cx="0" cy="27" rx="6" ry="8" fill="${C.ink}"/><ellipse cx="0" cy="31" rx="3.5" ry="3" fill="${C.red}"/>`;
    case 'worried': return eye(-E, Y) + eye(E, Y) + brow(-28, -20, -10, -27) + brow(28, -20, 10, -27) + ln('M-10 31 Q0 22 10 31');
    case 'cringe': return eye(-E, Y, 6) + eye(E, Y, 6) + brow(-28, -17, -9, -28) + brow(28, -17, 9, -28) + ln('M-15 29 L-8 24 L0 30 L8 24 L15 29');
    case 'relieved': return closed(-E, Y) + closed(E, Y) + ln('M-11 24 Q0 33 11 24');
    case 'laugh': return closed(-E, Y) + closed(E, Y) + mouthOpen(16, 16);
    case 'thinking': return eye(-E, Y, 9, -3, -3) + eye(E, Y, 9, -3, -3) + brow(8, -26, 28, -30) + ln('M-7 28 L9 25');
    case 'wink': return closed(-E, Y) + eye(E, Y) + mouthOpen(14, 13);
    default: return eye(-E, Y) + eye(E, Y) + ln('M-9 24 Q0 29 9 24'); // neutral
  }
}
const HAIR = {
  a: { back: '', front: `<path d="M-51 -6 Q-56 -60 0 -58 Q56 -60 51 -6 Q40 -34 4 -35 Q-30 -36 -51 -6Z" fill="${C.ink}" stroke="${C.ink}" stroke-width="3" stroke-linejoin="round"/>` },
  b: { back: '', front: '' },
  c: { back: `<path d="M-52 -10 Q-62 50 -44 66 L-30 40 L30 40 L44 66 Q62 50 52 -10Z" fill="${C.ink}" stroke="${C.ink}" stroke-width="3" stroke-linejoin="round"/>`,
    front: `<path d="M-51 -4 Q-52 -60 0 -58 Q52 -60 51 -4 Q30 -30 6 -34 Q-24 -30 -51 -4Z" fill="${C.ink}" stroke="${C.ink}" stroke-width="3" stroke-linejoin="round"/>` },
  d: { back: '', front: `<path d="M-50 -8 Q-54 -58 0 -57 Q54 -58 50 -4 Q44 -26 20 -40 Q-14 -28 -50 -8Z" fill="${C.ink}" stroke="${C.ink}" stroke-width="3" stroke-linejoin="round"/>` },
};
export const VARIANTS = { a: C.sky, b: C.sage, c: C.terracotta, d: C.sage };

// ---------------- figure ----------------
export function figure(kind, poseName, expr = 'neutral', opts = {}) {
  const pose = { ...POSES[poseName] };
  if (!POSES[poseName]) throw new Error(`unknown pose ${poseName}`);
  const narr = kind === 'narrator';
  const rim = opts.rim || C.ink;
  const line = narr ? 4 : 5;
  const flipSign = 1;
  const hipY = pose.hipY ?? HIP;
  const tilt = pose.tilt || 0;
  const hipDX = pose.hipDX || 0;
  const hipC = [hipDX, hipY];
  const hipsX = narr ? 16 : 14;
  const sx = narr ? 44 : 38;
  const sUp = pose.shoulderUp || 0;
  const shY = -TORSO + 12 - sUp; // relative to hip
  const R = (p) => rot(p, tilt, hipC);
  const shL = R([hipDX - sx, hipY + shY]), shR = R([hipDX + sx, hipY + shY]);
  const hipL = [hipDX - hipsX, hipY], hipR = [hipDX + hipsX, hipY];
  const kh = pose.kneeHint || [1, 0];
  const legL = ik(hipL, pose.fL, THIGH, SHIN, pose.rearKnee ? [0, 1] : kh);
  const legR = ik(hipR, pose.fR, THIGH, SHIN, kh);
  const armL = ik(shL, pose.hL, UPPER, LOWER, pose.eL || [-1, 0.3]);
  const armR = ik(shR, pose.hR, UPPER, LOWER, pose.eR || [1, 0.3]);
  const headBase = R([hipDX, hipY - TORSO + 6]);
  let headC = narr ? rot([0, -(TORSO) - 66 + (hipY - HIP) * 0 - 0], 0, [0, 0]) : [0, 0];
  const neckLen = narr ? 62 : 52; // from shoulder line to head centre (brain: 64+ overlap)
  const topOfTorso = R([hipDX, hipY - TORSO]);
  const dirUp = rot([0, -1], tilt);
  headC = [topOfTorso[0] + dirUp[0] * neckLen, topOfTorso[1] + dirUp[1] * neckLen];
  const headTilt = (pose.headTilt || 0) + tilt;

  // global transform for lying
  let G = (p) => p;
  if (pose.lie) {
    G = (p) => rot(p, -90, [0, hipY]);
    // head stays upright, tilted a little
  }
  const g = G;
  const pts = (a) => a.map(g);
  const [lL, aL] = [pts(legL), pts(armL)], [lR, aR] = [pts(legR), pts(armR)];

  let s = '';
  const limb = (a, w, fill, outline) => `<path d="${P(a)}" fill="none" stroke="${outline}" stroke-width="${w + line * 2}" stroke-linecap="round" stroke-linejoin="round"/>` +
    `<path d="${P(a)}" fill="none" stroke="${fill}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"/>`;
  const thin = (a) => `<path d="${P(a)}" fill="none" stroke="${C.ink}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>`;
  const shoe = (ankle, side) => {
    const dir = pose.profile ? 1 : (side === 'L' ? -1 : 1);
    const [ax, ay] = ankle;
    if (narr) {
      const x0 = dir > 0 ? ax - 13 : ax - 29;
      return `<g><rect x="${f(x0)}" y="${f(ay - 2)}" width="42" height="15" rx="7.5" fill="#fff" stroke="${rim === C.ink ? C.ink : rim}" stroke-width="3.2"/>` +
        `<path d="M${f(x0 + 5)} ${f(ay + 9.5)} L${f(x0 + 37)} ${f(ay + 9.5)}" stroke="${C.red}" stroke-width="2.6" stroke-linecap="round"/></g>`;
    }
    return `<ellipse cx="${f(ax + dir * 8)}" cy="${f(ay + 5)}" rx="17" ry="8" fill="${C.ink}"/>`;
  };
  const hand = (p, side, name) => {
    const r = narr ? 10.5 : 7.5;
    let h = `<circle cx="${f(p[0])}" cy="${f(p[1])}" r="${r}" fill="${narr ? C.hoodie : C.ink}" stroke="${narr ? rim : C.ink}" stroke-width="${narr ? 3 : 1}"/>`;
    if (pose.finger === side) h += `<path d="M${f(p[0] + (side === 'L' ? -2 : 2))} ${f(p[1] - 2)} l${side === 'L' ? -14 : 14} -22" stroke="${narr ? C.hoodie : C.ink}" stroke-width="7" stroke-linecap="round"/>`;
    if (pose.thumb === side) h += `<path d="M${f(p[0])} ${f(p[1] - 6)} l0 -17" stroke="${narr ? C.hoodie : C.ink}" stroke-width="8" stroke-linecap="round"/>`;
    if (pose.palm === side) h = `<ellipse cx="${f(p[0] + 8)}" cy="${f(p[1] - 3)}" rx="17" ry="9" fill="${narr ? C.hoodie : C.ink}" stroke="${narr ? rim : C.ink}" stroke-width="${narr ? 3 : 1}"/>`;
    return h;
  };

  // shadow
  if (opts.shadow !== false && !pose.lie) s += `<ellipse cx="${f(hipDX * 0.5)}" cy="2" rx="${pose.profile ? 96 : 84}" ry="11" fill="${C.shadow}"/>`;
  const torsoT = (inner) => {
    const [tx, ty] = g([hipDX, hipY]);
    const ang = pose.lie ? tilt - 90 : tilt;
    return `<g transform="translate(${f(tx)} ${f(ty)}) rotate(${f(ang)})">${inner}</g>`;
  };

  if (narr) {
    const legW = 17;
    // backpack (behind torso)
    if (opts.backpack) s += torsoT(`<rect x="-58" y="-132" width="116" height="118" rx="26" fill="${C.terracotta}" stroke="${rim}" stroke-width="${line}"/><rect x="-36" y="-84" width="72" height="50" rx="12" fill="${C.terracotta}" stroke="${rim}" stroke-width="${line - 1}"/>`);
    // legs
    s += limb(lL, legW, C.hoodie, rim) + limb(lR, legW, C.hoodie, rim);
    s += shoe(g(pose.fL), 'L') + shoe(g(pose.fR), 'R');
    // pelvis blend
    // neck + hood
    const hq = g(headBase);
    s += `<path d="${P([g(topOfTorso), g([headC[0], headC[1] + 36])])}" stroke="${rim}" stroke-width="${17 + line * 2}" stroke-linecap="round" fill="none"/><path d="${P([g(topOfTorso), g([headC[0], headC[1] + 36])])}" stroke="${C.hoodie}" stroke-width="17" stroke-linecap="round" fill="none"/>`;
    s += torsoT(`<path d="M-30 -118 Q-32 -142 -4 -136 L4 -136 Q32 -142 30 -118 Z" fill="${C.hoodie}" stroke="${rim}" stroke-width="${line}" stroke-linejoin="round"/>`);
    // torso hoodie
    s += torsoT(`<path d="M-43 2 L-47 -92 Q-48 -116 -28 -122 L28 -122 Q48 -116 47 -92 L43 2 Q0 8 -43 2Z" fill="${C.hoodie}" stroke="${rim}" stroke-width="${line}" stroke-linejoin="round"/>` +
      `<path d="M-43 -12 Q0 -6 43 -12" stroke="${C.ink}" stroke-width="3" fill="none"/>` +
      `<path d="M-25 -44 Q0 -36 25 -44 L28 -16 Q0 -10 -28 -16Z" fill="none" stroke="${C.ink}" stroke-width="3" stroke-linejoin="round"/>` +
      `<path d="M-9 -120 L-11 -80 M9 -120 L11 -80" stroke="${C.ink}" stroke-width="3.2" stroke-linecap="round"/><path d="M-26 -122 Q0 -108 26 -122" stroke="${C.ink}" stroke-width="3" fill="none"/>`);
    if (opts.backpack) {
      for (const sd of [-1, 1]) s += torsoT(`<path d="M${sd * 31} -118 L${sd * 34} -34" stroke="${rim}" stroke-width="${14 + line}" stroke-linecap="round"/><path d="M${sd * 31} -118 L${sd * 34} -34" stroke="${C.terracotta}" stroke-width="${14}" stroke-linecap="round"/>`);
    }
    // arms
    s += limb(aL, 13, C.hoodie, rim) + limb(aR, 13, C.hoodie, rim);
    // props held
    s += propsOnHands(pose, opts, aL[2], aR[2]);
    s += hand(aL[2], 'L') + hand(aR[2], 'R');
    // brain
    const face = narratorFace(expr);
    const o = { glow: opts.glow !== false, rim, line, face };
    s += `<g transform="translate(${f(g(headC)[0])} ${f(g(headC)[1])}) rotate(${f(pose.lie ? -14 : headTilt)})">${brainSvg(o)}${opts.sweat ? sweatDrop(66, -34) : ''}</g>`;
  } else {
    const color = VARIANTS[opts.variant || 'a'];
    const hair = HAIR[opts.variant || 'a'];
    s += thin(lL) + thin(lR) + shoe(g(pose.fL), 'L') + shoe(g(pose.fR), 'R');
    if (opts.shirt) { /* custom shirt overlay handled by caller */ }
    s += torsoT(`<path d="M-37 4 L-40 -92 Q-40 -118 -22 -122 L22 -122 Q40 -118 40 -92 L37 4 Q0 8 -37 4Z" fill="${opts.shirtColor || color}" stroke="${C.ink}" stroke-width="${line}" stroke-linejoin="round"/>${opts.shirtArt || ''}`);
    s += thin(aL) + thin(aR);
    s += propsOnHands(pose, opts, aL[2], aR[2]);
    s += hand(aL[2], 'L') + hand(aR[2], 'R');
    const hc = g(headC);
    s += `<g transform="translate(${f(hc[0])} ${f(hc[1])}) rotate(${f(pose.lie ? -14 : headTilt)})">${hair.back}<circle r="52" fill="#fff" stroke="${C.ink}" stroke-width="${line}"/>${hair.front}${personFace(expr)}${opts.sweat ? sweatDrop(62, -30) : ''}</g>`;
  }
  const hands = { L: aL[2], R: aR[2] };
  return { svg: `<g>${s}</g>`, hands, head: g(headC) };
}
function sweatDrop(x, y) {
  return `<path d="M${x} ${y - 20} Q${x + 14} ${y} ${x} ${y + 9} Q${x - 14} ${y} ${x} ${y - 20}Z" fill="${C.sky}" stroke="${C.ink}" stroke-width="3" stroke-linejoin="round"/>`;
}
function propsOnHands(pose, opts, hl, hr) {
  const held = { ...(pose.hold || {}), ...(opts.hold || {}) };
  let s = '';
  for (const [side, name] of Object.entries(held)) {
    const h = side === 'L' ? hl : hr;
    s += heldProp(name, h);
  }
  return s;
}
export function heldProp(name, [x, y]) {
  const I = C.ink;
  switch (name) {
    case 'dumbbell': return `<g transform="translate(${f(x)} ${f(y)})"><path d="M-30 0 H30" stroke="${I}" stroke-width="8" stroke-linecap="round"/><rect x="-42" y="-17" width="16" height="34" rx="5" fill="${C.terracotta}" stroke="${I}" stroke-width="4"/><rect x="26" y="-17" width="16" height="34" rx="5" fill="${C.terracotta}" stroke="${I}" stroke-width="4"/></g>`;
    case 'clipboard': return `<g transform="translate(${f(x)} ${f(y - 6)})"><rect x="-30" y="-44" width="60" height="78" rx="6" fill="${C.paper}" stroke="${I}" stroke-width="4"/><rect x="-12" y="-52" width="24" height="14" rx="4" fill="${C.mustard}" stroke="${I}" stroke-width="3.5"/><path d="M-18 -22 H18 M-18 -8 H18 M-18 6 H8" stroke="${I}" stroke-width="3.5" stroke-linecap="round"/></g>`;
    case 'magnifier': return `<g transform="translate(${f(x)} ${f(y)})"><path d="M0 0 L26 -26" stroke="${I}" stroke-width="9" stroke-linecap="round"/><circle cx="52" cy="-52" r="46" fill="${C.sky}" fill-opacity="0.35" stroke="${I}" stroke-width="6"/></g>`;
    case 'scissors': return `<g transform="translate(${f(x)} ${f(y)}) rotate(-20)"><path d="M0 0 L-70 -120 M0 0 L70 -120" stroke="${I}" stroke-width="9" stroke-linecap="round"/><circle cx="-18" cy="22" r="18" fill="none" stroke="${C.terracotta}" stroke-width="9"/><circle cx="18" cy="22" r="18" fill="none" stroke="${C.terracotta}" stroke-width="9"/></g>`;
    default: return '';
  }
}

// place a figure in scene coords: ground point (x,y), scale, optional horizontal flip
export function place(fig, x, y, scale = 1, flip = false) {
  return `<g transform="translate(${f(x)} ${f(y)}) scale(${flip ? -scale : scale} ${scale})">${fig.svg}</g>`;
}
export const DEFS = `<defs><filter id="hfBlur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14"/></filter></defs>`;
