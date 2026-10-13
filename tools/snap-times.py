#!/usr/bin/env python3
"""Snapshot times for every shot: just after the cut and just before the next one. usage: snap-times.py N [every]"""
import json, sys
n = sys.argv[1]; every = int(sys.argv[2]) if len(sys.argv) > 2 else 1
p = [x for x in json.load(open(f"scenes/part{n}.plan.json")) if x["scene"] != "host"]
ts = []
for i, s in enumerate(p):
    if i % every: continue
    ts.append(round(s["a"] + min(0.45, (s["e"] - s["a"]) * 0.3), 2))
    if s["e"] - s["a"] > 1.6: ts.append(round(s["e"] - 0.12, 2))
print(",".join(str(t) for t in sorted(set(ts))))
