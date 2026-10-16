#!/usr/bin/env python3
"""Video 4 (Open Your Eyes): writes scenes/partN.json (scene specs for tools/build-part.mjs) and scenes/foci.json. Scene list = VIDEO.md."""
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
def title(): return {"kind": "title", "dur": 2.5}
def mv(kind, word, f=None, occ=1, **kw): return {"kind": kind, "word": word, "occ": occ, "f": f, **kw}
def step(n, text, word, occ=1, **kw): return {"type": "step", "step": n, "text": text, "word": word, "occ": occ, **kw}
def pill(text, word, occ=1, **kw): return {"type": "pill", "text": text, "word": word, "occ": occ, **kw}
def serif(text, word, occ=1, **kw): return {"type": "serif", "text": text, "word": word, "occ": occ, "dur": 99, **kw}
def sc(id, narr, picture=None, camera="zoom-in", ev=None, **kw):
    d = {"id": id, "camera": camera, "narration": narr, "events": ev or []}
    if picture: d["picture"] = picture
    d.update(kw); return d
W_ = lambda w, o=1: {"word": w, "occ": o}
COLD = dict(cold=True, foci=[])
BATT = lambda **kw: {"kind": "battery", **kw}

P1 = [
 sc("E01", "Imagine your phone is at a hundred percent when you wake up. By lunch, it's almost dead. And you barely touched it.", "S01", pictureB="S01b",
    swap={"word": "lunch", "kind": "fade"}, push=[0.58, 0.66], **COLD),
 sc("E02", "So you open the battery settings to see what happened. And there it is. A list of apps eating your battery... including some you never even opened today. They've been running in the background. All morning. Quietly. So here's a question.", "S02",
    overlays=[{"type": "rect", "word": "never", "box": {"x": 0.385, "y": 0.535, "w": 0.165, "h": 0.30}, "rot": -16}], push=[0.45, 0.6], **COLD),
 sc("E03", "When you lock your phone and the screen goes black... do those apps close? No. The screen just goes dark. Everything behind it keeps running.", "S03", "hold",
    overlays=[serif("everything keeps running.", "running")], push=[0.62, 0.67], **COLD),
 sc("E04", "Now think about the last time you went to bed exhausted... after a day where you didn't really do that much. What was still running? The conversation you keep replaying. The decision you keep putting off. The text you never answered. The thing that ended... that you never really let end.", "S04",
    moves=[mv("slow", "conversation", [0.19, 0.28, 1.4], dur=0.6), mv("slow", "decision", [0.62, 0.17, 1.4], dur=0.6), mv("slow", "text", [0.37, 0.15, 1.4], dur=0.6),
           mv("slow", "ended", [0.84, 0.3, 1.4], dur=0.6), mv("slow", "never", [0.4, 0.58, 1.4], occ=2, dur=0.6)], cold=True),
 sc("E05", "Maybe you're not tired because you did too much. Maybe you're tired because too much inside you never finished.", "S05",
    ev=[title()], overlays=[serif("Open Your Eyes.", "finished", color="#B5484A")], push=[0.5, 0.45], lead=0.8,
    fx=[{"type": "riser", "word": "maybe"}, {"type": "ding", "word": "maybe", "low": True}], **COLD),
 sc("E06", "I know that feeling way too well. A while ago, I went through a stretch where I was tired all the time. Not from working out. Not from long days. Some days I barely left my room. I'd sleep nine hours and wake up like I'd just run a marathon.", "S23",
    ev=[icon("tired", "I56"), card("marathon", [("9 HOURS.",), ("STILL",), ("TIRED", R)])], moves=[mv("snap", "nine", [0.5, 0.38, 1.4])]),
 sc("E07", "And at night, I'd lie there going over the same stuff. A dumb thing I said to a friend weeks earlier. A message I was supposed to answer. A decision about what I actually wanted to do with my life, that I kept pushing to \"tomorrow.\" None of it was urgent. But none of it was ever finished either. So it just... stayed open.", "S06",
    ev=[card("open", [("IT JUST",), ("STAYED OPEN", Y)])],
    moves=[mv("snap", "dumb", [0.21, 0.27, 1.4]), mv("whip", "message", [0.5, 0.22, 1.4]), mv("whip", "decision", [0.8, 0.28, 1.4]), mv("zoom", "none", [0.5, 0.5, 1])]),
 sc("E08", "It turns out there's real psychology behind this. Researchers have studied what unfinished things do to your mind, and why some thoughts keep coming back no matter how many times you push them away.", "S20",
    ev=[icon("researchers", "I25")], host=[["N06"]], moves=[mv("snap", "unfinished", [0.77, 0.42, 1.4])]),
 sc("E09", "By the end of this video, you'll know what's actually running in the background of your mind, the four \"apps\" that drain people the most, and five simple ways to close them.", None, "hold", host=[["N01"]],
    diagram={"kind": "irow", "items": [{"icon": "I56", "label": "WHAT'S<br>RUNNING"}, {"icon": "I65", "label": "4 &ldquo;APPS&rdquo;"}, {"icon": "I69", "label": "5 WAYS TO<br>CLOSE THEM"}],
             "at": {"it0": W_("running"), "it1": W_("four"), "it2": W_("close")}}),
 sc("E10", "One of them takes about five minutes before bed. And quick note. If you're exhausted all the time no matter what you do, it's worth talking to a doctor too. This video is about the kind of tired that doesn't come from your body.", "S33",
    ev=[icon("five", "I11"), card("doctor", [P("ALWAYS EXHAUSTED?", sz="mid"), ("SEE A DOCTOR", Y)], dur=2.4)], moves=[mv("snap", "note", [0.55, 0.28, 1.4])]),
]
P2 = [
 sc("E11", "As the story goes, it started in the nineteen-twenties, in a café in Berlin. A psychologist named Kurt Lewin noticed something about a waiter. The waiter could remember every unpaid order at a busy table, without writing anything down.", "S07",
    host=[["N01"], ["N06", "a", 2]], trans="push", overlays=[pill("BERLIN, 1920s", "berlin")],
    moves=[mv("snap", "waiter", [0.66, 0.45, 1.4]), mv("whip", "every", [0.55, 0.2, 1.4]), mv("whip", "unpaid", [0.66, 0.14, 1.4]), mv("whip", "order", [0.76, 0.24, 1.4])]),
 sc("E12", "But as soon as the bill was paid... it was gone. He couldn't remember any of it.", "S07", camera="hold", pictureB="S07b", swap={"word": "paid"},
    ev=[card("gone", [("PAID =",), ("GONE", Y)])], host=[["N05"]]),
 sc("E13", "One of Lewin's students, Bluma Zeigarnik, turned that into an experiment. People worked through a bunch of small tasks, and some of them were interrupted halfway. Later, people seemed to remember the unfinished tasks better than the finished ones. It became known as the Zeigarnik effect. And you've probably seen it all over the internet.", "S08",
    ev=[card("effect", [("THE",), ("ZEIGARNIK EFFECT", Y)])], overlays=[pill("BLUMA ZEIGARNIK", "zeigarnik", dur=5)],
    moves=[mv("snap", "interrupted", [0.72, 0.66, 1.4]), mv("whip", "later", [0.34, 0.55, 1.4])]),
 sc("E14", "But to be honest, that memory part hasn't held up very well. A big review in twenty twenty-five found that unfinished tasks aren't reliably remembered better. It did find something else, though. People have a strong pull to go back to things that were interrupted.", None, "hold",
    host=[["N02"], ["N06", "it"]],
    diagram={"kind": "card", "parts": [P("UNFINISHED ="), P("REMEMBERED BETTER", R, x=True, sz="sm"), P("2025 REVIEW", small=True)], "at": {"x": W_("aren't")}},
    diagramB={"kind": "card", "sweep": True, "parts": [P("A PULL TO"), P("GO BACK", Y)]}, swap={"word": "something"}),
 sc("E15", "Your mind doesn't like open loops. It keeps nudging you back toward them. And another study shows what all that nudging actually costs you.", None, "hold",
    host=[["N06"], ["N01", "and"]], diagram={"kind": "loop", "at": {"draw": W_("loops"), "nudge": W_("nudging")}}),
 sc("E16", "In two thousand eleven, psychologists E.J. Masicampo and Roy Baumeister asked people to think about an important goal they hadn't finished yet. Then they gave them something completely different to work on. And the unfinished goal kept sneaking back in. People had more distracting thoughts about it... and they did worse on the task right in front of them.", "S09",
    overlays=[pill("MASICAMPO & BAUMEISTER, 2011", "masicampo", dur=5)],
    moves=[mv("snap", "sneaking", [0.84, 0.24, 1.4]), mv("whip", "worse", [0.62, 0.67, 1.4])]),
 sc("E17", "Then the researchers tried one small change. Before the second task, some people made a specific plan for their unfinished goal. When, where, and how they'd do it. And the distracting thoughts... mostly went away. They hadn't finished anything. They'd only made a plan. And that was enough for the mind to let it go, for now.", "S09", pictureB="S09b", swap={"word": "plan"},
    ev=[card("only", [("THEY ONLY MADE",), ("A PLAN", Y)])], host=[["N02"], ["N06", "they"]],
    overlays=[{"type": "circle", "cx": 0.64, "cy": 0.69, "rx": 0.1, "ry": 0.065, "word": "when"}, {"type": "sweep", "word": "away", "box": {"x": 0.52, "y": 0.3, "w": 0.45, "h": 0.5}}]),
 sc("E18", "And those distracting thoughts take up more of your day than you'd think. Researchers at Harvard checked in on more than two thousand people through an app on their phones, at random moments during the day. They asked: what are you doing right now? And are you thinking about something else?", "S10", "pan-right",
    ev=[icon("app", "I41")], overlays=[pill("HARVARD", "harvard", dur=3)],
    moves=[mv("snap", "doing", [0.1, 0.45, 1.4]), mv("whip", "else", [0.64, 0.4, 1.4])]),
 sc("E19", "Almost half the time... people's minds were somewhere else. And when their minds wandered, they were usually less happy than when they were focused on what they were doing.", None, "hold", host=[["N02"], ["N06", "and"]], lead=0.8,
    diagram={"kind": "pie", "pct": 47, "from": 0, "label": "MIND ELSEWHERE:", "badge": "yellow", "value": "47%", "sub": "Killingsworth &amp; Gilbert, 2010", "at": {"fill": W_("almost")}},
    fx=[{"type": "riser", "word": "almost"}, {"type": "impact", "word": "almost"}]),
 sc("E20", "So your mind isn't lazy when it feels drained. It might just be running too many things you can't see.", "S22", moves=[mv("snap", "running", [0.79, 0.6, 1.4])]),
]
IN0 = {"replay": 0.2, "decision": 0.5, "halfdone": 0.35, "ending": 0.7}
P3 = [
 sc("E21", "So what's actually running in the background? From all this research, there are four kinds of \"apps\" that seem to drain people the most.", None, "hold", host=[["N06"]],
    diagram=BATT(init={}, at={"frame": W_("so"), "appear": W_("so")})),
 sc("E22", "One. The replay. The conversation you keep going over. What you said. What you should have said. What they meant by that look.", "S11",
    ev=[icon("going", "I63")], overlays=[step("APP 1", "THE REPLAY", "one")],
    moves=[mv("snap", "said", [0.37, 0.45, 1.4]), mv("whip", "meant", [0.64, 0.5, 1.4])]),
 sc("E23", "Psychologists call this rumination. And it's strongly linked to having a harder time falling asleep, and to feeling worse the next day.", None, "hold", host=[["N06"]],
    ev=[icon("asleep", "I68")], overlays=[pill("RUMINATION", "rumination")],
    diagram=BATT(init=IN0, active="replay", grow=[{"row": "replay", "word": W_("rumination"), "to": 0.92}])),
 sc("E24", "For me, it was one comment at a party. Something I said that came out wrong. I must have replayed it fifty times that week. The friend I said it to? He didn't even remember it. The worst part? Replaying it never changes how it went. It just runs the same video again.", "S11", "zoom-out",
    ev=[card("fifty", [("REPLAYED",), ("50×", Y)]), pop("remember", "N05", [("HE DIDN'T",), ("EVEN REMEMBER", Y)])], fx=[{"type": "leak", "word": "party"}],
    moves=[mv("snap", "friend", [0.64, 0.5, 1.4])]),
 sc("E25", "Two. The decision you keep avoiding. Should I quit? Should I text them? Should I change what I'm studying? Remember that pull to go back to interrupted things? A decision you keep avoiding is the biggest interruption of all.", "S12",
    ev=[icon("quit", "I64")], overlays=[step("APP 2", "THE AVOIDED DECISION", "two")],
    moves=[mv("snap", "avoiding", [0.2, 0.7, 1.4]), mv("whip", "change", [0.8, 0.7, 1.4]), mv("snap", "remember", [0.5, 0.5, 1.4])]),
 sc("E26", "An avoided decision isn't closed. It's paused. And every time something reminds you of it, your mind opens it right back up. Then you push it away again. And again. That's not resting. That's running the same app over and over without ever letting it finish.", None, "hold",
    host=[["N06", "an"], ["N05", "then"], ["N02", "that's"]],
    ev=[card("resting", [("NOT", R), ("RESTING",)])],
    overlays=[{"type": "stamp", "text": "PAUSED, NOT CLOSED", "word": "paused", "box": {"x": 0.27, "y": 0.79, "w": 0.46, "h": 0.14}, "rot": -7, "fs": 74}],
    diagram=BATT(init={**IN0, "replay": 0.9}, active="decision", pulse=[{"row": "decision", "words": [W_("opens"), W_("away"), W_("again")]}])),
 sc("E27", "Three. The half-finished task. A researcher named Sophie Leroy found that when people switched to something new while an older task was still unfinished, part of their attention stayed stuck on the first one.", "S13",
    overlays=[step("APP 3", "THE HALF-FINISHED TASK", "three"), pill("SOPHIE LEROY", "leroy", dur=3)], moves=[mv("snap", "first", [0.17, 0.62, 1.4])]),
 sc("E28", "She called it \"attention residue.\" And those people did worse on the new task.", None, "hold", host=[["N06"], ["N01", "and"]],
    overlays=[pill("ATTENTION RESIDUE", "attention")],
    diagram=BATT(init={"replay": 0.9, "decision": 0.7, "halfdone": 0.15, "ending": 0.7}, active="halfdone", grow=[{"row": "halfdone", "word": W_("worse"), "to": 0.85}])),
 sc("E29", "So when you've got ten tabs open, three half-done assignments and an unanswered email... you're never fully anywhere.", "S13",
    ev=[icon("tabs", "I65"), card("anywhere", [("NEVER FULLY",), ("ANYWHERE", Y)])], moves=[mv("snap", "ten", [0.31, 0.4, 1.4])]),
 sc("E30", "Four. The ending you never accepted. A friendship that faded without a real goodbye. A relationship that ended before you were ready. A version of yourself you thought you'd be by now.", "S37", trans="fade",
    ev=[icon("relationship", "I66")], overlays=[step("APP 4", "THE ENDING YOU NEVER ACCEPTED", "four")], moves=[mv("snap", "friendship", [0.5, 0.25, 1.4])]),
 sc("E31", "Your mind keeps trying to write the last chapter, because nobody ever wrote it. It's part of why a song, a smell, or a random photo can drag you right back to something that ended years ago. That one usually runs the quietest... and the longest.", None, "hold",
    host=[["N06"], ["N01", "it's"], ["N02", "that", 2]], ev=[icon("chapter", "I46")],
    diagram=BATT(init={"replay": 0.9, "decision": 0.7, "halfdone": 0.85, "ending": 0.1}, active="ending", grow=[{"row": "ending", "word": W_("longest"), "to": 1.0, "dur": 1.6}])),
 sc("E32", "Here's what all four have in common. None of them are on your screen. You can be lying in bed, doing nothing at all... and they're still running.", "S06", "zoom-out",
    moves=[mv("snap", "lying", [0.45, 0.62, 1.4])]),
 sc("E33", "So how do you close them? Not by forcing them out of your head. Telling yourself \"stop thinking about it\" usually makes you think about it more. You close them the same way you'd close an app. On purpose. One at a time.", None, "hold",
    host=[["N06"], ["N01", "you"]], ev=[card("stop", [("“STOP THINKING", R), ("ABOUT IT”", R)]), icon("same", "I69")],
    diagram={"kind": "loop", "at": {"close": W_("purpose")}}),
]
P4 = [
 sc("E34", "So here's how I actually close them now. Five steps. One. Check your battery usage. Grab a piece of paper and write down everything that's still open in your head. Every conversation, every decision, every half-done thing. Don't fix anything yet. Just list it.", "S14",
    ev=[icon("write", "I67")], overlays=[step("STEP 1", "CHECK YOUR BATTERY USAGE", "one")], moves=[mv("snap", "paper", [0.34, 0.6, 1.4])]),
 sc("E35", "It sounds too simple, but a lot of these apps get quieter the second you can actually see them.", None, "hold", host=[["N01"]],
    diagram=BATT(init={"replay": 0.9, "decision": 0.7, "halfdone": 0.85, "ending": 1.0}, shrinkAll={"word": W_("quieter"), "f": 0.7})),
 sc("E36", "Two. Write tomorrow's to-do list before bed. In one study, researchers brought people into a sleep lab. Before bed, some of them spent five minutes writing a to-do list for the next few days. Others wrote about things they'd already finished.", "S15",
    ev=[icon("five", "I11")], host=[["N07"], ["N01", "in"]], overlays=[step("STEP 2", "TO-DO LIST BEFORE BED", "two")],
    moves=[mv("snap", "lab", [0.15, 0.52, 1.4]), mv("whip", "others", [0.81, 0.48, 1.4])]),
 sc("E37", "The to-do list group fell asleep faster. About nine minutes faster. And the more specific the list was, the faster they fell asleep. It was a small study. But it's five minutes and a pen.", None, "hold",
    host=[["N02"], ["N05", "it"]], ev=[icon("pen", "I67")],
    diagram={"kind": "card", "parts": [P("ABOUT"), P("9 MIN", Y, cnt={"to": 9, "suffix": " MIN"}), P("FASTER"), P("Scullin et al., 2018", small=True)], "at": {"cnt": W_("nine")}},
    fx=[{"type": "riser", "word": "nine"}, {"type": "impact", "word": "nine"}]),
 sc("E38", "Three. Give every open loop a plan. Remember the study where a plan made the distracting thoughts go away? You don't have to finish everything tonight. You just have to decide when, where, and how.", "S14",
    ev=[card("when", [P("WHEN. WHERE. HOW.", Y, sz="mid")])], overlays=[step("STEP 3", "GIVE IT A PLAN", "three")], moves=[mv("snap", "decide", [0.45, 0.56, 1.4])]),
 sc("E39", "\"I'll answer that text tomorrow at lunch.\" \"I'll make that decision by Friday, after I talk to my brother.\" That's often enough for your mind to stop nudging you.", None, "hold", host=[["N01"]],
    ev=[icon("friday", "I13")],
    diagram={"kind": "split", "left": ["THE TEXT", "TOMORROW, LUNCH"], "right": ["THE DECISION", "BY FRIDAY"], "rightBadge": "yellow", "fs": 84, "at": {"left": W_("answer"), "right": W_("decision")}}),
 sc("E40", "Four. Close one small app today. Pick the smallest thing on your list and finish it. Send the reply. Make the easy decision. Delete the thing you're never going to do. Every loop you close is one less thing running in the background.", None, "hold",
    host=[["N07"], ["N01", "pick"]], ev=[icon("reply", "I41")], overlays=[step("STEP 4", "CLOSE ONE SMALL APP", "four")],
    diagram=BATT(init={"replay": 0.75, "decision": 0.55, "halfdone": 0.2, "ending": 0.9}, closeRow={"row": "halfdone", "word": W_("finish"), "word2": W_("close", 2)})),
 sc("E41", "For me, it was finally texting that friend: \"Hey, that thing I said at the party came out wrong.\" It took thirty seconds. He replied, \"lol what?\" And that replay never ran again.", "S16",
    ev=[card("lol", [("“LOL",), ("WHAT?”", Y)])], moves=[mv("snap", "replied", [0.54, 0.57, 1.4])]),
 sc("E42", "Five. Let some things end. For the endings you never got, try writing it out. Fifteen minutes. What happened, how it felt, and what you'd want the last chapter to say.", "S17", trans="fade",
    ev=[icon("fifteen", "I43")], overlays=[step("STEP 5", "LET SOME THINGS END", "five")], moves=[mv("snap", "writing", [0.53, 0.76, 1.4])]),
 sc("E43", "A psychologist named James Pennebaker found that when people wrote about things that were still weighing on them, for a few days in a row, they went to the doctor less often over the next few months. You can't always get a real goodbye. But you can stop waiting for one.", "S20",
    host=[["N06"]], ev=[card("stop", [("STOP",), ("WAITING FOR ONE", Y)])], overlays=[pill("JAMES PENNEBAKER", "pennebaker", dur=4)]),
 sc("E44", "Here's what I keep coming back to. For a long time, I thought I was tired because I wasn't sleeping enough. But I could sleep for nine hours, and I still woke up with all my apps open.", "S23"),
 sc("E45", "Sleep turns the screen off. It doesn't close what's running.", "S03", "hold", trans="fade", overlays=[serif("Sleep turns the screen off.", "close")], push=[0.62, 0.67], **COLD),
 sc("E46", "So open your eyes to what's running in the background.", "S05", overlays=[serif("Open Your Eyes.", "eyes", color="#B5484A")], push=[0.5, 0.45], **COLD),
 sc("E47", "Close what you can. Plan what you can't. And let go of what's already over. Because sometimes, you don't need more rest. You need fewer things running.", "S31", "zoom-out", trans="iris", irisAt=[0.35, 0.3],
    overlays=[pill("CLOSE", "close", until="plan"), pill("PLAN", "plan", until="and"), pill("LET GO", "let", until="because"), {"type": "sweep", "word": "fewer", "box": {"x": 0.0, "y": 0.0, "w": 1.0, "h": 1.0}}]),
 sc("E48", "So what's running in your background right now? Tell me in the comments. Just one word. And if the app that's draining you is a decision you keep avoiding, I made a whole video on why the safe choice isn't always safe. I'll leave it right here.", "S29", "hold",
    ev=[pop("running", "N06", [("ONE WORD", Y)], dur=2.4)], holdEnd=True),
]
os.makedirs("scenes", exist_ok=True)
for n, sc_ in ((1, P1), (2, P2), (3, P3), (4, P4)):
    json.dump({"part": n, "audio": f"audio/padded/part{n}.wav", "scenes": sc_}, open(f"scenes/part{n}.json", "w"), indent=1)
FOCI = {
 "S01": [[.58, .66, 1.4]], "S02": [[.45, .45, 1.3]], "S03": [[.62, .67, 1.4]], "S04": [[.4, .58, 1.4]], "S05": [[.5, .45, 1.35]],
 "S06": [[.45, .62, 1.4], [.5, .22, 1.35]], "S07": [[.66, .45, 1.4]], "S08": [[.72, .66, 1.4], [.34, .55, 1.4]], "S09": [[.62, .45, 1.4], [.84, .24, 1.4]],
 "S10": [[.64, .4, 1.4], [.1, .45, 1.4]], "S11": [[.37, .45, 1.4], [.64, .5, 1.4]], "S12": [[.5, .55, 1.4]], "S13": [[.31, .4, 1.4], [.17, .62, 1.4]],
 "S14": [[.34, .6, 1.4], [.45, .56, 1.4]], "S15": [[.15, .52, 1.4], [.81, .48, 1.4]], "S16": [[.54, .57, 1.4]], "S17": [[.53, .76, 1.4], [.4, .4, 1.4]],
 "S20": [[.77, .42, 1.4], [.43, .3, 1.4]], "S22": [[.79, .6, 1.4]], "S23": [[.5, .38, 1.4]], "S29": [[.8, .5, 1.3]], "S31": [[.33, .3, 1.4]],
 "S33": [[.55, .28, 1.4]], "S37": [[.5, .25, 1.4], [.65, .65, 1.4]],
}
json.dump(FOCI, open("scenes/foci.json", "w"))
print("specs written", sum(len(x) for x in (P1, P2, P3, P4)), "scenes")
