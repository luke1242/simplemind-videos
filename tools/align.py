#!/usr/bin/env python3
"""Word timestamps by FORCED ALIGNMENT of the known script (PocketSphinx, model bundled in the pip wheel; no downloads).
Use when Whisper's model can't be downloaded (huggingface.co blocked). Aligns each clip audio/partNx.mp3 to its text in
prompts/voice-clips.md, then places the clips on the joined part timeline exactly like tools/join-clips.py (0.5s gaps).
usage: align.py N            -> scenes/partN.rawwords.json   (same format as transcribe.py: {"duration", "words":[{w,s,e}]})
Setup once: pip download pocketsphinx --no-deps -d /tmp/ps && pip install /tmp/ps/*.whl --break-system-packages"""
import sys, re, json, glob, subprocess
from pocketsphinx import Decoder
# pronunciations for names / words missing from the CMU dictionary (ARPAbet)
EXTRA = {"pychyl": "P AY K AH L", "sirois": "S IH R W AA", "fuschia": "F Y UW SH AH", "hershfield": "HH ER SH F IY L D",
         "gollwitzer": "G AA L W IH T S ER", "rothblum": "R AA TH B L UW M", "carleton": "K AA R L T AH N", "baumeister": "B AW M AY S T ER",
         "procrastinators": "P R OW K R AE S T AH N EY T ER Z", "procrastinated": "P R OW K R AE S T AH N EY T IH D",
         "procrastinating": "P R OW K R AE S T AH N EY T IH NG", "procrastinate": "P R OW K R AE S T AH N EY T",
         "procrastination": "P R OW K R AE S T AH N EY SH AH N", "unfinished": "AH N F IH N IH SH T", "rothbloom": "R AA TH B L UW M",
         "nolen": "N OW L AH N", "hoeksema": "HH UH K S M AH", "hoeksema's": "HH UH K S M AH Z", "beilock": "B AY L AA K", "borkovec": "B AO R K AH V EH K",
         "killingsworth": "K IH L IH NG Z W ER TH", "sian": "SH AA N", "gerardo": "HH EH R AA R D OW", "haha": "HH AA HH AA", "ruminating": "R UW M AH N EY T IH NG",
         "ruminate": "R UW M AH N EY T", "rumination": "R UW M AH N EY SH AH N", "overthinking": "OW V ER TH IH NG K IH NG", "autopilot": "AO T OW P AY L AH T"}
n = sys.argv[1]
txt = open("prompts/voice-clips.md").read()
clips = dict(re.findall(r"\*\*(part\d[a-z])\.mp3\*\*.*?```\n(.*?)```", txt, re.S))
def toks(t):
    t = re.sub(r"\[[^\]]+\]", " ", t).replace("’", "'")
    out = []
    for w in re.sub(r"[-–—]", " ", t).split():
        w = re.sub(r"[^a-z']", "", w.lower()).strip("'")
        if w: out.append(w)
    return out
SR = 16000
words, off = [], 0.0
files = sorted(glob.glob(f"audio/part{n}[a-z].mp3"))
for i, f in enumerate(files):
    key = f.split("/")[-1][:-4]
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout
    dur44 = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
    tk = toks(clips[key])
    d = Decoder(samprate=SR, bestpath=False)
    for w in set(tk):
        if d.lookup_word(w) is None:
            if w in EXTRA: d.add_word(w, EXTRA[w], True)
            else: raise SystemExit(f"{key}: no pronunciation for '{w}' - add it to EXTRA")
    d.set_align_text(" ".join(tk))
    d.start_utt(); d.process_raw(raw, full_utt=True); d.end_utt()
    d.set_alignment(); d.start_utt(); d.process_raw(raw, full_utt=True); d.end_utt()
    al = [(re.sub(r"\(\d+\)$", "", w.name), w.start / 100, (w.start + w.duration) / 100) for w in d.get_alignment()]
    al = [a for a in al if a[0] not in ("<sil>", "<s>", "</s>", "[NOISE]")]
    if [a[0] for a in al] != tk: raise SystemExit(f"{key}: alignment word mismatch")
    for w, s, e in al: words.append({"w": w, "s": round(off + s, 3), "e": round(off + e, 3)})
    clipdur = len(raw) / 2 / SR
    print(f"{key}: {len(al)} words, {clipdur:.2f}s")
    off += clipdur + (0.5 if i < len(files) - 1 else 0)
part = f"audio/part{n}.mp3"
pd = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", part]))
print(f"part{n}: clips sum {off:.3f}s vs joined {pd:.3f}s")
json.dump({"duration": pd, "words": words}, open(f"scenes/part{n}.rawwords.json", "w"), indent=0)
