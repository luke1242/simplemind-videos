import json, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont

SRC = '/home/claude/simplemind-videos/videos/02-regret/full-small.mp4'
OUT = '/tmp/claude-0/sh2/short-regret.mp4'
FONT = '/tmp/claude-0/sh/package/files/nunito-latin-800-normal.woff'
OFF = 138.0  # part 2 start in the full video
INK, CREAM, YEL = (26, 26, 26), (250, 247, 240), (242, 194, 48)
W, H = 1080, 1920
BX, BY, BW, BH = 40, 560, 1000, 750       # video box
SEGS = None
END_HOLD = 1.8

words = [w for w in json.load(open('/home/claude/simplemind-videos/videos/02-regret/scenes/part2.words.json'))['words']]
# merge 'eighty four %' -> '84%'
m=[]
for w in words:
    if w['w'].strip()=='%' and len(m)>=2 and m[-2]['w'].strip().lower()=='eighty':
        m[-2]={'w':'84%','s':m[-2]['s'],'e':w['e']}; m.pop(); continue
    m.append(w)
words=m
# segments by word ranges (part-2 time), padded
RANGES=[('They','frames.'),('First,','flip.'),('About','did.'),('Then','life?'),('84%','do.'),('So,','tonight.'),('But','grow.')]
idx=0; SEGS=[]
ws_=words
starts=[i for i,w in enumerate(ws_) if w['s']>=80.4]
i=starts[0]
for a,b in RANGES:
    while ws_[i]['w'].strip()!=a: i+=1
    j=i
    while ws_[j]['w'].strip()!=b: j+=1
    s=ws_[i]['s']-0.12; e=min(ws_[j]['e']+0.3, ws_[j+1]['s']-0.05)
    if b=='do.': e=ws_[j]['e']+1.8   # hold the reveal
    SEGS.append((round(s+OFF,2), round(e+OFF,2))); i=j+1
print(SEGS)
for w in words:
    w['s'] += OFF; w['e'] += OFF

# map original -> short time
def to_new(t):
    acc = 0
    for a, b in SEGS:
        if a <= t <= b: return acc + (t - a)
        acc += b - a
    return None
total = sum(b - a for a, b in SEGS)

# words inside segments, grouped into caption chunks (<=3 words, break at punctuation)
ws = []
for w in words:
    ns, ne = to_new(w['s']), to_new(min(w['e'], w['s'] + 0.9))
    if ns is None: continue
    if ne is None: ne = ns + 0.3
    txt = w['w'].strip()
    if txt.startswith('-'):  # whisper split "t -shirt"
        ws[-1]['t'] += txt; ws[-1]['e'] = ne; continue
    ws.append({'t': txt, 's': ns, 'e': ne})
chunks, cur = [], []
for w in ws:
    cur.append(w)
    if len(cur) == 3 or w['t'][-1] in '.,?!' or sum(len(x['t']) + 1 for x in cur) > 13:
        chunks.append(cur); cur = []
if cur: chunks.append(cur)
for i, c in enumerate(chunks):
    c_end = chunks[i + 1][0]['s'] if i + 1 < len(chunks) else total + END_HOLD
    for w in c: w['chunk_end'] = min(c_end, c[-1]['e'] + 0.6)

f_head = ImageFont.truetype(FONT, 92)
f_cap = ImageFont.truetype(FONT, 88)
f_end = ImageFont.truetype(FONT, 80)

def badge(d, xy, text, font, fill, fg=INK, pad=(22, 10)):
    x, y = xy
    l, t, r, b = d.textbbox((x, y), text, font=font)
    d.rounded_rectangle((l - pad[0], t - pad[1], r + pad[0], b + pad[1]), 22, fill=fill, outline=INK, width=6)
    d.text((x, y), text, font=font, fill=fg)

def line_w(d, parts, font, gap):
    return sum(d.textlength(p, font=font) for p in parts) + gap * (len(parts) - 1)

# static background: cream + header + box outline
base = Image.new('RGB', (W, H), CREAM)
d = ImageDraw.Draw(base)
y = 250
for line in [['WHAT', 'DO', 'PEOPLE'], ['REGRET', 'MOST?']]:
    gap = 40; x = (W - line_w(d, line, f_head, gap)) / 2
    for p in line:
        if p == 'REGRET': badge(d, (x, y), p, f_head, YEL)
        else: d.text((x, y), p, font=f_head, fill=INK)
        x += d.textlength(p, font=f_head) + gap
    y += 130

def caption(img, t):
    d = ImageDraw.Draw(img)
    if t > total:  # end card
        msg = [['FULL', 'VIDEO'], ['LINKED', 'BELOW']]
        y = 1385
        for line in msg:
            x = (W - line_w(d, line, f_end, 40)) / 2
            for p in line:
                if p == 'BELOW': badge(d, (x, y), p, f_end, YEL)
                else: d.text((x, y), p, font=f_end, fill=INK)
                x += d.textlength(p, font=f_end) + 40
            y += 100
        return
    for c in chunks:
        if c[0]['s'] - 0.05 <= t < c[-1]['chunk_end']:
            parts = [w['t'].upper().rstrip(',.') for w in c]
            hi = max([i for i, w in enumerate(c) if w['s'] - 0.05 <= t] or [0])
            size = 88
            while True:
                f = ImageFont.truetype(FONT, size); gap = 52
                if line_w(d, parts, f, gap) <= 940 or size <= 56: break
                size -= 4
            x = (W - line_w(d, parts, f, gap)) / 2; y = 1410 + (88 - size) // 2
            for i, p in enumerate(parts):
                if i == hi: badge(d, (x, y), p, f, YEL)
                else: d.text((x, y), p, font=f, fill=INK)
                x += d.textlength(p, font=f) + gap
            return

# 1) cut segments (video + audio, tiny audio fades to avoid clicks)
fc, cat = [], ''
for i, (a, b) in enumerate(SEGS):
    fc.append(f'[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}]')
    fc.append(f'[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={b-a-0.04:.3f}:d=0.04[a{i}]')
    cat += f'[v{i}][a{i}]'
fc.append(f'{cat}concat=n={len(SEGS)}:v=1:a=1[v][a]')
fc.append(f'[v]tpad=stop_mode=clone:stop_duration={END_HOLD}[vo]')
fc.append(f'[a]apad=pad_dur={END_HOLD}[ao]')
import os
if not os.path.exists("/tmp/claude-0/sh2/cut.mp4"): subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', SRC, '-filter_complex', ';'.join(fc),
                '-map', '[vo]', '-map', '[ao]', '-c:v', 'libx264', '-crf', '14', '-preset', 'fast',
                '-c:a', 'aac', '-b:a', '192k', '/tmp/claude-0/sh2/cut.mp4'], check=True)

# 2) compose vertical frames
dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', '/tmp/claude-0/sh2/cut.mp4', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '30', '-i', '-',
                        '-i', '/tmp/claude-0/sh2/cut.mp4', '-map', '0:v', '-map', '1:a',
                        '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11',
                        '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
                        '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-shortest', OUT], stdin=subprocess.PIPE)
mask = Image.new('L', (BW, BH), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, BW - 1, BH - 1), 34, fill=255)
n = 0
while True:
    raw = dec.stdout.read(1920 * 1080 * 3)
    if len(raw) < 1920 * 1080 * 3: break
    t = n / 30; n += 1
    fr = Image.frombuffer('RGB', (1920, 1080), raw)
    a = np.asarray(fr)
    corner = a[10:60, 10:60].reshape(-1, 3)
    side = np.concatenate([a[:, :240], a[:, 1680:]], 1).mean(2)
    left = a[300:1000, 40:380].mean(2)
    if corner.std(0).max() < 6 and corner.mean() > 200 and (left < 60).sum() > 2000:
        box = fr.crop((440, 0, 1880, 1080)).resize((BW, BH), Image.LANCZOS)   # host: the content frame
    else:
        box = fr.crop((240, 0, 1680, 1080)).resize((BW, BH), Image.LANCZOS)
    img = base.copy()
    img.paste(box, (BX, BY), mask)
    ImageDraw.Draw(img).rounded_rectangle((BX - 3, BY - 3, BX + BW + 2, BY + BH + 2), 36, outline=INK, width=7)
    caption(img, t)
    enc.stdin.write(img.tobytes())
enc.stdin.close(); enc.wait()
print('frames', n, 'dur', n / 30, 'speech', total)
