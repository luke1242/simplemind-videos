#!/usr/bin/env python3
import json, sys
n = sys.argv[1]; p = json.load(open(f"scenes/part{n}.plan.json")); sw = json.load(open(f"scenes/part{n}.timing.json"))
ts = set()
for s in p:
    ts.add(round(s['start'] + 0.4, 2))
    if s['id'] != p[0]['id']: ts.add(round(s['start'] - 0.2, 2))
    for b in s['beats']:
        ts |= {round(b['a'] + 0.3, 2), round(b['e'] - 0.1, 2), round(b['e'] + 0.12, 2)}
    ts.add(round(s['end'] - 0.1, 2))
print(','.join(str(t) for t in sorted(ts)))
