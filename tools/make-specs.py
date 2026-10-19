#!/usr/bin/env python3
"""Video 6 (procrastination): writes scenes/partN.json (scene specs for tools/build-part.mjs) and scenes/foci.json.
Narration text and host tracks are read straight from VIDEO.md, so they always match it."""
import json, os, re
Y, R = "yellow", "red"
def P(t, b=None, **fl):
    d = {"t": t}
    if b: d["badge"] = b
    d.update(fl); return d
def _parts(ps): return [p if isinstance(p, dict) else P(*p) for p in ps]
def icon(word, ic, occ=1, dur=1.8): return {"kind": "icon", "icon": ic, "word": word, "occ": occ, "dur": dur}
def card(word, parts, occ=1, dur=1.9): return {"kind": "card", "parts": _parts(parts), "word": word, "occ": occ, "dur": dur}
def pop(word, pose, content, occ=1, dur=2.8):
    c = {"type": "icon", "icon": content} if isinstance(content, str) else {"type": "card", "parts": _parts(content)}
    return {"kind": "pop", "pose": pose, "content": c, "word": word, "occ": occ, "dur": dur}
def title(pill="LESSON", l1="PSYCHOLOGY OF", l2="PROCRASTINATION"): return {"kind": "title", "dur": 2.5, "pill": pill, "l1": l1, "l2": l2}
def mv(kind, word, f=None, occ=1, **kw): return {"kind": kind, "word": word, "occ": occ, "f": f, **kw}
def step(n, text, word, occ=1, **kw): return {"type": "step", "step": n, "text": text, "word": word, "occ": occ, **kw}
W_ = lambda w, o=1: {"word": w, "occ": o}
FULL = [0.5, 0.5, 1]
def pill(text, word, until=None, dur=3.0, occ=1, **kw): return {"type": "pill", "text": text, "word": word, "occ": occ, "until": until, "dur": dur, **kw}
def sb(text, word, until=None, dur=2.6, occ=1, red=False): return {"type": "sbadge", "text": text, "word": word, "occ": occ, "until": until, "dur": dur, "red": red}
def bub(text, word, x, y, w=0.31, h=0.17): return {"type": "bubble", "text": text, "word": word, "box": {"x": x, "y": y, "w": w, "h": h}}
def pbadge(text, word, x, y, w, h, b=Y, fs=70, dur=None): o = {"type": "badge", "text": text, "word": word, "badge": b, "fs": fs, "box": {"x": x, "y": y, "w": w, "h": h}}; o.update({"dur": dur} if dur else {}); return o
def circ(word, cx, cy, rx, ry): return {"type": "circle", "word": word, "cx": cx, "cy": cy, "rx": rx, "ry": ry}
def sweep(word, x, y, w, h): return {"type": "sweep", "word": word, "box": {"x": x, "y": y, "w": w, "h": h}}

# ---- narration + host tracks from VIDEO.md
V = open("VIDEO.md").read()
NAR, HOST = {}, {}
cur = None
for line in V.split("\n"):
    m = re.match(r"\*\*(D\d+)\*\*", line)
    if m: cur = m.group(1); continue
    if cur and line.startswith("narration: "): NAR[cur] = line[len('narration: "'):-1]
    if cur and line.startswith("host: "):
        tr = []
        for k, seg in enumerate(line[6:].split(" → ")):
            mm = re.match(r'(N\d\d) "([^"]+)"(?: \((\d)\w\w occurrence\))?', seg.strip())
            tr.append([mm.group(1)] if k == 0 else [mm.group(1), mm.group(2).lower()] + ([int(mm.group(3))] if mm.group(3) else []))
        HOST[cur] = tr
def sc(id, picture=None, camera="zoom-in", ev=None, **kw):
    d = {"id": id, "camera": camera, "narration": NAR[id], "events": ev or []}
    if picture: d["picture"] = picture
    if id in HOST: d["host"] = HOST[id]
    d.update(kw); return d
def loop(nodes, **kw): return {"kind": "loop", "nodes": [{"t": t, "word": w} for t, w in nodes], **kw}
def split(left, right, at, **kw): return {"kind": "split", "left": left, "right": right, "at": at, **kw}
def bars3(title_, bars, grow, badge=None): return {"kind": "bars3", "title": title_, "bars": bars, "at": {"grow": grow}, **({"badge": badge} if badge else {})}
SKY, SAGE, RED_ = "#8EC5E8", "#9CC08B", "#D64545"
GUILT = [("AVOID", W_("avoid")), ("FEEL WORSE", W_("worse")), ("AVOID MORE", W_("more"))]

P1 = [
 sc("D01", "S01", moves=[mv("snap", "nine", [0.42, 0.16, 1.4]), mv("whip", "thing", [0.32, 0.34, 1.4])]),
 sc("D02", "S02", moves=[mv("snap", "decide", [0.62, 0.3, 1.3]), mv("snap", "clean", [0.62, 0.55, 1.25])]),
 sc("D03", "S02", "zoom-out", ev=[icon("messages", "I80"), card("procrastinating", [("HOW TO STOP",), P("PROCRASTINATING", Y, sz="mid")])],
    moves=[mv("snap", "video", [0.62, 0.28, 1.35])]),
 sc("D04", "S03", moves=[mv("snap", "thing", [0.4, 0.6, 1.3]), mv("whip", "lie", [0.7, 0.52, 1.4]), mv("zoom", "thinking", FULL)],
    overlays=[bub("WHAT IS WRONG WITH ME?", "wrong", 0.42, 0.05, 0.38, 0.15), bub("WHY AM I SO LAZY?", "lazy", 0.45, 0.25, 0.3, 0.14)]),
 sc("D05", "S04", trans="push", overlays=[pill("TICE & BAUMEISTER (1997)", "psychologists", dur=3.2)]),
 sc("D06", "S04", moves=[mv("snap", "procrastinators", [0.27, 0.66, 1.4]), mv("whip", "rushing", [0.75, 0.48, 1.35])],
    overlays=[sb("LESS STRESS", "less", until="fewer"), sb("FEWER HEALTH PROBLEMS", "fewer", dur=2.4)]),
 sc("D07", "S04", pictureB="S04b", swap={"word": "flipped"}, moves=[mv("snap", "stressed", [0.36, 0.52, 1.35])],
    overlays=[sb("MORE STRESS", "stressed", until="sick", red=True), sb("SICKER", "sick", until="grades", red=True), sb("LOWER GRADES", "grades", dur=2.4, red=True)]),
 sc("D08", None, "hold", ev=[title()],
    diagram={"kind": "lines2", "title": "STRESS OVER THE TERM", "xl": "START", "xr": "END OF TERM",
             "pathA": "M260 520 C 700 515, 1200 525, 1660 520", "pathB": "M260 800 C 900 790, 1250 520, 1660 190",
             "labA": {"t": "EVERYONE ELSE", "x": 300, "y": 430}, "labB": {"t": "PROCRASTINATORS", "x": 300, "y": 815},
             "tags": [{"t": "BORROWED", "word": W_("borrowed"), "x": 1240, "y": 250}], "at": {"draw": W_("avoided")}},
    fx=[{"type": "riser", "word": "avoided"}, {"type": "impact", "word": "future"}]),
 sc("D09", "S05", ev=[icon("week", "I83")], moves=[mv("snap", "idea", [0.2, 0.66, 1.4])]),
 sc("D10", "S05", moves=[mv("snap", "folder", [0.3, 0.27, 1.4]), mv("whip", "videos", [0.3, 0.44, 1.4]), mv("whip", "made", [0.46, 0.42, 1.4])]),
 sc("D11", "S05", "zoom-out", ev=[pop("thumbnail", "N10", [("NO SCRIPT",), P("YET", Y)], dur=2.4)],
    moves=[mv("snap", "lazy", [0.62, 0.3, 1.35]), mv("whip", "working", [0.4, 0.45, 1.3]), mv("snap", "except", [0.22, 0.64, 1.4])], overlays=[circ("except", 0.19, 0.69, 0.11, 0.09)]),
 sc("D12", "I81", "hold", moves=[mv("snap", "run", [0.5, 0.5, 1.25])]),
 sc("D13", None, "hold", diagram={"kind": "irow", "items": [{"icon": "I88", "label": "WHAT IT REALLY IS", "word": W_("know")},
    {"icon": "I84", "label": "4 TRAPS", "word": W_("four")}, {"icon": "I85", "label": "5 WAYS TO START", "word": W_("five")}]}),
 sc("D14", None, "hold", diagram={"kind": "card", "parts": [P("THE"), P("OPPOSITE", mk=True), P("OF WHAT MOST PEOPLE DO", small=True)]}),
]
P2 = [
 sc("D15", "I79", "hold", moves=[mv("snap", "time", [0.5, 0.5, 1.25], occ=2)],
    overlays=[sb("BAD PLANNING", "bad", until="not", red=True), sb("NOT ENOUGH DISCIPLINE", "discipline", dur=2.2, red=True)]),
 sc("D16", "S20", overlays=[pill("TIM PYCHYL", "psychologist", dur=3.0)], moves=[mv("snap", "different", [0.46, 0.4, 1.4])]),
 sc("D17", None, "hold", swap={"word": "emotion"},
    diagram={"kind": "card", "parts": [P("A"), P("TIME", R, slam=True), P("PROBLEM?", sz="mid")]},
    diagramB={"kind": "card", "parts": [P("AN"), P("EMOTION", Y), P("PROBLEM", sz="mid")]}, fx=[{"type": "impact", "word": "emotion"}]),
 sc("D18", None, "hold", overlays=[pill("SIROIS & PYCHYL (2013)", "psychologist", dur=3.0)],
    diagram=split(["", "FEEL BETTER NOW"], ["FUTURE YOU", "PAYS"], {"left": W_("better"), "right": W_("expense"), "rack": W_("future")}, fs=88)),
 sc("D19", "S06", moves=[mv("snap", "boring", [0.13, 0.5, 1.4]), mv("whip", "confusing", [0.27, 0.47, 1.4]), mv("whip", "scary", [0.43, 0.49, 1.4]), mv("zoom", "big", [0.3, 0.42, 1.15])]),
 sc("D20", "S06", "zoom-out", ev=[icon("way", "I81")], moves=[mv("snap", "feeling", [0.7, 0.32, 1.4])]),
 sc("D21", "S07", ev=[card("relief", [P("RELIEF", Y)], dur=1.7)], moves=[mv("snap", "avoid", [0.62, 0.45, 1.25]), mv("snap", "close", [0.66, 0.3, 1.4])],
    overlays=[sweep("instantly", 0.5, 0.05, 0.4, 0.9)]),
 sc("D22", None, "hold", diagram=loop([("BAD FEELING", W_("every")), ("AVOID", W_("avoid")), ("RELIEF", W_("better"))],
    center={"t": "\"AVOIDING WORKS\"", "word": W_("avoiding")}, pulse=W_("faster"))),
 sc("D23", None, "hold", swap={"word": "loop"},
    diagram={"kind": "card", "parts": [P("NOT"), P("LAZY", R, slam=True)]}, diagramB={"kind": "card", "parts": [P("A"), P("LEARNED LOOP", Y)]}),
 sc("D24", "S08", trans="push", overlays=[pill("HAL HERSHFIELD", "researcher", dur=3.0), sb("NOW", "now", until="ten"), sb("+10 YEARS", "ten", dur=2.4)],
    moves=[mv("snap", "scanned", [0.7, 0.42, 1.4])]),
 sc("D25", "S09", moves=[mv("snap", "people", [0.66, 0.36, 1.4]), mv("whip", "someone", [0.23, 0.45, 1.4])]),
 sc("D26", "S10", moves=[mv("snap", "tomorrow", [0.22, 0.5, 1.4]), mv("whip", "someone", [0.64, 0.4, 1.4])],
    overlays=[bub("I'LL DO IT TOMORROW", "tomorrow", 0.03, 0.06, 0.3, 0.16)]),
 sc("D27", "S10", moves=[mv("snap", "motivated", [0.64, 0.38, 1.3])],
    overlays=[sb("MORE MOTIVATED", "motivated", until="rested"), sb("MORE RESTED", "rested", until="organized"), sb("MORE ORGANIZED", "organized", dur=2.2)]),
 sc("D28", "S10", pictureB="S10b", swap={"word": "turn"}, moves=[mv("snap", "until", [0.62, 0.4, 1.25])], fx=[{"type": "impact", "word": "you"}]),
 sc("D29", None, "hold", swap={"word": "choosing"}, ev=[icon("bill", "I82")],
    diagram={"kind": "card", "parts": [P("NOT"), P("LAZINESS", R, slam=True)]}, diagramB={"kind": "card", "parts": [P("FEEL BETTER"), P("NOW", Y)]}),
 sc("D30", None, "hold", overlays=[pill("PIERS STEEL", "researcher", dur=2.8)],
    diagram={"kind": "people", "rows": 4, "cols": 5, "redIdx": [2, 6, 13, 17], "label": "1 IN 5", "at": {"red": W_("one"), "label": W_("five"), "pulse": W_("alone")}}),
 sc("D31", "S05", moves=[mv("snap", "stuck", [0.2, 0.66, 1.4])],
    overlays=[sb("DAYS", "days", until="weeks"), sb("WEEKS", "weeks", until="years"), sb("YEARS", "years", dur=2.0)]),
]
P3 = [
 sc("D32", "I84", "hold", overlays=[sb("4 TRAPS", "four", dur=2.6)], moves=[mv("snap", "four", [0.5, 0.5, 1.2])]),
 sc("D33", "S11", overlays=[step("TRAP 1", "TOO BIG & BLURRY", "one", dur=3.0),
    pbadge("WORK ON THE PROJECT", "work", 0.42, 0.14, 0.42, 0.12), pbadge("GET IN SHAPE", "shape", 0.5, 0.36, 0.3, 0.12), pbadge("FIGURE OUT MY LIFE", "figure", 0.44, 0.58, 0.4, 0.12)]),
 sc("D34", "S11", "zoom-out", moves=[mv("snap", "brain", [0.25, 0.6, 1.4]), mv("zoom", "giant", FULL)]),
 sc("D35", "S20", trans="push", ev=[card("unpleasant", [("THE TASK FELT",), P("UNPLEASANT", Y)])],
    overlays=[pill("SOLOMON & ROTHBLUM (1984)", "psychologists", dur=3.2)], moves=[mv("snap", "hundreds", [0.78, 0.45, 1.35])]),
 sc("D36", "S11", moves=[mv("snap", "step", [0.24, 0.64, 1.4])]),
 sc("D37", "S12", overlays=[step("TRAP 2", "A TEST OF YOU", "two", dur=3.0), sb("FEAR OF FAILURE", "fear", dur=2.4, red=True)],
    moves=[mv("snap", "test", [0.8, 0.52, 1.4]), mv("zoom", "other", FULL)]),
 sc("D38", None, "hold", diagram={"kind": "card", "parts": [P("NEVER START =", sz="mid"), P("NEVER FAIL", mk=True)]}),
 sc("D39", "S12", moves=[mv("snap", "tell", [0.25, 0.42, 1.4])], overlays=[bub("I COULD HAVE DONE IT GREAT…", "could", 0.31, 0.03, 0.36, 0.17)]),
 sc("D40", "S12", "zoom-out", ev=[pop("that's", "N06", [("CARE MOST =",), P("PUT OFF LONGEST", Y, sz="mid")], dur=2.8)],
    moves=[mv("zoom", "delay", FULL), mv("snap", "finding", [0.25, 0.42, 1.3])]),
 sc("D41", "S13", overlays=[step("TRAP 3", "THE REWARD IS FAR AWAY", "three", dur=3.0)],
    moves=[mv("snap", "reward", [0.76, 0.32, 1.4]), mv("whip", "bad", [0.22, 0.28, 1.4])]),
 sc("D42", None, "hold", diagram=bars3("HOW REAL IT FEELS", [{"label": "RIGHT NOW", "h": 1.0, "col": RED_}, {"label": "LATER", "h": 0.3, "col": SKY}], W_("wins"))),
 sc("D43", None, "hold", ev=[icon("same", "I86")], fx=[{"type": "impact", "word": "emergency"}],
    diagram=split(["DEADLINE IN 3 WEEKS", "NOTHING"], ["DEADLINE TOMORROW", "EMERGENCY"], {"left": W_("three"), "right": W_("tomorrow")}, fs=96, fs0=62, norack=True)),
 sc("D44", "S14", overlays=[step("TRAP 4", "THE GUILT LOOP", "four", dur=3.0)], moves=[mv("snap", "bad", [0.5, 0.55, 1.25])]),
 sc("D45", None, "hold", diagram=loop(GUILT, pulse=W_("more"))),
 sc("D46", "S14", "zoom-out", moves=[mv("snap", "shame", [0.5, 0.32, 1.4]), mv("zoom", "standing", FULL)]),
 sc("D47", None, "hold", diagram={"kind": "list", "items": [{"t": "TOO BLURRY", "word": W_("blurry")}, {"t": "A TEST", "word": W_("test")}, {"t": "TOO FAR AWAY", "word": W_("far")}, {"t": "THE GUILT LOOP", "word": W_("guilt")}]}),
 sc("D48", "S15", moves=[mv("snap", "lazy", [0.4, 0.45, 1.15]), mv("snap", "protect", [0.3, 0.45, 1.4])], overlays=[circ("protect", 0.36, 0.52, 0.06, 0.15)]),
]
P4 = [
 sc("D49", None, "hold", diagram={"kind": "card", "parts": [P("5", Y), P("STEPS")]}),
 sc("D50", "S01", ev=[icon("shoes", "I85")], overlays=[step("STEP 1", "SHRINK IT", "one", dur=3.0)], moves=[mv("snap", "document", [0.3, 0.45, 1.4])]),
 sc("D51", "S01", moves=[mv("snap", "small", [0.32, 0.42, 1.35]), mv("zoom", "for", FULL)], overlays=[sb("WRITE THE FIRST LINE", "line", dur=2.2)]),
 sc("D52", None, "hold", diagram={"kind": "card", "parts": [P("STARTING IS THE", sz="mid"), P("HEAVIEST", mk=True), P("PART", sz="mid")]}),
 sc("D53", "S20", overlays=[step("STEP 2", "IF-THEN PLAN", "two", dur=2.4), pill("PETER GOLLWITZER", "psychologist", dur=3.0)], moves=[mv("snap", "exactly", [0.46, 0.4, 1.4])]),
 sc("D54", None, "hold", swap={"word": "then"},
    diagram={"kind": "card", "parts": [P("IF IT'S"), P("7:00…", Y)]}, diagramB={"kind": "card", "parts": [P("…THEN I OPEN", sz="mid"), P("MY NOTES", Y)]}),
 sc("D55", None, "hold", overlays=[pill("GOLLWITZER & SHEERAN (2006)", "researchers", dur=3.0)], fx=[{"type": "impact", "word": "goals"}],
    diagram={"kind": "dots", "n": 94, "text": "STUDIES", "badge": {"t": "MEDIUM-TO-LARGE EFFECT", "word": W_("effect")}, "at": {"count": W_("combined")}}),
 sc("D56", "S01", "zoom-out", moves=[mv("snap", "show", [0.55, 0.42, 1.3])]),
 sc("D57", "S16", overlays=[step("STEP 3", "MEET FUTURE YOU", "three", dur=3.0)], moves=[mv("snap", "pictures", [0.6, 0.38, 1.4])]),
 sc("D58", None, "hold", fx=[{"type": "impact", "word": "twice"}],
    diagram=bars3("PUT AWAY FOR THE FUTURE", [{"label": "SAW THEIR FACE TODAY", "h": 0.45, "col": SKY, "val": "1×"}, {"label": "SAW THEIR OLDER FACE", "h": 0.9, "col": SAGE, "val": "2×"}], W_("willing"))),
 sc("D59", "S16", moves=[mv("snap", "ask", [0.44, 0.3, 1.4])], overlays=[bub("HOW WILL TOMORROW-ME FEEL?", "how", 0.08, 0.05, 0.3, 0.18)]),
 sc("D60", "S09", trans="fade", moves=[mv("snap", "just", [0.24, 0.45, 1.3])]),
 sc("D61", "S17", ev=[icon("draft", "I87")], overlays=[step("STEP 4", "DO IT BADLY", "four", dur=3.0)], moves=[mv("snap", "permission", [0.46, 0.7, 1.35])]),
 sc("D62", None, "hold", diagram=split(["A ROUGH DRAFT", "FIXABLE"], ["PERFECT IN YOUR HEAD", "STUCK"], {"left": W_("fix"), "right": W_("perfect"), "rack": W_("can't")}, fs=100, fs0=62)),
 sc("D63", "S17", "zoom-out", moves=[mv("snap", "messy", [0.4, 0.35, 1.35]), mv("zoom", "allowed", FULL)], overlays=[sweep("allowed", 0.2, 0.05, 0.5, 0.9)]),
 sc("D64", "S18", overlays=[step("STEP 5", "FORGIVE YOURSELF", "five", dur=3.0)], moves=[mv("snap", "forgive", [0.5, 0.55, 1.3])]),
 sc("D65", "S04", trans="push", overlays=[pill("CARLETON UNIVERSITY", "researchers", dur=2.6), sb("134 STUDENTS", "students", dur=2.4)], moves=[mv("snap", "exams", [0.75, 0.48, 1.3])]),
 sc("D66", None, "hold", diagram=bars3("PROCRASTINATION BEFORE EXAM 2", [{"label": "DIDN'T FORGIVE THEMSELVES", "h": 0.85, "col": RED_}, {"label": "FORGAVE THEMSELVES", "h": 0.4, "col": SAGE}], W_("forgave"),
    badge={"t": "LESS", "word": W_("less"), "top": 300})),
 sc("D67", None, "hold", diagram=loop([(t, None) for t, _ in GUILT], pre=True, brk=W_("breaks"))),
 sc("D68", "S18", moves=[mv("snap", "catch", [0.5, 0.55, 1.3]), mv("zoom", "say", FULL)],
    overlays=[sb("LAZY", "lazy", dur=1.6, red=True), bub("WHAT'S THE SMALLEST NEXT STEP?", "what's", 0.04, 0.05, 0.4, 0.17)]),
 sc("D69", "S05", trans="fade", ev=[card("lot", [("YOU",), P("CARE A LOT", Y)])], moves=[mv("snap", "care", [0.2, 0.66, 1.4]), mv("zoom", "enough", FULL)]),
 sc("D70", "S15", overlays=[sweep("protecting", 0.15, 0.25, 0.3, 0.55)], moves=[mv("snap", "brain", [0.3, 0.42, 1.3])]),
 sc("D71", "S19", trans="iris", irisAt=[0.43, 0.6], moves=[mv("snap", "step", [0.43, 0.58, 1.4])]),
 sc("D72", "S19", "zoom-out", overlays=[sweep("today", 0.3, 0.45, 0.3, 0.3)], moves=[mv("snap", "smallest", [0.5, 0.45, 1.25]), mv("zoom", "future", FULL)]),
 sc("D73", "S29", "hold", ev=[pop("what's", "N06", [("YOUR",), P("ONE THING?", Y)], dur=2.4)], holdEnd=True),
]
for n, sc_ in ((1, P1), (2, P2), (3, P3), (4, P4)):
    os.makedirs("scenes", exist_ok=True)
    json.dump({"part": n, "audio": f"audio/padded/part{n}.wav", "scenes": sc_}, open(f"scenes/part{n}.json", "w"), indent=1)
FOCI = {
 "S01": [[.6, .27, 1.4], [.3, .45, 1.35]], "S02": [[.62, .28, 1.35], [.66, .68, 1.4]], "S03": [[.7, .52, 1.4], [.33, .6, 1.4]],
 "S04": [[.27, .66, 1.4], [.75, .48, 1.35]], "S04b": [[.36, .52, 1.35], [.85, .55, 1.3]], "S05": [[.6, .28, 1.35], [.2, .66, 1.4]],
 "S06": [[.7, .32, 1.4], [.28, .45, 1.3]], "S07": [[.66, .3, 1.4], [.4, .55, 1.3]], "S08": [[.7, .42, 1.4], [.3, .5, 1.35]],
 "S09": [[.66, .36, 1.4], [.23, .45, 1.4]], "S10": [[.22, .5, 1.4], [.64, .4, 1.4]], "S10b": [[.78, .45, 1.35]], "S11": [[.25, .6, 1.4], [.55, .4, 1.2]],
 "S12": [[.25, .42, 1.4], [.8, .52, 1.4]], "S13": [[.2, .45, 1.4], [.76, .32, 1.4]], "S14": [[.5, .4, 1.35], [.5, .58, 1.2]],
 "S15": [[.3, .45, 1.4], [.62, .42, 1.25]], "S16": [[.6, .38, 1.4], [.44, .3, 1.4]], "S17": [[.4, .35, 1.35], [.46, .72, 1.35]],
 "S18": [[.5, .55, 1.3], [.62, .3, 1.35]], "S19": [[.43, .58, 1.4], [.6, .28, 1.35]], "S20": [[.46, .42, 1.4], [.78, .45, 1.3]],
 "S29": [[.75, .5, 1.2]], "I79": [[.5, .5, 1.2]], "I81": [[.5, .5, 1.2]], "I84": [[.5, .5, 1.2]],
}
json.dump(FOCI, open("scenes/foci.json", "w"))
print("specs written", sum(len(x) for x in (P1, P2, P3, P4)), "scenes")
