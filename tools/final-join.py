#!/usr/bin/env python3
"""Join parts 1-4 (1.0s silence + held last frame between), mix SFX + soft music with ducking, loudnorm. -> renders/full.mp4"""
import json, subprocess, os, sys
R = "renders"; parts = [1, 2, 3, 4]; GAP = 1.0
dur = lambda f: float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
D = [dur(f"{R}/part{n}.mp4") for n in parts]
offs, t = [], 0.0
for d in D: offs.append(t); t += d + GAP
total = t - GAP + 4.0  # a little room after the last frame for the music fade
# 1) video+voice: each part padded with 1s held last frame + silence, concatenated
inputs, fc, labels = [], [], []
for i, n in enumerate(parts):
    inputs += ["-i", f"{R}/part{n}.mp4"]
    pad = GAP if i < len(parts) - 1 else 4.0
    fc.append(f"[{i}:v]tpad=stop_mode=clone:stop_duration={pad}[v{i}]")
    fc.append(f"[{i}:a]apad=pad_dur={pad}[a{i}]")
    labels.append(f"[v{i}][a{i}]")
fc.append("".join(labels) + f"concat=n={len(parts)}:v=1:a=1[v][a]")
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "pcm_s16le", f"{R}/full-voice.mkv"], check=True)
print("voice-only joined:", round(dur(f"{R}/full-voice.mkv"), 2), "s")
# 2) SFX track from cues (min 2.5s apart, quiet)
ev = []
for i, n in enumerate(parts):
    for e in json.load(open(f"scenes/part{n}.sfx.json")): ev.append((offs[i] + e["t"], e["kind"]))
ev.sort(); keep, last = [], -9
for tt, k in ev:
    if tt - last >= 2.5: keep.append((tt, k)); last = tt
print("sfx cues:", len(keep), "of", len(ev))
sin, sfc, sl = [], [], []
for j, (tt, k) in enumerate(keep):
    sin += ["-i", f"assets/sfx/{k}.wav"]
    sfc.append(f"[{j}:a]adelay={int(tt*1000)}|{int(tt*1000)},volume=0.12[s{j}]"); sl.append(f"[s{j}]")
sfc.append("".join(sl) + f"amix=n={len(keep)}:normalize=0:dropout_transition=0,apad=whole_dur={total:.2f}[sfx]")
subprocess.run(["ffmpeg", "-v", "error", "-y", *sin, "-filter_complex", ";".join(sfc), "-map", "[sfx]", "-t", f"{total:.2f}", "-ar", "44100", "-ac", "1", f"{R}/sfx.wav"], check=True)
# 3) music + sidechain duck + mix
music = [f for f in os.listdir("music") if f.lower().endswith((".mp3", ".wav", ".m4a")) and os.path.getsize(f"music/{f}") > 50000]
if not music:
    print("NO MUSIC FILE: delivering voice + sfx only")
    mus_chain = None
else:
    mus_chain = f"music/{music[0]}"
vd = f"{R}/full-voice.mkv"
if mus_chain:
    gain = float(sys.argv[1]) if len(sys.argv) > 1 else 0.063  # about -24 dB
    fc = (f"[1:a]aloop=loop=-1:size=2e9,atrim=0:{total:.2f},asetpts=PTS-STARTPTS,volume={gain},afade=t=in:d=2,afade=t=out:st={total-4:.2f}:d=4,aformat=sample_rates=44100:channel_layouts=mono[m];"
          f"[0:a]aformat=sample_rates=44100:channel_layouts=mono,asplit=2[vo][vk];"
          f"[m][vk]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=400[md];"
          f"[2:a]aformat=sample_rates=44100:channel_layouts=mono[sf];"
          f"[vo][md][sf]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[mix]")
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", vd, "-i", mus_chain, "-i", f"{R}/sfx.wav", "-filter_complex", fc, "-map", "0:v", "-map", "[mix]"]
else:
    fc = "[0:a]aformat=sample_rates=44100:channel_layouts=mono[vo];[1:a]aformat=sample_rates=44100:channel_layouts=mono[sf];[vo][sf]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[mix]"
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", vd, "-i", f"{R}/sfx.wav", "-filter_complex", fc, "-map", "0:v", "-map", "[mix]"]
subprocess.run(cmd + ["-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", f"{R}/full.mp4"], check=True)
print("full.mp4:", round(dur(f"{R}/full.mp4"), 2), "s")
