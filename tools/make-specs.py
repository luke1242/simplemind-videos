#!/usr/bin/env python3
"""Video 7 (overthinking): writes scenes/partN.json (scene specs for tools/build-part.mjs) and scenes/foci.json.
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
def sb(text, word, until=None, dur=2.6, occ=1, red=False, cnt=None, cs=""):
    o = {"type": "sbadge", "text": text, "word": word, "occ": occ, "until": until, "dur": dur, "red": red}
    if cnt is not None: o.update({"cnt": cnt, "cs": cs})
    return o
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
def stp(n, text, word, **kw): return step(f"TRAP {n}" if kw.pop("trap", False) else f"STEP {n}", text, word, **kw)
TOP = [0.4, 0.3, 1.4]
P1 = [
 sc("D01", "S01", moves=[mv("snap", "two", [0.13, 0.62, 1.4]), mv("snap", "closed", [0.34, 0.48, 1.4])]),
 sc("D02", "S01", moves=[mv("snap", "brain", [0.34, 0.48, 1.4])], overlays=[bub("REMEMBER THAT THING YOU SAID TODAY?", "remember", 0.35, 0.15, 0.35, 0.22)]),
 sc("D03", "S01", pictureB="S01b", swap={"word": "wide"}, moves=[mv("snap", "replaying", [0.5, 0.2, 1.4])]),
 sc("D04", "S01b", moves=[mv("snap", "weird", [0.55, 0.4, 1.15])],
    overlays=[bub("WHY DID I SAY IT LIKE THAT?", "say", 0.62, 0.04, 0.36, 0.2), bub("DID THEY THINK I WAS WEIRD?", "weird", 0.62, 0.3, 0.36, 0.2), bub("WHY DID I LAUGH AT MY OWN JOKE?", "laugh", 0.6, 0.56, 0.38, 0.22)]),
 sc("D05", "S02", moves=[mv("snap", "conversation", [0.38, 0.14, 1.4])], overlays=[sb("10 SECONDS", "ten", until="fifty", cnt=10, cs=" SECONDS"), sb("50 TIMES", "fifty", dur=2.4, red=True, cnt=50, cs=" TIMES")]),
 sc("D06", "S03", trans="push", moves=[mv("snap", "strangers", [0.5, 0.45, 1.3])], overlays=[pill("BOOTHBY ET AL. (2018)", "researchers", until="five"), sb("5 MINUTES", "five", dur=2.4, cnt=5, cs=" MINUTES")]),
 sc("D07", "S03", moves=[mv("snap", "liked", [0.36, 0.34, 1.4]), mv("whip", "thought", [0.66, 0.34, 1.4])]),
 sc("D08", None, "hold", diagram=bars3("AFTER 5 MINUTES OF TALKING", [{"label": "HOW MUCH THEY THOUGHT THEY WERE LIKED", "h": 0.5, "col": SKY}, {"label": "HOW MUCH THEY WERE ACTUALLY LIKED", "h": 0.9, "col": SAGE}], W_("partner"))),
 sc("D09", "S03b", moves=[mv("snap", "called", [0.2, 0.2, 1.4])], overlays=[sb("THE LIKING GAP", "liking", dur=2.6)]),
 sc("D10", "S01b", ev=[card("better", [P("IT WENT"), P("BETTER", Y), P("THAN YOU THINK", sz="mid")], dur=2.0), title("LESSON", "PSYCHOLOGY OF", "OVERTHINKING")],
    moves=[mv("snap", "replaying", [0.33, 0.5, 1.4])], fx=[{"type": "riser", "word": "better"}, {"type": "impact", "word": "better"}]),
 sc("D11", "S04", ev=[icon("reply", "I89")], moves=[mv("snap", "message", [0.49, 0.55, 1.4])]),
 sc("D12", "S05", overlays=[sb("20 TIMES", "twenty", dur=2.4, red=True, cnt=20, cs=" TIMES")], moves=[mv("snap", "apologies", [0.3, 0.5, 1.35]), mv("whip", "friendship", [0.62, 0.2, 1.4])]),
 sc("D13", "S05b", trans="whip", moves=[mv("snap", "haha", [0.47, 0.5, 1.2])], overlays=[bub("HAHA SORRY, I WAS AT THE GYM", "haha", 0.46, 0.1, 0.4, 0.22)]),
 sc("D14", "S05b", "zoom-out", ev=[pop("brain", "N10", [("SOLVED",), P("NOTHING", Y)], dur=2.4)], moves=[mv("cut", "and", [0.47, 0.55, 1.2]), mv("zoom", "brain", FULL)]),
 sc("D15", "I90", "hold", moves=[mv("snap", "replaying", [0.5, 0.5, 1.25])]),
 sc("D16", None, "hold", diagram={"kind": "irow", "items": [{"icon": "I91", "label": "THINKING VS OVERTHINKING", "word": W_("know")},
    {"icon": "I84", "label": "4 TRAPS", "word": W_("four")}, {"icon": "I95", "label": "5 WAYS OUT", "word": W_("five")}]}),
 sc("D17", None, "hold", diagram={"kind": "card", "parts": [P("10", Y, cnt=10, cs=" MINUTES", at=W_("ten")), P("AND A PIECE OF PAPER", small=True, at=W_("piece"))]}),
]
P2 = [
 sc("D18", "S06", moves=[mv("snap", "over", [0.5, 0.5, 1.3])], overlays=[sb("RUMINATION", "rumination", dur=2.6)]),
 sc("D19", "S20", overlays=[pill("SUSAN NOLEN-HOEKSEMA", "psychologist", dur=3.2)], moves=[mv("snap", "surprising", [0.45, 0.35, 1.4])]),
 sc("D20", None, "hold", swap={"word": "worse"}, diagram={"kind": "card", "parts": [P("FEELS LIKE"), P("SOLVING", Y)]},
    diagramB={"kind": "card", "parts": [P("MAKES YOU"), P("WORSE", R, slam=True), P("AT IT")]}, fx=[{"type": "impact", "word": "worse"}]),
 sc("D21", None, "hold", diagram=bars3("HOW GOOD THE SOLUTIONS WERE", [{"label": "AFTER RUMINATING", "h": 0.35, "col": RED_}, {"label": "AFTER THINKING ABOUT SOMETHING ELSE", "h": 1.0, "col": SAGE}], W_("ruminating"))),
 sc("D22", "S06", "zoom-out", moves=[mv("snap", "harder", [0.55, 0.3, 1.4]), mv("zoom", "less", FULL)]),
 sc("D23", None, "hold", diagram=split(["THINKING", "NEXT STEP"], ["OVERTHINKING", "LOOPS"], {"left": W_("thinking"), "right": W_("overthinking")}, fs=90, fs0=70, norack=True),
    overlays=[bub("WHAT CAN I DO ABOUT THIS?", "what", 0.03, 0.68, 0.44, 0.2), bub("WHY? WHAT DOES IT SAY ABOUT ME?", "why", 0.53, 0.68, 0.44, 0.22)]),
 sc("D24", None, "hold", swap={"word": "other"}, diagram={"kind": "card", "parts": [P("ENDS IN"), P("ACTION", Y)]}, diagramB={"kind": "card", "parts": [P("ENDS"), P("WHERE IT STARTED", R, sz="mid")]}),
 sc("D25", "S07", "zoom-out", ev=[icon("mud", "I97")], moves=[mv("snap", "spinning", [0.61, 0.7, 1.4]), mv("whip", "engine", [0.46, 0.33, 1.4]), mv("zoom", "going", FULL)]),
 sc("D26", "S08", trans="push", ev=[icon("app", "I80")], overlays=[pill("KILLINGSWORTH & GILBERT (2010)", "researchers", until="built"), sb("2,250 PEOPLE", "people", dur=2.6, cnt=2250, cs=" PEOPLE")]),
 sc("D27", "S08", moves=[mv("snap", "doing", [0.14, 0.25, 1.4]), mv("whip", "thinking", [0.5, 0.55, 1.35])],
    overlays=[bub("WHAT ARE YOU DOING?", "doing", 0.24, 0.34, 0.3, 0.17), bub("WHAT ARE YOU THINKING ABOUT?", "thinking", 0.3, 0.72, 0.36, 0.2)]),
 sc("D28", None, "hold", diagram={"kind": "pie", "pct": 47, "from": 0, "label": "MIND SOMEWHERE ELSE:", "fs": 90, "badge": Y, "value": "47%", "at": {"fill": W_("forty")}},
    fx=[{"type": "riser", "word": "forty"}, {"type": "impact", "word": "forty"}]),
 sc("D29", "S08", "zoom-out", overlays=[sb("LESS HAPPY", "less", dur=2.6, red=True)], moves=[mv("snap", "wandered", [0.82, 0.5, 1.4])]),
 sc("D30", None, "hold", diagram={"kind": "card", "parts": [P("WANDERING MIND =", sz="mid"), P("UNHAPPY MIND", mk=True, at=W_("unhappy"))]}),
 sc("D31", None, "hold", diagram=bars3("DEVELOPED MAJOR DEPRESSION", [{"label": "RUMINATORS", "h": 1.0, "col": RED_}, {"label": "NON-RUMINATORS", "h": 0.25, "col": SKY}], W_("ruminate"),
    badge={"t": "4×", "word": W_("four"), "top": 330}), overlays=[pbadge("1,300 ADULTS", "thirteen", 0.3, 0.17, 0.4, 0.11, fs=60)], fx=[{"type": "impact", "word": "four"}]),
 sc("D32", "S06", "zoom-out", moves=[mv("snap", "waste", [0.55, 0.3, 1.4]), mv("zoom", "mood", FULL)]),
 sc("D33", None, "hold", swap={"word": "loop"},
    diagram={"kind": "card", "parts": [P("NOT", sz="mid"), P("SMART", R, sz="mid", at=W_("smart")), P("CAREFUL", R, sz="mid", at=W_("careful")), P("DEEP", R, sz="mid", at=W_("deep"))]},
    diagramB={"kind": "card", "parts": [P("A"), P("LOOP", Y)]}),
 sc("D34", "S06", moves=[mv("snap", "begging", [0.55, 0.3, 1.4])]),
]
P3 = [
 sc("D35", "I84", "hold", overlays=[sb("4 TRAPS", "four", dur=2.6)], moves=[mv("snap", "four", [0.5, 0.5, 1.2])]),
 sc("D36", "S09", overlays=[step("TRAP 1", "IT FEELS LIKE SOLVING", "one", dur=3.0)], moves=[mv("snap", "replaying", [0.55, 0.3, 1.4])]),
 sc("D37", "S09", ev=[icon("understand", "I91")], overlays=[bub("ONE MORE TIME…", "one", 0.56, 0.04, 0.26, 0.15)], moves=[mv("snap", "ready", [0.51, 0.32, 1.4])]),
 sc("D38", "S20", overlays=[sb("MORE NEGATIVE", "negative", until="pessimistic", red=True), sb("MORE PESSIMISTIC", "pessimistic", dur=2.4, red=True)], moves=[mv("snap", "opposite", [0.45, 0.4, 1.35])]),
 sc("D39", None, "hold", diagram=loop([("REPLAY IT", W_("think")), ("ANALYZE IT", W_("way")), ("FEEL WORSE", W_("loop"))], pulse=W_("around"))),
 sc("D40", "S10", overlays=[step("TRAP 2", "PREDICTING THE WORST", "two", dur=3.0), bub("WHAT IF THEY'RE MAD?", "mad", 0.62, 0.05, 0.33, 0.17), bub("WHAT IF I FAIL?", "fail", 0.04, 0.15, 0.28, 0.16)],
    moves=[mv("snap", "worst", [0.52, 0.5, 1.3]), mv("zoom", "future", FULL)]),
 sc("D41", "S20", trans="push", ev=[icon("write", "I94")], overlays=[pill("PENN STATE (2020)", "researchers", until="write"), sb("10 DAYS", "ten", dur=2.4, cnt=10, cs=" DAYS")]),
 sc("D42", None, "hold", lead=0.7, diagram={"kind": "pie", "pct": 91, "from": 0, "label": "NEVER CAME TRUE:", "fs": 100, "badge": Y, "value": "91%", "at": {"fill": W_("ninety")}},
    fx=[{"type": "riser", "word": "ninety"}, {"type": "impact", "word": "ninety"}]),
 sc("D43", "S10", ev=[pop("terrible", "N05", [("TERRIBLE",), P("FORTUNE TELLER", Y, sz="mid")], dur=2.6)], moves=[mv("snap", "better", [0.5, 0.33, 1.4]), mv("whip", "your", [0.52, 0.5, 1.3])]),
 sc("D44", "S11", "zoom-out", overlays=[step("TRAP 3", "EVERYONE'S JUDGING ME", "three", dur=3.0)], moves=[mv("cut", "three", [0.3, 0.4, 1.3]), mv("zoom", "liking", FULL)]),
 sc("D45", "S11", overlays=[sb("PAUSE", "pause", until="weird"), sb("WEIRD LAUGH", "laugh", dur=2.4)], moves=[mv("snap", "replays", [0.38, 0.28, 1.4])]),
 sc("D46", "S11", moves=[mv("whip", "other", [0.8, 0.3, 1.4])]),
 sc("D47", None, "hold", diagram={"kind": "card", "parts": [P("COLLEGE ROOMMATES:", sz="mid", at=W_("college")), P("THE GAP LASTED", sz="mid"), P("MONTHS", Y, at=W_("months"))]}),
 sc("D48", "S12", overlays=[step("TRAP 4", "IT'S A HABIT", "four", dur=2.8), pill("WATKINS & NOLEN-HOEKSEMA", "psychologists", dur=3.2)], moves=[mv("snap", "habit", [0.38, 0.17, 1.4], occ=2)]),
 sc("D49", "S12", ev=[icon("bed", "I93"), icon("phone", "I89")], moves=[mv("snap", "car", [0.37, 0.5, 1.35])]),
 sc("D50", None, "hold", diagram=loop([("THE CUE", W_("cue")), ("THE LOOP STARTS", W_("starts")), ("REPLAY", W_("think"))], pulse=W_("anything"))),
 sc("D51", "S01b", ev=[card("bed", [P("BED IS"), P("THE CUE", Y)], dur=2.0)], moves=[mv("snap", "two", [0.4, 0.45, 1.2])]),
 sc("D52", None, "hold", diagram={"kind": "list", "items": [{"t": "1. FEELS LIKE SOLVING", "word": W_("solving")}, {"t": "2. PREDICTS THE WORST", "word": W_("worst")}, {"t": "3. EVERYONE'S JUDGING", "word": W_("judging")}, {"t": "4. AUTOPILOT", "word": W_("autopilot")}]}),
 sc("D53", "S09", "zoom-out", moves=[mv("snap", "cares", [0.51, 0.32, 1.4]), mv("zoom", "wrong", FULL)]),
]
P4 = [
 sc("D54", None, "hold", diagram={"kind": "card", "parts": [P("5", Y, cnt=5, at=W_("five")), P("WAYS OUT", at=W_("five"))]}),
 sc("D55", "S13", overlays=[step("STEP 1", "SOLVING OR SPINNING?", "one", dur=3.0)], moves=[mv("snap", "solving", [0.23, 0.32, 1.4]), mv("whip", "spinning", [0.79, 0.53, 1.4]), mv("zoom", "question", FULL)]),
 sc("D56", "S13", overlays=[sb("SEND THE TEXT", "send", until="make"), sb("MAKE THE PLAN", "make", dur=2.2)], moves=[mv("snap", "yes", [0.23, 0.32, 1.4])]),
 sc("D57", None, "hold", swap={"word": "write"}, diagram={"kind": "card", "parts": [P("CAN YOU"), P("FIX IT", Y), P("TOMORROW?")]}, diagramB={"kind": "card", "parts": [P("WRITE THE FIX."), P("DONE.", Y)]}),
 sc("D58", "S13", overlays=[bub("OH, I'M SPINNING.", "oh", 0.62, 0.2, 0.3, 0.15)], moves=[mv("whip", "spinning", [0.79, 0.53, 1.4])]),
 sc("D59", "S14", ev=[icon("schedule", "I86")], overlays=[step("STEP 2", "A WORRY APPOINTMENT", "two", until="back"), pill("TOM BORKOVEC", "psychologist", dur=3.0)], moves=[mv("snap", "instead", [0.36, 0.5, 1.4])]),
 sc("D60", "S14", overlays=[sb("30 MINUTES A DAY", "thirty", until="when", cnt=30, cs=" MINUTES A DAY"), bub("NOT NOW. LATER.", "not", 0.14, 0.08, 0.33, 0.17)], moves=[mv("snap", "window", [0.5, 0.4, 1.3])]),
 sc("D61", None, "hold", diagram=bars3("ANXIETY & STRESS DROPPED", [{"label": "STANDARD TREATMENT", "h": 0.45, "col": SKY}, {"label": "+ WORRY TIME", "h": 0.9, "col": SAGE}], W_("dropped")), overlays=[pill("NETHERLANDS (2011)", "study", dur=3.0)]),
 sc("D62", "S14", "zoom-out", moves=[mv("snap", "finally", [0.36, 0.5, 1.4]), mv("zoom", "simple", FULL)]),
 sc("D63", "S15", overlays=[step("STEP 3", "WRITE IT DOWN", "three", until="at"), pill("RAMIREZ & BEILOCK (2011)", "researchers", until="had"), sb("10 MINUTES", "ten", dur=2.6, cnt=10, cs=" MINUTES")], moves=[mv("snap", "chicago", [0.64, 0.3, 1.3])]),
 sc("D64", None, "hold", diagram=bars3("ANXIOUS STUDENTS' FINAL GRADE", [{"label": "WROTE FIRST", "h": 0.85, "col": SAGE, "val": "B+"}, {"label": "DIDN'T WRITE", "h": 0.6, "col": SKY, "val": "B−"}], W_("wrote")), fx=[{"type": "impact", "word": "minus"}]),
 sc("D65", "S15", "zoom-out", moves=[mv("snap", "head", [0.65, 0.15, 1.4]), mv("whip", "page", [0.375, 0.72, 1.4]), mv("zoom", "test", FULL)]),
 sc("D66", None, "hold", ev=[icon("pen", "I94")], diagram={"kind": "card", "parts": [P("THE", sz="mid"), P("10-MINUTE", mk=True, at=W_("ten")), P("ONE", sz="mid"), P("A PAPER AND A PEN", small=True)]}),
 sc("D67", "S16", ev=[icon("nature", "I95")], overlays=[step("STEP 4", "WALK OUTSIDE", "four", until="at"), pill("STANFORD (2015)", "researchers", until="ninety"), sb("90 MINUTES", "ninety", dur=2.6, cnt=90, cs=" MINUTES")], moves=[mv("snap", "walk", [0.39, 0.4, 1.4])]),
 sc("D68", None, "hold", diagram=split(["NATURE WALK", "LESS RUMINATION"], ["BRAIN SCANS", "QUIETER"], {"left": W_("nature"), "right": W_("brain"), "rack": W_("negative")}, fs=80, fs0=70)),
 sc("D69", "S16", "zoom-out", ev=[icon("walk", "I85")], overlays=[sweep("real", 0.2, 0.5, 0.6, 0.45)], moves=[mv("snap", "green", [0.62, 0.28, 1.3]), mv("zoom", "short", FULL)]),
 sc("D70", "S17", overlays=[step("STEP 5", "GET ABSORBED", "five", dur=3.0)], moves=[mv("snap", "focused", [0.43, 0.28, 1.4])]),
 sc("D71", None, "hold", diagram=loop([("REPLAY IT", None), ("ANALYZE IT", None), ("FEEL WORSE", None)], pre=True, brk=W_("interrupted"))),
 sc("D72", "S17", overlays=[sb("A GAME", "game", until="workout"), sb("A WORKOUT", "workout", until="cooking"), sb("COOKING", "cooking", until="music"), sb("MUSIC", "music", until="friend"), sb("A FRIEND", "friend", dur=2.0)], moves=[mv("snap", "attention", [0.41, 0.54, 1.3])]),
 sc("D73", "S04", overlays=[sb("SCROLLING", "scrolling", dur=2.6, red=True)], moves=[mv("snap", "scrolling", [0.49, 0.55, 1.4])]),
 sc("D74", "S11", trans="fade", moves=[mv("snap", "conversation", [0.25, 0.45, 1.4]), mv("whip", "other", [0.8, 0.3, 1.4])]),
 sc("D75", "S02", ev=[card("facts", [P("THOUGHTS AREN'T", sz="mid"), P("FACTS", Y)], dur=2.0)], moves=[mv("snap", "guesses", [0.38, 0.14, 1.4])]),
 sc("D76", "S18", trans="iris", irisAt=[0.34, 0.47], overlays=[sweep("peace", 0.5, 0.2, 0.4, 0.6)]),
 sc("D77", "S18", "zoom-out", overlays=[sb("SOLVING OR SPINNING?", "solving", until="write"), sb("WRITE IT DOWN", "write", until="outside"), sb("GO OUTSIDE", "outside", dur=2.2)], moves=[mv("snap", "watch", [0.34, 0.47, 1.3]), mv("zoom", "ask", FULL)]),
 sc("D78", "S29", "hold", ev=[pop("what's", "N06", [("YOUR",), P("REPLAY?", Y)], dur=2.4)], holdEnd=True),
]
for n, sc_ in ((1, P1), (2, P2), (3, P3), (4, P4)):
    os.makedirs("scenes", exist_ok=True)
    json.dump({"part": n, "audio": f"audio/padded/part{n}.wav", "scenes": sc_}, open(f"scenes/part{n}.json", "w"), indent=1)
FOCI = {
 "S01": [[.13, .62, 1.4], [.34, .48, 1.4]], "S01b": [[.5, .2, 1.4], [.33, .5, 1.4]], "S02": [[.38, .14, 1.4], [.33, .5, 1.4]], "S03": [[.36, .34, 1.4], [.66, .34, 1.4]],
 "S03b": [[.2, .2, 1.4], [.66, .34, 1.4]], "S04": [[.49, .55, 1.4], [.36, .32, 1.4]], "S05": [[.3, .5, 1.35], [.62, .2, 1.4]], "S05b": [[.47, .5, 1.2], [.39, .42, 1.2]],
 "S06": [[.55, .3, 1.4], [.5, .5, 1.3]], "S07": [[.61, .7, 1.4], [.46, .33, 1.4]], "S08": [[.14, .25, 1.4], [.5, .55, 1.35]], "S09": [[.51, .32, 1.4], [.5, .4, 1.2]],
 "S10": [[.52, .5, 1.3], [.5, .33, 1.4]], "S11": [[.3, .4, 1.4], [.8, .3, 1.4]], "S12": [[.37, .5, 1.35], [.38, .17, 1.4]], "S13": [[.23, .32, 1.4], [.79, .53, 1.4]],
 "S14": [[.36, .5, 1.4], [.65, .3, 1.35]], "S15": [[.65, .15, 1.4], [.375, .72, 1.4]], "S16": [[.39, .4, 1.4], [.62, .28, 1.3]], "S17": [[.43, .28, 1.4], [.41, .54, 1.3]],
 "S18": [[.34, .47, 1.3], [.8, .28, 1.3]], "S20": [[.45, .35, 1.4], [.8, .4, 1.3]], "S29": [[.8, .3, 1.25]], "I90": [[.5, .5, 1.2]], "I84": [[.5, .5, 1.2]],
}
json.dump(FOCI, open("scenes/foci.json", "w"))
print("specs written", sum(len(x) for x in (P1, P2, P3, P4)), "scenes")
