"""Short from video 7: the 2 AM replay and the liking gap (cold open).
Cuts the full render, puts it on a vertical blurred background, adds a title and word-timed captions.
Run: python3 shorts/overthinking/make.py  ->  shorts/overthinking/short-liking-gap.mp4"""
import json, os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

R = os.path.dirname(os.path.abspath(__file__)) + '/'
ROOT = R + '../../'
SRC = ROOT + 'renders/full-small.mp4'
D = '/tmp/claude-0/overshort/'; os.makedirs(D, exist_ok=True)
FONT = ROOT + 'assets/fonts/nunito-latin-900-normal.woff'
W, H, FPS = 1080, 1920, 30
T0, T1 = 0.0, 58.5          # global times in the full video: the whole cold open, D01-D10
END = T1 - T0; HOLD = 2.8; TOTAL = END + HOLD
INK, PAPER, MUST = (26, 26, 26), (250, 247, 240), (242, 194, 48)

TEXT = 'It\'s two in the morning. You\'re exhausted. Your eyes are closed. And then your brain says, "Hey. Remember that thing you said today?" And now you\'re wide awake. Replaying it. "Why did I say it like that?" "Did they think I was weird?" "Why did I laugh at my own joke?" Ten seconds of a conversation... and you\'ve watched it fifty times. Here\'s what\'s strange. In two thousand eighteen, a team of researchers paired up strangers and had them talk for just five minutes. Afterward, each person rated how much they liked the other one, and how much they thought the other one liked them. Almost everyone made the same mistake. Their partner liked them more than they thought. The researchers called it the liking gap. The conversation you\'re replaying at two A.M.? It probably went better than you think.'

# word times from the build's transcript (part 4 starts after parts 1-3 + two 1s gaps... + 1s)
off = sum(json.load(open(ROOT + f'scenes/part{n}.timing.json'))['duration'] + 1.0 for n in ())
tw = [w for s in json.load(open(ROOT + 'scenes/part1.timing.json'))['scenes'] for w in s['words']]
tw = [dict(w, s=w['s'] + off - T0, e=w['e'] + off - T0) for w in tw if T0 - 0.05 <= w['s'] + off <= T1]
toks = TEXT.split()
assert len(toks) == len(tw), (len(toks), len(tw))
WORDS = [{'w': t, 's': w['s'], 'e': w['e']} for t, w in zip(toks, tw)]

# chunks of up to 3 words, broken at punctuation
CHUNKS, cur = [], []
for i, w in enumerate(WORDS):
    cur.append(w)
    gap = i + 1 < len(WORDS) and WORDS[i + 1]['s'] - w['e'] > 0.45
    if len(cur) == 3 or w['w'][-1] in '.,?!"' or gap or i + 1 == len(WORDS):
        CHUNKS.append(cur); cur = []
for i, c in enumerate(CHUNKS):
    nxt = CHUNKS[i + 1][0]['s'] if i + 1 < len(CHUNKS) else END
    c_end = min(nxt, c[-1]['e'] + 0.5)
    for w in c: w['ce'] = c_end

FONTS = {}
def font(sz):
    if sz not in FONTS: FONTS[sz] = ImageFont.truetype(FONT, sz)
    return FONTS[sz]

def clean(w):
    w = w.strip('"')
    return w.rstrip('.,') if w.endswith(('.', ',')) else w

def caption(im, t):
    for c in CHUNKS:
        if c[0]['s'] - 0.04 <= t < c[0]['ce']:
            words = [clean(w['w']).upper() for w in c]
            hi = max([i for i, w in enumerate(c) if t >= w['s'] - 0.04] or [0])
            sz = 118; tmp = ImageDraw.Draw(im)
            while tmp.textlength(' '.join(words), font=font(sz)) > 960 and sz > 70: sz -= 6
            f = font(sz)
            p = min(1, (t - c[0]['s'] + 0.04) / 0.14); p = 1 - (1 - p) ** 3
            sc = 0.9 + 0.1 * p
            layer = Image.new('RGBA', (W, 300), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
            x = (W - ld.textlength(' '.join(words), font=f)) / 2
            for i, w in enumerate(words):
                ld.text((x, 80), w, font=f, fill=MUST if i == hi else (255, 255, 255),
                        stroke_width=10, stroke_fill=INK)
                x += ld.textlength(w + ' ', font=f)
            if sc < 1:
                big = layer.resize((int(W * sc), int(300 * sc)), Image.LANCZOS)
                layer = Image.new('RGBA', (W, 300), (0, 0, 0, 0))
                layer.paste(big, ((W - big.width) // 2, (300 - big.height) // 2))
            im.paste(layer, (0, 1270), layer)
            return

def pill(d, cx, y, text, f, fill, fg):
    tw_ = d.textlength(text, font=f); bb = f.getbbox(text)
    h = bb[3] - bb[1]; pad = 34
    d.rounded_rectangle((cx - tw_ / 2 - pad, y - 16, cx + tw_ / 2 + pad, y + h + 30), radius=28,
                        fill=fill, outline=INK, width=8)
    d.text((cx - tw_ / 2, y - bb[1] + 6), text, font=f, fill=fg)

def title(d):
    f1, f2 = font(96), font(84)
    pill(d, W / 2, 250, 'STOP REPLAYING', f1, MUST, INK)
    t = 'THAT CONVERSATION'
    d.text(((W - d.textlength(t, font=f2)) / 2, 395), t, font=f2, fill=(255, 255, 255), stroke_width=10, stroke_fill=INK)

# 1) vertical base: blurred fill + full 16:9 frame; freeze the last frame for the end card
if not os.path.exists(D + 'base.mp4'):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(T0), '-t', str(END), '-i', SRC, '-filter_complex',
        f'[0:v]setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration={HOLD},split[a][b];'
        '[a]scale=1080:1920,drawbox=0:0:1080:1920:color=0x141414:t=fill[bg];'
        '[b]scale=1080:-2:flags=lanczos[fg];[bg][fg]overlay=0:(H-h)/2-40[v]',
        '-map', '[v]', '-an', '-c:v', 'libx264', '-crf', '14', '-preset', 'fast', '-r', '30', D + 'base.mp4'], check=True)

dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', D + 'base.mp4', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '30', '-i', '-',
                        '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', D + 'video.mp4'], stdin=subprocess.PIPE)
n = 0
while True:
    raw = dec.stdout.read(W * H * 3)
    if len(raw) < W * H * 3: break
    t = n / FPS; n += 1
    im = Image.frombuffer('RGB', (W, H), raw).copy(); d = ImageDraw.Draw(im)
    title(d)
    if t < END:
        caption(im, t)
    else:
        p = min(1, (t - END) / 0.3)
        f = font(64)
        for i, line in enumerate(['FULL VIDEO ON MY CHANNEL', 'Psychology of Overthinking']):
            ff = f if i == 0 else font(58)
            col = MUST if i == 0 else (255, 255, 255)
            y = 1330 + i * 96 + (1 - p) * 20
            d.text(((W - d.textlength(line, font=ff)) / 2, y), line, font=ff, fill=col, stroke_width=8, stroke_fill=INK)
    enc.stdin.write(im.tobytes())
enc.stdin.close(); enc.wait()

# 2) audio: the finished mix (voice + soft music), trimmed, faded over the end card
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', D + 'video.mp4', '-ss', str(T0), '-t', str(TOTAL), '-i', SRC, '-filter_complex',
    f'[1:a]asetpts=PTS-STARTPTS,apad,atrim=0:{TOTAL},afade=t=out:st={END - 0.2}:d={HOLD},loudnorm=I=-14:TP=-1.5:LRA=11[a]',
    '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-t', str(TOTAL),
    '-movflags', '+faststart', R + 'short-liking-gap.mp4'], check=True)
print('done', n, n / FPS)
