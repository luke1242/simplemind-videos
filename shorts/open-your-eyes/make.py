import re, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

D = '/tmp/claude-0/eyesshort/'
SERIF = '/tmp/claude-0/-home-claude/91500ffa-c02b-5439-9cdd-158af1875c8c/scratchpad/th/package/files/eb-garamond-latin-500-normal.woff'
W, H, FPS = 1080, 1920, 30
END = 63.35          # last frame of the painting before the title card
HOLD = 3.0
TOTAL = END + HOLD
OFF, RED, DIM = (236, 230, 222), (190, 70, 72), (150, 140, 135)

PHR = [(0.3, 3.00, "Imagine your phone is at a hundred percent when you wake up."), (3.76, 5.60, "By lunch, it's almost dead."),
       (6.36, 7.48, "And you barely touched it."), (8.64, 10.94, "So you open the battery settings to see what happened."),
       (11.76, 12.60, "And there it is."), (13.32, 15.21, "A list of apps eating your battery..."),
       (15.95, 17.91, "including some you never even opened today."), (18.78, 20.19, "They've been running in the background."),
       (20.96, 21.45, "All morning."), (22.38, 22.87, "Quietly."), (23.78, 24.67, "So here's a question."),
       (25.86, 28.09, "When you lock your phone and the screen goes black..."), (28.83, 29.93, "do those apps close?"),
       (30.77, 31.19, "No."), (32.13, 33.50, "The screen just goes dark."), (34.34, 36.03, "Everything behind it keeps running."),
       (37.37, 42.37, "Now think about the last time you went to bed exhausted... after a day where you didn't really do that much."),
       (43.13, 43.94, "What was still running?"), (44.87, 46.55, "The conversation you keep replaying."),
       (47.50, 49.07, "The decision you keep putting off."), (49.84, 51.23, "The text you never answered."),
       (52.04, 53.05, "The thing that ended..."), (53.76, 55.66, "that you never really let end."),
       (56.16, 59.18, "Maybe you're not tired because you did too much."),
       (59.94, 63.41, "Maybe you're tired because too much inside you never finished.")]

# 1) vertical base: blurred, zoomed fill + full 16:9 frame in the middle; freeze the last frame
import os
if not os.path.exists(D + 'base.mp4'): subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', D + 'cold.mp4', '-filter_complex',
    f'[0:v]trim=0:{END},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration={HOLD},split[a][b];'
    '[a]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.32:saturation=0.8[bg];'
    '[b]scale=1080:-2[fg];[bg][fg]overlay=0:(H-h)/2-60[v]',
    '-map', '[v]', '-an', '-c:v', 'libx264', '-crf', '14', '-preset', 'fast', '-r', '30', D + 'base.mp4'], check=True)

f_title = ImageFont.truetype(SERIF, 104)
f_cap = ImageFont.truetype(SERIF, 72)
f_small = ImageFont.truetype(SERIF, 54)

def syl(w):
    w = re.sub(r"[^a-z]", "", w.lower()); n = len(re.findall(r"[aeiouy]+", w))
    if w.endswith('e') and n > 1: n -= 1
    return max(1, n) + 0.4

BOLD = SERIF.replace('500-normal', '700-normal')
WORDS = []
for s_, e_, txt in PHR:
    ws_ = txt.split(); sy = [syl(w) for w in ws_]; tot = sum(sy); acc = 0
    for w, y_ in zip(ws_, sy):
        WORDS.append({'w': w, 's': s_ + (e_ - s_) * acc / tot, 'pe': e_}); acc += y_
CHUNKS, cur = [], []
for i, w in enumerate(WORDS):
    cur.append(w)
    last_of_phrase = i + 1 == len(WORDS) or WORDS[i + 1]['pe'] != w['pe']
    if len(cur) == 3 or w['w'][-1] in '.,?!' or last_of_phrase or len(' '.join(x['w'] for x in cur)) > 16:
        CHUNKS.append(cur); cur = []
for i, c in enumerate(CHUNKS):
    nxt = CHUNKS[i + 1][0]['s'] if i + 1 < len(CHUNKS) else 999
    c_end = min(nxt, c[-1]['pe'] + 0.35)
    for w in c: w['ce'] = c_end
FONTS = {}
def font(sz):
    if sz not in FONTS: FONTS[sz] = ImageFont.truetype(BOLD, sz)
    return FONTS[sz]

def caption(im, t):
    for c in CHUNKS:
        if c[0]['s'] - 0.04 <= t < c[0]['ce']:
            words = [w['w'].rstrip('.,') if w['w'].endswith((',', '.')) and not w['w'].endswith('...') else w['w'] for w in c]
            hi = max([i for i, w in enumerate(c) if t >= w['s'] - 0.04] or [0])
            sz = 124
            tmp = ImageDraw.Draw(im)
            while tmp.textlength(' '.join(words), font=font(sz)) > 980 and sz > 70: sz -= 6
            f = font(sz)
            p = min(1, (t - c[0]['s'] + 0.04) / 0.16); p = 1 - (1 - p) ** 3
            y = 1330 + (1 - p) * 22
            layer = Image.new('RGBA', (W, 360), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
            x = (W - ld.textlength(' '.join(words), font=f)) / 2
            pos = []
            for w in words:
                pos.append(x); x += ld.textlength(w + ' ', font=f)
            shadow = Image.new('RGBA', (W, 360), (0, 0, 0, 0)); sd = ImageDraw.Draw(shadow)
            for w, px in zip(words, pos): sd.text((px, 90), w, font=f, fill=(0, 0, 0, 235))
            shadow = shadow.filter(ImageFilter.GaussianBlur(14))
            layer.alpha_composite(shadow); layer.alpha_composite(shadow)
            for i, (w, px) in enumerate(zip(words, pos)):
                ld.text((px, 90), w, font=f, fill=(214, 78, 74, 255) if i == hi else (246, 241, 233, 255),
                        stroke_width=2, stroke_fill=(10, 8, 8, 255))
            if p < 1:
                al = layer.getchannel('A').point(lambda v: int(v * p)); layer.putalpha(al)
            im.paste(layer, (0, int(y) - 90), layer)
            return

dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', D + 'base.mp4', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '30', '-i', '-',
                        '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', D + 'video.mp4'], stdin=subprocess.PIPE)
n = 0
while True:
    raw = dec.stdout.read(W * H * 3)
    if len(raw) < W * H * 3: break
    t = n / FPS; n += 1
    im = Image.frombuffer('RGB', (W, H), raw).copy(); d = ImageDraw.Draw(im)
    tt = 'Open Your Eyes.'
    a = 1.0 if t < END else 1.0
    d.text(((W - d.textlength(tt, font=f_title)) / 2, 230), tt, font=f_title, fill=RED)
    if t < END:
        caption(im, t)
    else:
        for i, line in enumerate(['Full video on my channel', 'link below']):
            d.text(((W - d.textlength(line, font=f_small)) / 2, 1430 + i * 74), line, font=f_small, fill=OFF if i == 0 else DIM)
    enc.stdin.write(im.tobytes())
enc.stdin.close(); enc.wait()

# 2) audio: original mix (voice + soft music), trimmed, with a gentle fade over the hold
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', D + 'video.mp4', '-i', D + 'cold.mp4', '-filter_complex',
    f'[1:a]atrim=0:{TOTAL},asetpts=PTS-STARTPTS,afade=t=out:st={END}:d={HOLD},loudnorm=I=-14:TP=-1.5:LRA=11[a]',
    '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-t', str(TOTAL),
    '-movflags', '+faststart', D + 'short-open-your-eyes.mp4'], check=True)
print('done', n, n / FPS)
