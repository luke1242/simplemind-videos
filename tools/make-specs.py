#!/usr/bin/env python3
"""Video 3 (manifestation): writes scenes/partN.json (specs for tools/build-part.mjs) and scenes/foci.json. Scene list = VIDEO.md."""
import json, os
Y, R = "yellow", "red"
def P(t, b=None, **fl):
    d = {"t": t}
    if b: d["badge"] = b
    d.update(fl); return d
def _parts(ps): return [p if isinstance(p, dict) else P(*p) for p in ps]
def icon(word, ic, occ=1, dur=1.8): return {"kind": "icon", "icon": ic, "word": word, "occ": occ, "dur": dur}
def card(word, parts, occ=1, dur=1.9, **kw): return {"kind": "card", "parts": _parts(parts), "word": word, "occ": occ, "dur": dur, **kw}
def pop(word, pose, content, occ=1, dur=2.8):
    c = {"type": "icon", "icon": content} if isinstance(content, str) else {"type": "card", "parts": _parts(content)}
    return {"kind": "pop", "pose": pose, "content": c, "word": word, "occ": occ, "dur": dur}
def crop(word, focus, occ=1, dur=2.4): return {"kind": "crop", "focus": focus, "word": word, "occ": occ, "dur": dur}
def title(l1, l2): return {"kind": "title", "dur": 2.5, "l1": l1, "l2": l2}
def flash(pic, word, until, occ=1): return {"kind": "flash", "pic": pic, "word": word, "occ": occ, "until": until}
def mv(kind, word, f=None, occ=1, **kw): return {"kind": kind, "word": word, "occ": occ, "f": f, **kw}
def step(n, text, word, occ=1, **kw): return {"type": "step", "step": n, "text": text, "word": word, "occ": occ, **kw}
def tag(word, parts, dur=2.6, occ=1, **kw): return {"type": "tag", "parts": _parts(parts), "word": word, "occ": occ, "dur": dur, **kw}
def pill(text, word, dur=2.6, occ=1, **kw): return {"type": "pill", "text": text, "word": word, "occ": occ, "dur": dur, **kw}
def label(text, word, dur=2.4, occ=1, **kw): return {"type": "label", "text": text, "word": word, "occ": occ, "dur": dur, **kw}
def circle(word, cx, cy, rx, ry, occ=1): return {"type": "circle", "cx": cx, "cy": cy, "rx": rx, "ry": ry, "word": word, "occ": occ}
def arrow(word, x0, y0, x1, y1, occ=1): return {"type": "arrow", "x0": x0, "y0": y0, "x1": x1, "y1": y1, "word": word, "occ": occ}
def sweep(word, x, y, w, h, occ=1): return {"type": "sweep", "word": word, "occ": occ, "box": {"x": x, "y": y, "w": w, "h": h}}
def sc(id, narr, picture=None, camera="zoom-in", ev=None, **kw):
    d = {"id": id, "camera": camera, "narration": narr, "events": ev or []}
    if picture: d["picture"] = picture
    d.update(kw); return d
W_ = lambda w, o=1: {"word": w, "occ": o}
def split(left, right, lw, rw, fs=100, **kw): return {"kind": "split", "left": left, "right": right, "fs": fs, "at": {"left": lw, "right": rw}, **kw}
def drops(header, rows, dir="down"): return {"kind": "drops", "header": header, "dir": dir, "rows": [{"label": l, "word": w, "occ": o} for l, w, o in rows]}
def cards(*states): return {"kind": "cards", "states": list(states)}
def st(parts, w=None, **kw):
    d = {"parts": _parts(parts)}
    if w: d["w"] = w
    d.update(kw); return d
def irow(items): return {"kind": "iconrow", "items": [{"icon": i, "word": w, "label": l} for i, w, l in items]}
WISH_A = "CHALLENGING BUT|**POSSIBLE**"
Hd = lambda *h: list(h)

P1 = [
 sc("M01", '''You've probably heard it a hundred times. Picture your dream life. See it clearly. Feel it like it's already yours... and the universe will bring it to you.''', "S01",
    ev=[icon("universe", "I57")], moves=[mv("snap", "picture", [0.5, 0.26, 1.25])], overlays=[sweep("feel", 0.02, 0.02, 0.95, 0.5)]),
 sc("M02", '''Vision boards. Scripting. Saying it out loud every morning. It's everywhere. TikTok, YouTube, half the books in the self-help section.''', "S02", "pan-right",
    ev=[icon("books", "I46")], moves=[mv("snap", "vision", [0.16, 0.38, 1.4]), mv("whip", "scripting", [0.34, 0.28, 1.4]), mv("whip", "saying", [0.53, 0.2, 1.4]), mv("zoom", "everywhere", [0.5, 0.5, 1])]),
 sc("M03", '''But a psychologist named Gabriele Oettingen spent more than twenty years actually testing what happens when people daydream about their goals. Not in theory. In real people, with real goals, followed for months and even years.''', "S20", trans="whip",
    host=[["N02"], ["N06", "not"]], moves=[mv("snap", "psychologist", [0.46, 0.4, 1.4]), mv("whip", "real", [0.78, 0.4, 1.3])],
    overlays=[pill("GABRIELE OETTINGEN", "oettingen", dur=2.2), tag("twenty", [P("20+", Y), ("YEARS OF TESTS",)], dur=2.6, count=20, suffix="+", pos="bottom")]),
 sc("M04", '''And what she found... is not what most manifestation videos tell you.''', "S02",
    ev=[pop("not", "N09", [("NOT", R), P("WHAT YOU'VE HEARD", sz="mid")], dur=2.4)], moves=[mv("snap", "found", [0.55, 0.45, 1.4])]),
 sc("M05", '''In one study, she followed college students who were about to graduate and look for their first job. She asked how often they had positive daydreams about landing that dream job. Then she checked back two years later.''', "S04", "pan-right",
    ev=[icon("job", "I53"), card("two", [P("2 YEARS", Y), ("LATER",)], trans="push")],
    moves=[mv("snap", "college", [0.2, 0.5, 1.4]), mv("whip", "graduate", [0.82, 0.6, 1.4]), mv("snap", "daydreams", [0.17, 0.55, 1.4]), mv("whip", "landing", [0.41, 0.2, 1.4])]),
 sc("M06", '''The students who daydreamed the most... had sent out fewer applications. Gotten fewer job offers. And were earning lower salaries.''', None, "hold", host=[["N02"]],
    diagram=drops("THE BIGGEST DAYDREAMERS", [("APPLICATIONS", "applications", 1), ("JOB OFFERS", "offers", 1), ("SALARY", "salaries", 1)]),
    fx=[{"type": "riser", "word": "fewer"}, {"type": "impact", "word": "salaries"}]),
 sc("M07", '''Picturing the dream... had made them less likely to get it.''', "S04",
    ev=[card("less", [("LESS", R), ("LIKELY",), ("TO GET IT",)])], overlays=[circle("picturing", 0.17, 0.64, 0.14, 0.26)]),
 sc("M08", '''And honestly, that one stung a little.''', "S34", "hold"),
 sc("M09", '''Because I used to be big on manifesting. I'd lie in bed at night and picture everything. The body I wanted. The channel I wanted to build. The version of me who had it all figured out.''', "S01",
    moves=[mv("snap", "picture", [0.5, 0.26, 1.25]), mv("whip", "body", [0.15, 0.25, 1.4]), mv("whip", "channel", [0.45, 0.25, 1.4]), mv("whip", "version", [0.78, 0.28, 1.4]), mv("zoom", "figured", [0.5, 0.5, 1])],
    fx=[{"type": "leak", "word": "used"}]),
 sc("M10", '''And it felt amazing. Like I was already halfway there.''', "S25",
    ev=[card("halfway", [("ALREADY",), ("HALFWAY", Y), ("THERE",)])], overlays=[sweep("amazing", 0.45, 0.28, 0.4, 0.4)]),
 sc("M11", '''And then the next morning... I'd do basically nothing. Because somehow, my brain felt like I'd already done the work.''', "S23", trans="push",
    ev=[pop("brain", "N10", [("ALREADY",), ("DONE THE WORK", Y)], dur=2.6)], moves=[mv("snap", "nothing", [0.85, 0.86, 1.4])]),
 sc("M12", '''I even made a vision board once. Pictures of the gym body, a big subscriber count, the whole thing. I hung it right over my desk. It stayed there for months... looking at me... while I didn't do much of anything on it.''', "S03",
    ev=[icon("months", "I13"), pop("didn't", "N05", [("MONTHS OF",), ("NOTHING", Y)], dur=2.6)],
    moves=[mv("snap", "vision", [0.72, 0.28, 1.3]), mv("whip", "gym", [0.6, 0.3, 1.4]), mv("whip", "subscriber", [0.84, 0.4, 1.4]), mv("zoom", "hung", [0.5, 0.5, 1])],
    overlays=[arrow("looking", 0.72, 0.47, 0.58, 0.57)]),
 sc("M13", '''But here's the thing. Manifestation isn't completely wrong. There's one part of it that's backed by real science. And one part that quietly works against you.''', None, "hold",
    ev=[card("isn't", [("NOT COMPLETELY",), ("WRONG", Y)])], host=[["N06"], ["N02", "there's"]],
    diagram=split(["BACKED BY", "SCIENCE"], ["WORKS", "AGAINST YOU"], W_("science"), W_("against"), rb="red",
                  syms=[{"side": "L", "sym": "tick", "word": "science"}, {"side": "R", "sym": "cross", "word": "against"}])),
 sc("M14", '''By the end of this video, you'll know why manifesting feels like it works, the one part everyone gets wrong, and the five-step version that researchers have actually tested.''', None, "hold", host=[["N01"]],
    diagram=irow([("I61", "feels", "WHY IT FEELS REAL"), ("I58", "wrong", "THE MISTAKE"), ("I59", "five", "5 STEPS")])),
 sc("M15", '''It takes about five minutes. And it's the only kind of manifesting I still do.''', "S36",
    ev=[icon("five", "I11"), title("PSYCHOLOGY OF", "MANIFESTATION")], moves=[mv("snap", "only", [0.3, 0.5, 1.3])]),
]
P2 = [
 sc("M16", '''So let's start with what the research actually found. Oettingen and her colleague Doris Mayer didn't just study job seekers. They studied four completely different groups.''', "S20",
    ev=[icon("job", "I53")], host=[["N01"], ["N06", "oettingen"]], moves=[mv("snap", "oettingen", [0.46, 0.4, 1.4])],
    overlays=[pill("OETTINGEN & MAYER", "oettingen", dur=2.4), tag("four", [P("4", Y), ("GROUPS",)], dur=2.4, count=4, **{"from": 1}, pos="bottom")]),
 sc("M17", '''Students with a crush on someone. Students getting ready for an exam. And even older adults about to have hip replacement surgery.''', None, "hold",
    diagram=irow([("I54", "crush", "THE CRUSH"), ("I46", "exam", "THE EXAM"), ("I55", "hip", "THE SURGERY")])),
 sc("M18", '''Every time, they measured two different things. First: how likely did people think it was that things would work out? And second: how much did they daydream about the perfect outcome? And those two things pointed in opposite directions.''', None, "hold",
    ev=[card("two", [P("TWO", Y), ("THINGS",)])], host=[["N06"], ["N02", "and", 2]],
    diagram=split(["HOW", "LIKELY?"], ["HOW MUCH", "DAYDREAMING?"], W_("likely"), W_("daydream"), rb="yellow",
                  syms=[{"side": "L", "sym": "up", "word": "opposite"}, {"side": "R", "sym": "down", "word": "opposite"}])),
 sc("M19", '''The students who daydreamed the most about their crush were less likely to actually end up together months later.''', "S05",
    moves=[mv("snap", "daydreamed", [0.68, 0.22, 1.4]), mv("whip", "less", [0.4, 0.55, 1.4])], overlays=[tag("less", [("LESS", R), ("LIKELY",)], dur=2.6)]),
 sc("M20", '''The students who daydreamed most about acing the exam studied less... and their grades went down.''', "S06",
    moves=[mv("snap", "acing", [0.6, 0.25, 1.4]), mv("whip", "studied", [0.65, 0.8, 1.4])], overlays=[arrow("grades", 0.5, 0.52, 0.5, 0.72)]),
 sc("M21", '''And the surgery patients who pictured a perfect, easy recovery... were recovering worse two weeks later.''', "S21",
    host=[["N06"]], moves=[mv("snap", "pictured", [0.76, 0.5, 1.4])], overlays=[tag("worse", [("WORSE", R), ("AT 2 WEEKS",)], dur=2.6)]),
 sc("M22", '''And when the researchers looked at what those daydreams actually sounded like, there was a pattern.''', "S20",
    moves=[mv("snap", "sounded", [0.78, 0.4, 1.3])], overlays=[circle("pattern", 0.52, 0.87, 0.06, 0.07)]),
 sc("M23", '''They were effortless. No setbacks. No hard days. Just... arriving.''', "S24", "hold",
    ev=[card("effortless", [("ALWAYS",), ("EFFORTLESS", Y)])], moves=[mv("whip", "arriving", [0.5, 0.15, 1.4])],
    overlays=[label("NO SETBACKS", "setbacks", until="hard"), label("NO HARD DAYS", "hard", dur=1.6)]),
 sc("M24", '''Now, to be fair, these studies show a link, not proof. But the same pattern kept showing up, in very different people.''', None, "hold", host=[["N01"]],
    diagram=cards(st([("A",), P("LINK,", mk=True), ("NOT PROOF.",)], W_("studies"), mk=W_("link")), st([("SAME",), P("PATTERN", Y), ("EVERY TIME.",)], W_("same")))),
 sc("M25", '''But the people who simply expected things to go well, who believed it was likely, because they'd done it before or knew they could... they did better. They tried harder. They got more of what they wanted.''', "S35",
    ev=[pop("believed", "N11", [P("BELIEVED IT WAS", sz="mid"), ("LIKELY", Y)], dur=2.6), card("better", [("THEY DID",), ("BETTER", Y)])],
    moves=[mv("snap", "expected", [0.4, 0.58, 1.3]), mv("whip", "harder", [0.62, 0.45, 1.3])]),
 sc("M26", '''So believing it can happen... helps. Daydreaming that it already happened... hurts.''', None, "hold", host=[["N06"], ["N02", "daydreaming"]],
    diagram=split(["BELIEVING IT", "CAN HAPPEN:", "HELPS"], ["DAYDREAMING IT", "HAPPENED:", "HURTS"], W_("helps"), W_("hurts"), lb="yellow", rb="red"),
    fx=[{"type": "riser", "word": "helps"}, {"type": "impact", "word": "hurts"}]),
 sc("M27", '''Why would daydreaming hurt? Oettingen and another researcher, Heather Kappes, found a clue in people's bodies.''', "S33",
    ev=[icon("clue", "I25")], moves=[mv("snap", "kappes", [0.6, 0.2, 1.4])], overlays=[pill("HEATHER KAPPES", "kappes", dur=2.4)]),
 sc("M28", '''In one study, they had students skip food and water for a few hours. Then some of the thirstiest students were asked to picture a glass of ice-cold water.''', "S07",
    ev=[icon("hours", "I11")], moves=[mv("snap", "skip", [0.54, 0.82, 1.4]), mv("whip", "picture", [0.67, 0.22, 1.4])], overlays=[sweep("ice", 0.55, 0.05, 0.22, 0.45)]),
 sc("M29", '''And when they did... their blood pressure dropped. Their energy dropped.''', None, "hold", host=[["N06"]],
    diagram=drops("PICTURING THE WATER", [("BLOOD PRESSURE", "dropped", 1), ("ENERGY", "dropped", 2)])),
 sc("M30", '''Their bodies relaxed, almost as if they'd already had the drink.''', "S07",
    overlays=[circle("already", 0.66, 0.2, 0.1, 0.2), tag("already", [("ALREADY",), P("HAD IT", Y)], dur=2.4)]),
 sc("M31", '''In another study, people who spent time picturing an amazing week ahead felt less energized. And by the end of that week... they'd gotten fewer of their goals done.''', "S22",
    ev=[icon("energized", "I56"), card("fewer", [("FEWER", R), ("GOALS DONE",)])], moves=[mv("snap", "picturing", [0.78, 0.62, 1.4])]),
 sc("M32", '''That's the trap. When you picture the finish line in perfect detail, your brain gets a little taste of the reward. And it relaxes... right when you need it to get moving.''', "S12",
    ev=[pop("trap", "N02", [("THAT'S",), ("THE TRAP", Y)], dur=2.4), icon("taste", "I52")],
    moves=[mv("snap", "reward", [0.55, 0.47, 1.4]), mv("zoom", "relaxes", [0.5, 0.5, 1]), mv("whip", "moving", [0.42, 0.87, 1.4])]),
]
P3 = [
 sc("M33", '''So if daydreaming can backfire, why does manifestation seem to work for so many people? Because some of it really does. Just not for the reasons people think. Here are three.''', None, "hold",
    ev=[card("not", [("NOT", R), ("WHY YOU THINK",)])],
    diagram={"kind": "grid", "pop": True, "lit": {"n": 6}, "badge": {"parts": _parts([P("3", Y), P("REASONS")])}, "at": {"pop": W_("many"), "lit": W_("some"), "badge": W_("three")}}),
 sc("M34", '''One. You start noticing things. A psychologist named Richard Wiseman once gave people a newspaper and asked them to count the photos inside.''', "S08", trans="whip",
    host=[["N08"], ["N01", "a"]], moves=[mv("snap", "newspaper", [0.5, 0.5, 1.25]), mv("whip", "count", [0.68, 0.45, 1.4])],
    overlays=[step("REASON 1", "YOU START NOTICING", "one", dur=3.0), pill("RICHARD WISEMAN", "wiseman", dur=2.4, pos="bottom")]),
 sc("M35", '''On the second page, in big letters, was a message: "Stop counting. There are forty-three photographs in this newspaper."''', "S08",
    host=[["N05"]], moves=[mv("snap", "second", [0.38, 0.48, 1.4])],
    overlays=[{"type": "sign", "text": "STOP COUNTING.<br>THERE ARE<br>{N} PHOTOS.", "word": "message", "cnt": 43, "cntWord": "forty", "card": True, "box": {"x": 0.26, "y": 0.33, "w": 0.24, "h": 0.26}, "rot": -2, "fs": 40}]),
 sc("M36", '''The people who called themselves lucky usually spotted it in seconds. The people who called themselves unlucky were so focused on counting, they flew right past it.''', "S08",
    host=[["N01"], ["N05", "the", 2]], moves=[mv("snap", "lucky", [0.34, 0.42, 1.4]), mv("whip", "unlucky", [0.68, 0.45, 1.4])],
    overlays=[tag("seconds", [P("SECONDS", Y)], dur=2.2), tag("past", [P("MISSED IT", R)], dur=2.4)]),
 sc("M37", '''When you decide something matters to you, you start seeing chances you used to miss.''', "S27",
    moves=[mv("snap", "chances", [0.72, 0.47, 1.4])]),
 sc("M38", '''That's not the universe. That's your attention.''', None, "hold", host=[["N06"]],
    diagram=cards(st([("NOT THE",), ("UNIVERSE", R)]), st([("YOUR",), P("ATTENTION", mk=True)], W_("attention")))),
 sc("M39", '''The lucky people in that experiment didn't get more chances. They just saw more of the ones that were already there.''', "S08", "zoom-out",
    ev=[card("saw", [("THEY JUST",), ("SAW MORE", Y)])], host=[["N01"]], overlays=[circle("already", 0.38, 0.48, 0.1, 0.13)]),
 sc("M40", '''Two. Belief changes what you do. Remember those studies. Expecting that something is possible made people try harder and keep going.''', None, "hold",
    ev=[icon("going", "I49")], host=[["N08"], ["N01", "remember"]],
    diagram=split(["BELIEVING IT", "CAN HAPPEN:", "HELPS"], ["DAYDREAMING IT", "HAPPENED:", "HURTS"], W_("remember"), W_("remember"), lb="yellow", rb="red", dimRight=True),
    overlays=[step("REASON 2", "BELIEF CHANGES WHAT YOU DO", "two", dur=4.0)]),
 sc("M41", '''So the "believe it" part of manifestation? That part is real. Believing you can do something makes you act like someone who can. That's honestly such a big topic that I'm making a whole video on it next.''', "S26",
    ev=[card("real", [("THAT PART IS",), ("REAL", Y)]), pop("whole", "N05", [P("NEXT", Y), ("VIDEO",)], dur=2.4)],
    moves=[mv("snap", "so", [0.6, 0.5, 1.3]), mv("whip", "act", [0.33, 0.5, 1.35])]),
 sc("M42", '''Three. You remember the hits. When you manifest something and it happens, it feels like magic, and you tell everyone. When you manifest something and it doesn't happen... you just quietly forget about it.''', None, "hold",
    ev=[icon("magic", "I57")], host=[["N08"], ["N01", "when"], ["N05", "when", 2]],
    diagram={"kind": "grid", "lit": {"n": 6}, "dim": True, "at": {"lit": W_("happens"), "dim": W_("forget")}},
    overlays=[step("REASON 3", "YOU REMEMBER THE HITS", "three", dur=4.0)]),
 sc("M43", '''So every success story you hear has a lot of silent ones behind it.''', "S28",
    moves=[mv("snap", "success", [0.32, 0.52, 1.4]), mv("whip", "silent", [0.3, 0.82, 1.3]), mv("whip", "behind", [0.75, 0.82, 1.3])]),
 sc("M44", '''Someone manifests a new job, gets it, and posts about it. Nobody posts, "I manifested this for a year and nothing happened."''', "S02",
    ev=[icon("posts", "I41"), card("nobody", [("NOBODY POSTS",), ("THE MISSES", R)])], moves=[mv("snap", "manifests", [0.34, 0.28, 1.4])]),
 sc("M45", '''Which brings us to the one part everyone gets wrong.''', None, "hold", host=[["N02"]],
    diagram=cards(st([P("THE PART EVERYONE", sz="mid"), P("GETS WRONG", mk=True)], W_("which"), mk=W_("gets"))),
    fx=[{"type": "riser", "word": "which"}]),
 sc("M46", '''Manifestation tells you to picture the outcome. The finish line. The moment you've already made it. But that's exactly the kind of picture that drains your energy.''', "S25",
    ev=[icon("drains", "I56")], moves=[mv("snap", "outcome", [0.58, 0.25, 1.4]), mv("zoom", "but", [0.5, 0.5, 1])]),
 sc("M47", '''Researchers at UCLA, Lien Pham and Shelley Taylor, tested this with students before a big midterm. One group spent a few minutes a day picturing themselves getting a great grade. Another group pictured the process. Where they'd sit. When they'd study. What they'd go over.''', "S09", trans="whip",
    host=[["N01"], ["N06", "one"]], moves=[mv("snap", "one", [0.18, 0.4, 1.3]), mv("whip", "another", [0.8, 0.55, 1.3])],
    overlays=[pill("PHAM & TAYLOR, UCLA", "pham", dur=2.6), sweep("midterm", 0.0, 0.0, 1.0, 1.0), circle("sit", 0.86, 0.72, 0.07, 0.1), circle("when", 0.76, 0.14, 0.06, 0.09), circle("what", 0.57, 0.83, 0.08, 0.07)]),
 sc("M48", '''The students who pictured the process studied longer... and did better on the exam.''', None, "hold", host=[["N02"]],
    diagram=drops("PICTURED THE PROCESS", [("STUDIED LONGER", "longer", 1), ("BETTER GRADES", "better", 1)], "up"), fx=[{"type": "impact", "word": "better"}]),
 sc("M49", '''Picturing the grade felt good. Picturing the process made them actually plan.''', None, "hold", host=[["N06"]],
    diagram=cards(st([P("THE GRADE: FELT", sz="mid"), P("GOOD", Y)]), st([P("THE PROCESS: MADE A", sz="mid"), P("PLAN", Y, ul=True)], W_("process"), ul=W_("plan")))),
 sc("M50", '''So the problem isn't that you're picturing your goal. It's that you're only picturing the ending. And you're skipping the most important part of the picture... the part where something gets in your way.''', "S11",
    pictureB="S11b", swap={"word": "way"}, moves=[mv("snap", "ending", [0.78, 0.21, 1.4]), mv("zoom", "skipping", [0.3, 0.5, 1.15])]),
]
P4 = [
 sc("M51", '''So here's how I actually manifest now. Five steps.''', "S36",
    ev=[icon("steps", "I59")], moves=[mv("snap", "five", [0.3, 0.5, 1.3])]),
 sc("M52", '''The first four come from a method Oettingen built out of all this research. It's called WOOP.''', None, "hold", host=[["N01"]],
    diagram={"kind": "woop", "intro": W_("woop")}),
 sc("M53", '''One. Wish. Pick one thing you really want, that's challenging but actually possible. Not "be rich" or "be happy." Something like "start my YouTube channel," or "run a 5K by spring." Something that's actually up to you.''', None, "hold",
    ev=[card("rich", [("NOT",), ("BE RICH", R)]), icon("youtube", "I60"), pop("up", "N11", [("ACTUALLY",), ("UP TO YOU", Y)], dur=2.4)], host=[["N07"], ["N01", "pick"]],
    diagram={"kind": "woop", "active": "WISH", "answers": {"WISH": [WISH_A, "possible", 1]}},
    overlays=[step("STEP 1", "WISH", "one", dur=3.2)]),
 sc("M54", '''Two. Outcome. Now picture the best result. How would it feel? What would change? Go ahead and enjoy it for a moment. This part is fine.''', "S31", "zoom-out", trans="iris", irisAt=[0.83, 0.22],
    ev=[card("fine", [("THIS PART IS",), ("FINE", Y)])], overlays=[step("STEP 2", "OUTCOME", "two", dur=3.2), sweep("enjoy", 0.0, 0.0, 1.0, 0.5)]),
 sc("M55", '''It's the next step that makes it work.''', None, "hold", host=[["N01"]],
    diagram={"kind": "woop", "ticks": ["WISH", "OUTCOME"], "pulse": ["OBSTACLE", "next"], "answers": {"WISH": [WISH_A, None, 1]}}),
 sc("M56", '''Three. Obstacle. This is the step everyone skips. Ask yourself: what's the main thing inside me that's going to get in the way?''', "S11b",
    moves=[mv("snap", "skips", [0.72, 0.52, 1.4]), mv("whip", "inside", [0.3, 0.5, 1.15])],
    overlays=[step("STEP 3", "OBSTACLE", "three", until="skips"), tag("skips", [("THE ONE",), ("EVERYONE SKIPS", R)], dur=2.6)]),
 sc("M57", '''Not other people. Not bad luck. You.''', None, "hold", host=[["N02"]],
    diagram=cards(st([("NOT",), ("OTHER PEOPLE", R)]), st([("NOT",), ("BAD LUCK", R)], W_("luck")), st([P("YOU.", Y)], W_("you"))), fx=[{"type": "impact", "word": "you"}]),
 sc("M58", '''Maybe it's that you get home tired and scroll instead. Maybe it's that you're scared of what people will think.''', "S22",
    ev=[icon("people", "I06")], moves=[mv("snap", "scroll", [0.76, 0.55, 1.4])]),
 sc("M59", '''Picture that obstacle as clearly as you pictured the dream.''', "S11b",
    moves=[mv("snap", "obstacle", [0.72, 0.52, 1.4]), mv("whip", "dream", [0.78, 0.21, 1.4])]),
 sc("M60", '''And here's the surprising part. This doesn't kill your motivation. When the wish is realistic, seeing the obstacle is what tells your brain it's time to get ready.''', None, "hold",
    ev=[pop("surprising", "N09", [("DOESN'T",), ("KILL", R), ("MOTIVATION",)], dur=2.6)], host=[["N01"]],
    diagram={"kind": "woop", "active": "OBSTACLE", "answers": {"OBSTACLE": ["TIME TO|**GET READY**", "ready", 1]}}),
 sc("M61", '''Four. Plan. Make one simple if-then plan for that obstacle.''', None, "hold", host=[["N07"], ["N01", "make"]],
    diagram={"kind": "woop", "active": "PLAN"}, overlays=[step("STEP 4", "PLAN", "four", dur=3.2)]),
 sc("M62", '''"If I get home tired and grab my phone, then I'll put it in the other room and do ten minutes first."''', None, "hold",
    ev=[icon("ten", "I43")], host=[["N01"]], diagram=split(["IF:", "TIRED + PHONE"], ["THEN:", "OTHER ROOM"], W_("if"), W_("then"), fs=92, rb="yellow")),
 sc("M63", '''In one study, high school students who used this method completed more than sixty percent more practice questions for a big exam than students who didn't.''', None, "hold", host=[["N02"]],
    diagram={"kind": "bars", "raw": True, "colorA": "#F2C230", "bars": [{"label": "USED WOOP", "v": 140}, {"label": "DIDN'T", "v": 84}], "title": "PRACTICE QUESTIONS", "source": "Duckworth et al., 2011", "plus": "+60%",
             "at": {"grow": W_("used"), "plus": W_("sixty")}},
    fx=[{"type": "riser", "word": "sixty"}, {"type": "impact", "word": "sixty"}]),
 sc("M64", '''Five. Picture the process, not just the finish line.''', "S11",
    moves=[mv("snap", "finish", [0.78, 0.21, 1.4])], overlays=[step("STEP 5", "PICTURE THE PROCESS", "five", dur=3.4)]),
 sc("M65", '''When you visualize, don't just see yourself holding the trophy. See yourself doing the boring part. Opening the laptop. Lacing up your shoes. Hitting record.''', None, "hold", host=[["N01"]],
    ev=[icon("trophy", "I52"), card("boring", [("THE",), ("BORING PART", Y)])],
    diagram=irow([("I60", "laptop", "OPEN THE LAPTOP"), ("I49", "shoes", "LACE UP"), ("I62", "record", "HIT RECORD")])),
 sc("M66", '''That's the picture that actually gets you moving.''', "S35", moves=[mv("snap", "moving", [0.4, 0.58, 1.3])]),
 sc("M67", '''Let me show you how this sounds for me.''', "S10"),
 sc("M68", '''My wish: post one video every week. The outcome: a channel I'm proud of, and people in the comments saying a video actually helped them. The obstacle... honestly? It's me deciding a video isn't good enough yet, and not posting it. So my plan: if I catch myself thinking "it's not ready," then I post it anyway and make the next one better.''', None, "hold",
    ev=[icon("week", "I13"), icon("comments", "I41"), pop("deciding", "N10", [P("NOT GOOD ENOUGH", R, sz="mid"), ("YET",)], dur=2.8)], host=[["N01"]],
    diagram={"kind": "woop", "answers": {"WISH": ["1 VIDEO|**EVERY WEEK**", "wish", 1], "OUTCOME": ["A CHANNEL|I'M **PROUD OF**", "outcome", 1], "OBSTACLE": ["~~\"IT'S NOT READY\"~~", "obstacle", 1], "PLAN": ["POST IT|**ANYWAY**", "plan", 1]}, "ul": ["PLAN", "anyway"]}),
 sc("M69", '''And the process? I picture Sunday night. Me, the laptop, hitting upload. Not the million views. Just the upload.''', "S10",
    ev=[card("million", [("NOT THE",), ("MILLION VIEWS", R)])], moves=[mv("snap", "laptop", [0.3, 0.68, 1.4]), mv("zoom", "just", [0.64, 0.3, 1.3])], overlays=[circle("upload", 0.29, 0.68, 0.05, 0.075)]),
 sc("M70", '''Here's what I keep coming back to. I don't think wanting things and dreaming big is the problem. Dreaming is where everything starts.''', "S37", trans="fade",
    ev=[card("dreaming", [("WHERE",), ("IT ALL STARTS", Y)], occ=2)], moves=[mv("snap", "dreaming", [0.5, 0.22, 1.4], occ=2)]),
 sc("M71", '''The problem is when the dream feels so good... that it replaces the doing.''', "S12",
    moves=[mv("snap", "good", [0.55, 0.47, 1.4]), mv("whip", "doing", [0.42, 0.87, 1.4])]),
 sc("M72", '''Because the version of you in the daydream isn't someone you become by picturing. It's someone you become by doing the boring part, over and over.''', "S26",
    ev=[card("over", [P("OVER AND OVER", Y)])], moves=[mv("snap", "version", [0.33, 0.5, 1.35]), mv("whip", "doing", [0.6, 0.5, 1.3])]),
 sc("M73", '''So keep the dream. Just stop letting it be the finish line. Let it be the starting line.''', "S11", "zoom-out",
    ev=[card("finish", [("NOT THE",), ("FINISH LINE", R)], max=3.6, dur=3.2, swap={"word": "starting", "parts": _parts([("THE",), ("STARTING LINE", Y)])})],
    moves=[mv("snap", "dream", [0.78, 0.21, 1.4]), mv("whip", "just", [0.3, 0.5, 1.15])], overlays=[sweep("just", 0.0, 0.0, 1.0, 0.5)]),
 sc("M74", '''Dream big. Then get specific. Picture what you want. Then picture what's in your way. Then make a plan to get past it.''', None, "hold", host=[["N01"], ["N02", "picture"]],
    diagram={"kind": "woop", "lights": [[["WISH", "OUTCOME"], "want"], [["OBSTACLE"], "way"], [["PLAN"], "plan"]]}),
 sc("M75", '''That's not as magical as the universe handing it to you. But it's a version of manifesting that actually works... and you're the one making it happen.''', "S27", trans="fade",
    ev=[icon("magical", "I51")], moves=[mv("snap", "you're", [0.72, 0.47, 1.4])]),
 sc("M76", '''Which step do you usually skip? Tell me the number in the comments. And if your biggest obstacle is that voice in your head saying everyone's watching, I made a whole video on why that's not true. I'll leave it right here.''', "S29", "hold", moves=[mv("zoom", "which", [0.5, 0.5, 1])],
    ev=[pop("number", "N08", [("WHICH",), ("NUMBER?", Y)], dur=2.2), flash("S28", "voice", "made")], holdEnd=True),
]
for n, sc_ in ((1, P1), (2, P2), (3, P3), (4, P4)):
    os.makedirs("scenes", exist_ok=True)
    json.dump({"part": n, "audio": f"audio/padded/part{n}.wav", "scenes": sc_}, open(f"scenes/part{n}.json", "w"), indent=1)
FOCI = {
 "S01": [[.15, .25, 1.4], [.78, .28, 1.4], [.55, .62, 1.4]], "S02": [[.16, .38, 1.4], [.53, .2, 1.4], [.53, .5, 1.3]], "S03": [[.6, .3, 1.4], [.5, .55, 1.3]], "S04": [[.2, .55, 1.4], [.82, .6, 1.4]],
 "S05": [[.68, .22, 1.4], [.4, .55, 1.4]], "S06": [[.6, .25, 1.4], [.65, .8, 1.4]], "S07": [[.67, .22, 1.4], [.54, .82, 1.4]], "S08": [[.34, .42, 1.4], [.68, .45, 1.4]], "S09": [[.18, .4, 1.3], [.8, .55, 1.3]],
 "S10": [[.3, .68, 1.4], [.64, .3, 1.3]], "S11": [[.78, .21, 1.4], [.3, .5, 1.15]], "S11b": [[.72, .52, 1.4], [.3, .5, 1.15]], "S12": [[.55, .47, 1.4], [.42, .87, 1.4]],
 "S20": [[.46, .4, 1.4], [.78, .4, 1.3]], "S21": [[.76, .5, 1.4]], "S22": [[.78, .62, 1.4]], "S23": [[.85, .86, 1.4], [.45, .58, 1.3]], "S24": [[.5, .15, 1.4], [.39, .8, 1.4]],
 "S25": [[.58, .25, 1.4], [.6, .5, 1.3]], "S26": [[.33, .5, 1.35], [.6, .5, 1.3]], "S27": [[.72, .47, 1.4], [.55, .55, 1.2]], "S28": [[.32, .52, 1.4], [.5, .85, 1.3]],
 "S29": [[.85, .5, 1.3]], "S31": [[.35, .5, 1.3], [.6, .25, 1.2]], "S33": [[.6, .2, 1.4], [.5, .6, 1.2]], "S34": [[.5, .5, 1.2]], "S35": [[.4, .58, 1.3], [.62, .45, 1.3]],
 "S36": [[.3, .5, 1.3], [.78, .45, 1.3]], "S37": [[.5, .22, 1.4], [.68, .7, 1.3]],
}
json.dump(FOCI, open("scenes/foci.json", "w"))
print("specs written", sum(len(x) for x in (P1, P2, P3, P4)), "scenes")
