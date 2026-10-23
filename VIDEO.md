# Current video: "The Psychology of Overthinking" (final title TBD)

**Working title:** Why You Replay Conversations at 2 AM (Psychology of Overthinking). Luke will pick the final title later; the title card just says PSYCHOLOGY OF / OVERTHINKING.
**Topic:** overthinking (rumination) feels like problem solving but makes you worse at it. The liking gap, mind-wandering, worry predictions. Four traps (it feels like solving, predicting the worst, everyone's judging me, autopilot habit) and five research-backed ways out.
**Follows:** `PLAYBOOK.md` (cold open with a study → personal story → research → 4 traps → 5 steps → emotional close). It points to the procrastination video at the end.
**Length:** the raw voice is about 1,590 words. After pause padding, the target is about **11:00**.
**Audio:** 15 clips, `audio/part1a.mp3` … (Part 1 a–c, Part 2 a–b, Part 3 a–d, Part 4 a–f). Run `python3 tools/join-clips.py` first.
**Music:** `music/track.mp3`, mixed softly. Keep it at its quietest during the cold open (D01–D10) and the final scenes (D78–D79).
**Upload kit:** `prompts/upload-package.md`.
**Spec examples:** copy the helpers from `videos/06-procrastination/make-specs.py` (the newest build: it reads narration and host tracks straight from VIDEO.md, and uses loop, lines2, bars3, people, dots, split `fs0`, red screen badges). Copy the word-timing steps from `videos/06-procrastination/VIDEO.md` ("Build status") if Whisper can't download its model.

## Inputs (checked Oct 23)

- **Audio:** all 15 clips are in `audio/` and already joined into `audio/part1-4.mp3` (raw total about 9:16; about 11:10 after padding). Clip order was checked (steady 2.7–3.3 words per second).
- **Pictures:** 20 of 21 are in `pictures/` (plus S20 and S29). **S05b is missing**, so D13–D14 reuse S04.
- **Icons:** I89–I97 are in `icons/` (1376×768, fine for icons). **I98 is missing**, so D16 uses I91.
- `scenes/partN.rawwords.json` already holds forced-alignment word times for the raw parts (`tools/align.py`). Use Whisper if it works; if not, continue from these with the steps in `videos/06-procrastination/VIDEO.md` ("Build status").

## How to read this list

- **Scene IDs (D01…) and picture files (S01.png…) are separate.** `(NEW)` = Luke makes it (`prompts/nano-banana-prompts.md`). `(COPY)` = already in `pictures/`. `CODED` = build it in code.
- **beats:** key moments with the exact trigger word in quotes: `icon Ixx "word"`, `pop Nxx "word" → content`, `card "word" → TEXT`, `step "word" → STEP n + TEXT`, `badge "word" → TEXT`. **Bold** = yellow badge, ~~struck~~ = red badge. Fill the rest per CLAUDE.md (every shot ≤ 4s, except the cold-open scenes).
- **edit:** specific moves (CLAUDE.md section 9). **host:** the narrator-host pose track; no `host:` line = full-frame.
- **narration** is for timing only and must match the audio. Never show it on screen.
- **Icons:** I89–I97 are new (I98 was not made) (`prompts/icon-prompts.md`). I80, I84, I85 and I86 are reused from video 6 (already in `icons/`). Missing icon → skip that beat.
- **Numbers:** Whisper may write "two thousand eighteen" as "2018", "forty-seven percent" as "47%", "ninety-one percent" as "91%", "thirteen hundred" as "1,300", "two thousand two hundred fifty" as "2,250", "thirty-minute" as "30-minute", "B-plus" as "B+". Match triggers either way.
- **Names:** Nolen-Hoeksema ("NO-len HOOK-sma"), Beilock ("BYE-lock"), Borkovec ("BOR-ko-vek"). If Whisper writes them differently, match the scene by its other words. The forced-alignment fallback (`tools/align.py`) already has pronunciations for them.

---

## The cold open

D01–D10 are in the normal comic style, but slightly slower and calmer: shots may run up to **4.5s**, moves are snap zooms and soft pushes on words, and the music stays at its quietest. After D10, show the **title card** right away: green pill **LESSON**, big text PSYCHOLOGY OF / OVERTHINKING, with "OVERTHINKING" in orange, 2.5s.

## The narrator host

Same rules as before (poses from the tone tags, frame on the right, hard-cut pose changes, never animated, he stays put between host scenes). Host scenes are pictures without the narrator, icons used as the main picture, and coded diagrams. No host stretch longer than about 40s.

---

## PART 1: The cold open and my story (`audio/part1.mp3`)

**D01** · picture S01 (NEW: the narrator asleep in bed at night, eyes closed, a small glowing bedside clock, dark blue room) · camera zoom-in
edit: snap zoom to the glowing clock on "two" · snap zoom to his closed eyes on "closed"
narration: "It's two in the morning. You're exhausted. Your eyes are closed."

**D02** · picture S01 · camera zoom-in
edit: snap zoom to his brain head on "brain" · thought-bubble pill "REMEMBER THAT THING YOU SAID TODAY?" on "remember"
narration: "And then your brain says, "Hey. Remember that thing you said today?""

**D03** · picture S01, swapping to S01b on "wide" (NEW, edit of S01: the same bed, but his eyes snap wide open, and a thought bubble above his head shows a tiny scene of him talking awkwardly to a stickman) · camera zoom-in
edit: hard swap to S01b on "wide", with a ding · snap zoom to the thought bubble on "replaying"
narration: "And now you're wide awake. Replaying it."

**D04** · picture S01b · camera zoom-in
edit: three thought-bubble pills pop beside him: "WHY DID I SAY IT LIKE THAT?" on "say", "DID THEY THINK I WAS WEIRD?" on "weird", "WHY DID I LAUGH AT MY OWN JOKE?" on "laugh"
narration: ""Why did I say it like that?" "Did they think I was weird?" "Why did I laugh at my own joke?""

**D05** · picture S02 (NEW: the narrator lying in bed staring up; a beam from his glowing brain projects the same tiny awkward conversation onto the ceiling like a movie, with a film strip of the same frame repeating over and over) · camera zoom-in
edit: snap zoom to the ceiling movie on "conversation" · badges count up: **10 SECONDS** on "ten", ~~50 TIMES~~ on "fifty"
narration: "Ten seconds of a conversation... and you've watched it fifty times."

**D06** · picture S03 (NEW: two stickman strangers sitting across a small café table, chatting; one in a sage shirt smiles warmly, the other in a sky-blue shirt looks nervous; a stickman researcher with a clipboard in the background) · camera zoom-in
edit: push wipe in (time jump) on "in" · name pill BOOTHBY ET AL. (2018) on "researchers" · badge **5 MINUTES** on "five"
host: N02 "here's"
narration: "Here's what's strange. In two thousand eighteen, a team of researchers paired up strangers and had them talk for just five minutes."

**D07** · picture S03 · camera zoom-in
edit: tour: snap zoom to the warm stickman on "liked" (1st occurrence) → whip slide to the nervous stickman on "thought"
host: N02 "afterward"
narration: "Afterward, each person rated how much they liked the other one, and how much they thought the other one liked them."

**D08** · CODED bars3 · camera hold
edit: bars grow on "partner"
host: N06 "almost" → N02 "their"
Bars (no numbers): HOW MUCH THEY THOUGHT THEY WERE LIKED (sky, shorter) vs HOW MUCH THEY WERE ACTUALLY LIKED (sage, taller). Title: AFTER 5 MINUTES OF TALKING.
narration: "Almost everyone made the same mistake. Their partner liked them more than they thought."

**D09** · picture S03b (NEW, edit of S03: the same café table; now a thought bubble above the warm stickman shows a big smiling heart, while the nervous one still frowns) · camera zoom-in
edit: snap zoom to the heart bubble on "called" · badge **THE LIKING GAP** on "liking"
host: N02 "the"
narration: "The researchers called it the liking gap."

**D10** · picture S01b · camera zoom-in · **reveal: at least 2s of silence after**, then the title card
edit: soft riser · snap zoom to his wide eyes on "replaying" · impact hit on "better"
narration: "The conversation you're replaying at two A.M.? It probably went better than you think."
beats: card "better" → IT WENT **BETTER** THAN YOU THINK

**D11** · picture S04 (NEW: the narrator sitting on a couch staring at his phone, a sweat drop on his brain head; on the phone screen, one sent message bubble and no reply) · camera zoom-in
edit: hard cut from the title card · snap zoom to the phone on "message"
narration: "I do this all the time. A few weeks ago, I sent someone a message, and they took a few hours to reply."
beats: icon I89 "reply"

**D12** · picture S05 (NEW: the narrator surrounded by floating crumpled drafts and little grey thought clouds; in one big thought cloud, a wooden bridge between him and a stickman friend is crumbling) · camera zoom-in
edit: badge ~~20 TIMES~~ on "twenty" · tour: snap zoom to the floating drafts on "apologies" → whip slide to the crumbling bridge on "friendship"
narration: "In those few hours, I reread my message about twenty times, decided it sounded rude, wrote three different apologies in my head, and imagined the whole friendship falling apart."

**D13** · picture S04 (S05b was not made, so reuse S04: the narrator on the couch staring at his phone) · camera zoom-in
edit: whip-pan cut in on "then" · snap zoom to the phone on "haha" · speech pill "HAHA SORRY, I WAS AT THE GYM" on "haha"
narration: "Then they replied. "Haha sorry, I was at the gym.""

**D14** · picture S04 · camera zoom-out
edit: zoom out on "brain"
narration: "And it wasn't even a big deal. It was one text. My brain had worked for hours... and solved absolutely nothing."
beats: pop N10 "brain" → card SOLVED **NOTHING**

**D15** · icon I90 as the main picture · camera hold
edit: snap zoom into the film reel on "replaying"
host: N06 "so"
narration: "So why does your brain do this? Why does it keep replaying things it can't change?"

**D16** · CODED iconRow · camera hold
host: N01 "by"
Icons: I91 on "know" (I98 was not made), I84 on "four", I95 on "five". Labels: THINKING VS OVERTHINKING · 4 TRAPS · 5 WAYS OUT.
narration: "By the end of this video, you'll know the difference between thinking and overthinking, the four traps that keep your mind stuck on repeat, and five research-backed ways to finally turn it off."

**D17** · CODED card · camera hold
edit: count-up 10 on "ten"
host: N01 "one"
Card: **10 MINUTES** / AND A PIECE OF PAPER (small second line).
narration: "One of them takes ten minutes and a piece of paper."

---

## PART 2: What overthinking really is (`audio/part2.mp3`)

**D18** · picture S06 (NEW: the narrator running hard inside a giant hamster wheel in a dim room, sweat drops, the wheel spinning fast, going nowhere) · camera zoom-in
edit: snap zoom to the wheel on "over" · badge **RUMINATION** on "rumination"
narration: "Psychologists have a name for this. Rumination. Thinking about the same problem, over and over, without getting anywhere."

**D19** · picture S20 (COPY: researcher at a desk with a huge pile of notes) · camera zoom-in
edit: name pill SUSAN NOLEN-HOEKSEMA on "psychologist" · snap zoom to the researcher on "surprising"
host: N06 "psychologist"
narration: "Psychologist Susan Nolen-Hoeksema spent decades studying it, and she found something surprising."

**D20** · CODED card, swapping to card B on "worse" · camera hold
edit: kinetic swap to card B with a ding · impact hit on "worse"
host: N02 "rumination"
Card A: FEELS LIKE **SOLVING**. Card B: MAKES YOU ~~WORSE~~ AT IT.
narration: "Rumination feels like problem solving. But it makes you worse at it."

**D21** · CODED bars3 · camera hold
edit: bars grow on "worse"
host: N01 "in"
Bars (no numbers), title HOW GOOD THE SOLUTIONS WERE: AFTER RUMINATING (red, short) vs AFTER THINKING ABOUT SOMETHING ELSE (sage, tall).
narration: "In her studies, people who spent a few minutes ruminating came up with worse solutions to problems than people who spent the same time thinking about something else."

**D22** · picture S06 · camera zoom-out
edit: snap zoom to his sweating face on "harder" · zoom out on "less"
narration: "They were thinking harder. And getting less done."

**D23** · CODED split · camera hold
edit: left side pops on "thinking" (1st occurrence), right side on "overthinking" · speech pills: "WHAT CAN I DO ABOUT THIS?" on "what" (1st occurrence), "WHY? WHAT DOES IT SAY ABOUT ME?" on "why"
host: N08 "here's" → N01 "thinking" → N02 "overthinking"
Left (sage): THINKING → **NEXT STEP**. Right (red): OVERTHINKING → ~~LOOPS~~.
narration: "Here's the easiest way to tell the difference. Thinking moves you toward a next step. "What can I do about this?" Overthinking just loops. "Why did this happen? What does it say about me? What if it happens again?""

**D24** · CODED card, swapping to card B on "other" · camera hold
host: N06 "one"
Card A: ENDS IN **ACTION**. Card B: ENDS ~~WHERE IT STARTED~~.
narration: "One ends with an action. The other ends right where it started."

**D25** · picture S07 (NEW: the narrator gripping the steering wheel of a small car stuck in deep mud, the back wheel spinning and spraying mud, engine smoke puffing, the car not moving) · camera zoom-in
edit: snap zoom to the spinning wheel on "spinning" → whip slide to his face on "engine" · zoom out on "going"
narration: "It's like a car spinning its wheels in the mud. The engine is loud. You're just not going anywhere."
beats: icon I97 "mud"

**D26** · picture S08 (NEW: a busy city street; several stickmen doing everyday things: cooking at a window, riding a bus, typing at a desk; each has a little thought cloud showing somewhere else: a beach, an argument, a phone; a few phones show a notification bubble) · camera zoom-in
edit: push wipe in on "in" · name pill KILLINGSWORTH & GILBERT (2010) on "researchers" · badge **2,250 PEOPLE** on "people"
host: N01 "and"
narration: "And it happens way more than you'd think. In two thousand ten, Harvard researchers Matthew Killingsworth and Daniel Gilbert built an app that checked in on two thousand two hundred fifty people at random moments during their day."
beats: icon I80 "app"

**D27** · picture S08 · camera zoom-in
edit: tour: snap zoom to the cooking stickman on "doing" → whip slide to the bus rider on "thinking" · speech pills: "WHAT ARE YOU DOING?" on "doing", "WHAT ARE YOU THINKING ABOUT?" on "thinking"
host: N06 "it"
narration: "It asked, "What are you doing right now? And what are you thinking about?""

**D28** · CODED pie · camera hold
edit: soft riser · pie fills with a count-up to **47%** on "forty" · impact hit on "forty"
host: N02 "almost"
Pie label: MIND SOMEWHERE ELSE:
narration: "Almost forty-seven percent of the time, people's minds were somewhere else."

**D29** · picture S08 · camera zoom-out
edit: snap zoom to a stickman with a thought cloud on "wandered" · badge ~~LESS HAPPY~~ on "less"
host: N02 "and"
narration: "And when their minds wandered, they were less happy than when they were focused on what they were doing."

**D30** · CODED card · camera hold
edit: marker highlight on UNHAPPY MIND on "unhappy"
host: N06 "a"
Card: WANDERING MIND = / **UNHAPPY MIND**.
narration: "A wandering mind, the researchers wrote, is an unhappy mind."

**D31** · CODED bars3 · camera hold
edit: badge **1,300 ADULTS** on "thirteen" · bars grow on "ruminate" · badge **4×** on "four" · impact hit on "four"
host: N02 "and"
Bars, title DEVELOPED MAJOR DEPRESSION: RUMINATORS (red, 20%) vs NON-RUMINATORS (sky, 5%).
narration: "And it isn't harmless. In one survey of about thirteen hundred adults, Nolen-Hoeksema found that people who tended to ruminate were about four times more likely to develop major depression than people who didn't."

**D32** · picture S06 · camera zoom-out
edit: snap zoom to his tired face on "waste" · zoom out on "mood"
narration: "Overthinking doesn't just waste your time. Over time, it can wear down your mood."

**D33** · CODED card, swapping to card B on "loop" · camera hold
edit: red badges pop: ~~SMART~~ on "smart", ~~CAREFUL~~ on "careful", ~~DEEP~~ on "deep" · kinetic swap to card B
host: N02 "so" → N06 "it's"
Card A: NOT ~~SMART~~ ~~CAREFUL~~ ~~DEEP~~. Card B: A **LOOP**.
narration: "So overthinking isn't a sign that you're smart, or careful, or deep. It's a loop your brain gets stuck in."

**D34** · picture S06 · camera zoom-in
edit: snap zoom to his face on "begging"
narration: "But why does it get stuck? Why does the same thought keep coming back, even when you're begging it to stop?"

---

## PART 3: The four traps (`audio/part3.mp3`)

**D35** · icon I84 as the main picture · camera hold
edit: badge **4 TRAPS** on "four"
host: N01 "there"
narration: "There are four traps that keep the loop running."

**D36** · picture S09 (NEW: the narrator in front of a huge detective corkboard covered in photos and notes connected by a mess of red string, holding more string, exhausted eyes) · camera zoom-in
edit: snap zoom to the red strings on "replaying"
narration: "One. It feels like you're solving something. Your brain thinks replaying the problem is the same as fixing it."
beats: step "one" → TRAP 1 + IT FEELS LIKE SOLVING

**D37** · picture S09 · camera zoom-in
edit: thought-bubble pill "ONE MORE TIME…" on "one" · snap zoom to his face on "ready"
narration: "If you just think about it one more time, maybe you'll finally understand. Maybe you'll be ready next time."
beats: icon I91 "understand"

**D38** · picture S20 · camera zoom-in
edit: red badges: ~~MORE NEGATIVE~~ on "negative", ~~MORE PESSIMISTIC~~ on "pessimistic"
host: N02 "but"
narration: "But Nolen-Hoeksema's research found the opposite. Ruminating made people more negative, and more pessimistic about the future."

**D39** · CODED loop · camera hold
edit: nodes pop: REPLAY IT on "think", ANALYZE IT on "way", FEEL WORSE on "loop" · pulse on "around"
host: N05 "you"
narration: "You can't think your way out of a loop. You just go around it again."

**D40** · picture S10 (NEW: the narrator hunched over a glowing crystal ball that shows a dark storm and lightning, while the window behind him shows a sunny, calm day) · camera zoom-in
edit: snap zoom to the stormy crystal ball on "worst" · thought-bubble pills: "WHAT IF THEY'RE MAD?" on "mad", "WHAT IF I FAIL?" on "fail"
narration: "Two. Your brain predicts the worst. Overthinking is usually about the future. "What if they're mad?" "What if I fail?""
beats: step "two" → TRAP 2 + PREDICTING THE WORST

**D41** · picture S20 · camera zoom-in
edit: push wipe in on "in" · name pill PENN STATE (2020) on "researchers" · badge **10 DAYS** on "ten"
host: N01 "in"
narration: "In two thousand twenty, researchers at Penn State had people with anxiety write down their worries every day for ten days, then checked what actually happened."
beats: icon I94 "write"

**D42** · CODED pie · camera hold · **reveal: at least 2s of silence after**
edit: soft riser · pie fills with a count-up to **91%** on "ninety" · impact hit on "ninety"
host: N02 "ninety-one"
Pie label: NEVER CAME TRUE:
narration: "Ninety-one percent of those worries never came true."

**D43** · picture S10 · camera zoom-in
edit: snap zoom to the sunny window on "better" → whip slide to the crystal ball on "fortune"
narration: "And some of the ones that did turned out better than people expected. Your brain is a terrible fortune teller. It just sounds really confident."
beats: pop N05 "terrible" → card TERRIBLE **FORTUNE TELLER**

**D44** · picture S11 (NEW: after a conversation, the narrator and a stickman friend walk away from each other on a sidewalk; above the narrator a thought bubble replays a close-up of himself laughing awkwardly, red-faced; above the friend a thought bubble shows a big happy smiley face) · camera zoom-in
edit: zoom out to the whole picture on "liking"
narration: "Three. You think everyone's judging you. Remember the liking gap."
beats: step "three" → TRAP 3 + EVERYONE'S JUDGING ME

**D45** · picture S11 · camera zoom-in
edit: snap zoom to the narrator's replay bubble on "replays" · badges: PAUSE on "pause", WEIRD LAUGH on "laugh"
narration: "After a conversation, your brain replays your awkward moments, because those are the ones you were watching. You noticed every pause and every weird laugh."

**D46** · picture S11 · camera zoom-in
edit: whip slide to the friend's happy bubble on "other"
narration: "The other person mostly noticed that you were nice to talk to."

**D47** · CODED card · camera hold
edit: "MONTHS" pops on "months"
host: N02 "and"
Card: COLLEGE ROOMMATES: / THE GAP LASTED / **MONTHS**.
narration: "And in that research, the gap didn't fade after a few minutes. For college roommates, it lasted for months."

**D48** · picture S12 (NEW: the narrator alone in a car at night, stopped at a red light on an empty street, staring ahead; little grey thought clouds are starting to rise out of his brain head on their own) · camera zoom-in
edit: name pill WATKINS & NOLEN-HOEKSEMA on "psychologists" · snap zoom to the rising clouds on "habit" (2nd occurrence)
narration: "Four. It turns into a habit. Psychologists Ed Watkins and Susan Nolen-Hoeksema have argued that rumination works a lot like a habit."
beats: step "four" → TRAP 4 + IT'S A HABIT

**D49** · picture S12 · camera zoom-in
edit: snap zoom to the narrator on "car"
narration: "It gets linked to certain cues. Lying in bed. A quiet car ride. A phone that hasn't buzzed back."
beats: icon I93 "bed" · icon I89 "phone"

**D50** · CODED loop · camera hold
edit: nodes pop: THE CUE on "cue", THE LOOP STARTS on "starts", REPLAY on "think" · pulse on "anything"
host: N02 "when"
narration: "When the cue shows up, the loop starts on its own, before you've even decided to think about anything."

**D51** · picture S01b · camera zoom-in
edit: snap zoom to the bed on "bed"
narration: "That's why it always seems to hit at two A.M. Bed is the cue."
beats: card "bed" → BED IS **THE CUE**

**D52** · CODED list · camera hold
edit: items pop on their words
host: N02 "so"
Items: 1 FEELS LIKE SOLVING on "solving", 2 PREDICTS THE WORST on "worst", 3 EVERYONE'S JUDGING on "judging", 4 AUTOPILOT on "autopilot".
narration: "So put those four together. It feels like solving. Your brain predicts the worst. You think everyone's judging you. And it runs on autopilot."

**D53** · picture S09 · camera zoom-out
edit: snap zoom to his face on "cares" · zoom out on "wrong"
narration: "That's not a broken mind. That's a mind that cares a lot, stuck using the wrong tool."

---

## PART 4: Five ways out of the loop (`audio/part4.mp3`)

**D54** · CODED card · camera hold
edit: count-up 5 on "five"
host: N01 "so"
Card: **5** WAYS OUT.
narration: "So here's how to get out of the loop. Five steps."

**D55** · picture S13 (NEW: the narrator standing at a fork in a path: the left path leads to a ladder climbing up to a sunny hill; the right path curls into a small circular track that loops back on itself) · camera zoom-in
edit: tour: snap zoom to the ladder path on "solving" → whip slide to the looping path on "spinning" → zoom out on "question"
narration: "One. Ask, "Am I solving or spinning?" When you catch yourself replaying something, ask one question. "Is there something I can actually do about this right now?""
beats: step "one" → STEP 1 + SOLVING OR SPINNING?

**D56** · picture S13 · camera zoom-in
edit: snap zoom to the ladder path on "yes" · pills: SEND THE TEXT on "send", MAKE THE PLAN on "make"
narration: "If the answer is yes, do the smallest version of it. Send the text. Make the plan."
beats: icon I80 "text"

**D57** · CODED card, swapping to card B on "write" · camera hold
host: N01 "say"
Card A: CAN YOU **FIX IT** TOMORROW? Card B: WRITE THE FIX. **DONE.**
narration: "Say you're replaying a mistake from work. Can you fix it tomorrow? Then write down the fix, and you're done for tonight."

**D58** · picture S13 · camera zoom-in
edit: whip slide to the looping path on "spinning" (1st occurrence) · thought-bubble pill "OH, I'M SPINNING." on "oh"
narration: "If the answer is no, you're not solving anything. You're spinning. And just naming it, "Oh, I'm spinning," can give you a little distance from it."

**D59** · picture S14 (NEW: the narrator calmly dropping folded worry notes into a small wooden box with a round clock on its lid; a few notes are already inside) · camera zoom-in
edit: name pill TOM BORKOVEC on "psychologist" · snap zoom to the box on "schedule"
narration: "Two. Give your worries an appointment. Back in the nineteen-eighties, psychologist Tom Borkovec came up with a strange idea. Instead of trying to stop worrying, schedule it."
beats: step "two" → STEP 2 + A WORRY APPOINTMENT · icon I86 "schedule"

**D60** · picture S14 · camera zoom-in
edit: badge **30 MINUTES A DAY** on "thirty" · speech pill "NOT NOW. LATER." on "not"
narration: "Pick one thirty-minute window each day. When a worry shows up outside that window, write it down and tell yourself, "Not now. Later.""

**D61** · CODED bars3 · camera hold
edit: name pill NETHERLANDS (2011) on "study" · bars grow on "dropped"
host: N02 "in"
Bars (no numbers), title ANXIETY & STRESS DROPPED: STANDARD TREATMENT (sky, short) vs + WORRY TIME (sage, tall).
narration: "In a two thousand eleven study in the Netherlands, people who practiced this coped better with their problems, and their anxiety and stress dropped more than people who only got standard treatment."

**D62** · picture S14 · camera zoom-out
edit: snap zoom to the box on "finally" · zoom out on "simple"
narration: "When the thirty minutes finally come, a lot of those worries won't feel as urgent anymore. It sounds too simple. But your brain lets go more easily when it knows the worry has a time slot."

**D63** · picture S15 (NEW: the narrator at a desk writing on a sheet of paper; little grey worry clouds flow out of his brain head and turn into ink lines on the page; his eyes look lighter and calmer) · camera zoom-in
edit: name pill RAMIREZ & BEILOCK (2011) on "researchers" · badge **10 MINUTES** on "ten"
narration: "Three. Write it down. At the University of Chicago, researchers Gerardo Ramirez and Sian Beilock had students spend ten minutes writing about their worries right before a big exam."
beats: step "three" → STEP 3 + WRITE IT DOWN

**D64** · CODED bars3 · camera hold
edit: bars grow on "wrote" · impact hit on "minus"
host: N02 "students"
Bars, title ANXIOUS STUDENTS' FINAL GRADE: WROTE FIRST (sage, B+) vs DIDN'T WRITE (sky, B−).
narration: "Students with high test anxiety who wrote first averaged a B-plus. Anxious students who didn't write averaged a B-minus."

**D65** · picture S15 · camera zoom-in
edit: tour: snap zoom to the clouds leaving his head on "head" → whip slide to the page on "page" · zoom out on "test"
narration: "Writing it down moves the worry out of your head and onto the page, so your brain doesn't have to keep holding it. You can do it before a test, before bed, or any time a thought keeps circling."

**D66** · CODED card · camera hold
edit: marker highlight on 10-MINUTE on "ten"
host: N01 "this"
Card: THE **10-MINUTE** ONE / A PAPER AND A PEN (small second line).
narration: "This is the ten-minute one. Just a piece of paper and a pen."
beats: icon I94 "pen"

**D67** · picture S16 (NEW: the narrator walking calmly along a sunny park path under green trees, small birds, his eyes soft and relaxed) · camera zoom-in
edit: name pill STANFORD (2015) on "researchers" · badge **90 MINUTES** on "ninety"
narration: "Four. Go outside and walk. At Stanford, researchers sent people on a ninety-minute walk, either through nature or along a busy road."
beats: step "four" → STEP 4 + WALK OUTSIDE · icon I95 "nature"

**D68** · CODED split · camera hold
edit: left side pops on "nature", right side on "brain" · focus rack from left to right on "negative"
host: N02 "only"
Left (sage): NATURE WALK → **LESS RUMINATION**. Right (sky): BRAIN SCANS → **QUIETER**.
narration: "Only the nature walk reduced rumination. And brain scans showed less activity in an area linked to negative, self-focused thinking."

**D69** · picture S16 · camera zoom-in
edit: snap zoom to the trees on "green" · zoom out on "short" · light sweep along the path on "real"
narration: "You don't need a forest. A park, a quiet street with trees, anything green. It gives your brain something real to look at, instead of the replay. And even a short walk is a better use of that energy than watching the same conversation again."
beats: icon I85 "walk"

**D70** · picture S17 (NEW: the narrator happily absorbed in playing an acoustic guitar on his bed, focused content eyes; behind him a few grey thought clouds fade away) · camera zoom-in
edit: snap zoom to his focused eyes on "focused"
narration: "Five. Get absorbed in something. In Nolen-Hoeksema's experiments, people who spent a few minutes focused on something other than their problems felt better afterward."
beats: step "five" → STEP 5 + GET ABSORBED

**D71** · CODED loop · camera hold
edit: the loop from D39 (REPLAY IT → ANALYZE IT → FEEL WORSE) is already there · break on "interrupted"
host: N01 "not"
narration: "Not because the problem went away. Because the loop got interrupted. Even a few minutes can be enough to break the spin."

**D72** · picture S17 · camera zoom-in
edit: pills top-center one by one: A GAME on "game", A WORKOUT on "workout", COOKING on "cooking", MUSIC on "music", A FRIEND on "friend"
narration: "So pick something that takes your full attention. A game. A workout. Cooking. Music. A conversation with a friend."
beats: icon I96 "game"

**D73** · picture S04 · camera zoom-in
edit: snap zoom to the phone on "scrolling" · red badge ~~SCROLLING~~ on "scrolling"
narration: "Scrolling usually doesn't work, because it hands your brain new things to compare and worry about."

**D74** · picture S11 · camera zoom-in · crossfade in
edit: snap zoom to the narrator on "conversation" → whip slide to the friend's happy bubble on "other"
narration: "Here's what I keep coming back to. That conversation you replayed at two A.M.? The other person probably isn't thinking about it at all. And they probably liked you more than you think."

**D75** · picture S02 · camera zoom-in
edit: snap zoom to the ceiling movie on "guesses"
narration: "Your thoughts aren't facts. They're guesses your brain makes when it's tired and scared. Overthinking promises that if you just think hard enough, you'll be safe."
beats: card "facts" → THOUGHTS AREN'T **FACTS**

**D76** · picture S18 (NEW: the same bedroom as S01, now peaceful: the narrator sleeping calmly with a soft content look, moonlight through the window, the ceiling dark, no projector, no clouds) · camera zoom-in · crossfade in
edit: iris reveal into the picture on "but" · light sweep on "peace"
narration: "But you don't find peace at the end of the loop. You find it by stepping out of it."

**D77** · picture S18 · camera zoom-out · **at least 2s of silence after "tomorrow" (2nd occurrence)**
edit: pills top-center one by one: SOLVING OR SPINNING? on "solving", WRITE IT DOWN on "write", GO OUTSIDE on "outside"
narration: "So next time your brain hits replay, you don't have to watch. Ask if you're solving or spinning. Write it down. Go outside. And let tomorrow handle tomorrow."

**D78** · picture S29 (COPY: narrator on the right, pointing left; end screen) · camera hold · hold the last frame 5s after the narration
narration: "What's the thing your brain replays the most? Tell me in the comments. You might find out you're not the only one. And if your overthinking keeps stopping you from starting things, I made a whole video on why we procrastinate. I'll leave it right here."
beats: pop N06 "what's" → card YOUR **REPLAY?** (finish it before "and if" so the end screen stays clean)
