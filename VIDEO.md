# Current video: "Open Your Eyes: Why You're Always Tired (Even When You Do Nothing)"

**Series:** the first **"Open Your Eyes"** video. It opens with a slow, eerie question-chain cold open (a phone battery that drains while you barely use it), then flips it onto the viewer.
**Topic:** mental "background apps". Unfinished things (replayed conversations, avoided decisions, half-done tasks, endings never accepted) keep running and leave people drained. The fix: see them, plan them, close them, let them end.
**Follows:** `PLAYBOOK.md` (hook → personal story → research → 4 "apps" → 5 steps → emotional close). It points to the regret video at the end.
**Length:** the raw voice is about 1,690 words. After pause padding, the target is about **11:30–12:00**.
**Audio:** 13 clips, `audio/part1a.mp3` … (Part 1 a–c, Part 2 a–c, Part 3 a–c, Part 4 a–d). Run `python3 tools/join-clips.py` first; it joins them into `audio/part1.mp3` … `part4.mp3`.
**Music:** `music/track.mp3`, mixed softly as before. For the cold open (E01–E05), keep the music at its quietest and let the room tone breathe.
**Upload kit** (title, thumbnail, description, tags): `prompts/upload-package.md`.
**Spec examples:** copy the helpers from `videos/02-regret/make-specs.py`. Videos 2 and 3 use the same notation.

## How to read this list

- **Scene IDs (E01…) and picture files (S01.png…) are separate.** The `picture` field names the exact file in `pictures/`.
  - `(NEW)` means Luke makes it (prompt in `prompts/nano-banana-prompts.md`). `(COPY)` means it's already in `pictures/`. `CODED` means you build it in code.
- **beats:** key moments with the exact trigger word in quotes. Fill the rest with crops, cards, icons and pop-ups per CLAUDE.md (every shot ≤ 4s, except the cold open, see below).
  - `icon Ixx "word"`, `pop Nxx "word" → content`, `card "word" → TEXT`, `step "word" → STEP n + TEXT` (or `APP n`), `badge "word" → TEXT`.
  - **Bold** words go in a yellow badge, ~~struck~~ words in a red badge.
- **edit:** the specific moves for that scene (CLAUDE.md section 9). **host:** the narrator-host pose track; no `host:` line means full-frame.
- **narration** is for timing only and must match the audio. Never show it on screen.
- **Icons:** I11, I13, I25, I41, I43, I46 and I56 are reused (already in `icons/`). I63–I69 are new (prompts in `prompts/icon-prompts.md`). If an icon file is missing, skip that beat.
- **Numbers:** Whisper may write "nineteen-twenties" as "1920s", "twenty twenty-five" as "2025", "two thousand eleven" as "2011", "nine" as "9". Match triggers either way.

---

## The cold open (new for this series)

E01–E05 are **oil-painting pictures** (S01–S05), darker and slower than the rest of the video, to match the thumbnail.
- **Pacing exception:** shots may run up to **5s** here. Moves are slow but still motivated: a slow push (≤ 4% over the shot) that lands on a word, a soft swap, or a hard cut on a word. No snap zooms, no whips, no icons, no text cards, no narrator host or pop-ups.
- Overlays in the cold open are only small, elegant **serif** text (Georgia-style, muted red `#B5484A` or off-white), top-center, fading in over 0.4s.
- SFX: no pops or clicks. Only one soft low *riser* into E05 and a single low *ding* on its first word.
- After E05, the **title card** shows right away (instead of at the end of Part 1): black background, small serif "Open Your Eyes." in muted red, 2.5s, then a hard cut into E06 and the normal bright style.

## The narrator host

Same rules as videos 2 and 3 (poses from the tone tags, frame on the right, hard-cut pose changes, never animated, he stays put between host scenes). Host scenes are pictures without the narrator and coded diagrams. Aim for about 45–50% host time, no host stretch longer than about 40s.

---

## PART 1: The cold open and my story (`audio/part1.mp3`)

**E01** · picture S01 (NEW, oil: a phone on a nightstand at dawn, its battery icon glowing full), swapping to S01b (NEW, oil: the same phone at midday, battery icon almost empty and red) on "lunch" · camera zoom-in
edit: slow push toward the phone · soft 0.3s crossfade swap to S01b on "lunch"
narration: "Imagine your phone is at a hundred percent when you wake up. By lunch, it's almost dead. And you barely touched it."

**E02** · picture S02 (NEW, oil: close-up of a glowing phone screen showing a battery-usage list: app icons with long and short bars) · camera zoom-in
edit: slow push down the list · on "never" a soft red outline glows around the two lowest app rows
narration: "So you open the battery settings to see what happened. And there it is. A list of apps eating your battery... including some you never even opened today. They've been running in the background. All morning. Quietly."

**E03** · picture S03 (NEW, oil: the same phone, screen locked and black, faint ghostly app shapes still glowing behind the dark glass) · camera hold
edit: hard cut in on "when" · slow push on "everything" · serif text "everything keeps running." fades in on "running"
narration: "So here's a question. When you lock your phone and the screen goes black... do those apps close? No. The screen just goes dark. Everything behind it keeps running."

**E04** · picture S04 (NEW, oil: a pale, simple figure lying in bed in the dark, eyes open; above him four faint floating "app windows", each holding a tiny scene: two people talking, a phone with an unanswered message, a fork in a road, a torn photo) · camera zoom-in
edit: slow tour of the windows: drift to the talking pair on "conversation", the fork on "decision", the phone on "text", the torn photo on "ended" (each move 0.6s, `power2.inOut`, no blur) · settle back on his open eyes on "never" (2nd occurrence)
narration: "Now think about the last time you went to bed exhausted... after a day where you didn't really do that much. What was still running? The conversation you keep replaying. The decision you keep putting off. The text you never answered. The thing that ended... that you never really let end."

**E05** · picture S05 (NEW: the "Open Your Eyes" thumbnail painting, without its text) · camera zoom-in · **reveal: at least 2s of silence after**, then the title card
edit: soft riser into the scene · slow push to the two faces · serif text "Open Your Eyes." fades in top-center on "finished"
narration: "Maybe you're not tired because you did too much. Maybe you're tired because too much inside you never finished."

**E06** · picture S23 (COPY: narrator on the edge of his bed in the morning, sneakers and gym bag by the door) · camera zoom-in
edit: hard cut from the title card (the bright style starts here) · snap zoom to his tired face on "nine"
narration: "I know that feeling way too well. A while ago, I went through a stretch where I was tired all the time. Not from working out. Not from long days. Some days I barely left my room. I'd sleep nine hours and wake up like I'd just run a marathon."
beats: icon I56 "tired" · card "marathon" → 9 HOURS. STILL ~~TIRED~~.

**E07** · picture S06 (NEW: narrator lying awake in bed at night, three thought bubbles above him: him at a party saying something awkward, a phone with an unanswered message, a fork in a road) · camera zoom-in
edit: tour: snap zoom to the party bubble on "dumb" → whip slide to the phone bubble on "message" → whip slide to the fork on "decision" → zoom back out on "none" (1st occurrence)
narration: "And at night, I'd lie there going over the same stuff. A dumb thing I said to a friend weeks earlier. A message I was supposed to answer. A decision about what I actually wanted to do with my life, that I kept pushing to "tomorrow." None of it was urgent. But none of it was ever finished either. So it just... stayed open."
beats: card "open" → IT JUST **STAYED OPEN**

**E08** · picture S20 (COPY: researcher at a desk with a huge pile of notes) · camera zoom-in
edit: snap zoom to the note pile on "unfinished"
host: N06 "it"
narration: "It turns out there's real psychology behind this. Researchers have studied what unfinished things do to your mind, and why some thoughts keep coming back no matter how many times you push them away."
beats: icon I25 "researchers"

**E09** · CODED iconRow · camera hold
host: N01 "by"
Icons: I56 on "running", I65 on "four", I69 on "close". Labels: WHAT'S RUNNING · 4 "APPS" · 5 WAYS TO CLOSE THEM.
narration: "By the end of this video, you'll know what's actually running in the background of your mind, the four "apps" that drain people the most, and five simple ways to close them."

**E10** · picture S33 (COPY: narrator thinking, a lightbulb above him) · camera zoom-in
edit: snap zoom to him on "note"
narration: "One of them takes about five minutes before bed. And quick note. If you're exhausted all the time no matter what you do, it's worth talking to a doctor too. This video is about the kind of tired that doesn't come from your body."
beats: icon I11 "five" · badge "doctor" → ALWAYS EXHAUSTED? **SEE A DOCTOR**

---

## PART 2: The research (`audio/part2.mp3`)

**E11** · picture S07 (NEW: a busy 1920s café, a stickman waiter in an apron at a crowded table, little floating bubbles of dishes above his head) · camera zoom-in
edit: push wipe in (time jump) on "as" · badge BERLIN, 1920s on "Berlin" · snap zoom to the waiter on "waiter" (1st occurrence) · tour the dish bubbles on "every"
host: N01 "as" → N06 "a" (2nd occurrence)
narration: "As the story goes, it started in the nineteen-twenties, in a café in Berlin. A psychologist named Kurt Lewin noticed something about a waiter. The waiter could remember every unpaid order at a busy table, without writing anything down."

**E12** · picture S07b (NEW: the same café, the bill paid, coins on the table, customers leaving, the bubbles above the waiter gone) · camera hold
edit: hard swap to S07b with a ding on "paid"
host: N05 "but"
narration: "But as soon as the bill was paid... it was gone. He couldn't remember any of it."
beats: card "gone" → PAID = **GONE**

**E13** · picture S08 (NEW: a 1920s study room, a young woman researcher with a notebook watching a stickman do small puzzles at a table, some puzzles left half-done) · camera zoom-in
edit: name pill BLUMA ZEIGARNIK on "Zeigarnik" (1st occurrence) · snap zoom to the half-done puzzles on "interrupted" · whip slide to the researcher on "later"
narration: "One of Lewin's students, Bluma Zeigarnik, turned that into an experiment. People worked through a bunch of small tasks, and some of them were interrupted halfway. Later, people seemed to remember the unfinished tasks better than the finished ones. It became known as the Zeigarnik effect. And you've probably seen it all over the internet."
beats: card "effect" → THE **ZEIGARNIK EFFECT**

**E14** · CODED card, swapping to card B on "something" · camera hold
edit: card A: red ~~X~~ stamps over REMEMBERED BETTER on "aren't" · kinetic swap to card B
host: N02 "but" → N06 "it"
Card A: UNFINISHED = ~~REMEMBERED BETTER~~ (small line under it: 2025 review). Card B: A PULL TO **GO BACK**.
narration: "But to be honest, that memory part hasn't held up very well. A big review in twenty twenty-five found that unfinished tasks aren't reliably remembered better. It did find something else, though. People have a strong pull to go back to things that were interrupted."

**E15** · CODED loop · camera hold
edit: the open loop draws on (1s) on "loops"; a small arrow nudges along it on "nudging" (1st occurrence)
host: N06 "your" → N01 "and"
narration: "Your mind doesn't like open loops. It keeps nudging you back toward them. And another study shows what all that nudging actually costs you."

**E16** · picture S09 (NEW: a stickman at a desk trying to read, while a big nagging thought bubble of a half-built project tugs at his attention) · camera zoom-in
edit: name pill MASICAMPO & BAUMEISTER, 2011 on "Masicampo" · snap zoom to the nagging bubble on "sneaking" · whip slide to his book on "worse"
narration: "In two thousand eleven, psychologists E.J. Masicampo and Roy Baumeister asked people to think about an important goal they hadn't finished yet. Then they gave them something completely different to work on. And the unfinished goal kept sneaking back in. People had more distracting thoughts about it... and they did worse on the task right in front of them."

**E17** · picture S09, swapping to S09b (NEW: the same stickman writing in a small planner, the nagging bubble faded and small, his face relaxed) on "plan" (1st occurrence) · camera zoom-in · **reveal: at least 2s of silence after**
edit: swap with a ding on "plan" · hand-drawn callout circle around the planner on "when" · light sweep on "away"
host: N02 "then" → N06 "they"
narration: "Then the researchers tried one small change. Before the second task, some people made a specific plan for their unfinished goal. When, where, and how they'd do it. And the distracting thoughts... mostly went away. They hadn't finished anything. They'd only made a plan. And that was enough for the mind to let it go, for now."
beats: card "only" → THEY ONLY MADE **A PLAN**

**E18** · picture S10 (NEW: a city street of stickmen doing different things, each phone buzzing; about half have thought bubbles drifting away) · camera pan-right
edit: badge HARVARD on "Harvard" · tour: snap zoom to a stickman cooking on "doing" → whip slide to a stickman with a drifting bubble on "else"
narration: "And those distracting thoughts take up more of your day than you'd think. Researchers at Harvard checked in on more than two thousand people through an app on their phones, at random moments during the day. They asked: what are you doing right now? And are you thinking about something else?"
beats: icon I41 "app"

**E19** · CODED pie · camera hold · **reveal: at least 2s of silence after**
edit: riser before it · the pie fills 0 → 47% with a count-up on "almost" (1st occurrence) · impact hit
host: N02 "almost" → N06 "and"
Pie label: MIND ELSEWHERE: **47%**. Small line under it: Killingsworth & Gilbert, 2010.
narration: "Almost half the time... people's minds were somewhere else. And when their minds wandered, they were usually less happy than when they were focused on what they were doing."

**E20** · picture S22 (COPY: narrator in bed at night, face lit by his phone) · camera zoom-in
edit: snap zoom to his face on "running"
narration: "So your mind isn't lazy when it feels drained. It might just be running too many things you can't see."

---

## PART 3: The 4 background apps (`audio/part3.mp3`)

**E21** · CODED battery · camera hold
edit: the phone frame pops in on "running"; the four rows appear one by one on "four" (0.12s apart), bars at zero
host: N06 "so"
narration: "So what's actually running in the background? From all this research, there are four kinds of "apps" that seem to drain people the most."

**E22** · picture S11 (NEW: a house party, the narrator holding a cup with embarrassed eyes, a stickman friend smiling politely) · camera zoom-in
edit: snap zoom to the narrator on "said" → whip slide to the friend on "meant"
narration: "One. The replay. The conversation you keep going over. What you said. What you should have said. What they meant by that look."
beats: step "one" → APP 1 + THE REPLAY · icon I63 "going"

**E23** · CODED battery (REPLAY row active) · camera hold
edit: the REPLAY bar grows on "rumination" · pill RUMINATION
host: N06 "psychologists"
narration: "Psychologists call this rumination. And it's strongly linked to having a harder time falling asleep, and to feeling worse the next day."
beats: icon I68 "asleep"

**E24** · picture S11 · camera zoom-out
edit: soft light leak (memory) on "party" · snap zoom to the friend on "friend"
narration: "For me, it was one comment at a party. Something I said that came out wrong. I must have replayed it fifty times that week. The friend I said it to? He didn't even remember it. The worst part? Replaying it never changes how it went. It just runs the same video again."
beats: badge "fifty" → REPLAYED **50×** · pop N05 "remember" → card HE DIDN'T **EVEN REMEMBER**

**E25** · picture S12 (NEW: narrator standing at a fork in a road at dusk, phone in hand, frozen, two empty signposts) · camera zoom-in
edit: whip slide left path → right path on "text" · snap zoom to him on "remember"
narration: "Two. The decision you keep avoiding. Should I quit? Should I text them? Should I change what I'm studying? Remember that pull to go back to interrupted things? A decision you keep avoiding is the biggest interruption of all."
beats: step "two" → APP 2 + THE AVOIDED DECISION · icon I64 "quit"

**E26** · CODED battery (DECISION row active) · camera hold
edit: the DECISION bar pulses, rising and falling, on "opens", "away" and "again" (1st occurrence) · stamp PAUSED, NOT CLOSED on "paused"
host: N06 "an" → N05 "then" → N02 "that's"
narration: "An avoided decision isn't closed. It's paused. And every time something reminds you of it, your mind opens it right back up. Then you push it away again. And again. That's not resting. That's running the same app over and over without ever letting it finish."
beats: card "resting" → ~~NOT~~ RESTING

**E27** · picture S13 (NEW: narrator at a desk, laptop covered in many open windows and tabs, half-done papers everywhere) · camera zoom-in
edit: name pill SOPHIE LEROY on "Leroy" · snap zoom to the old half-done paper on "first"
narration: "Three. The half-finished task. A researcher named Sophie Leroy found that when people switched to something new while an older task was still unfinished, part of their attention stayed stuck on the first one."
beats: step "three" → APP 3 + THE HALF-FINISHED TASK

**E28** · CODED battery (HALF-DONE row active) · camera hold
edit: pill ATTENTION RESIDUE on "attention" · the bar grows on "worse"
host: N06 "she" → N01 "and"
narration: "She called it "attention residue." And those people did worse on the new task."

**E29** · picture S13 · camera zoom-in
edit: snap zoom to the tabs on "tabs"
narration: "So when you've got ten tabs open, three half-done assignments and an unanswered email... you're never fully anywhere."
beats: icon I65 "tabs" · card "anywhere" → NEVER FULLY **ANYWHERE**

**E30** · picture S37 (COPY: narrator sitting on a curb at dusk, thought bubbles) · camera zoom-in · crossfade in (calm moment)
edit: snap zoom to the thought bubbles on "friendship"
narration: "Four. The ending you never accepted. A friendship that faded without a real goodbye. A relationship that ended before you were ready. A version of yourself you thought you'd be by now."
beats: step "four" → APP 4 + THE ENDING YOU NEVER ACCEPTED · icon I66 "relationship"

**E31** · CODED battery (ENDING row active, the longest bar) · camera hold
edit: the ENDING bar grows the slowest and longest on "longest"
host: N06 "your" → N01 "it's" → N02 "that" (2nd occurrence)
narration: "Your mind keeps trying to write the last chapter, because nobody ever wrote it. It's part of why a song, a smell, or a random photo can drag you right back to something that ended years ago. That one usually runs the quietest... and the longest."
beats: icon I46 "chapter"

**E32** · picture S06 · camera zoom-out
edit: snap zoom to his open eyes on "lying"
narration: "Here's what all four have in common. None of them are on your screen. You can be lying in bed, doing nothing at all... and they're still running."

**E33** · CODED card, then the loop · camera hold
edit: card on "stop" (1st occurrence) · then the open loop from E15 closes into a full circle with a ding on "purpose"
host: N06 "so" → N01 "you" (3rd occurrence)
Card: ~~"STOP THINKING ABOUT IT"~~
narration: "So how do you close them? Not by forcing them out of your head. Telling yourself "stop thinking about it" usually makes you think about it more. You close them the same way you'd close an app. On purpose. One at a time."
beats: icon I69 "app"

---

## PART 4: The 5 steps and the ending (`audio/part4.mp3`)

**E34** · picture S14 (NEW: narrator at a desk at night under a lamp, writing a long list on paper) · camera zoom-in
edit: snap zoom to the list on "paper"
narration: "So here's how I actually close them now. Five steps. One. Check your battery usage. Grab a piece of paper and write down everything that's still open in your head. Every conversation, every decision, every half-done thing. Don't fix anything yet. Just list it."
beats: step "one" → STEP 1 + CHECK YOUR BATTERY USAGE · icon I67 "write"

**E35** · CODED battery (all four rows, then they dim) · camera hold
edit: all four bars shrink a little on "quieter"
host: N01 "it"
narration: "It sounds too simple, but a lot of these apps get quieter the second you can actually see them."

**E36** · picture S15 (NEW: a sleep lab: a stickman in bed with a few sensor wires on his head, a researcher watching a monitor through a window) · camera zoom-in
edit: snap zoom to the sleeper on "lab" → whip slide to the researcher on "others"
host: N07 "two" → N01 "in"
narration: "Two. Write tomorrow's to-do list before bed. In one study, researchers brought people into a sleep lab. Before bed, some of them spent five minutes writing a to-do list for the next few days. Others wrote about things they'd already finished."
beats: step "two" → STEP 2 + TO-DO LIST BEFORE BED · icon I11 "five"

**E37** · CODED card · camera hold · **reveal: at least 2s of silence after "faster" (3rd occurrence)**
edit: riser before it · count-up to 9 on "nine" · impact hit
host: N02 "the" → N05 "it"
Card: ABOUT **9 MIN** FASTER. Small line under it: Scullin et al., 2018.
narration: "The to-do list group fell asleep faster. About nine minutes faster. And the more specific the list was, the faster they fell asleep. It was a small study. But it's five minutes and a pen."
beats: icon I67 "pen"

**E38** · picture S14 · camera zoom-in
edit: snap zoom to his pen on "decide"
narration: "Three. Give every open loop a plan. Remember the study where a plan made the distracting thoughts go away? You don't have to finish everything tonight. You just have to decide when, where, and how."
beats: step "three" → STEP 3 + GIVE IT A PLAN · card "when" → **WHEN. WHERE. HOW.**

**E39** · CODED split · camera hold
edit: the left side pops on "answer", the right side on "decision"
host: N01 "i'll"
Left: THE TEXT → **TOMORROW, LUNCH**. Right: THE DECISION → **BY FRIDAY**.
narration: ""I'll answer that text tomorrow at lunch." "I'll make that decision by Friday, after I talk to my brother." That's often enough for your mind to stop nudging you."
beats: icon I13 "Friday"

**E40** · CODED battery (closing mode) · camera hold
edit: on "finish" the smallest row swipes off with a *swoosh*; on "close" (2nd occurrence) its bar empties
host: N07 "four" → N01 "pick"
narration: "Four. Close one small app today. Pick the smallest thing on your list and finish it. Send the reply. Make the easy decision. Delete the thing you're never going to do. Every loop you close is one less thing running in the background."
beats: step "four" → STEP 4 + CLOSE ONE SMALL APP · icon I41 "reply"

**E41** · picture S16 (NEW: narrator sitting on his bed laughing at his phone, the screen showing a laughing emoji reply) · camera zoom-in
edit: snap zoom to the phone on "replied"
narration: "For me, it was finally texting that friend: "Hey, that thing I said at the party came out wrong." It took thirty seconds. He replied, "lol what?" And that replay never ran again."
beats: card "lol" → "LOL **WHAT?**"

**E42** · picture S17 (NEW: narrator writing in a notebook by a window at dusk, calm) · camera zoom-in · crossfade in (calm moment)
edit: snap zoom to the notebook on "writing"
narration: "Five. Let some things end. For the endings you never got, try writing it out. Fifteen minutes. What happened, how it felt, and what you'd want the last chapter to say."
beats: step "five" → STEP 5 + LET SOME THINGS END · icon I43 "fifteen"

**E43** · picture S20 · camera zoom-in
edit: name pill JAMES PENNEBAKER on "Pennebaker"
host: N06 "a"
narration: "A psychologist named James Pennebaker found that when people wrote about things that were still weighing on them, for a few days in a row, they went to the doctor less often over the next few months. You can't always get a real goodbye. But you can stop waiting for one."
beats: card "stop" → STOP **WAITING FOR ONE**

**E44** · picture S23 · camera zoom-in
narration: "Here's what I keep coming back to. For a long time, I thought I was tired because I wasn't sleeping enough. But I could sleep for nine hours, and I still woke up with all my apps open."

**E45** · picture S03 (the cold-open painting, a callback) · camera hold · **reveal: at least 2s of silence after**
edit: crossfade in · slow push (cold-open style) · serif text fades in on "close": "Sleep turns the screen off."
narration: "Sleep turns the screen off. It doesn't close what's running."

**E46** · picture S05 · camera zoom-in
edit: slow push to the faces · serif "Open Your Eyes." fades in on "eyes"
narration: "So open your eyes to what's running in the background."

**E47** · picture S31 (COPY: narrator on a hilltop at sunrise) · camera zoom-out
edit: iris reveal into the sunrise on "close" · pills pop top-center one by one: **CLOSE** on "close", **PLAN** on "plan", **LET GO** on "let" · light sweep on "fewer"
narration: "Close what you can. Plan what you can't. And let go of what's already over. Because sometimes, you don't need more rest. You need fewer things running."

**E48** · picture S29 (COPY: narrator on the right, pointing left; end screen) · camera hold · hold the last frame 5s after the narration
narration: "So what's running in your background right now? Tell me in the comments. Just one word. And if the app that's draining you is a decision you keep avoiding, I made a whole video on why the safe choice isn't always safe. I'll leave it right here."
beats: pop N06 "running" → card **ONE WORD** (finish it before "and if" so the end screen stays clean)

---

## New diagram kinds to add to `tools/build-part.mjs`

Same look as before: cream background, 9px ink outlines, Nunito ExtraBold, yellow or red outlined badges, seek-safe.

- **battery:** a big rounded phone outline (ink, 9px) holding a "battery usage" list with 4 rows: REPLAY (icon I63), DECISION (I64), HALF-DONE (I65), ENDING (I66). Each row has a small icon, a label (≥ 56px) and a horizontal bar (terracotta fill, ink outline). Options: `appear` (rows pop in on a word), `active` (that row full-color, the rest at 40%), `grow: [row, word, width]`, `pulse: [row, words]` (bar rises and falls), `shrinkAll` (word), `close: [row, word]` (the row swipes off right, 0.3s, with a *swoosh*). Used in E21, E23, E26, E28, E31, E35, E40.
- **loop:** a thick ink circle with a gap at the top (an "open loop"), drawn on with stroke-dashoffset over 1s; a small mustard arrow travels along it on `nudge`; option `close` makes the gap close into a full circle with a ding. Used in E15 and E33.
- **pie, split, card → card swap, iconRow:** reuse the existing kinds (pie at 47%, E19).
- **Cold-open text:** small serif overlay (Georgia, about 64px, muted red `#B5484A` or off-white), top-center, fade in 0.4s. Used in E03, E05, E45, E46 and the title card.

### Description sources (for Luke, not on screen)
- Zeigarnik, B. (1927), on the recall of finished and unfinished tasks, *Psychologische Forschung*
- Ghibellini & Meier (2025), "Interruption, recall and resumption: a meta-analysis of the Zeigarnik and Ovsiankina effects," *Humanities and Social Sciences Communications*
- Masicampo & Baumeister (2011), "Consider it done! Plan making can eliminate the cognitive effects of unfulfilled goals," *JPSP*
- Killingsworth & Gilbert (2010), "A wandering mind is an unhappy mind," *Science*
- Leroy (2009), "Why is it so hard to do my work? The challenge of attention residue when switching between work tasks," *OBHDP*
- Scullin et al. (2018), "The effects of bedtime writing on difficulty falling asleep," *Journal of Experimental Psychology: General*
- Pennebaker & Beall (1986), expressive writing, *Journal of Abnormal Psychology*
