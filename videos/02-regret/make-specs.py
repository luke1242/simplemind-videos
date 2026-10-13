#!/usr/bin/env python3
"""Video 2 (regret): writes scenes/partN.json (scene specs for tools/build-part.mjs) and scenes/foci.json. Scene list = VIDEO.md."""
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
def title(): return {"kind": "title", "dur": 2.5}
def iconrow(items): return {"kind": "iconrow", "items": [{"icon": i, "word": w} for i, w in items], "word": items[0][1], "dur": 3.5}
def quote(word, until, text, by): return {"kind": "quote", "word": word, "until": until, "text": text, "by": by}
def mv(kind, word, f=None, occ=1, **kw): return {"kind": kind, "word": word, "occ": occ, "f": f, **kw}
def step(n, text, word, occ=1, **kw): return {"type": "step", "step": n, "text": text, "word": word, "occ": occ, **kw}
def sc(id, narr, picture=None, camera="zoom-in", ev=None, **kw):
    d = {"id": id, "camera": camera, "narration": narr, "events": ev or []}
    if picture: d["picture"] = picture
    d.update(kw); return d
W_ = lambda w, o=1: {"word": w, "occ": o}

P1 = [
 sc("R01", "Most people think the choice they'll regret is the risky one. Saying the wrong thing. Trying and failing. Looking stupid in front of everyone.", "S59",
    ev=[card("risky", [("THE",), ("RISKY", Y), ("ONE?",)], dur=1.8)],
    moves=[mv("snap", "trying", [0.45, 0.2, 1.4])], fx=[{"type": "impact", "word": "stupid"}]),
 sc("R02", "But when researchers actually asked people about their biggest regrets... that's not what they found.", "S03",
    ev=[pop("not", "N09", [("THAT'S",), ("NOT", R), ("IT",)], dur=2.4)], host=[["N02"]], trans="whip"),
 sc("R03", "They asked college students. Office workers. Retired professors. People living in nursing homes, looking back on almost their whole lives. One simple question.", "S02", "pan-right",
    host=[["N06"]], bleed="#FDEACD", moves=[mv("snap", "college", [0.2, 0.42, 1.4]), mv("whip", "office", [0.39, 0.42, 1.4]), mv("whip", "retired", [0.62, 0.42, 1.4]), mv("whip", "nursing", [0.83, 0.42, 1.4]), mv("zoom", "one", [0.5, 0.5, 1])]),
 sc("R04", "What's the biggest regret of your life? And most people's biggest regrets... weren't about the things they did. They were about the things they didn't do.", "S01",
    ev=[icon("what's", "I17"), card("didn't", [("WHAT THEY",), ("DIDN'T", R), ("DO",)])], host=[["N06"], ["N02", "and"], ["N06", "they", 2]]),
 sc("R05", "The class they never took. The person they never talked to. The trip they kept putting off. The thing they always wanted to try... but never did, because it felt too risky, too embarrassing, or like it just wasn't the right time.", "S04",
    ev=[card("right", [("NOT THE",), ("RIGHT TIME", Y)])], host=[["N06"]],
    moves=[mv("snap", "class", [0.17, 0.17, 1.4]), mv("whip", "person", [0.38, 0.17, 1.4]), mv("whip", "trip", [0.57, 0.17, 1.4]), mv("whip", "thing", [0.74, 0.17, 1.4]), mv("zoom", "because", [0.5, 0.5, 1])]),
 sc("R06", "When I first read that, it hit me pretty hard. Because I had a whole list of those.", "S05",
    ev=[pop("whole", "N10", [("A WHOLE",), ("LIST", Y)], dur=2.6)]),
 sc("R07", "There was a tryout I talked myself out of. I had the date written down. I even bought the shoes.", "S06",
    ev=[icon("shoes", "I49")], host=[["N01"]]),
 sc("R08", "And the morning of, I just sat on the edge of my bed... and didn't go. I told myself I wasn't good enough yet. That I'd try next year. Next year, I didn't go either.", "S58",
    ev=[card("either", [("NEXT YEAR:",), ("DIDN'T GO", R)])],
    moves=[mv("slow", "sat", [0.5, 0.5, 1.08], dur=2.0), mv("cut", "next", [0.86, 0.86, 1.4])]),
 sc("R09", "There was a message I typed out three times... and deleted three times.", "S07",
    ev=[card("deleted", [("DELETED", R), ("3 TIMES",)])]),
 sc("R10", "There was a question I didn't ask in class, and then heard someone else ask five minutes later. And the teacher said, \"Great question.\"", "S08",
    ev=[icon("question", "I17"), pop("great", "N10", [("GREAT",), ("QUESTION.", Y)], dur=2.6)]),
 sc("R11", "Every time, my brain had a really good reason. \"You'll look dumb.\" \"It's not worth it.\" \"Maybe next time.\" And every time, it felt like the safe choice.", "S09",
    ev=[card("safe", [("THE",), ("SAFE", Y), ("CHOICE",)])],
    overlays=[{"type": "bubble", "text": "YOU'LL LOOK DUMB", "word": "dumb", "box": {"x": 0.05, "y": 0.06, "w": 0.36, "h": 0.17}},
              {"type": "bubble", "text": "NOT WORTH IT", "word": "worth", "box": {"x": 0.03, "y": 0.30, "w": 0.30, "h": 0.15}},
              {"type": "bubble", "text": "MAYBE NEXT TIME", "word": "next", "box": {"x": 0.09, "y": 0.52, "w": 0.34, "h": 0.15}}]),
 sc("R12", "But here's what the research shows. The safe choice isn't always safe. It just sends you the bill later.", "S10",
    ev=[pop("safe", "N02", [("ISN'T ALWAYS",), ("SAFE", R)], occ=2, dur=2.4)], moves=[mv("whip", "bill", [0.82, 0.82, 1.4])], trans="whip"),
 sc("R13", "By the end of this video, you'll know exactly what those researchers found, why the things we don't do stay with us so much longer than our mistakes, and the five steps I now use whenever I'm about to talk myself out of something. The first one takes about ten seconds. And it's changed a lot of my decisions.", "S04", "zoom-out",
    ev=[pop("found", "N08", [("WHAT THEY",), ("FOUND", Y)], dur=2.4), icon("longer", "I43"), pop("five", "N07", [("5", Y), ("STEPS",)], dur=2.4), icon("ten", "I11"), title()], host=[["N01"]]),
]
P2 = [
 sc("R14", "In the mid nineteen-nineties, two psychologists, Thomas Gilovich and Victoria Medvec, started studying regret.", "S12", "pan-right",
    ev=[icon("psychologists", "I16")], host=[["N01"]], trans="fade",
    overlays=[{"type": "circle", "cx": 0.42, "cy": 0.3, "rx": 0.2, "ry": 0.2, "label": "Cornell", "lx": 0.26, "ly": 0.52, "word": "psychologists"},
              {"type": "label", "text": "Cornell University, 1994", "word": "nineties"}], fx=[{"type": "leak", "word": "nineties"}]),
 sc("R15", "If those names sound familiar, they're two of the same researchers behind the embarrassing T-shirt study from my last video. They spent a lot of their careers figuring out how our brains trick us.", "S13",
    ev=[icon("shirt", "I08"), pop("trick", "N05", [("HOW OUR BRAINS",), ("TRICK US", Y)], dur=2.6)], host=[["N05"]]),
 sc("R16", "First, they kept it simple. They asked sixty adults one question.", None, "hold", host=[["N06"]],
    diagram={"kind": "grid", "draw": True, "label": "", "count": {"to": 60, "suffix": "", "text": "ADULTS", "badge": "yellow"}, "at": {"count": W_("sixty")}}),
 sc("R17", "When you look back on your life, what do you regret more? The things you did, and wish you hadn't? Or the things you didn't do, and wish you had?", "S15",
    moves=[mv("snap", "did", [0.375, 0.2, 1.4]), mv("whip", "didn't", [0.4, 0.38, 1.4]), mv("zoom", "wish", [0.5, 0.5, 1], occ=2)],
    overlays=[{"type": "sign", "text": "THINGS<br>I DID", "word": "did", "box": {"x": 0.305, "y": 0.125, "w": 0.18, "h": 0.14}, "rot": 3, "fs": 46},
              {"type": "sign", "text": "THINGS I<br>DIDN'T DO", "word": "didn't", "box": {"x": 0.305, "y": 0.32, "w": 0.16, "h": 0.14}, "rot": -2, "fs": 42}]),
 sc("R18", "Seventy-five percent said the things they didn't do.", None, "hold", host=[["N02"]], lead=0.8,
    diagram={"kind": "grid", "fill": 45, "label": "", "count": {"to": 75, "suffix": "%", "text": "DIDN'T DO", "badge": "red"}, "at": {"red": W_("seventy"), "count": W_("seventy")}},
    fx=[{"type": "riser", "word": "seventy"}, {"type": "impact", "word": "seventy"}]),
 sc("R19", "Then they went deeper. They interviewed seventy-seven people, from college students, to retired professors, to people in nursing homes, and asked them to list their biggest regrets.", "S02", "pan-left",
    ev=[card("seventy", [("77", Y), ("PEOPLE",)])], host=[["N01"]], bleed="#FDEACD",
    moves=[mv("snap", "college", [0.2, 0.42, 1.4]), mv("whip", "professors", [0.62, 0.42, 1.4]), mv("whip", "nursing", [0.83, 0.42, 1.4]), mv("zoom", "asked", [0.5, 0.5, 1])]),
 sc("R20", "Over two hundred regrets in total.", "S03", host=[["N06"]],
    overlays=[{"type": "wheel", "value": "213", "word": "two", "box": {"x": 0.04, "y": 0.05, "w": 0.3, "h": 0.25}}]),
 sc("R21", "And the regrets about not acting outnumbered the regrets about acting... almost two to one.", None, "hold", host=[["N02"]],
    diagram={"kind": "bars", "bars": [{"label": "DIDN'T ACT", "pct": 63}, {"label": "ACTED", "pct": 37}],
             "badge": [{"t": "ALMOST"}, {"t": "2 TO 1", "b": "yellow"}], "at": {"grow": W_("outnumbered"), "badge": W_("two")}}),
 sc("R22", "And here's a detail I didn't expect. Out of all those regrets, only about ten were about things outside their control. Bad luck. Things that just happened to them. Almost everything else... was a choice. Their own.", None, "hold",
    ev=[pop("detail", "N09", [("I DIDN'T",), ("EXPECT THIS", Y)], dur=2.4)], host=[["N06"], ["N02", "almost"]],
    diagram={"kind": "card", "parts": [P("ONLY"), P("10", Y, circ=True, after=" OF 213"), P("were bad luck", small=True)]},
    diagramB={"kind": "card", "parts": [P("ALMOST ALL:"), P("A CHOICE", R)]}, swap={"word": "choice"}),
 sc("R23", "But here's where it gets really interesting. They also asked people to think about two different time frames. First: what's your biggest regret from just this past week? For that one, it was basically a coin flip. About half the people picked something they did. A dumb comment. A bad decision. Something they'd messed up.", "S20",
    ev=[pop("two", "N02", [("TWO", Y), ("TIME FRAMES",)], dur=2.4), icon("week", "I13"), icon("coin", "I42"), card("half", [("ABOUT",), ("HALF", Y)])], trans="whip"),
 sc("R24", "Then they asked: what's the biggest regret of your whole life?", "S04", host=[["N06"]]),
 sc("R25", "Eighty-four percent... picked something they didn't do.", None, "hold", host=[["N02"]], lead=0.8,
    diagram={"kind": "pie", "pct": 84, "from": 0, "label": "WHOLE LIFE:", "badge": "red", "value": "84%", "at": {"fill": W_("eighty")}},
    fx=[{"type": "riser", "word": "eighty"}, {"type": "impact", "word": "eighty", "off": 0.0}]),
 sc("R26", "So in the short term, our mistakes hurt more. That part is real. If you say something awkward today, you'll probably feel it tonight.", "S23",
    ev=[card("short", [("SHORT TERM:",), ("MISTAKES", R), ("HURT",)]), icon("tonight", "I14")], trans="fade"),
 sc("R27", "But over the years, that flips. The mistakes fade. And the missed chances... grow.", None, "hold", host=[["N02"], ["N06", "the", 2]],
    diagram={"kind": "lines", "sweep": True, "at": {"draw": W_("flips"), "fade": W_("fade"), "grow": W_("grow")}}),
 sc("R28", "They even tested this with a little story. Two college students, both unhappy at their school.", "S25", host=[["N01"]]),
 sc("R29", "One of them transfers to a new school. The other one stays. And it turns out, both of them made the wrong choice.", "S26", "pan-right",
    ev=[card("both", [("BOTH", Y), ("CHOICES WERE",), ("WRONG", R)])], host=[["N01"]], moves=[mv("whip", "transfers", [0.7, 0.5, 1.4])]),
 sc("R30", "So who feels worse? Right after the decision, most people said the one who transferred. Seventy-six percent. He took the risk, and it didn't work out.", "S26",
    ev=[pop("who", "N06", [("WHO FEELS",), ("WORSE?", Y)], dur=2.4), crop("transferred", [0.7, 0.5, 1.4], dur=2.4)], host=[["N06"]],
    overlays=[{"type": "badge", "badge": "yellow", "text": "0%", "count": 76, "word": "seventy", "box": {"x": 0.62, "y": 0.14, "w": 0.2, "h": 0.13}, "fs": 96},
              {"type": "arrow", "x0": 0.72, "y0": 0.29, "x1": 0.7, "y1": 0.37, "word": "seventy"}]),
 sc("R31", "But years later? Most people said the one who stayed. The one who never found out.", "S28", host=[["N06"]], trans="push",
    overlays=[{"type": "pill", "text": "YEARS LATER", "word": "years"}], fx=[{"type": "leak", "word": "years"}]),
]
P3 = [
 sc("R32", "So why does this happen? Why do the things we don't do follow us around for so much longer? The researchers pointed to a few reasons. And once you see them, it's hard to unsee them.", "S09", "zoom-out",
    ev=[pop("why", "N06", [("WHY?", Y)], dur=2.0), pop("few", "N08", [("4", Y), ("REASONS",)], dur=2.4)]),
 sc("R33", "One. When you make a mistake, you do something about it. You apologize. You fix it. You laugh about it later. Or you find the silver lining. \"Well, at least I learned something.\" Your brain does a lot of quiet repair work on the things you did.", "S30",
    ev=[icon("fix", "I44"), icon("learned", "I09"), crop("repair", [0.5, 0.5, 1.35])], overlays=[step("REASON 1", "YOU REPAIR MISTAKES", "one")]),
 sc("R34", "But there's nothing to repair when nothing happened. So it just... sits there.", "I45", host=[["N06"]]),
 sc("R35", "Two. A mistake has an ending. A missed chance doesn't. If you try something and it goes badly, you know exactly how bad it was. The story is over.", "I46",
    ev=[pop("badly", "N01", [("THE STORY IS",), ("OVER", Y)], dur=2.4)], host=[["N08"], ["N01", "if"]], overlays=[step("REASON 2", "A MISTAKE HAS AN ENDING", "two")]),
 sc("R36", "But if you never try, the story stays open. And your imagination keeps writing new endings. Maybe it would have worked. Maybe it would have changed everything.", "S33",
    moves=[mv("snap", "imagination", [0.58, 0.3, 1.4]), mv("whip", "maybe", [0.75, 0.22, 1.4]), mv("whip", "changed", [0.6, 0.3, 1.4])]),
 sc("R37", "You'll never know. And \"I'll never know\" is a heavy thing to carry.", "S34", ev=[card("never", [("YOU'LL",), ("NEVER", R), ("KNOW",)], dur=1.8)]),
 sc("R38", "Three. Over time, you forget why you were scared. In the moment, the fear feels huge. Like the most important thing in the room. But ten years later, you can barely remember it. You remember the reasons you had to go. You just can't remember the reasons you had to stay. And from far away, the thing that stopped you looks... kind of small.", "S35",
    pictureB="S35b", swap={"word": "small", "kind": "iris", "pt": [0.45, 0.8]}, ev=[card("huge", [("THE FEAR FEELS",), ("HUGE", Y)]), icon("ten", "I43")],
    overlays=[step("REASON 3", "YOU FORGET THE FEAR", "three")], fx=[{"type": "impact", "word": "huge"}]),
 sc("R39", "Which, if you saw my last video, makes a lot of sense. Most of the time, the fear was about people watching... who weren't really watching.", "S36", "zoom-out",
    ev=[icon("watching", "I06", dur=1.6), icon("weren't", "I29", dur=1.6)], host=[["N05"]]),
 sc("R40", "Four. Unfinished things stay on your mind. Your brain is good at letting go of things that are done. It's much worse at letting go of things that never got finished, or never even got started. So the door you never opened... keeps coming back.", "S37",
    ev=[icon("finished", "I47")], moves=[mv("snap", "door", [0.58, 0.2, 1.4])], overlays=[step("REASON 4", "UNFINISHED THINGS STAY", "four")]),
 sc("R41", "And there's one more study, from two thousand eighteen, that I think is the most important part of all of this. Gilovich and another researcher, Shai Davidai, asked people about their regrets again. But this time, they sorted them differently.", "S03", "zoom-out",
    ev=[pop("important", "N02", [("THE", ), ("MOST IMPORTANT", Y), ("PART",)], dur=2.6)], host=[["N02"], ["N01", "gilovich"]],
    overlays=[{"type": "label", "text": "Davidai & Gilovich, 2018", "word": "davidai", "ul": True, "dur": 5}]),
 sc("R42", "Were they about who you felt you should be? Your duties. Your responsibilities.", "S39",
    ev=[card("should", [("WHO YOU",), ("SHOULD", Y), ("BE",)])]),
 sc("R43", "Or were they about who you wanted to be? Your dreams. Your goals. The person you hoped you'd become.", "S40",
    moves=[mv("snap", "become", [0.33, 0.5, 1.4])], overlays=[{"type": "sweep", "word": "become", "box": {"x": 0.17, "y": 0.2, "w": 0.3, "h": 0.62}}]),
 sc("R44", "Seventy-six percent of people said their single biggest regret was about not becoming the person they wanted to be.", None, "hold", host=[["N02"]], lead=1.0,
    diagram={"kind": "bars", "bars": [{"label": "WHO I<br>WANTED TO BE", "pct": 76}, {"label": "WHO I<br>SHOULD BE", "pct": 24}], "rack": True, "rackFirst": 1,
             "at": {"grow": W_("seventy"), "rack": W_("seventy")}}, fx=[{"type": "riser", "word": "seventy"}, {"type": "impact", "word": "seventy", "off": 0.0}]),
 sc("R45", "Think about that. The regrets that last the longest aren't about the times you messed up. They're about the version of you that never got a chance to show up.", "S40", "zoom-out",
    ev=[pop("version", "N02", [("NEVER GOT",), ("A CHANCE", Y)], dur=2.6)]),
 sc("R46", "A nurse named Bronnie Ware spent years caring for people in the last weeks of their lives, and she wrote down what they told her. The regret she heard most often was this: \"I wish I'd had the courage to live a life true to myself, not the life others expected of me.\" Notice what that regret is about. It's not about a mistake. It's about courage.", "S42",
    ev=[quote("wish", "notice", "I wish I'd had the [[courage]] to live a life [[true to myself,]] not the life others expected of me.", "Bronnie Ware, palliative care nurse"),
        card("courage", [("IT'S ABOUT",), P("COURAGE", mk=True)], occ=2)], host=[["N06"], ["N02", "notice"]]),
]
P4 = [
 sc("R47", "So here's how I actually use this now. Five steps.", None, "hold", host=[["N01"]], ev=[pop("five", "N08", [("5", Y), ("STEPS",)], dur=2.0)],
    diagram={"kind": "card", "parts": [P("HOW I USE"), P("THIS", Y)]}),
 sc("R48", "One. The rocking chair test. When I'm about to talk myself out of something, I picture myself old, sitting in a rocking chair, looking back on my life. And I ask: will that version of me care that this was awkward? Or will he care that I never tried? Almost every time, the answer is obvious. Old me does not care about the awkward part. Old me is annoyed that I didn't go.", "S44",
    pictureB="S44b", swap={"word": "annoyed"}, ev=[icon("rocking", "I40"), pop("awkward", "N06", [("AWKWARD?", Y)], dur=2.2), card("never", [("OR",), ("NEVER TRIED?", R)])],
    moves=[mv("snap", "obvious", [0.34, 0.34, 1.4])], overlays=[step("STEP 1", "THE ROCKING CHAIR TEST", "one")]),
 sc("R49", "Two. Remember which regret fades. If you try and it goes badly, it'll sting for a few days. Maybe a few weeks. Then it fades, and your brain turns it into a lesson, or a funny story. If you don't try, that one doesn't fade. It grows.", None, "hold",
    ev=[icon("sting", "I44"), icon("grows", "I48")], host=[["N07"], ["N02", "if", 2]], overlays=[step("STEP 2", "REMEMBER WHICH ONE FADES", "two")],
    diagram={"kind": "lines", "at": {"draw": W_("fades"), "fade": W_("fades", 2), "grow": W_("one")}}),
 sc("R50", "So you're not choosing between pain and no pain. You're choosing between a short sting... and a long \"what if.\"", None, "hold", host=[["N01"]],
    diagram={"kind": "split", "left": ["A SHORT", "STING"], "right": ["A LONG", "WHAT IF"], "at": {"left": W_("short"), "right": W_("long"), "rack": W_("long")}}),
 sc("R51", "Three. Make it smaller. A lot of the time, we don't act because the thing feels too big. So shrink it. Don't plan to become a runner. Go for one run. Don't write the perfect message. Send a simple one. You don't have to change your whole life today. You just have to open the door a little.", "S47",
    pictureB="S47b", swap={"word": "open", "kind": "iris", "pt": [0.76, 0.5]}, ev=[icon("run", "I49"), icon("message", "I41"), card("change", [("NOT YOUR",), ("WHOLE LIFE", Y)])],
    moves=[mv("whip", "big", [0.5, 0.28, 1.4]), mv("zoom", "shrink", [0.5, 0.5, 1])], overlays=[step("STEP 3", "MAKE IT SMALLER", "three")]),
 sc("R52", "Four. Ask yourself: is this a should, or a want? Remember that last study. The regrets that hit hardest aren't about what you were supposed to do. They're about who you wanted to be. So if something keeps pulling at you, the guitar, the business idea, the person you want to talk to... that pull is worth listening to.", "S40", "zoom-out",
    ev=[iconrow([("I50", "guitar"), ("I09", "business"), ("I26", "person")]), pop("pull", "N02", [("WORTH",), ("LISTENING TO", Y)], dur=2.6)],
    overlays=[step("STEP 4", "A SHOULD, OR A WANT?", "four")]),
 sc("R53", "Five. Decide before the fear shows up. Fear is loudest in the moment. So make the decision earlier, when you're calm. Sign up tonight. Put it on the calendar. Tell a friend you're doing it. Then when the nerves show up later, the hard part is already done.", "S35",
    ev=[icon("sign", "I30"), icon("calendar", "I13"), pop("hard", "N07", [("HARD PART:",), ("DONE", Y)], dur=2.4)], overlays=[step("STEP 5", "DECIDE BEFORE THE FEAR", "five")]),
 sc("R54", "Here's the thing I keep coming back to. Every mistake I've ever made, I can tell you exactly what happened. The story's over. Most of them are just funny now.", "S50",
    ev=[icon("story's", "I46"), pop("funny", "N05", [("JUST",), P("FUNNY", Y, ul=True), ("NOW",)], dur=2.6)]),
 sc("R55", "But the things I didn't do? I still wonder about those.", "S37", fx=[{"type": "leak", "word": "wonder"}], trans="fade"),
 sc("R56", "And if you've got a list like mine, that doesn't mean you're a coward. It means your brain was doing exactly what it was built to do. Protecting you from a little bit of pain today... by charging you a lot more later. You can stop paying that.", "S10", "zoom-out",
    ev=[pop("built", "N01", [("BUILT TO",), ("PROTECT YOU", Y)], dur=2.6), card("stop", [("YOU CAN",), ("STOP PAYING", Y)])], moves=[mv("whip", "charging", [0.82, 0.85, 1.4])]),
 sc("R57", "So the next time your brain says, \"It's safer not to\"... remember what all those people said, looking back on their whole lives.", "S04", "zoom-out",
    ev=[card("safer", [("IT'S",), ("SAFER", R), ("NOT TO",)])], host=[["N01"]]),
 sc("R58", "They didn't wish they'd played it safer. They wished they'd tried.", None, "hold", host=[["N01"], ["N06", "they", 2]],
    diagram={"kind": "card", "parts": [P("THEY DIDN'T WISH THEY'D", sz="mid"), P("PLAYED IT SAFE", R)]},
    diagramB={"kind": "card", "sweep": True, "parts": [P("THEY WISHED THEY'D", sz="mid"), P("TRIED", Y)]}, swap={"word": "tried"}),
 sc("R59", "So go try. Send the message. Sign up.", "S54", ev=[icon("message", "I41")]),
 sc("R60", "Ask the question.", "S55"),
 sc("R61", "Worst case, you get a funny story. Best case... you never have to wonder.", "S56", "zoom-out",
    ev=[pop("worst", "N05", [("WORST CASE:",), ("A FUNNY STORY", Y)], dur=3.0)], irisWord={"word": "best", "pt": [0.5, 0.45]}),
 sc("R62", "Which of the five steps do you need most? Tell me the number in the comments. And if the thing stopping you is that feeling that everyone's watching, my last video breaks down exactly why that's not true. I'll leave it right here.", "S57", "hold",
    ev=[pop("number", "N08", [("WHICH",), ("NUMBER?", Y)], dur=2.2)], holdEnd=True),
]
for n, sc_ in ((1, P1), (2, P2), (3, P3), (4, P4)):
    os.makedirs("scenes", exist_ok=True)
    json.dump({"part": n, "audio": f"audio/padded/part{n}.wav", "scenes": sc_}, open(f"scenes/part{n}.json", "w"), indent=1)
FOCI = {
 "S01": [[.3, .38, 1.4], [.68, .42, 1.35]], "S02": [[.2, .42, 1.4], [.62, .42, 1.4]], "S03": [[.52, .4, 1.4], [.76, .5, 1.35]], "S04": [[.4, .62, 1.35], [.45, .2, 1.3]],
 "S05": [[.5, .38, 1.3]], "S06": [[.58, .45, 1.25], [.9, .65, 1.4]], "S07": [[.72, .55, 1.4]], "S08": [[.6, .4, 1.4]], "S09": [[.62, .45, 1.3], [.73, .5, 1.3]],
 "S10": [[.4, .45, 1.4]], "S12": [[.42, .3, 1.4]], "S13": [[.5, .4, 1.4]], "S15": [[.68, .5, 1.3]], "S20": [[.52, .4, 1.4]], "S23": [[.64, .22, 1.4], [.75, .62, 1.3]],
 "S25": [[.52, .55, 1.4]], "S26": [[.7, .5, 1.4], [.55, .55, 1.4]], "S28": [[.58, .62, 1.4]], "S30": [[.5, .5, 1.35]], "S33": [[.62, .28, 1.4]],
 "S34": [[.58, .45, 1.3]], "S35": [[.5, .45, 1.3]], "S35b": [[.35, .6, 1.3]], "S36": [[.5, .5, 1.4]], "S37": [[.58, .2, 1.4], [.77, .62, 1.3]], "S39": [[.58, .5, 1.3]],
 "S40": [[.6, .5, 1.3], [.33, .5, 1.4]], "S42": [[.3, .4, 1.4], [.77, .38, 1.4]], "S44": [[.4, .5, 1.35]], "S44b": [[.4, .5, 1.35]], "S47": [[.4, .75, 1.3]], "S47b": [[.7, .5, 1.3]],
 "S50": [[.65, .52, 1.4]], "S54": [[.38, .5, 1.4]], "S55": [[.58, .45, 1.4]], "S56": [[.35, .45, 1.4]], "S57": [[.82, .5, 1.3]], "S58": [[.5, .5, 1.4]], "S59": [[.45, .35, 1.4]],
 "I45": [[.5, .5, 1.2]], "I46": [[.5, .5, 1.2]],
}
json.dump(FOCI, open("scenes/foci.json", "w"))
print("specs written", sum(len(x) for x in (P1, P2, P3, P4)), "scenes")
