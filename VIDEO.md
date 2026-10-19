# Current video: "Psychology of Procrastination (And How to Trick Your Brain Out of It)"

**Topic:** procrastination isn't laziness, it's mood repair. Your brain trades a bad feeling now for a worse one later, and treats future you like someone else. Four traps (too big and blurry, a test of who you are, a reward too far away, the guilt loop) and five research-backed ways to start.
**Follows:** `PLAYBOOK.md` (cold open with a study → personal story → research → 4 traps → 5 steps → emotional close). It points to the self-doubt video at the end.
**Length:** the raw voice is about 1,600 words. After pause padding, the target is about **11:00**.
**Audio:** 15 clips, `audio/part1a.mp3` … (Part 1 a–c, Part 2 a–b, Part 3 a–d, Part 4 a–f). Run `python3 tools/join-clips.py` first.
**Music:** `music/track.mp3`, mixed softly. Keep it at its quietest during the cold open (D01–D08) and the final scenes (D71–D72).
**Upload kit:** `prompts/upload-package.md`.
**Spec examples:** copy the helpers from `videos/05-self-doubt/make-specs.py` (the newest build: quad, list, bars2, irow). It uses the same notation.

## How to read this list

- **Scene IDs (D01…) and picture files (S01.png…) are separate.** `(NEW)` = Luke makes it (`prompts/nano-banana-prompts.md`). `(COPY)` = already in `pictures/`. `CODED` = build it in code.
- **beats:** key moments with the exact trigger word in quotes: `icon Ixx "word"`, `pop Nxx "word" → content`, `card "word" → TEXT`, `step "word" → STEP n + TEXT`, `badge "word" → TEXT`. **Bold** = yellow badge, ~~struck~~ = red badge. Fill the rest per CLAUDE.md (every shot ≤ 4s, except the cold-open scenes).
- **edit:** specific moves (CLAUDE.md section 9). **host:** the narrator-host pose track; no `host:` line = full-frame.
- **narration** is for timing only and must match the audio. Never show it on screen.
- **Icons:** I79–I88 are all new (`prompts/icon-prompts.md`). Missing icon → skip that beat.
- **Numbers:** Whisper may write "nineteen-nineties" as "1990s", "two thousand thirteen" as "2013", "nineteen eighty-four" as "1984", "ninety-four" as "94", "a hundred and thirty-four" as "134", "seven o'clock" as "7 o'clock". Match triggers either way.
- **Pychyl** is said "PIE-kul". If Whisper writes it differently, match the scene by its other words.
- **New diagram kind: `loop`.** Three labeled nodes on a circle (cream tiles, 9px ink outline) joined by curved ink arrows that run clockwise. Nodes pop on their words (`back.out`). "Pulse" = the arrows race around once (0.4s) with a swoosh. "Break" = one arrow snaps in two with a small crack line and a ding, and the loop stops. Add it to `tools/build-part.mjs`.

---

## The cold open

D01–D08 are in the normal comic style, but slightly slower and calmer: shots may run up to **4.5s**, moves are snap zooms and soft pushes on words, and the music stays at its quietest. After D08, show the **title card** right away: green pill **LESSON**, big text PSYCHOLOGY OF / PROCRASTINATION, with "PROCRASTINATION" in orange (shrink to fit), 2.5s.

## The narrator host

Same rules as before (poses from the tone tags, frame on the right, hard-cut pose changes, never animated, he stays put between host scenes). Host scenes are pictures without the narrator, icons used as the main picture, and coded diagrams. No host stretch longer than about 40s.

---

## PART 1: The cold open and my story (`audio/part1.mp3`)

**D01** · picture S01 (NEW: the narrator sitting at his desk at night, laptop open, one sticky note on the laptop, a wall clock at 9) · camera zoom-in
edit: snap zoom to the wall clock on "nine" → whip slide to the sticky note on "thing"
narration: "It's nine at night. You have one thing to do. One."

**D02** · picture S02 (NEW: the narrator happily spraying and wiping an already tidy desk, laptop pushed to the side) · camera zoom-in
edit: hard cut in on "so" · snap zoom to the spray bottle on "clean"
narration: "So you sit down... and decide your desk is too messy to work at. So you clean the desk."

**D03** · picture S02 · camera zoom-out
edit: punch-in crop on his face on "video" (1st occurrence)
narration: "Then you reply to a few messages. Then you watch a video. Maybe even a video about how to stop procrastinating."
beats: icon I80 "messages" · card "procrastinating" → HOW TO STOP **PROCRASTINATING**

**D04** · picture S03 (NEW: the narrator lying in bed in the dark at midnight, eyes open, staring at the ceiling; across the room the closed laptop with the sticky note) · camera zoom-in
edit: snap zoom to the laptop on "thing" · zoom back to his face on "lie" · two thought-bubble pills pop above him: "WHAT IS WRONG WITH ME?" on "wrong", "WHY AM I SO LAZY?" on "lazy"
narration: "And by midnight, the one thing still isn't done. So you lie in bed thinking, "What is wrong with me? Why am I so lazy?""

**D05** · picture S04 (NEW: a sunny college campus early in the term; one relaxed stickman student lies in a hammock reading a comic while other students rush past carrying books) · camera zoom-in
edit: push wipe in (time jump) on "in" · name pill TICE & BAUMEISTER (1997) on "psychologists"
host: N02 "here's"
narration: "Here's the thing. In the nineteen-nineties, two psychologists followed a group of college students through an entire semester."

**D06** · picture S04 · camera zoom-in
edit: snap zoom to the stickman in the hammock on "procrastinators" · badges pop beside him: **LESS STRESS** on "less", **FEWER HEALTH PROBLEMS** on "fewer" · whip slide to the rushing students on "rushing"
host: N06 "and"
narration: "And early on, the procrastinators were actually doing better. Less stress. Fewer health problems. They were relaxed, while everyone else was rushing."

**D07** · picture S04b (NEW, edit of S04: the same campus at the end of term, grey and rainy; the same stickman now buried in papers at a desk, a thermometer in his mouth, panicking, while the other students relax) · camera zoom-in
edit: whip-pan cut to S04b on "flipped", with a ding · red badges pop beside him: ~~MORE STRESS~~ on "stressed", ~~SICKER~~ on "sick", ~~LOWER GRADES~~ on "grades"
host: N02 "but"
narration: "But by the end of the semester, everything flipped. The procrastinators were more stressed, they got sick more often, and they got lower grades on every single assignment."

**D08** · CODED lines · camera hold · **reveal: at least 2s of silence after**, then the title card
edit: soft riser into the scene · lines draw on "avoided" · badge **BORROWED** on "borrowed" · impact hit on "future"
host: N02 "they" → N06 "they" (2nd occurrence)
Lines (no numbers, just the shape): x-axis START OF TERM → END OF TERM, y-axis STRESS. PROCRASTINATORS (red) starts low and climbs steeply. EVERYONE ELSE (sky) stays flat in the middle. The red line crosses the blue one.
narration: "They hadn't avoided the stress. They had just borrowed it... from their future selves."

**D09** · picture S05 (NEW: the narrator very busy at his desk: floating neat folders, a screen full of productivity videos, a stack of to-do lists; in the corner of the desk one closed notebook glows softly under its own little spotlight, untouched) · camera zoom-in
edit: hard cut from the title card · snap zoom to the glowing notebook on "idea"
narration: "I know this one really well. I had the idea for this video over a week ago."
beats: icon I83 "week"

**D10** · picture S05 · camera zoom-in
edit: tour: snap zoom to the floating folders on "folder" → whip slide to the videos on the screen on "videos" → whip slide to the stack of to-do lists on "made"
narration: "And in that week, I reorganized every folder on my computer, I watched four videos about other people's productivity systems, and I made a to-do list... for my to-do list."

**D11** · picture S05 · camera zoom-out
edit: zoom out to the whole desk on "strange" · snap zoom plus a hand-drawn circle around the glowing notebook on "except"
narration: "Then I made a thumbnail for a video I hadn't even written yet. And the strange part is, I wasn't being lazy. I was working really hard. Just on everything except the one thing that mattered."
beats: pop N10 "thumbnail" → card NO SCRIPT **YET**

**D12** · icon I81 as the main picture · camera hold
edit: snap zoom into the open door on "run"
host: N06 "so"
narration: "So why do we do this? Why does your brain run from the exact things you care about most?"

**D13** · CODED iconRow · camera hold
host: N01 "by"
Icons: I88 on "really", I84 on "four", I85 on "five". Labels: WHAT IT REALLY IS · 4 TRAPS · 5 WAYS TO START.
narration: "By the end of this video, you'll know what procrastination really is, the four traps that keep you stuck, and five research-backed ways to finally get started."

**D14** · CODED card · camera hold
edit: marker highlight on OPPOSITE on "opposite"
host: N01 "and"
Card: THE **OPPOSITE** OF WHAT MOST PEOPLE DO (small second line).
narration: "And the last one is the opposite of what most people do. It's the one that surprised me the most."

---

## PART 2: What procrastination really is (`audio/part2.mp3`)

**D15** · icon I79 as the main picture · camera hold
edit: snap zoom to the clock on "time" (2nd occurrence) · red badges pop top-center: ~~BAD PLANNING~~ on "bad", ~~NOT ENOUGH DISCIPLINE~~ on "discipline"
host: N01 "for"
narration: "For a long time, people thought procrastination was a time problem. Bad planning. Not enough discipline."

**D16** · picture S20 (COPY: researcher at a desk with a huge pile of notes) · camera zoom-in
edit: name pill TIM PYCHYL on "psychologist" · snap zoom to the researcher on "different"
host: N06 "but"
narration: "But psychologist Tim Pychyl has studied procrastination for decades, and he says something different."

**D17** · CODED card, swapping to card B on "emotion" · camera hold
edit: ~~TIME~~ stamps on "time" · kinetic swap to card B with a ding · impact hit on "emotion"
host: N02 "procrastination"
Card A: A ~~TIME~~ PROBLEM? Card B: AN **EMOTION** PROBLEM.
narration: "Procrastination isn't a time management problem. It's an emotion management problem."

**D18** · CODED split · camera hold
edit: name pill SIROIS & PYCHYL (2013) on "psychologist" · left side pops on "better", right side on "expense" · focus rack from left to right on "future"
host: N06 "in"
Left (sage): **FEEL BETTER NOW**. Right (red): FUTURE YOU ~~PAYS~~.
narration: "In two thousand thirteen, he and psychologist Fuschia Sirois described it as choosing to feel better right now, at the expense of your future self."

**D19** · picture S06 (NEW: the narrator at his desk staring at one sheet of paper; around the paper float four small grey cartoon clouds with faces: a bored yawning one, a confused one with a question mark, a scared one, and one huge heavy one) · camera zoom-in
edit: tour: snap zoom to the bored cloud on "boring" → whip slide to the confused cloud on "confusing" → whip slide to the scared cloud on "scary" → zoom out to the huge cloud on "big"
narration: "Think about how a task makes you feel. Boring. Confusing. Scary. Too big."

**D20** · picture S06 · camera zoom-out
edit: snap zoom to his worried eyes on "feeling"
narration: "Your brain doesn't like that feeling. So it looks for a way out."
beats: icon I81 "way"

**D21** · picture S07 (NEW: the narrator snapping his laptop shut and leaning back with relief, happy closed eyes, little relief sparkles around him) · camera zoom-in
edit: snap zoom to his relieved eyes on "relief" · light sweep across him on "instantly"
narration: "And the second you avoid the task, you get a little reward. Relief. Close the laptop, and the bad feeling is gone. Instantly."
beats: card "relief" → **RELIEF**

**D22** · CODED loop · camera hold
edit: nodes pop: BAD FEELING on "every", AVOID on "avoid", RELIEF on "better" · center badge **"AVOIDING WORKS"** on "avoiding" · pulse on "faster"
host: N02 "and" → N06 "so"
narration: "And your brain remembers that. Every time you avoid something hard and feel better, your brain learns, "Avoiding works." So the next time, it reaches for that escape even faster."

**D23** · CODED card, swapping to card B on "loop" · camera hold
edit: ~~LAZY~~ stamps on "lazy" · kinetic swap to card B on "loop"
host: N02 "that's" → N06 "you're" (2nd occurrence)
Card A: NOT ~~LAZY~~. Card B: A **LEARNED LOOP**.
narration: "That's why procrastination can feel almost automatic. You're not deciding to be lazy. You're following a loop your brain learned to keep you comfortable."

**D24** · picture S08 (NEW: a brain-scan lab; a stickman lies in a big friendly MRI scanner while a stickman researcher looks at two brain-scan pictures side by side on a monitor) · camera zoom-in
edit: push wipe in on "in" · name pill HAL HERSHFIELD on "researcher" · snap zoom to the monitor on "scanned" · badges on the two scans: NOW on "now", +10 YEARS on "ten"
host: N01 "and"
narration: "And there's another piece to this. In two thousand nine, researcher Hal Hershfield and his team scanned people's brains while they thought about themselves now, and themselves ten years in the future."

**D25** · picture S09 (NEW: the narrator looking into a tall mirror; the reflection is not him but a dark, blurry, faceless stranger in a hoodie behind frosted glass) · camera zoom-in
edit: snap zoom to the narrator on "people" → whip slide to the blurry stranger in the mirror on "someone" · focus rack between them on "else"
narration: "When people thought about their future selves, their brain activity looked less like thinking about themselves... and more like thinking about someone else."

**D26** · picture S10 (NEW: the narrator relaxing on the couch, happily handing a big stack of homework and to-do papers to a tall grey silhouette standing in the doorway, its face hidden in shadow) · camera zoom-in
edit: snap zoom to the narrator on "tomorrow" → whip slide to the silhouette on "someone" · speech pill "I'LL DO IT TOMORROW" on "tomorrow"
narration: "So when you say, "I'll do it tomorrow," part of your brain hears, "Someone else will do it.""

**D27** · picture S10 · camera zoom-in
edit: three pills pop beside the silhouette: MORE MOTIVATED on "motivated", MORE RESTED on "rested", MORE ORGANIZED on "organized"
narration: "And that someone else is always more motivated, more rested, and more organized than you."

**D28** · picture S10b (NEW, edit of S10: the same doorway, but now the light reveals the silhouette is the narrator himself, tired eyes, holding the huge stack of papers) · camera zoom-in
edit: hard cut swap to S10b on "turn", with a ding · impact hit on "you"
narration: "Until tomorrow comes. And they turn out to be you."

**D29** · CODED card, swapping to card B on "choosing" · camera hold
edit: ~~LAZINESS~~ stamps on "laziness" · kinetic swap to card B
host: N06 "so"
Card A: NOT ~~LAZINESS~~. Card B: FEEL BETTER **NOW**.
narration: "So put it together. Procrastination isn't laziness. It's your brain choosing to feel better now, and sending the bill to a version of you it doesn't really see as you."
beats: icon I82 "bill"

**D30** · CODED grid · camera hold
edit: name pill PIERS STEEL on "researcher" · 20 little people in a 5×4 grid, 4 of them turn red on "one" · badge **1 IN 5** on "five" · all 20 pulse once on "alone"
host: N01 "researcher"
narration: "Researcher Piers Steel estimates that somewhere around one in five adults are chronic procrastinators. So if this sounds like you, you're definitely not alone."

**D31** · picture S05 · camera zoom-in
edit: snap zoom to the glowing notebook on "stuck" · badges count up beside it: DAYS on "days", WEEKS on "weeks", YEARS on "years"
narration: "But why does it get so stuck? Why do some tasks sit there for days, or weeks, or even years?"

---

## PART 3: The four traps (`audio/part3.mp3`)

**D32** · icon I84 as the main picture · camera hold
edit: badge **4 TRAPS** on "four"
host: N01 "researchers"
narration: "Researchers keep finding the same few traps. Here are the four that show up the most."

**D33** · picture S11 (NEW: the narrator standing small at the bottom of a giant foggy mountain made of tangled black scribbles, with no path and no first step) · camera zoom-in
edit: three fog pills pop over the mountain: WORK ON THE PROJECT on "work", GET IN SHAPE on "shape", FIGURE OUT MY LIFE on "figure"
narration: "One. The task is too big and too blurry. "Work on the project." "Get in shape." "Figure out my life.""
beats: step "one" → TRAP 1 + TOO BIG & BLURRY

**D34** · picture S11 · camera zoom-out
edit: zoom out to the whole mountain on "giant"
narration: "Your brain can't see where to start, so it all feels like one giant, heavy thing."

**D35** · picture S20 · camera zoom-in
edit: push wipe in (time jump) on "back" · name pill SOLOMON & ROTHBLUM (1984) on "psychologists" · snap zoom to the pile of notes on "hundreds"
host: N01 "back" → N02 "one"
narration: "Back in nineteen eighty-four, psychologists Laura Solomon and Esther Rothblum asked hundreds of college students why they put things off. One of the biggest reasons was simply that the task felt unpleasant to face."
beats: card "unpleasant" → THE TASK FELT **UNPLEASANT**

**D36** · picture S11 · camera zoom-in
edit: snap zoom to the narrator at the bottom on "step"
narration: "And nothing feels worse to face than a task with no clear first step."

**D37** · picture S12 (NEW: the narrator standing nervously in front of a giant blank exam paper; beside it a row of three stern stickman judges holding up blank score cards) · camera zoom-in
edit: snap zoom to the judges on "test" · red badge ~~FEAR OF FAILURE~~ on "fear"
narration: "Two. The task feels like a test of who you are. The other big reason in that same study was fear of failure."
beats: step "two" → TRAP 2 + A TEST OF YOU

**D38** · CODED card · camera hold
edit: marker highlight on NEVER FAIL on "fail"
host: N06 "if"
Card: NEVER START = **NEVER FAIL**.
narration: "If you never really start, you can never really fail."

**D39** · picture S12 · camera zoom-in
edit: snap zoom to the narrator on "tell" · thought-bubble pill "I COULD HAVE DONE IT GREAT…" on "could"
narration: "As long as it's unfinished, you can still tell yourself, "I could have done it great if I'd had more time.""

**D40** · picture S12 · camera zoom-out
edit: zoom out to the whole scene on "delay"
narration: "So the delay protects you. Not from the work... from finding out what you're capable of. That's why the thing you care about most is so often the thing you put off the longest."
beats: pop N06 "that's" → card CARE MOST = **PUT OFF LONGEST**

**D41** · picture S13 (NEW: the narrator standing on a long road; far away on the horizon a tiny shining gold trophy; right above his head a small grumpy grey rain cloud drizzling on him) · camera zoom-in
edit: snap zoom to the tiny trophy on "reward" → whip slide to the rain cloud over his head on "bad"
narration: "Three. Future you feels like a stranger. Remember those brain scans. The reward for doing the task lives in the future. The bad feeling lives right now."
beats: step "three" → TRAP 3 + THE REWARD IS FAR AWAY

**D42** · CODED bars2 · camera hold
edit: bars grow on "wins"
host: N05 "and"
Bars (no numbers), title HOW REAL IT FEELS: RIGHT NOW (red, tall) vs LATER (sky, short).
narration: "And right now always wins, because right now is the only one your brain fully believes in."

**D43** · CODED split · camera hold
edit: left side pops on "three", right side on "tomorrow" · impact hit on "emergency"
host: N01 "that's"
Left (sky): DEADLINE IN 3 WEEKS → "NOTHING". Right (red): DEADLINE TOMORROW → ~~EMERGENCY~~.
narration: "That's why a deadline three weeks away feels like nothing, and a deadline tomorrow feels like an emergency. Same task. Different distance."
beats: icon I86 "same"

**D44** · picture S14 (NEW: the narrator sitting on the floor hugging his knees inside a slow whirl of grey guilt clouds that circle around him like a ring) · camera zoom-in
edit: snap zoom to the circling clouds on "bad" (1st occurrence)
narration: "Four. The guilt loop. You put something off. Then you feel bad about it. And feeling bad is exactly the kind of feeling your brain wants to escape."
beats: step "four" → TRAP 4 + THE GUILT LOOP

**D45** · CODED loop · camera hold
edit: nodes pop: AVOID on "avoid" (1st occurrence), FEEL WORSE on "worse", AVOID MORE on "more" · pulse on "more"
host: N06 "so"
narration: "So you avoid the task even harder, which makes you feel worse, which makes you avoid it even more."

**D46** · picture S14 · camera zoom-out
edit: zoom out on "standing"
narration: "The shame doesn't push you forward. It becomes one more bad feeling standing between you and the work."

**D47** · CODED list · camera hold
edit: items pop on their words
host: N02 "so"
Items: 1 TOO BLURRY on "blurry", 2 A TEST on "test", 3 TOO FAR AWAY on "far", 4 THE GUILT LOOP on "guilt".
narration: "So put those four together. A task that's too blurry. A task that feels like a test. A reward that feels too far away. And guilt that keeps feeding the loop."

**D48** · picture S15 (NEW: the narrator holding up a small round cartoon shield, protecting himself from a giant looming task paper; his eyes are worried but brave, his brain glows warmly) · camera zoom-in
edit: snap zoom plus a hand-drawn circle around the shield on "protect"
narration: "That's not a lazy person. That's a brain trying to protect you, in a way that's quietly costing you the things you want most."

---

## PART 4: Five ways to start (`audio/part4.mp3`)

**D49** · CODED card · camera hold
edit: count-up 5 on "five"
host: N01 "so"
Card: **5** STEPS.
narration: "So here's what actually works. Five steps."

**D50** · picture S01 · camera zoom-in
edit: snap zoom to the laptop on "document"
narration: "One. Shrink it until it's almost silly. Don't "write the essay." Open the document and write one bad sentence. Don't "go to the gym." Just put your shoes on."
beats: step "one" → STEP 1 + SHRINK IT · icon I85 "shoes"

**D51** · picture S01 · camera zoom-in
edit: punch-in crop on the laptop on "small" · pill WRITE THE FIRST LINE on "line"
narration: "The goal isn't to finish. The goal is to make the first step so small that your brain has nothing to run from. For this video, my first step wasn't "write a script." It was "write the first line.""

**D52** · CODED card · camera hold
edit: marker highlight on HEAVIEST on "heaviest"
host: N01 "once"
Card: STARTING IS THE **HEAVIEST** PART.
narration: "Once you're moving, the task almost always feels lighter than you expected. Starting is the heaviest part."

**D53** · picture S20 · camera zoom-in
edit: name pill PETER GOLLWITZER on "psychologist" · snap zoom to the researcher on "exactly"
host: N07 "two" → N01 "psychologist"
narration: "Two. Make an if-then plan. Psychologist Peter Gollwitzer studied what he called implementation intentions. Instead of "I'll study this week," you decide exactly when and where."
beats: step "two" → STEP 2 + IF-THEN PLAN

**D54** · CODED card, swapping to card B on "then" · camera hold
host: N01 "if"
Card A: IF IT'S **7:00**… Card B: …THEN I OPEN MY NOTES.
narration: ""If it's seven o'clock, then I sit at my desk and open my notes.""

**D55** · CODED grid · camera hold
edit: name pill GOLLWITZER & SHEERAN (2006) on "researchers" · 94 small dots fill in with a count-up to **94 STUDIES** on "combined" · badge **MEDIUM-TO-LARGE EFFECT** on "effect" · impact hit on "goals"
host: N02 "when"
narration: "When researchers combined ninety-four studies on this, if-then plans had a medium-to-large effect on people actually reaching their goals."

**D56** · picture S01 · camera zoom-out
edit: snap zoom to the empty chair at the desk on "show"
narration: "Because you're not waiting to feel like it anymore. The decision has already been made. All you have to do is show up for it."

**D57** · picture S16 (NEW: the narrator at his laptop, surprised wide eyes, looking at the screen, which shows an aged-up older version of himself: a slightly greyer, wrinklier brain head with round glasses, waving back) · camera zoom-in
edit: snap zoom to the older face on the screen on "pictures"
narration: "Three. Meet your future self. In a later study, Hershfield showed people realistic aged-up pictures of their own faces."
beats: step "three" → STEP 3 + MEET FUTURE YOU

**D58** · CODED bars2 · camera hold
edit: bars grow on "willing" · badge **2×** on "twice" · ding
host: N02 "the"
Bars, title PUT AWAY FOR THE FUTURE: SAW THEIR FACE TODAY (sky, 1×) vs SAW THEIR OLDER FACE (sage, 2×).
narration: "The people who saw their older selves were willing to put away about twice as much money for the future."

**D59** · picture S16 · camera zoom-in
edit: snap zoom to the narrator's face on "ask" · thought-bubble pill "HOW WILL TOMORROW-ME FEEL?" on "how"
narration: "You can do the same thing without a photo. Before you put something off, ask, "How will tomorrow-me feel when they find this still waiting?" Then do one small thing as a favor to them."

**D60** · picture S09 · camera zoom-in · crossfade in
edit: focus rack onto the reflection on "just"
narration: "Future you isn't a stranger. They're just you, a little later."

**D61** · picture S17 (NEW: the narrator relaxed and smiling, drawing a messy, scribbly rough sketch on a big sheet of paper, eraser crumbs everywhere, not caring that it's messy) · camera zoom-in
edit: snap zoom to the messy sketch on "permission"
narration: "Four. Give yourself permission to do it badly. If fear of failure is what's stopping you, take the test away. Tell yourself, "This is just a rough draft. Nobody has to see it.""
beats: step "four" → STEP 4 + DO IT BADLY · icon I87 "draft"

**D62** · CODED split · camera hold
edit: left side pops on "fix", right side on "perfect" · focus rack from right to left on "can't"
host: N05 "a"
Left (sage): A ROUGH DRAFT → **FIXABLE**. Right (red): PERFECT IN YOUR HEAD → ~~STUCK~~.
narration: "A bad first version is something you can fix. A perfect version that only lives in your head is something you can't."

**D63** · picture S17 · camera zoom-out
edit: zoom out on "messy" (1st occurrence) · light sweep on "allowed"
narration: "Most good work starts out messy. You're allowed to be messy too."

**D64** · picture S18 (NEW: the narrator kneeling and gently helping a small, tired, sad version of himself up off the floor, a kind hand on his shoulder, warm light) · camera zoom-in
edit: snap zoom to the two of them on "forgive"
narration: "Five. Forgive yourself. This is the one that surprised me."
beats: step "five" → STEP 5 + FORGIVE YOURSELF

**D65** · picture S04 · camera zoom-in
edit: push wipe in (time jump) on "in" · name pill CARLETON UNIVERSITY on "researchers" · badge count-up **134 STUDENTS** on "students" · snap zoom to the students on "exams"
host: N01 "in"
narration: "In two thousand ten, researchers at Carleton University followed a hundred and thirty-four first-year students across two rounds of exams."

**D66** · CODED bars2 · camera hold
edit: bars grow on "forgave" · badge **LESS** on "less"
host: N02 "the"
Bars (no numbers), title PROCRASTINATION BEFORE EXAM 2: DIDN'T FORGIVE THEMSELVES (red, tall) vs FORGAVE THEMSELVES (sage, short).
narration: "The students who forgave themselves for procrastinating before the first exams procrastinated less before the second ones."

**D67** · CODED loop · camera hold
edit: the guilt loop from D45 (AVOID → FEEL WORSE → AVOID MORE) is already there · break on "breaks"
host: N06 "because"
narration: "Because forgiving yourself breaks the guilt loop. It takes away the bad feeling your brain was trying to escape."

**D68** · picture S18 · camera zoom-in
edit: snap zoom to the two of them on "catch" · ~~LAZY~~ pill pops and is crossed out on "lazy" · speech pill "WHAT'S THE SMALLEST NEXT STEP?" on "what's"
narration: "So next time you catch yourself putting something off, don't call yourself lazy. Say, "Okay. That happened. What's the smallest next step?""

**D69** · picture S05 · camera zoom-in · crossfade in
edit: snap zoom to the glowing notebook on "care" (1st occurrence)
narration: "Here's what I keep coming back to. Procrastination isn't proof that you don't care. Most of the time, it's proof that you care a lot. Enough that the task feels heavy. Enough that failing would hurt."
beats: card "lot" → YOU **CARE A LOT**

**D70** · picture S15 · camera zoom-in
edit: light sweep across the shield on "protecting"
narration: "Your brain isn't broken. It's been protecting you from a feeling, with a shortcut that costs more than it saves."

**D71** · picture S19 (NEW: the next morning; the same desk from S01 in warm sunrise light, the narrator sitting at it with the glowing notebook finally open, writing the first line, calm happy eyes) · camera zoom-in · crossfade in
edit: iris reveal into the picture on "so" · snap zoom to the open notebook on "step"
narration: "So you don't need to become a different person. And you don't need to wait until you feel ready. You just need one step that's easier than avoiding it."

**D72** · picture S19 · camera zoom-out · **at least 2s of silence after "did"**
edit: light sweep across the notebook on "today"
narration: "So pick the one thing you've been putting off. And do the smallest piece of it. Today. Future you is going to be really glad you did."

**D73** · picture S29 (COPY: narrator on the right, pointing left; end screen) · camera hold · hold the last frame 5s after the narration
narration: "What's the one thing you've been putting off the longest? Tell me in the comments, along with your first tiny step. Saying it out loud makes it real. And if fear of failure is what's really holding you back, I made a whole video on where self-doubt comes from. I'll leave it right here."
beats: pop N06 "what's" → card YOUR **ONE THING?** (finish it before "and if" so the end screen stays clean)
