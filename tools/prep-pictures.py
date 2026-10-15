#!/usr/bin/env python3
"""Full 1920x1080 pictures, focus crops (cut from the 2K sources, lanczos) and icons. usage: prep-pictures.py N"""
import sys, json, os
from PIL import Image
n = sys.argv[1]; cfg = json.load(open(f"scenes/part{n}.json")); FOCI = json.load(open("scenes/foci.json"))
os.makedirs("assets/pictures", exist_ok=True); os.makedirs("assets/icons", exist_ok=True)
def load(name):
    for p in (f"pictures/{name}.png", f"pictures/{name}.jpg", f"icons/{name}.jpg"):  # an icon can be used as a full-frame picture
        if os.path.exists(p): return Image.open(p).convert("RGB")
def to169(im):
    w, h = im.size; tw = round(h * 16 / 9)
    if tw <= w: x = (w - tw) // 2; return im.crop((x, 0, x + tw, h))
    th = round(w * 9 / 16); y = (h - th) // 2; return im.crop((0, y, w, y + th))
def rect(cx, cy, z):
    z = min(z, 1.35); cw = 1 / z
    x0 = min(max(cx - cw / 2, 0), 1 - cw); y0 = min(max(cy - cw / 2, 0), 1 - cw); return [x0, y0, cw]
pics = set(); icons = set(); resolved = {}
for sc in cfg["scenes"]:
    for k in ("picture", "pictureB"):
        if sc.get(k): pics.add(sc[k])
    dg = sc.get("diagram") or {}
    if dg.get("kind") == "battery": icons.update(["I63", "I64", "I65", "I66"])
    if dg.get("kind") == "irow": icons.update(i["icon"] for i in dg["items"])
    for e in sc.get("events", []):
        if e["kind"] == "icon": icons.add(e["icon"])
        if e["kind"] == "iconrow": icons.update(i["icon"] for i in e["items"])
        if e["kind"] == "pop" and e["content"]["type"] == "icon": icons.add(e["content"]["icon"])
for name in sorted(pics):
    im = load(name)
    if im is None: print("MISSING", name); continue
    full = to169(im); full.resize((2560, 1440), Image.LANCZOS).save(f"assets/pictures/{name}.jpg", quality=93)  # 2560 wide so camera zooms up to 1.4x stay sharp; shown at 1920
for ic in sorted(icons):
    Image.open(f"icons/{ic}.jpg").convert("RGB").resize((1920, 1080), Image.LANCZOS).save(f"assets/icons/{ic}.jpg", quality=95)
json.dump({k: v for k, v in FOCI.items()}, open(f"scenes/part{n}.foci.json", "w"))
print("pictures", len(pics), "icons", len(icons))
