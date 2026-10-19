#!/usr/bin/env python3
"""Map forced-alignment word times from the raw part audio onto the padded audio (pad-audio.py writes the inserted pauses
to audio/padded/partN.cuts.json). usage: shift-words.py N -> scenes/partN.words.json"""
import sys, json, subprocess
n = sys.argv[1]
raw = json.load(open(f"scenes/part{n}.rawwords.json")); cuts = json.load(open(f"audio/padded/part{n}.cuts.json"))
sh = lambda t: t + sum(e for c, e in cuts if c <= t)
import re
log = subprocess.run(["ffmpeg", "-i", f"audio/part{n}.mp3", "-af", "silencedetect=noise=-35dB:d=0.25", "-f", "null", "-"], capture_output=True, text=True).stderr
sil = list(zip([float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)], [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]))
for w in raw["words"]:  # a word start the aligner put inside a pause really starts where the pause ends
    for a, b in sil:
        if a < w["s"] < b: w["s"] = b
words = [{"w": w["w"], "s": round(sh(w["s"]), 3), "e": round(sh(w["e"]), 3)} for w in raw["words"]]
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"audio/padded/part{n}.wav"]))
json.dump({"duration": dur, "words": words}, open(f"scenes/part{n}.words.json", "w"), indent=0)
print(f"part{n}: {len(words)} words, padded {dur:.2f}s")
