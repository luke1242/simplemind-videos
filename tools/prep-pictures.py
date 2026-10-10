#!/usr/bin/env python3
"""Make 16:9 full pictures + crops from the 2K sources (lanczos). usage: prep-pictures.py N"""
import sys, json, os
from PIL import Image
n = sys.argv[1]; cfg = json.load(open(f"scenes/part{n}.json")); out = f"assets/pictures"; os.makedirs(out, exist_ok=True)
def load(name):
    for ext in ("png", "jpg"):
        p = f"pictures/{name}.{ext}"
        if os.path.exists(p): return Image.open(p).convert("RGB")
def to169(im):  # center-crop to exact 16:9 (sources are 2752x1536)
    w, h = im.size; tw = round(h * 16 / 9)
    if tw <= w: x = (w - tw) // 2; return im.crop((x, 0, x + tw, h))
    th = round(w * 9 / 16); y = (h - th) // 2; return im.crop((0, y, w, y + th))
done = set()
for sc in cfg["scenes"]:
    for key in ("picture", "pictureB"):
        nm = sc.get(key)
        if not nm or nm in done: continue
        done.add(nm); im = load(nm)
        if im is None: print("MISSING", nm); continue
        to169(im).resize((1920, 1080), Image.LANCZOS).save(f"{out}/{nm}.jpg", quality=95)
    for bi, b in enumerate(sc.get("beats", [])):
        if b["type"] != "crop": continue
        im = to169(load(sc["picture"])); W, H = im.size; z = b["z"]
        cw, ch = W / z, H / z
        x0 = min(max(b["cx"] * W - cw / 2, 0), W - cw); y0 = min(max(b["cy"] * H - ch / 2, 0), H - ch)
        b["rect"] = [x0 / W, y0 / H, 1 / z]
        im.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch))).resize((1920, 1080), Image.LANCZOS).save(f"{out}/{sc['id']}-crop{bi}.jpg", quality=95)
json.dump(cfg, open(f"scenes/part{n}.resolved.json", "w"), indent=1)
print("pictures ready:", len(done))
