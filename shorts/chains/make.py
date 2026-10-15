import re, subprocess, random, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

D = '/tmp/claude-0/chains/'
FONT = '/tmp/claude-0/sh/package/files/nunito-latin-800-normal.woff'
W, H, FPS = 1080, 1920, 30
VO_LEN = 30.51
TOTAL = 32.0
INK, WHITE, YEL, RED = (20, 20, 20), (255, 255, 255), (242, 194, 48), (214, 69, 69)

# phrase start times (from the pauses in the voice) and texts
PHR = [(0.15, "When you're young,"), (1.41, "you think your life will start..."), (3.05, "once you're free."),
       (4.35, "First, you just have to finish school."), (6.82, "Then get a good job."), (8.40, "Then pay off the bills."),
       (10.19, "Then make everyone proud."), (12.44, "So you keep pulling."), (14.19, "One chain at a time."),
       (16.00, "And when the last one finally breaks..."), (18.53, "you're free."),
       (19.61, "But you're too old to experience freedom."), (22.40, "You spend your whole life fighting to be free..."),
       (25.14, "and forget to live while you're pulling."), (27.38, "Don't wait for the last chain to break..."),
       (29.70, "Be free...")]
PEND = [0.97, 2.66, 3.84, 6.39, 8.00, 9.82, 11.90, 13.56, 15.38, 17.94, 19.01, 21.84, 24.69, 26.79, 29.17, 30.3]

# chain snaps: (time, label index)
SNAPS = [(5.95, 0), (7.65, 1), (9.42, 2), (11.40, 3), (17.40, 4)]
LABELS = ['SCHOOL', 'A GOOD JOB', 'THE BILLS', 'MAKE THEM PROUD', 'SOMEDAY']

# shots: (start, end, image, zoom_from, zoom_to, focus_x, focus_y)
SHOTS = [(0.0, 4.35, 'SH1', 1.00, 1.04, .5, .55), (4.35, 5.95, 'SH1', 1.22, 1.25, .62, .5),
         (5.95, 9.42, 'SH2', 1.00, 1.05, .5, .55), (9.42, 11.40, 'SH3', 1.00, 1.04, .5, .55),
         (11.40, 14.19, 'SH4', 1.00, 1.04, .5, .55), (14.19, 17.40, 'SH4', 1.18, 1.22, .45, .55),
         (17.40, 19.61, 'SH5', 1.06, 1.00, .45, .5), (19.61, 22.40, 'SH6', 1.00, 1.05, .6, .6),
         (22.40, 27.38, 'SH6', 1.20, 1.28, .62, .52), (27.38, TOTAL, 'SH7', 1.00, 1.06, .45, .45)]

imgs = {}
for k in ['SH1', 'SH2', 'SH3', 'SH4', 'SH5', 'SH6', 'SH7']:
    im = Image.open(D + k + '.jpg').convert('RGB')
    s = max(W / im.width, H / im.height) * 1.3
    imgs[k] = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)

def frame_img(k, z, fx, fy):
    im = imgs[k]; base = max(W / im.width, H / im.height) * 1.3
    cw, ch = W / (z * base / base) / 1.3 * 1.0, None
    # crop window in the 1.3x image: window size = (W,H)*1.3/z
    ww, wh = W * 1.3 / z, H * 1.3 / z
    cx, cy = fx * im.width, fy * im.height
    x0 = min(max(cx - ww / 2, 0), im.width - ww); y0 = min(max(cy - wh / 2, 0), im.height - wh)
    return im.resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + ww, y0 + wh))

f_cap = ImageFont.truetype(FONT, 76)
f_lab = ImageFont.truetype(FONT, 44)
f_big = ImageFont.truetype(FONT, 120)

def syl(w):
    w = re.sub(r"[^a-z]", "", w.lower()); n = len(re.findall(r"[aeiouy]+", w))
    if w.endswith('e') and n > 1: n -= 1
    return max(1, n) + 0.4

def stroke_text(d, xy, text, font, fill, sw=8):
    d.text(xy, text, font=font, fill=fill, stroke_width=sw, stroke_fill=INK)

def ease(x): return 1 - (1 - x) ** 3

def draw_labels(d, t):
    if t < 1.0 or 19.61 <= t < 27.38 or t >= 28.2: return
    restored = t >= 27.38
    y = 150
    for i, lab in enumerate(LABELS):
        appear = 1.0 + i * 0.15 if not restored else 27.38
        if t < appear: continue
        snapped = (not restored) and any(t >= st and li == i for st, li in SNAPS)
        tw = d.textlength(lab, font=f_lab); x = (W - tw) / 2
        if snapped:
            d.rounded_rectangle((x - 26, y - 10, x + tw + 26, y + 62), 20, fill=(70, 70, 70), outline=INK, width=5)
            d.text((x, y), lab, font=f_lab, fill=(150, 150, 150))
            st = [s for s, li in SNAPS if li == i][0]
            p = min(1, (t - st) / 0.25)
            d.line((x - 14, y + 27, x - 14 + (tw + 28) * p, y + 27), fill=RED, width=9)
        else:
            d.rounded_rectangle((x - 26, y - 10, x + tw + 26, y + 62), 20, fill=YEL, outline=INK, width=5)
            d.text((x, y), lab, font=f_lab, fill=INK)
        y += 88

def draw_caption(d, t):
    for i, (s, txt) in enumerate(PHR):
        e = PEND[i]
        if s - 0.05 <= t < e + 0.25:
            words = txt.split(); ws = [syl(w) for w in words]; tot = sum(ws)
            dur = e - s; acc = 0; hi = 0
            for j, w in enumerate(ws):
                if t >= s + dur * acc / tot - 0.05: hi = j
                acc += w
            # wrap into lines of <= 18 chars
            lines, cur = [], []
            for j, w in enumerate(words):
                if cur and len(' '.join(words[k] for k in cur + [j])) > 18: lines.append(cur); cur = []
                cur.append(j)
            lines.append(cur)
            y = 1440 - (len(lines) - 1) * 50
            for ln in lines:
                parts = [words[j].upper() for j in ln]
                gap = 26; lw = sum(d.textlength(p, font=f_cap) for p in parts) + gap * (len(parts) - 1)
                x = (W - lw) / 2
                for j, p in zip(ln, parts):
                    col = YEL if j == hi else WHITE
                    stroke_text(d, (x, y), p, f_cap, col)
                    x += d.textlength(p, font=f_cap) + gap
                y += 100
            return

def draw_end(d, t):
    if t >= 28.2:
        a = min(1, (t - 28.2) / 0.3)
        txt = "DON'T WAIT." if t < 29.7 else "BE FREE."
        tw = d.textlength(txt, font=f_big)
        stroke_text(d, ((W - tw) / 2, 230), txt, f_big, YEL if t < 29.7 else WHITE, 12)

enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p', D + 'video.mp4'], stdin=subprocess.PIPE)
N = int(TOTAL * FPS)
for n in range(N):
    t = n / FPS
    sh = [s for s in SHOTS if s[0] <= t < s[1]][-1]
    p = (t - sh[0]) / (sh[1] - sh[0])
    z = sh[3] + (sh[4] - sh[3]) * p
    # snap: punch + shake for 3 frames
    dx = dy = 0
    for st, li in SNAPS:
        if 0 <= t - st < 0.1:
            k = 14 if li == 4 else 7
            dx, dy = random.choice([-k, k]), random.choice([-k, k])
        if 0 <= t - st < 0.2: z *= 1 + 0.04 * (1 - (t - st) / 0.2)
    im = frame_img(sh[2], z, sh[5] + dx / 3000, sh[6] + dy / 3000)
    # final break: white flash
    if 0 <= t - 17.40 < 0.25:
        a = 1 - (t - 17.40) / 0.25
        im = Image.blend(im, Image.new('RGB', (W, H), (255, 240, 210)), 0.75 * a)
    # gentle fade from SH5 into SH6 and out at the end
    if 19.61 <= t < 19.91:
        prev = frame_img('SH5', 1.0, .45, .5)
        im = Image.blend(prev, im, (t - 19.61) / 0.3)
    # darken bottom for captions
    d = ImageDraw.Draw(im)
    draw_labels(d, t)
    draw_caption(d, t)
    draw_end(d, t)
    enc.stdin.write(im.tobytes())
enc.stdin.close(); enc.wait()

# audio: voice + snaps + soft music
snap_f = ' '.join([])
snd = D + 'snap.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'anoisesrc=d=0.18:c=white:a=0.9', '-f', 'lavfi', '-i', 'sine=f=1850:d=0.35',
                '-f', 'lavfi', '-i', 'sine=f=2650:d=0.3', '-filter_complex',
                '[0]highpass=f=1800,afade=t=out:d=0.18[n];[1]afade=t=out:d=0.35,volume=0.5[a];[2]afade=t=out:d=0.3,volume=0.35[b];[n][a][b]amix=inputs=3:normalize=0,volume=1.4',
                snd], check=True)
boom = D + 'boom.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'sine=f=55:d=1.2', '-af', 'afade=t=out:d=1.2,volume=1.6', boom], check=True)
inputs = ['-i', D + 'vo.mp3', '-ss', '30', '-i', '/home/claude/simplemind-videos/music/track.mp3']
fc = []; mix = ['[vo]', '[mu]']
fc.append('[0]apad=pad_dur=%.2f[vo]' % (TOTAL - VO_LEN))
fc.append('[1]atrim=0:%.2f,asetpts=PTS-STARTPTS,volume=0.10,afade=t=in:d=1.5,afade=t=out:st=%.2f:d=2[mu]' % (TOTAL, TOTAL - 2))
idx = 2
for st, li in SNAPS:
    inputs += ['-i', snd]
    fc.append(f'[{idx}]adelay={int(st*1000)}|{int(st*1000)},volume={0.5 if li < 4 else 0.8}[s{idx}]'); mix.append(f'[s{idx}]'); idx += 1
inputs += ['-i', boom]; fc.append(f'[{idx}]adelay=17400|17400[s{idx}]'); mix.append(f'[s{idx}]'); idx += 1
inputs += ['-i', '/home/claude/simplemind-videos/assets/sfx/riser.wav']; fc.append(f'[{idx}]adelay=16700|16700,volume=0.5[s{idx}]'); mix.append(f'[s{idx}]'); idx += 1
fc.append(''.join(mix) + f'amix=inputs={len(mix)}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[out]')
subprocess.run(['ffmpeg', '-v', 'error', '-y', *inputs, '-i', D + 'video.mp4', '-filter_complex', ';'.join(fc),
                '-map', f'{idx}:v', '-map', '[out]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-t', str(TOTAL),
                '-movflags', '+faststart', D + 'short-chains.mp4'], check=True)
print('done')
