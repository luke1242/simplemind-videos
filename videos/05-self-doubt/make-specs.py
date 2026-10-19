#!/usr/bin/env python3
"""Video 5 (self-doubt): writes scenes/partN.json (scene specs for tools/build-part.mjs) and scenes/foci.json. Scene list = VIDEO.md."""
import json, os
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
def crop(word, focus, occ=1, dur=2.4): return {"kind": "crop", "focus": focus, "word": word, "occ": occ, "dur": dur}
def title(pill="LESSON", l1="PSYCHOLOGY OF", l2="SELF-DOUBT"): return {"kind": "title", "dur": 2.5, "pill": pill, "l1": l1, "l2": l2}
def iconrow(items): return {"kind": "iconrow", "items": [{"icon": i, "word": w} for i, w in items], "word": items[0][1], "dur": 3.5}
def quote(word, until, text, by): return {"kind": "quote", "word": word, "until": until, "text": text, "by": by}
def mv(kind, word, f=None, occ=1, **kw): return {"kind": kind, "word": word, "occ": occ, "f": f, **kw}
def step(n, text, word, occ=1, **kw): return {"type": "step", "step": n, "text": text, "word": word, "occ": occ, **kw}
def sc(id, narr, picture=None, camera="zoom-in", ev=None, **kw):
    d = {"id": id, "camera": camera, "narration": narr, "events": ev or []}
    if picture: d["picture"] = picture
    d.update(kw); return d
W_ = lambda w, o=1: {"word": w, "occ": o}

FULL = [0.5, 0.5, 1]
def pill(text, word, until=None, dur=3.0, occ=1, **kw): return {"type": "pill", "text": text, "word": word, "occ": occ, "until": until, "dur": dur, **kw}
def sbadge(text, word, dur=2.6, occ=1): return {"type": "sbadge", "text": text, "word": word, "occ": occ, "dur": dur}
def bub(text, word, x, y, w=0.31, h=0.17): return {"type": "bubble", "text": text, "word": word, "box": {"x": x, "y": y, "w": w, "h": h}}
def quad(tiles, **kw): return {"kind": "quad", "tiles": [{"label": l, "icon": i, "word": w_} for l, i, w_ in tiles], **kw}
Q = [("DOING IT", "I52", W_("doing")), ("WATCHING OTHERS", "I06", W_("watching")), ("WHAT PEOPLE SAY", "I41", W_("tell")), ("YOUR BODY", "I75", W_("body"))]
Qpre = [(l, i, None) for l, i, _ in Q]

P1 = [
 sc("D01", "Think about a little kid who just drew a picture. A purple sun. A dog with six legs.", "S01",
    moves=[mv("snap", "picture", [0.64, 0.25, 1.4]), mv("whip", "purple", [0.64, 0.17, 1.4]), mv("whip", "dog", [0.66, 0.33, 1.4])]),
 sc("D02", "Do they wonder if it's good enough? Do they compare it to anyone else's? No. They run straight to you and hold it up as high as they can.", "S01", "zoom-out",
    moves=[mv("cut", "do", [0.64, 0.25, 1.4]), mv("zoom", "run", FULL), mv("snap", "hold", [0.64, 0.22, 1.4])],
    overlays=[{"type": "sweep", "word": "high", "box": {"x": 0.55, "y": 0.04, "w": 0.2, "h": 0.42}}]),
 sc("D03", "Now think about the last time you made something. A drawing. A song. A business idea. A message to someone you like. Did you hold it up? Or did you hide it... until it was perfect... and then never show anyone at all?", "S02",
    moves=[mv("snap", "something", [0.55, 0.35, 1.3]), mv("zoom", "business", FULL), mv("snap", "hide", [0.52, 0.47, 1.4]), mv("zoom", "never", FULL)]),
 sc("D04", "Somewhere between that kid and you, a voice showed up. The one that says, \"You're not ready.\" \"Who do you think you are?\" \"Don't embarrass yourself.\" And here's the part most people never stop to think about.", "S03",
    moves=[mv("snap", "voice", [0.6, 0.5, 1.25]), mv("zoom", "here's", FULL)],
    overlays=[bub("YOU'RE NOT READY", "ready", 0.66, 0.16), bub("WHO DO YOU THINK YOU ARE?", "who", 0.64, 0.38, 0.34, 0.2), bub("DON'T EMBARRASS YOURSELF", "embarrass", 0.64, 0.62, 0.34, 0.2)]),
 sc("D05", "You weren't born with that voice. You learned it.", "S04",
    ev=[card("learned", [("YOU",), P("LEARNED", Y), ("IT",)], dur=1.9), title()],
    moves=[mv("snap", "born", [0.38, 0.8, 1.4])], fx=[{"type": "riser", "word": "you"}, {"type": "impact", "word": "learned"}]),
 sc("D06", "I know that voice really well. When I started this channel, I wrote my first script three times. I recorded it, listened back, and deleted it. Twice.", "S05",
    ev=[icon("recorded", "I71"), icon("twice", "I72")], moves=[mv("snap", "deleted", [0.43, 0.55, 1.4]), mv("snap", "channel", [0.6, 0.35, 1.3])]),
 sc("D07", "Every time, the voice had a new reason. \"Your voice sounds weird.\" \"Nobody's going to watch this.\" \"Real creators don't make videos like this.\" I almost didn't post anything at all. And if you're watching this, you already know how that turned out.", "S06",
    ev=[pop("watching", "N05", [("YOU KNOW",), P("HOW IT ENDED", Y)], dur=2.6)],
    moves=[mv("snap", "voice", [0.6, 0.4, 1.3]), mv("zoom", "almost", FULL)],
    overlays=[bub("YOUR VOICE SOUNDS WEIRD", "weird", 0.7, 0.08, 0.29, 0.2), bub("NOBODY'S GOING TO WATCH", "nobody's", 0.7, 0.32, 0.29, 0.2), bub("REAL CREATORS DON'T…", "real", 0.7, 0.56, 0.29, 0.2)]),
 sc("D08", "But it made me want to understand where that voice actually comes from. So I went looking at what psychologists have found.", "S20",
    host=[["N06"], ["N01", "so"]], moves=[mv("snap", "psychologists", [0.46, 0.45, 1.4])]),
 sc("D09", "By the end of this video, you'll know the four places self-doubt really comes from, why \"just believe in yourself\" almost never works, and five ways to rebuild your confidence that are actually backed by research.", None, "hold",
    host=[["N01"]], diagram={"kind": "irow", "items": [{"icon": "I74", "label": "4 SOURCES", "word": W_("four")}, {"icon": "I72", "label": "WHY \"BELIEVE\" FAILS", "word": W_("believe")}, {"icon": "I67", "label": "5 FIXES", "word": W_("five")}]}),
 sc("D10", "One of them takes about two seconds, and you can use it before anything that scares you.", "I11", "hold",
    host=[["N01"]], overlays=[sbadge("2 SECONDS", "two", dur=3.0)]),
]
P2 = [
 sc("D11", "In the nineteen-seventies, a psychologist named Albert Bandura became obsessed with one question. Why do some people keep going when things get hard, while others give up before they even start?", "S20",
    host=[["N01"], ["N06", "why"]], trans="push", moves=[mv("snap", "why", [0.46, 0.45, 1.4])], overlays=[pill("ALBERT BANDURA", "bandura", dur=3.0)]),
 sc("D12", "It wasn't talent. It wasn't intelligence. It was what he called self-efficacy. Your belief that you can actually do the thing in front of you.", None, "hold",
    host=[["N01"], ["N02", "it", 3]], swap={"word": "self"},
    diagram={"kind": "card", "parts": [P("TALENT", R, at=W_("talent")), P("INTELLIGENCE", R, at=W_("intelligence"))]},
    diagramB={"kind": "card", "parts": [P("SELF-EFFICACY", mk=True, sz="mid"), P("believing you can do it", small=True)]}),
 sc("D13", "And Bandura found something surprising. That belief doesn't come from nowhere. And it doesn't come from repeating \"I can do it\" in the mirror.", "S26",
    moves=[mv("snap", "belief", [0.62, 0.45, 1.25]), mv("snap", "mirror", [0.3, 0.55, 1.4])]),
 sc("D14", "It comes from evidence. Your brain is constantly collecting proof about what you can and can't do. And self-doubt is what happens when your brain has collected the wrong proof.", None, "hold",
    host=[["N02"]], swap={"word": "wrong"},
    diagram={"kind": "card", "parts": [P("IT COMES FROM", sz="mid"), P("EVIDENCE", mk=True)]},
    diagramB={"kind": "card", "parts": [P("SELF-DOUBT =", sz="mid"), P("WRONG PROOF", R, slam=True)]}),
 sc("D15", "He found four main places that belief comes from. Doing something yourself. Watching someone like you do it. What other people tell you. And how your body feels when you try. Keep those four in mind, because they're going to come back.", None, "hold",
    host=[["N01"], ["N06", "keep"]], diagram=quad(Q, pulse=W_("mind"))),
 sc("D16", "One of his most famous experiments involved people with a serious fear of snakes. Not a little nervous. Some of them couldn't even stand near one in a glass tank.", "S07",
    ev=[icon("snakes", "I73")], host=[["N01"], ["N05", "not"]], moves=[mv("snap", "nervous", [0.17, 0.55, 1.4]), mv("whip", "tank", [0.42, 0.6, 1.4])]),
 sc("D17", "Bandura didn't tell them to be brave, and he didn't try to talk them out of it. Instead, they watched someone else handle a snake calmly. Then, step by step, they did tiny pieces themselves. Look at the snake. Stand a little closer. Touch it with a glove. Then without one.", "S07",
    host=[["N01"]], moves=[mv("snap", "watched", [0.6, 0.45, 1.4]), mv("whip", "step", [0.17, 0.55, 1.4]), mv("zoom", "stand", FULL)],
    overlays=[pill("LOOK", "look", until="closer"), pill("CLOSER", "closer", until="glove"), pill("GLOVE", "glove", until="without"), pill("NO GLOVE", "without", dur=2.2)]),
 sc("D18", "By the end, ninety-two percent of the people in that group could sit with a snake resting in their lap.", None, "hold",
    host=[["N02"]], pictureB="S07b", swap={"word": "lap"},
    diagram={"kind": "pie", "pct": 92, "from": 0, "label": "SNAKE IN THEIR LAP:", "fs": 84, "badge": "yellow", "value": "92%", "small": "Bandura, Blanchard & Ritter, 1969", "at": {"fill": W_("ninety")}},
    fx=[{"type": "riser", "word": "ninety"}, {"type": "impact", "word": "ninety", "off": 0.0}]),
 sc("D19", "They didn't feel brave first. They became brave by collecting small proof that they could handle it. And a lot of them reported feeling less afraid of other things in their lives too. Proof in one area spilled into others.", "S07b",
    ev=[card("first", [P("THEY DIDN'T FEEL", sz="mid"), P("BRAVE FIRST", Y)])], host=[["N06"], ["N01", "and"], ["N06", "proof", 2]],
    moves=[mv("snap", "brave", [0.2, 0.42, 1.4], occ=2), mv("zoom", "and", FULL)]),
 sc("D20", "That's the key to this whole video. Confidence isn't a feeling you wait for. It's a conclusion your brain reaches after enough evidence.", None, "hold",
    host=[["N02"], ["N06", "confidence"], ["N01", "it's"]], swap={"word": "conclusion"},
    diagram={"kind": "card", "parts": [P("CONFIDENCE ISN'T", sz="mid"), P("A FEELING", R)]},
    diagramB={"kind": "card", "sweep": True, "parts": [P("IT'S A"), P("CONCLUSION", Y)]}),
 sc("D21", "So if self-belief is built from evidence... where does all the evidence for self-doubt come from?", "S06",
    moves=[mv("snap", "doubt", [0.62, 0.28, 1.4])]),
]
P3 = [
 sc("D22", "Bandura and the researchers who followed him point to a few main sources. Here are the four that show up the most.", "S20", "zoom-out",
    host=[["N01"]]),
 sc("D23", "One. You don't have proof yet. This is the most common one, and the most fixable. If you've never done something, your brain has no evidence that you can. So it fills the gap with doubt.", "S08",
    moves=[mv("snap", "never", [0.25, 0.5, 1.3]), mv("snap", "gap", [0.78, 0.42, 1.4])], overlays=[step("SOURCE 1", "NO PROOF YET", "one", dur=3.6)]),
 sc("D24", "The first time you drive, give a speech, or walk into a gym, your brain is basically guessing. And when it guesses, it guesses low, to keep you safe.", None, "hold",
    host=[["N01"]], diagram={"kind": "irow", "items": [{"icon": "I77", "word": W_("drive")}, {"icon": "I71", "word": W_("speech")}, {"icon": "I78", "word": W_("gym")}],
                             "under": {"html": 'YOUR BRAIN IS <span class="badge yellow">GUESSING</span>', "word": W_("guesses")}}),
 sc("D25", "That doesn't mean you can't do it. It means you haven't shown yourself yet. Your brain isn't saying \"you're bad at this.\" It's saying \"I have no idea.\"", None, "hold",
    host=[["N06"], ["N05", "your"]], swap={"word": "idea"},
    diagram={"kind": "card", "parts": [P("NOT"), P("\"YOU'RE BAD AT THIS\"", R, sz="mid")]},
    diagramB={"kind": "card", "sweep": True, "parts": [P("\"I HAVE NO IDEA\"", Y, sz="mid")]}),
 sc("D26", "Two. You compare your inside to everyone else's outside.", "S09", "zoom-out",
    moves=[mv("snap", "outside", [0.5, 0.3, 1.3])], overlays=[step("SOURCE 2", "UNFAIR COMPARISON", "two", dur=3.4)]),
 sc("D27", "Back in the nineteen-fifties, a psychologist named Leon Festinger pointed out that we figure out how good we are by comparing ourselves to other people.", "S20",
    host=[["N01"]], trans="push", moves=[mv("snap", "festinger", [0.46, 0.45, 1.4])], overlays=[pill("LEON FESTINGER", "festinger", dur=3.0)]),
 sc("D28", "The problem is, today you're comparing yourself to millions of people... and only seeing their best moments. You see their finished painting, not the hundred bad ones before it. You see the gym photo, not the year of showing up tired. So your messy middle always looks worse than their highlight reel.", "S09", "pan-right",
    ev=[card("messy", [("YOUR MIDDLE VS",), P("THEIR HIGHLIGHTS", Y, sz="mid")])],
    moves=[mv("snap", "painting", [0.4, 0.35, 1.4]), mv("whip", "gym", [0.2, 0.4, 1.4]), mv("snap", "tired", [0.3, 0.85, 1.4])],
    overlays=[sbadge("MILLIONS OF PEOPLE", "millions", dur=2.6)]),
 sc("D29", "Three. The critical voice is louder than the kind one.", "S10",
    moves=[mv("snap", "louder", [0.66, 0.78, 1.4])], overlays=[step("SOURCE 3", "THE LOUDER VOICE", "three", dur=3.4)]),
 sc("D30", "In two thousand one, a group of researchers led by Roy Baumeister reviewed hundreds of studies and came to a simple conclusion. Bad is stronger than good.", "S20",
    host=[["N02"]], ev=[card("stronger", [("BAD IS",), P("STRONGER", Y), ("THAN GOOD",)], dur=2.0)], overlays=[pill("ROY BAUMEISTER, 2001", "baumeister", dur=3.0)]),
 sc("D31", "One harsh comment sticks with you longer than ten compliments.", "S10",
    moves=[mv("snap", "harsh", [0.66, 0.78, 1.4]), mv("whip", "ten", [0.3, 0.53, 1.4])]),
 sc("D32", "In another study, researchers at Harvard collected almost twelve thousand daily diary entries from people at work. A setback hit people's mood about two to three times harder than a step forward helped it.", None, "hold",
    host=[["N01"], ["N02", "a"]],
    diagram={"kind": "bars2", "bars": ["SETBACK", "STEP FORWARD"], "small": "Amabile & Kramer, Harvard", "at": {"count": W_("twelve"), "grow": W_("setback"), "badge": W_("two")}},
    fx=[{"type": "impact", "word": "two"}]),
 sc("D33", "So if someone once told you that you weren't good at something, that one moment might still be louder than everything good anyone's said since.", "S06",
    moves=[mv("snap", "someone", [0.62, 0.3, 1.3]), mv("snap", "louder", [0.62, 0.28, 1.4])]),
 sc("D34", "Four. You misread your own body. Before something big, your heart beats faster. Your hands shake a little. Your stomach drops.", "S11",
    ev=[icon("stomach", "I75")], moves=[mv("snap", "heart", [0.53, 0.43, 1.4]), mv("whip", "hands", [0.52, 0.5, 1.4])], overlays=[step("SOURCE 4", "MISREAD NERVES", "four", dur=3.4)]),
 sc("D35", "And your brain takes that feeling as a message: \"See? You can't handle this.\" Bandura listed this as one of the main sources of self-doubt. People treat normal nerves as proof that they're not ready.", None, "hold",
    host=[["N06"], ["N02", "bandura"]], ev=[pop("see", "N06", [("SEE?",), P("YOU CAN'T", Y)], dur=2.4)],
    diagram=quad(Qpre, active={"idx": 3, "word": W_("bandura")})),
 sc("D36", "So put those four together. No proof yet. Unfair comparisons. A louder critical voice. And misread nerves. That's not the truth about who you are. That's just a lot of bad evidence.", None, "hold",
    host=[["N02"], ["N06", "that's"]],
    diagram={"kind": "list", "items": [{"t": "NO PROOF YET", "word": W_("proof")}, {"t": "UNFAIR COMPARISONS", "word": W_("unfair")}, {"t": "A LOUDER VOICE", "word": W_("louder")}, {"t": "MISREAD NERVES", "word": W_("misread")}],
             "stamp": {"text": "BAD EVIDENCE", "word": W_("bad")}}),
 sc("D37", "And that's why \"just believe in yourself\" almost never works. You can't argue your brain out of something it thinks it has evidence for. But you can give it new evidence.", "S26", "zoom-out",
    ev=[card("new", [("GIVE IT",), P("NEW EVIDENCE", Y)])], moves=[mv("snap", "believe", [0.3, 0.55, 1.4]), mv("zoom", "argue", FULL)]),
]
P4 = [
 sc("D38", "So here's how I actually do that now. Five steps. One. Collect tiny proof. Remember the snake study. Nobody went from terrified to holding a snake in one jump.", "S24",
    moves=[mv("snap", "nobody", [0.5, 0.8, 1.4]), mv("zoom", "terrified", FULL)], overlays=[step("STEP 1", "COLLECT TINY PROOF", "one", dur=3.4)]),
 sc("D39", "Pick something you doubt you can do, and break it into a step so small it's almost embarrassing. Then do that step. Then the next one. Every small step is one more piece of evidence for your brain.", "S24",
    ev=[card("embarrassing", [("ALMOST",), P("EMBARRASSING", Y)]), icon("evidence", "I52")], moves=[mv("snap", "pick", [0.45, 0.85, 1.35]), mv("whip", "next", [0.5, 0.2, 1.4])]),
 sc("D40", "For this channel, my first step wasn't \"make a great video.\" It was \"record one minute and don't delete it.\"", "S05",
    moves=[mv("snap", "great", [0.6, 0.3, 1.3]), mv("snap", "record", [0.43, 0.45, 1.4])], overlays=[sbadge("1 MINUTE. DON'T DELETE.", "record", dur=3.0)]),
 sc("D41", "In that diary study, the days people felt best weren't the days they did something huge. They were the days they made a little progress.", None, "hold",
    host=[["N05"]], swap={"word": "little"},
    diagram={"kind": "card", "parts": [P("BEST DAYS ≠", sz="mid"), P("HUGE WINS", R)]},
    diagramB={"kind": "card", "sweep": True, "parts": [P("BEST DAYS =", sz="mid"), P("A LITTLE PROGRESS", Y, sz="mid")]}),
 sc("D42", "Two. Watch someone like you do it. Not the most famous person in the world. Someone a few steps ahead of you. Someone who started where you are.", "S12",
    moves=[mv("snap", "ahead", [0.63, 0.35, 1.4]), mv("whip", "started", [0.35, 0.5, 1.4])], overlays=[step("STEP 2", "WATCH SOMEONE LIKE YOU", "two", dur=3.4)]),
 sc("D43", "Bandura found that seeing someone similar succeed is one of the strongest ways to build belief. Because your brain thinks, \"If they can, maybe I can.\"", None, "hold",
    host=[["N06"]], ev=[card("if", [("IF THEY CAN,",), P("MAYBE I CAN", Y)], dur=2.2)],
    diagram=quad(Qpre, active={"idx": 1, "word": W_("seeing")})),
 sc("D44", "Three. Talk to yourself by name. Psychologist Ethan Kross found that when people talked to themselves using their own name or \"you,\" instead of \"I,\" they felt less anxious and actually performed better under pressure.", "S26",
    moves=[mv("snap", "kross", [0.62, 0.45, 1.25]), mv("snap", "own", [0.3, 0.55, 1.4]), mv("zoom", "anxious", FULL)],
    overlays=[step("STEP 3", "TALK TO YOURSELF BY NAME", "three", dur=3.0), pill("ETHAN KROSS", "kross", dur=2.8)]),
 sc("D45", "So instead of \"I can't do this,\" try \"Luke, you've done hard things before. You can do this too.\" It sounds a little strange. But it gives you a bit of distance from the panic, like advice from a friend.", None, "hold",
    host=[["N01"], ["N05", "it"]], swap={"word": "luke"}, ev=[pop("strange", "N05", [("LIKE A",), P("FRIEND", Y)], dur=2.4)],
    diagram={"kind": "card", "parts": [P("\"I CAN'T DO THIS\"", R, sz="mid")]},
    diagramB={"kind": "card", "parts": [P("\"LUKE,"), P("YOU CAN DO THIS\"", mk=True, sz="mid")]}),
 sc("D46", "Four. Rename the nerves. This is the two-second one. Before something scary, say out loud, \"I'm excited.\"", "S13",
    ev=[icon("two", "I11")], moves=[mv("snap", "scary", [0.54, 0.3, 1.3]), mv("snap", "excited", [0.54, 0.25, 1.4])], overlays=[step("STEP 4", "RENAME THE NERVES", "four", dur=3.2)]),
 sc("D47", "A Harvard researcher named Alison Wood Brooks had people do stressful things like singing in front of others and giving a speech. The people who said \"I'm excited\" first did better than the people who tried to calm down.", "S28",
    ev=[card("better", [("\"I'M EXCITED\"",), P("WINS", Y)])], moves=[mv("snap", "singing", [0.32, 0.45, 1.4]), mv("zoom", "giving", FULL)], overlays=[pill("ALISON WOOD BROOKS", "brooks", dur=3.0)]),
 sc("D48", "Because nerves and excitement feel almost the same in your body. You're just choosing which story your brain tells about it.", None, "hold",
    host=[["N06"]], diagram={"kind": "split", "left": ["", "NERVES"], "right": ["", "EXCITEMENT"], "norack": True, "fs": 100, "at": {"left": W_("nerves"), "right": W_("excitement"), "sign": W_("same")}}),
 sc("D49", "Five. Keep a proof list. Get a note on your phone, and every time you do something you doubted you could do, write it down. Even small things. You spoke up in class. You finished the workout. You posted the video.", "S14",
    moves=[mv("snap", "note", [0.5, 0.48, 1.4]), mv("zoom", "even", FULL)],
    overlays=[step("STEP 5", "KEEP A PROOF LIST", "five", dur=3.2), pill("SPOKE UP ✓", "spoke", until="finished"), pill("FINISHED THE WORKOUT ✓", "finished", until="posted"), pill("POSTED THE VIDEO ✓", "posted", dur=2.4)]),
 sc("D50", "Then, the next time the voice says \"you can't,\" you open the list. It's a lot harder for your brain to argue with a receipt.", "I76", "hold",
    host=[["N01"], ["N05", "it's"]], unroll={"word": "list", "from": 62}, overlays=[sbadge("ARGUE WITH A RECEIPT", "receipt", dur=2.6)]),
 sc("D51", "Here's what I keep coming back to. That little kid with the drawing didn't have more talent than you. They just didn't have any bad evidence yet. Nobody had told them it wasn't good enough. They hadn't compared it to anyone. They hadn't learned to read their nerves as a warning.", "S01",
    trans="fade", moves=[mv("snap", "drawing", [0.64, 0.25, 1.4]), mv("zoom", "nobody", FULL), mv("snap", "compared", [0.5, 0.5, 1.3]), mv("zoom", "learned", FULL)], fx=[{"type": "leak", "word": "kid"}]),
 sc("D52", "Every confident person you've ever met was once a beginner with no proof at all.", "S12", "zoom-out", trans="fade"),
 sc("D53", "And the good news is, if self-doubt was learned... it can be unlearned. Not by pretending. By collecting new proof, one small step at a time. So find one thing you've been hiding until it's perfect. And show someone. Hold it up, like you used to.", "S15",
    trans="iris", irisAt=[0.5, 0.35], moves=[mv("snap", "pretending", [0.5, 0.45, 1.3]), mv("zoom", "collecting", FULL), mv("snap", "hiding", [0.5, 0.4, 1.3]), mv("zoom", "show", FULL), mv("snap", "hold", [0.62, 0.25, 1.4])],
    overlays=[{"type": "sweep", "word": "hold", "box": {"x": 0.55, "y": 0.04, "w": 0.2, "h": 0.42}}]),
 sc("D54", "What's one thing you doubted you could do, that you ended up doing anyway? Tell me in the comments. It might be exactly the proof someone else needs. And if your doubt is really about what other people will think, I made a whole video on why they're barely watching. I'll leave it right here.", "S29", "hold",
    ev=[pop("doubted", "N06", [P("YOUR PROOF?", Y)], dur=2.2)], holdEnd=True),
]
for n, sc_ in ((1, P1), (2, P2), (3, P3), (4, P4)):
    os.makedirs("scenes", exist_ok=True)
    json.dump({"part": n, "audio": f"audio/padded/part{n}.wav", "scenes": sc_}, open(f"scenes/part{n}.json", "w"), indent=1)
FOCI = {
 "S01": [[.64, .25, 1.4], [.5, .5, 1.3]], "S02": [[.5, .4, 1.35]], "S03": [[.62, .5, 1.3], [.5, .55, 1.3]], "S04": [[.38, .8, 1.4], [.62, .5, 1.3]],
 "S05": [[.6, .3, 1.3], [.43, .5, 1.4]], "S06": [[.62, .3, 1.4], [.4, .55, 1.3]], "S07": [[.17, .55, 1.4], [.42, .6, 1.4], [.6, .45, 1.4]], "S07b": [[.2, .45, 1.4], [.8, .55, 1.3]],
 "S08": [[.25, .5, 1.3], [.78, .42, 1.4]], "S09": [[.2, .4, 1.4], [.4, .35, 1.4], [.55, .65, 1.3]], "S10": [[.66, .78, 1.4], [.3, .53, 1.4]], "S11": [[.53, .43, 1.4], [.52, .5, 1.4]],
 "S12": [[.63, .35, 1.4], [.35, .5, 1.4]], "S13": [[.54, .3, 1.4]], "S14": [[.5, .48, 1.4], [.56, .3, 1.3]], "S15": [[.62, .25, 1.4], [.5, .5, 1.3]],
 "S20": [[.46, .45, 1.4], [.78, .45, 1.3]], "S24": [[.5, .8, 1.4], [.5, .25, 1.3]], "S26": [[.3, .55, 1.4], [.62, .45, 1.25]], "S28": [[.32, .45, 1.4]], "S29": [[.7, .5, 1.2]],
}
json.dump(FOCI, open("scenes/foci.json", "w"))
print("specs written", sum(len(x) for x in (P1, P2, P3, P4)), "scenes")
