#!/usr/bin/env python3
"""Lengthen pauses only (never stretch speech). usage: pad-audio.py N scene_start_seconds_json [short_pad]"""
import sys, re, json, subprocess
n = sys.argv[1]; starts = json.loads(sys.argv[2]); short = float(sys.argv[3]) if len(sys.argv) > 3 else 0.25
extras = json.loads(sys.argv[4]) if len(sys.argv) > 4 else {}  # {"5": 1.9} = extra seconds at that scene's boundary
src = f"audio/part{n}.mp3"; out = f"audio/padded/part{n}.wav"
log = subprocess.run(["ffmpeg","-i",src,"-af","silencedetect=noise=-35dB:d=0.25","-f","null","-"],capture_output=True,text=True).stderr
ss = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
se = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
dur = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",src]))
sil = list(zip(ss, se))
extra = []
for a, b in sil:
    d = b - a
    extra.append(0.9 if d >= 0.6 else short)
for si, s in enumerate(starts[1:], start=1):  # scene change: closest pause before the scene's first word
    i = min(range(len(sil)), key=lambda k: abs(sil[k][1] - s))
    extra[i] += 0.4 + float(extras.get(str(si), 0))
cuts = [((a + b) / 2, e) for (a, b), e in zip(sil, extra)]
parts, labels, prev = [], [], 0.0
fc = []
for i, (t, e) in enumerate(cuts):
    fc.append(f"[0:a]atrim={prev:.4f}:{t:.4f},asetpts=PTS-STARTPTS[a{i}]")
    fc.append(f"anullsrc=r=44100:cl=mono,atrim=0:{e:.3f}[s{i}]")
    labels += [f"[a{i}]", f"[s{i}]"]; prev = t
fc.append(f"[0:a]atrim={prev:.4f}:{dur:.4f},asetpts=PTS-STARTPTS[aend]")
labels.append("[aend]")
fc.append("".join(labels) + f"concat=n={len(labels)}:v=0:a=1[o]")
subprocess.run(["ffmpeg","-v","error","-y","-i",src,"-filter_complex",";".join(fc),"-map","[o]","-ar","44100","-ac","1",out],check=True)
new = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",out]))
print(f"part{n}: old {dur:.2f}s -> new {new:.2f}s ({len(cuts)} pauses padded)")
