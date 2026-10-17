import re, subprocess
from PIL import Image, ImageDraw, ImageFont

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
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', D + 'cold.mp4', '-filter_complex',
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

def caption(d, t):
    for s, e, txt in PHR:
        if s - 0.05 <= t < e + 0.3:
            words = txt.split(); ws = [syl(w) for w in words]; tot = sum(ws); acc = 0; hi = 0
            for j, w in enumerate(ws):
                if t >= s + (e - s) * acc / tot - 0.05: hi = j
                acc += w
            lines, cur = [], []
            for j, w in enumerate(words):
                if cur and d.textlength(' '.join(words[k] for k in cur + [j]), font=f_cap) > 940: lines.append(cur); cur = []
                cur.append(j)
            lines.append(cur)
            y = 1400
            for ln in lines:
                txtl = ' '.join(words[j] for j in ln)
                x = (W - d.textlength(txtl, font=f_cap)) / 2
                for j in ln:
                    wd = words[j] + ' '
                    d.text((x, y), wd, font=f_cap, fill=RED if j == hi else OFF, stroke_width=5, stroke_fill=(8, 6, 6))
                    x += d.textlength(wd, font=f_cap)
                y += 88
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
        caption(d, t)
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
