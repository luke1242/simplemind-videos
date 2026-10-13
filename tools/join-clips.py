#!/usr/bin/env python3
"""Join ElevenLabs clips audio/partNa.mp3, partNb.mp3 ... into audio/partN.mp3 (0.5s silence between).
Skips a part if partN.mp3 already exists or it has no clips. Run before pad-audio."""
import glob, os, subprocess
for n in range(1, 5):
    out = f"audio/part{n}.mp3"
    clips = sorted(glob.glob(f"audio/part{n}[a-z].mp3"))
    if os.path.exists(out) or not clips:
        continue
    inputs, labels = [], []
    for i, c in enumerate(clips):
        inputs += ["-i", c]
        labels.append(f"[{i}:a]aresample=44100,aformat=channel_layouts=mono[c{i}]")
    n_in = 2 * len(clips) - 1
    fc = ";".join(labels) + f";anullsrc=r=44100:cl=mono,atrim=0:0.5,asplit={max(len(clips)-1,1)}" + \
         "".join(f"[g{i}]" for i in range(max(len(clips)-1,1))) + ";"
    seq = "".join(f"[c{i}]" + (f"[g{i}]" if i < len(clips) - 1 else "") for i in range(len(clips)))
    fc += seq + f"concat=n={n_in}:v=0:a=1[o]"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", *inputs, "-filter_complex", fc, "-map", "[o]", "-b:a", "192k", out], check=True)
    print(out, "<-", ", ".join(os.path.basename(c) for c in clips))
