#!/usr/bin/env python3
"""Build labelled contact sheets from hyperframes snapshots. usage: review-sheets.py N snapdir outdir"""
import sys, json, glob, re, os
from PIL import Image, ImageDraw
n, snap, out = sys.argv[1], sys.argv[2], sys.argv[3]; os.makedirs(out, exist_ok=True)
plan = json.load(open(f"scenes/part{n}.plan.json"))
files = sorted(glob.glob(f"{snap}/frame-*-at-*.png"), key=lambda f: float(re.search(r"at-([\d.]+)s", f).group(1)))
W, H, C = 480, 270, 4
pages = [files[i:i + 16] for i in range(0, len(files), 16)]
for pi, pg in enumerate(pages):
    sh = Image.new("RGB", (W * C, H * ((len(pg) + C - 1) // C)), "white")
    for i, f in enumerate(pg):
        t = float(re.search(r"at-([\d.]+)s", f).group(1))
        sp = next((p for p in plan if p["a"] <= t < p["e"]), None)
        im = Image.open(f).convert("RGB").resize((W, H)); d = ImageDraw.Draw(im)
        d.rectangle([0, 0, 170, 14], fill="black"); d.text((3, 1), f"{t:.1f} {sp['scene'] if sp else ''} {sp['kind'] if sp else ''}", fill="white")
        sh.paste(im, ((i % C) * W, (i // C) * H))
    sh.save(f"{out}/p{n}-{pi+1}.jpg", quality=80)
print(len(files), "frames,", len(pages), "sheets")
