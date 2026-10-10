#!/usr/bin/env python3
"""Real word-timestamp timing. usage: timing.py N
Fuzzy-matches each scene's narration to scenes/partN.words.json (faster-whisper) and writes scenes/partN.timing.json."""
import sys, json, re, difflib
n = sys.argv[1]
cfg = json.load(open(f"scenes/part{n}.json"))
tr = json.load(open(f"scenes/part{n}.words.json"))
norm = lambda w: re.sub(r"[^a-z0-9']", "", w.lower().replace("-", " ")).strip()
tw = []  # transcript tokens (split hyphen pieces) -> word index
for i, w in enumerate(tr["words"]):
    for p in re.sub(r"[-]", " ", w["w"]).split():
        if norm(p): tw.append((norm(p), i))
# narration tokens
nt, scene_of, sent_of = [], [], []
for si, sc in enumerate(cfg["scenes"]):
    sents = [s for s in re.split(r"(?<=[.!?])\s+", sc["narration"].strip()) if s]
    for k, s in enumerate(sents):
        for p in re.sub(r"-", " ", s).split():
            if norm(p): nt.append(norm(p)); scene_of.append(si); sent_of.append(k)
sm = difflib.SequenceMatcher(None, nt, [t[0] for t in tw], autojunk=False)
m = [None] * len(nt)
for a, b, size in sm.get_matching_blocks():
    for k in range(size): m[a + k] = tw[b + k][1]
# fill gaps by interpolation between matched neighbours
idx = [i for i, v in enumerate(m) if v is not None]
assert idx, "no match"
for i in range(len(m)):
    if m[i] is None:
        lo = max([j for j in idx if j < i], default=None); hi = min([j for j in idx if j > i], default=None)
        m[i] = m[lo] if hi is None else (m[hi] if lo is None else round(m[lo] + (m[hi] - m[lo]) * (i - lo) / (hi - lo)))
W = tr["words"]; dur = tr["duration"]
scenes = []
for si, sc in enumerate(cfg["scenes"]):
    toks = [i for i in range(len(nt)) if scene_of[i] == si]
    first = W[m[toks[0]]]["s"]; last_end = W[m[toks[-1]]]["e"]
    sents = {}
    for i in toks: sents.setdefault(sent_of[i], []).append(m[i])
    scenes.append({"id": sc["id"], "start": first, "narrationEnd": last_end,
                   "sentenceStarts": [W[min(v)]["s"] for k, v in sorted(sents.items())],
                   "sentenceEnds": [W[max(v)]["e"] for k, v in sorted(sents.items())],
                   "words": [{"w": nt[i], "s": W[m[i]]["s"], "e": W[m[i]]["e"]} for i in toks]})
for i, s in enumerate(scenes):
    s["end"] = scenes[i + 1]["start"] if i + 1 < len(scenes) else dur
scenes[0]["start"] = 0.0
json.dump({"duration": dur, "scenes": scenes}, open(f"scenes/part{n}.timing.json", "w"), indent=1)
print("scene  start    end    dur  sentences")
for s in scenes: print(f"{s['id']}  {s['start']:7.2f} {s['end']:7.2f} {s['end']-s['start']:6.2f}  {len(s['sentenceStarts'])}")
print("unmatched narration words:", sum(1 for a in range(len(nt)) if all(not (a>=x[0] and a<x[0]+x[2]) for x in sm.get_matching_blocks())))
