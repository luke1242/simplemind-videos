#!/usr/bin/env python3
"""Full 1920x1080 pictures, focus crops (cut from the 2K sources, lanczos) and icons. usage: prep-pictures.py N"""
import sys, json, os
from PIL import Image
n = sys.argv[1]; cfg = json.load(open(f"scenes/part{n}.json")); FOCI = json.load(open("scenes/foci.json"))
os.makedirs("assets/pictures", exist_ok=True); os.makedirs("assets/icons", exist_ok=True)
def load(name):
    for ext in ("png", "jpg"):
        p = f"pictures/{name}.{ext}"
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
    for e in sc.get("events", []):
        if e["kind"] == "icon": icons.add(e["icon"])
        if e["kind"] == "pop" and e["content"]["type"] == "icon": icons.add(e["content"]["icon"])
    if sc.get("foci"): resolved["__" + sc["id"]] = [rect(*f) for f in sc["foci"]]
for name in sorted(pics):
    im = load(name)
    if im is None: print("MISSING", name); continue
    full = to169(im); full.resize((1920, 1080), Image.LANCZOS).save(f"assets/pictures/{name}.jpg", quality=95)
    rs = []
    for i, f in enumerate(FOCI.get(name, [])):
        r = rect(*f); rs.append(r); W, H = full.size
        full.crop((round(r[0] * W), round(r[1] * H), round((r[0] + r[2]) * W), round((r[1] + r[2]) * H))).resize((1920, 1080), Image.LANCZOS).save(f"assets/pictures/{name}-f{i}.jpg", quality=95)
    resolved[name] = rs
for ic in sorted(icons):
    Image.open(f"icons/{ic}.jpg").convert("RGB").resize((1920, 1080), Image.LANCZOS).save(f"assets/icons/{ic}.jpg", quality=95)
json.dump(resolved, open(f"scenes/part{n}.foci.json", "w"))
print("pictures", len(pics), "icons", len(icons))
