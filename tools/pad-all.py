#!/usr/bin/env python3
"""Pause padding (video 6) (reveal ids below): scene starts come from the raw word timing; reveals get >= 2.0s of silence after, lead scenes get room before.
usage: pad-all.py [short_pad]"""
import json, subprocess, sys
short = sys.argv[1] if len(sys.argv) > 1 else "0.25"
REVEAL = {"D10", "D42", "D77"}      # >= 2s silence after these scenes
MINGAP = {"D10": 3.6}                              # title card after "than you think"
TAIL = {1: 1.0, 2: 1.0, 3: 1.0, 4: 5.0}                          # title card / part-end holds
for n in (1, 2, 3, 4):
    cfg = json.load(open(f"scenes/part{n}.json")); raw = json.load(open(f"scenes/part{n}.rawtiming.json"))
    firsts = [s["words"][0]["s"] for s in raw["scenes"]]; ends = [s["narrationEnd"] for s in raw["scenes"]]
    extras = {}
    for i in range(1, len(firsts)):
        gap = firsts[i] - ends[i - 1]; base = (0.9 if gap >= 0.6 else float(short)) + 0.4
        need = 0.0
        if raw["scenes"][i - 1]["id"] in REVEAL: need = max(need, 2.75 - (gap + base))
        if raw["scenes"][i - 1]["id"] in MINGAP: need = max(need, MINGAP[raw["scenes"][i - 1]["id"]] - (gap + base))
        lead = cfg["scenes"][i].get("lead", 0)
        if lead: need = max(need, lead + 0.6 - (gap + base))
        if need > 0.01: extras[str(i)] = round(need, 2)
    print(n, "extras", extras)
    subprocess.run(["python3", "tools/pad-audio.py", str(n), json.dumps(firsts), short, json.dumps(extras), str(TAIL[n])], check=True)
