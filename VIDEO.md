# Current video: "Psychology of Manifestation: Why It Works (And the One Part Everyone Gets Wrong)"

**Topic:** manifestation. Believing you *can* get something helps; daydreaming that you *already have* it quietly drains your drive. The fix is WOOP (wish, outcome, obstacle, plan) plus picturing the process.
**Follows:** `PLAYBOOK.md` (hook → personal story → research → 3 reasons → the part everyone gets wrong → 5 steps → emotional close). It calls back to the spotlight video at the end and teases the self-belief video in Part 3.
**Length:** the raw voice is about 1,680 words. After pause padding, the target is about **11:30–12:00**.
**Audio:** Luke records shorter clips so ElevenLabs stays clean: `audio/part1a.mp3`, `part1b.mp3` … (13 clips: Part 1 a–c, Part 2 a–c, Part 3 a–c, Part 4 a–d). Run `python3 tools/join-clips.py` first; it joins them into `audio/part1.mp3` … `part4.mp3`. Then continue as normal.
**Music:** `music/track.mp3`, mixed softly as before.
**Upload kit** (title, thumbnail, description, tags): `prompts/upload-package.md`.
**Spec examples:** copy the helpers from `videos/02-regret/make-specs.py` (host mode, edits, steps, swaps). Video 2's `VIDEO.md` uses the same notation.

## How to read this list

- **Scene IDs (M01…) and picture files (S01.png…) are separate.** The `picture` field names the exact file in `pictures/`. The same picture can be used by several scenes.
  - `(NEW)` means Luke makes it (prompt in `prompts/nano-banana-prompts.md`).
  - `(COPY)` means it's already in `pictures/` (reused from videos 1 and 2).
  - `CODED` means you build it in code (see "New diagram kinds" at the bottom).
- **beats:** the key moments, with the exact trigger word in quotes. Fill the remaining time with crops, cards, icons and pop-ups as the CLAUDE.md pacing rules say (every shot ≤ 4s).
  - `icon Ixx "word"` is an icon cutaway.
  - `pop Nxx "word" → content` is a narrator pop-up.
  - `card "word" → TEXT` is a text card. **Bold** words go in a yellow badge and ~~struck~~ words in a red badge.
  - `step "word" → STEP n + TEXT` (or `REASON n`) is the top-center step pill.
  - `badge "word" → TEXT` is an overlay badge on the picture (top-center, ≥ 56px).
- **edit:** lines are the specific edits for that scene (snap zoom, whip slide, callout, count-up…). See CLAUDE.md section 9. Scenes without an `edit:` line still get motivated moves from the toolkit defaults.
- **host:** lines are the narrator-host pose track (see below). No `host:` line means full-frame.
- **narration** is used for timing only and must match the audio. Never show it on screen.
- **Icons:** I06, I11, I13, I25, I41, I43, I46 and I49 are reused (already in `icons/`). I51–I62 are new (Luke makes them; prompts in `prompts/icon-prompts.md`). If an icon file is missing, skip that beat.
- **Numbers:** Whisper may write "twenty" as "20", "forty-three" as "43", "sixty percent" as "60%", "5K" as "5K" or "five K". Match triggers either way.

---

## The narrator host

**Note on Luke's pictures:** in S04, S05, S06 and S07 the narrator himself plays the student (instead of a stickman), so those scenes (M05, M07, M19, M20, M28, M30) are full-frame with no host.

Same as video 2. The narrator **stands at the side of scenes and "explains" them**, and his pose hard-cuts with the tone of the voice, even inside one scene.

- **`host:` lines** list his pose track for that scene: a pose, then the word where he hard-cuts to the next pose. They come from the tone tags in Luke's script:
  - calm, storytelling or warm → N01
  - curious, thoughtful, reflective or softly → N06
  - serious, emphatic or slow → N02
  - wry or light → N05
  - upbeat or encouraging → N07
  - counting a numbered reason → N08
  - a reveal → N09 · embarrassed → N10 · a confident statement → N11 · the outro → N12
  - At most 3 poses per scene, each held at least 2s.
- **Layout ("host frame"):** cream background; the scene's picture, diagram, card or icon goes in a **rounded frame on the right** (about 74% of the width, 6px ink outline, radius 28px, vertically centered). The narrator stands **lower-left**, about 60% of the frame height, overlapping the frame edge slightly, with a soft ground shadow. Crops and camera moves happen *inside* the frame.
- **Motion:** he slides in from the left (0.25s, ease-out) when a host stretch starts and out (0.2s) when it ends. Between consecutive host scenes **he stays put** and only the frame content changes. Pose changes are **hard cuts, never animated**.
- **When he's off:** scenes without a `host:` line are full-frame. Most of them are pictures that already show the narrator, so he's never on screen twice. Host time is about 45% of the video, and no host stretch runs longer than about 40s.
- **Pop-ups inside a host scene** don't add a second narrator. Their content goes in the frame and his pose switches to the pop's pose for that moment.

---

## PART 1: The hook and my story (`audio/part1.mp3`)

**M01** · picture S01 (NEW: narrator cross-legged on his bed at night, eyes closed, a big glowing dream bubble above him: a muscular version of him, a big screen with a cheering crowd, and him on a podium with a trophy) · camera zoom-in
edit: start wide on the dark bedroom · snap zoom into the dream bubble on "picture" · light sweep across the bubble on "feel"
narration: "You've probably heard it a hundred times. Picture your dream life. See it clearly. Feel it like it's already yours... and the universe will bring it to you."
beats: icon I57 "universe"

**M02** · picture S02 (NEW: narrator scrolling a glowing phone, surrounded by floating cards: a mini vision board, an open journal, a sunrise with a speech bubble, crystals, a crescent moon) · camera pan-right
edit: tour: snap zoom to the vision-board card on "vision" → whip slide to the journal card on "scripting" → whip slide to the sunrise card on "saying" → zoom back out to the full picture on "everywhere"
narration: "Vision boards. Scripting. Saying it out loud every morning. It's everywhere. TikTok, YouTube, half the books in the self-help section."
beats: icon I46 "books"

**M03** · picture S20 (COPY: researcher at a desk with a huge pile of notes) · camera zoom-in
edit: snap zoom to the researcher on "psychologist" · name pill GABRIELE OETTINGEN on "Oettingen" · count-up badge to 20+ on "twenty" · whip slide across the note pile on "real" (1st occurrence)
host: N02 "but" → N06 "not"
narration: "But a psychologist named Gabriele Oettingen spent more than twenty years actually testing what happens when people daydream about their goals. Not in theory. In real people, with real goals, followed for months and even years."
beats: badge "twenty" → **20+** YEARS OF TESTS

**M04** · picture S02 · camera zoom-in
edit: snap zoom to the glowing phone on "manifestation"
narration: "And what she found... is not what most manifestation videos tell you."
beats: pop N09 "not" → card ~~NOT~~ WHAT YOU'VE HEARD

**M05** · picture S04 (NEW: two graduates in caps and gowns: one daydreaming under a tree with a bubble of a fancy office, one at a picnic table with a laptop and a stack of envelopes) · camera pan-right
edit: tour: wide on both graduates → snap zoom to the graduates' caps on "college" → whip slide to the laptop graduate on "graduate" → (icon) → snap zoom to the daydreaming graduate on "daydreams" → whip slide up into his office bubble on "landing" → push wipe into the card on "two"
narration: "In one study, she followed college students who were about to graduate and look for their first job. She asked how often they had positive daydreams about landing that dream job. Then she checked back two years later."
beats: icon I53 "job" (1st occurrence) · card "two" → **2 YEARS** LATER

**M06** · CODED drops · camera hold
edit: riser before "fewer" (1st occurrence) · each red down arrow drops on its word with a pop · impact hit on "salaries"
host: N02 "the"
Header: THE BIGGEST DAYDREAMERS. Rows: APPLICATIONS (arrow on "applications"), JOB OFFERS (arrow on "offers"), SALARY (arrow on "salaries").
narration: "The students who daydreamed the most... had sent out fewer applications. Gotten fewer job offers. And were earning lower salaries."

**M07** · picture S04 · camera zoom-in · **reveal: at least 2s of silence after**
edit: hand-drawn callout circle around the daydreaming graduate on "picturing"
narration: "Picturing the dream... had made them less likely to get it."
beats: card "less" → ~~LESS~~ LIKELY TO GET IT

**M08** · picture S34 (COPY: narrator close-up, worried, sweat drop) · camera hold
narration: "And honestly, that one stung a little."

**M09** · picture S01 · camera zoom-in
edit: soft light leak on "used" (memory) · tour the dream bubble: snap zoom into the bubble on "picture" → whip slide to the muscular him on "body" → whip slide to the cheering screen on "channel" → whip slide to him on the podium on "version" → zoom back out on "figured"
narration: "Because I used to be big on manifesting. I'd lie in bed at night and picture everything. The body I wanted. The channel I wanted to build. The version of me who had it all figured out."

**M10** · picture S25 (COPY: narrator at a desk at night, glowing book with dreams floating out) · camera zoom-in
edit: light sweep across the glowing book on "amazing"
narration: "And it felt amazing. Like I was already halfway there."
beats: card "halfway" → ALREADY **HALFWAY** THERE

**M11** · picture S23 (COPY: narrator on the edge of his bed in the morning, sneakers and gym bag by the door) · camera zoom-in
edit: push wipe into the picture on "next" (time jump) · snap zoom to the unused sneakers on "nothing"
narration: "And then the next morning... I'd do basically nothing. Because somehow, my brain felt like I'd already done the work."
beats: pop N10 "brain" → card ALREADY **DONE THE WORK**

**M12** · picture S03 (NEW: narrator slouched at his desk on his phone, a big vision board on the wall above: muscular stickman, trophy, sports car, cheering crowd) · camera zoom-in
edit: tour the board: snap zoom to the vision board on "vision" → whip slide to the muscular stickman on "gym" → whip slide to the cheering crowd on "subscriber" → zoom out to the whole desk on "hung" · hand-drawn arrow from the board down to his phone on "looking"
narration: "I even made a vision board once. Pictures of the gym body, a big subscriber count, the whole thing. I hung it right over my desk. It stayed there for months... looking at me... while I didn't do much of anything on it."
beats: icon I13 "months" · pop N05 "didn't" → card MONTHS OF **NOTHING**

**M13** · CODED split · camera hold
edit: the left side pops on "science" with a sage tick; the right side pops on "against" with a red cross
host: N06 "but" → N02 "there's"
Left: BACKED BY **SCIENCE**. Right: WORKS ~~AGAINST YOU~~.
narration: "But here's the thing. Manifestation isn't completely wrong. There's one part of it that's backed by real science. And one part that quietly works against you."
beats: card "isn't" → NOT COMPLETELY **WRONG**

**M14** · CODED iconRow · camera hold
host: N01 "by"
Icons: I61 on "feels", I58 on "wrong", I59 on "five-step". Small labels under them: WHY IT FEELS REAL · THE MISTAKE · 5 STEPS.
narration: "By the end of this video, you'll know why manifesting feels like it works, the one part everyone gets wrong, and the five-step version that researchers have actually tested."

**M15** · picture S36 (COPY: narrator presenting at a blank whiteboard) · camera zoom-in
edit: snap zoom to him on "only"
narration: "It takes about five minutes. And it's the only kind of manifesting I still do."
beats: icon I11 "five" · **title card** at the end (2.5s): green pill **LESSON**, big text PSYCHOLOGY OF / MANIFESTATION, with "MANIFESTATION" in orange

---

## PART 2: The research (`audio/part2.mp3`)

**M16** · picture S20 · camera zoom-in
edit: snap zoom to the researcher on "Oettingen" + name pill OETTINGEN & MAYER · count-up 1 → 4 in the badge on "four"
host: N01 "so" → N06 "oettingen"
narration: "So let's start with what the research actually found. Oettingen and her colleague Doris Mayer didn't just study job seekers. They studied four completely different groups."
beats: icon I53 "job" · badge "four" → **4** GROUPS

**M17** · CODED iconRow (full-frame) · camera hold
Icons: I54 on "crush", I46 on "exam", I55 on "hip". Labels: THE CRUSH · THE EXAM · THE SURGERY.
narration: "Students with a crush on someone. Students getting ready for an exam. And even older adults about to have hip replacement surgery."

**M18** · CODED split · camera hold
edit: left text pops on "likely", right text pops on "daydream" · on "opposite" a sage up-arrow pops on the left and a red down-arrow on the right, with a ding
host: N06 "every" → N02 "and" (2nd occurrence)
Left: HOW **LIKELY**? Right: HOW MUCH **DAYDREAMING**?
narration: "Every time, they measured two different things. First: how likely did people think it was that things would work out? And second: how much did they daydream about the perfect outcome? And those two things pointed in opposite directions."
beats: card "two" (1st occurrence) → **TWO** THINGS

**M19** · picture S05 (NEW: library: a student daydreaming with a heart bubble, the crush walking past) · camera zoom-in
edit: snap zoom to the heart bubble on "daydreamed" → whip slide to the crush walking past on "less"
narration: "The students who daydreamed the most about their crush were less likely to actually end up together months later."
beats: badge "less" → ~~LESS~~ LIKELY

**M20** · picture S06 (NEW: student on a couch daydreaming of a gold-star test, textbooks unopened) · camera zoom-in
edit: snap zoom to the gold-star dream on "acing" → whip slide to the unopened textbooks on "studied" · hand-drawn red arrow pointing down on "grades"
narration: "The students who daydreamed most about acing the exam studied less... and their grades went down."

**M21** · picture S21 (COPY: nurse beside a patient in a hospital bed) · camera zoom-in
edit: snap zoom to the patient on "pictured"
host: N06 "and"
narration: "And the surgery patients who pictured a perfect, easy recovery... were recovering worse two weeks later."
beats: badge "worse" → ~~WORSE~~ AT 2 WEEKS

**M22** · picture S20 · camera zoom-in
edit: snap zoom to the note pile on "sounded" · hand-drawn callout circle on one note on "pattern"
narration: "And when the researchers looked at what those daydreams actually sounded like, there was a pattern."

**M23** · picture S24 (COPY: narrator at the foot of a giant mountain) · camera hold
edit: pill NO SETBACKS on "setbacks", swapping to NO HARD DAYS on "hard" · whip slide up the mountain to the peak on "arriving"
narration: "They were effortless. No setbacks. No hard days. Just... arriving."
beats: card "effortless" → ALWAYS **EFFORTLESS**

**M24** · CODED card, swapping to card B on "same" · camera hold
edit: marker highlight on LINK · kinetic word swap to card B on "same"
host: N01 "now"
Card A: A **LINK**, NOT PROOF. Card B: SAME **PATTERN** EVERY TIME.
narration: "Now, to be fair, these studies show a link, not proof. But the same pattern kept showing up, in very different people."

**M25** · picture S35 (COPY: narrator walking confidently into a gym) · camera zoom-in
edit: snap zoom to his confident stride on "expected" · whip slide through the door into the gym on "harder"
narration: "But the people who simply expected things to go well, who believed it was likely, because they'd done it before or knew they could... they did better. They tried harder. They got more of what they wanted."
beats: pop N11 "believed" → card BELIEVED IT WAS **LIKELY** · card "better" → THEY DID **BETTER**

**M26** · CODED split · camera hold · **reveal: at least 2s of silence after**
edit: riser before it · left pops on "helps" · right pops on "hurts" with an impact hit
host: N06 "so" → N02 "daydreaming"
Left: BELIEVING IT CAN HAPPEN: **HELPS**. Right: DAYDREAMING IT HAPPENED: ~~HURTS~~.
narration: "So believing it can happen... helps. Daydreaming that it already happened... hurts."

**M27** · picture S33 (COPY: narrator thinking, a lightbulb above him) · camera zoom-in
edit: snap zoom to the lightbulb on "Kappes" + name pill HEATHER KAPPES
narration: "Why would daydreaming hurt? Oettingen and another researcher, Heather Kappes, found a clue in people's bodies."
beats: icon I25 "clue"

**M28** · picture S07 (NEW: thirsty student slumped at a table, bubble with an ice-cold glass of water, empty plate) · camera zoom-in
edit: snap zoom to the empty plate on "skip" → whip slide to the icy water bubble on "picture" · light sweep across the glass on "ice-cold"
narration: "In one study, they had students skip food and water for a few hours. Then some of the thirstiest students were asked to picture a glass of ice-cold water."
beats: icon I11 "hours"

**M29** · CODED drops · camera hold
edit: each red down arrow drops on its word with a pop
host: N06 "and"
Header: PICTURING THE WATER. Rows: BLOOD PRESSURE (arrow on "dropped" (1st occurrence)), ENERGY (arrow on "dropped" (2nd occurrence)).
narration: "And when they did... their blood pressure dropped. Their energy dropped."

**M30** · picture S07 · camera zoom-in
edit: hand-drawn callout circle around the dream glass on "already"
narration: "Their bodies relaxed, almost as if they'd already had the drink."
beats: badge "already" → ALREADY **HAD IT**

**M31** · picture S22 (COPY: narrator lying in bed at night, face lit by his phone) · camera zoom-in
edit: snap zoom to his phone-lit face on "picturing"
narration: "In another study, people who spent time picturing an amazing week ahead felt less energized. And by the end of that week... they'd gotten fewer of their goals done."
beats: icon I56 "energized" · card "fewer" → ~~FEWER~~ GOALS DONE

**M32** · picture S12 (NEW: narrator relaxing in a hammock, a tiny gold trophy on his chest, sneakers unused on the grass) · camera zoom-in
edit: snap zoom to the trophy on "reward" · zoom out to the whole lazy pose on "relaxes" · whip slide down to the unused sneakers on "moving"
narration: "That's the trap. When you picture the finish line in perfect detail, your brain gets a little taste of the reward. And it relaxes... right when you need it to get moving."
beats: pop N02 "trap" → card THAT'S **THE TRAP** · icon I52 "taste"

---

## PART 3: Why it seems to work, and the part everyone gets wrong (`audio/part3.mp3`)

**M33** · CODED grid (full-frame) · camera hold
edit: the 60 people pop in row by row on "many" · 6 of them turn yellow on "some"
Badge under the grid on "three": **3** REASONS.
narration: "So if daydreaming can backfire, why does manifestation seem to work for so many people? Because some of it really does. Just not for the reasons people think. Here are three."
beats: card "not" → ~~NOT~~ WHY YOU THINK

**M34** · picture S08 (NEW: two people with newspapers: a relaxed one pointing at a big blank box on his page, a stressed one counting photos) · camera zoom-in
edit: snap zoom to the newspapers on "newspaper" + name pill RICHARD WISEMAN on "Wiseman" · whip slide to the stressed counter on "count"
host: N08 "one" → N01 "a"
narration: "One. You start noticing things. A psychologist named Richard Wiseman once gave people a newspaper and asked them to count the photos inside."
beats: step "one" → REASON 1 + YOU START NOTICING

**M35** · picture S08 · camera zoom-in
edit: snap zoom to the blank box on "second" · the message fills the box as a sign overlay on "message" · count-up to 43 on "forty-three"
host: N05 "on"
Sign text: STOP COUNTING. / THERE ARE **43** PHOTOS.
narration: "On the second page, in big letters, was a message: "Stop counting. There are forty-three photographs in this newspaper.""

**M36** · picture S08 · camera zoom-in
edit: snap zoom to the relaxed reader on "lucky" → whip slide to the stressed counter on "unlucky"
host: N01 "the" → N05 "the" (2nd occurrence)
narration: "The people who called themselves lucky usually spotted it in seconds. The people who called themselves unlucky were so focused on counting, they flew right past it."
beats: badge "seconds" → **SECONDS** · badge "past" → ~~MISSED IT~~

**M37** · picture S27 (COPY: narrator reaching for a door handle) · camera zoom-in
edit: snap zoom to his hand on the handle on "chances"
narration: "When you decide something matters to you, you start seeing chances you used to miss."

**M38** · CODED card, swapping to card B on "attention" · camera hold
edit: kinetic word swap UNIVERSE → ATTENTION · marker highlight on ATTENTION
host: N06 "that's"
Card A: NOT THE ~~UNIVERSE~~. Card B: YOUR **ATTENTION**.
narration: "That's not the universe. That's your attention."

**M39** · picture S08 · camera zoom-out
edit: hand-drawn callout circle around the message box on "already"
host: N01 "the"
narration: "The lucky people in that experiment didn't get more chances. They just saw more of the ones that were already there."
beats: card "saw" → THEY JUST **SAW MORE**

**M40** · CODED split (the same as M26, a callback) · camera hold
edit: the split from M26 reappears on "remember" with only BELIEVING: HELPS lit and the right side dimmed
host: N08 "two" → N01 "remember"
narration: "Two. Belief changes what you do. Remember those studies. Expecting that something is possible made people try harder and keep going."
beats: step "two" → REASON 2 + BELIEF CHANGES WHAT YOU DO · icon I49 "going"

**M41** · picture S26 (COPY: narrator facing a mirror that shows a confident version of him) · camera zoom-in
edit: whip slide from him to the mirror self on "act"
narration: "So the "believe it" part of manifestation? That part is real. Believing you can do something makes you act like someone who can. That's honestly such a big topic that I'm making a whole video on it next."
beats: card "real" → THAT PART IS **REAL** · pop N05 "whole" → card **NEXT** VIDEO

**M42** · CODED grid (highlight mode) · camera hold
edit: 6 people light up yellow with a ding on "happens" (1st occurrence) · the other 54 fade to pale grey on "forget"
host: N08 "three" → N01 "when" → N05 "when" (2nd occurrence)
narration: "Three. You remember the hits. When you manifest something and it happens, it feels like magic, and you tell everyone. When you manifest something and it doesn't happen... you just quietly forget about it."
beats: step "three" → REASON 3 + YOU REMEMBER THE HITS · icon I57 "magic"

**M43** · picture S28 (COPY: one figure on a lit stage, a dark crowd of eyes) · camera zoom-in
edit: snap zoom to the one on stage on "success" → whip slide across the dark crowd on "silent"
narration: "So every success story you hear has a lot of silent ones behind it."

**M44** · picture S02 · camera zoom-in
edit: snap zoom to a floating card on "manifests"
narration: "Someone manifests a new job, gets it, and posts about it. Nobody posts, "I manifested this for a year and nothing happened.""
beats: icon I41 "posts" (1st occurrence) · card "nobody" → NOBODY POSTS ~~THE MISSES~~

**M45** · CODED card · camera hold
edit: riser before it · marker highlight on GETS WRONG
host: N02 "which"
Card: THE PART EVERYONE **GETS WRONG**.
narration: "Which brings us to the one part everyone gets wrong."

**M46** · picture S25 · camera zoom-in
edit: snap zoom to the floating dream images on "outcome" · zoom out on "but"
narration: "Manifestation tells you to picture the outcome. The finish line. The moment you've already made it. But that's exactly the kind of picture that drains your energy."
beats: icon I56 "drains"

**M47** · picture S09 (NEW: split: one student dreaming of a gold star on a bed vs one at a desk with a planner, open books and a wall clock) · camera zoom-in
edit: name pill PHAM & TAYLOR, UCLA on "Pham" · light sweep across the picture on "midterm" · snap zoom to the dreaming student on "one" → whip slide to the desk student on "another" · hand-drawn callout circles on his chair on "sit", the wall clock on "when", the open books on "what"
host: N01 "researchers" → N06 "one"
narration: "Researchers at UCLA, Lien Pham and Shelley Taylor, tested this with students before a big midterm. One group spent a few minutes a day picturing themselves getting a great grade. Another group pictured the process. Where they'd sit. When they'd study. What they'd go over."

**M48** · CODED drops (up mode) · camera hold
edit: each sage up arrow rises on its word · impact hit on "better"
host: N02 "the"
Header: PICTURED THE PROCESS. Rows: STUDIED LONGER (arrow on "longer"), BETTER GRADES (arrow on "better").
narration: "The students who pictured the process studied longer... and did better on the exam."

**M49** · CODED card, swapping to card B on "process" · camera hold · **reveal: at least 2s of silence after**
edit: kinetic word swap GRADE → PROCESS · hand-drawn underline on PLAN on "plan"
host: N06 "picturing"
Card A: THE GRADE: FELT **GOOD**. Card B: THE PROCESS: MADE A **PLAN**.
narration: "Picturing the grade felt good. Picturing the process made them actually plan."

**M50** · picture S11 (NEW: narrator crouched at the start line of a running track at sunrise, a glowing dream bubble far down his lane), swapping to S11b (NEW: the same, but a brick wall now blocks his lane) on "way" · camera zoom-in · **reveal: at least 2s of silence after**
edit: snap zoom to the dream bubble at the end of the track on "ending" · zoom back to him on "skipping" · hard swap to S11b with a ding on "way"
narration: "So the problem isn't that you're picturing your goal. It's that you're only picturing the ending. And you're skipping the most important part of the picture... the part where something gets in your way."

---

## PART 4: The 5 steps and the ending (`audio/part4.mp3`)

**M51** · picture S36 · camera zoom-in
edit: snap zoom to him on "five"
narration: "So here's how I actually manifest now. Five steps."
beats: icon I59 "steps"

**M52** · CODED woop · camera hold
edit: the four letters W · O · O · P pop in one by one on "WOOP" (0.12s apart), then the row labels appear
host: N01 "the"
narration: "The first four come from a method Oettingen built out of all this research. It's called WOOP."

**M53** · CODED woop (WISH row active) · camera hold
edit: the WISH answer fills on "possible"
host: N07 "one" → N01 "pick"
WISH answer: CHALLENGING BUT **POSSIBLE**.
narration: "One. Wish. Pick one thing you really want, that's challenging but actually possible. Not "be rich" or "be happy." Something like "start my YouTube channel," or "run a 5K by spring." Something that's actually up to you."
beats: step "one" → STEP 1 + WISH · card "rich" → NOT ~~BE RICH~~ · icon I60 "YouTube" · pop N11 "up" → card ACTUALLY **UP TO YOU**

**M54** · picture S31 (COPY: narrator on a hilltop at sunrise) · camera zoom-out
edit: iris reveal into the sunrise on "picture" · light sweep across the sky on "enjoy"
narration: "Two. Outcome. Now picture the best result. How would it feel? What would change? Go ahead and enjoy it for a moment. This part is fine."
beats: step "two" → STEP 2 + OUTCOME · card "fine" → THIS PART IS **FINE**

**M55** · CODED woop (WISH and OUTCOME ticked) · camera hold
edit: the OBSTACLE row pulses yellow on "next"
host: N01 "it's"
narration: "It's the next step that makes it work."

**M56** · picture S11b · camera zoom-in
edit: snap zoom to the brick wall on "skips" · whip slide back to him on "inside"
narration: "Three. Obstacle. This is the step everyone skips. Ask yourself: what's the main thing inside me that's going to get in the way?"
beats: step "three" → STEP 3 + OBSTACLE · badge "skips" → THE ONE ~~EVERYONE SKIPS~~

**M57** · CODED card with two kinetic swaps · camera hold
edit: NOT ~~OTHER PEOPLE~~ → NOT ~~BAD LUCK~~ on "luck" → **YOU.** on "you" with an impact hit
host: N02 "not"
narration: "Not other people. Not bad luck. You."

**M58** · picture S22 · camera zoom-in
edit: snap zoom to the glowing phone on "scroll"
narration: "Maybe it's that you get home tired and scroll instead. Maybe it's that you're scared of what people will think."
beats: icon I06 "people"

**M59** · picture S11b · camera zoom-in
edit: snap zoom to the wall on "obstacle" → whip slide to the dream bubble on "dream"
narration: "Picture that obstacle as clearly as you pictured the dream."

**M60** · CODED woop (OBSTACLE row active) · camera hold
edit: the OBSTACLE answer fills on "ready"
host: N01 "and"
OBSTACLE answer: TIME TO **GET READY**.
narration: "And here's the surprising part. This doesn't kill your motivation. When the wish is realistic, seeing the obstacle is what tells your brain it's time to get ready."
beats: pop N09 "surprising" → card DOESN'T ~~KILL~~ MOTIVATION

**M61** · CODED woop (PLAN row active) · camera hold
host: N07 "four" → N01 "make"
narration: "Four. Plan. Make one simple if-then plan for that obstacle."
beats: step "four" → STEP 4 + PLAN

**M62** · CODED split · camera hold
edit: the left side pops on "if", the right side pops on "then"
host: N01 "if"
Left: IF: **TIRED + PHONE**. Right: THEN: **OTHER ROOM**.
narration: ""If I get home tired and grab my phone, then I'll put it in the other room and do ten minutes first.""
beats: icon I43 "ten"

**M63** · CODED bars · camera hold · **reveal: at least 2s of silence after**
edit: riser before it · bars grow with count-ups to 140 and 84 · impact hit and a **+60%** badge on "sixty"
host: N02 "in"
Bars: "USED WOOP" (mustard, 140) vs "DIDN'T" (grey, 84). Title: PRACTICE QUESTIONS. Small source line: Duckworth et al., 2011.
narration: "In one study, high school students who used this method completed more than sixty percent more practice questions for a big exam than students who didn't."

**M64** · picture S11 · camera zoom-in
edit: snap zoom to the dream bubble at the finish on "finish"
narration: "Five. Picture the process, not just the finish line."
beats: step "five" → STEP 5 + PICTURE THE PROCESS

**M65** · CODED iconRow · camera hold
host: N01 "when"
Icons: I60 on "laptop", I49 on "shoes", I62 on "record".
narration: "When you visualize, don't just see yourself holding the trophy. See yourself doing the boring part. Opening the laptop. Lacing up your shoes. Hitting record."
beats: icon I52 "trophy" · card "boring" → THE **BORING PART**

**M66** · picture S35 · camera zoom-in
edit: snap zoom to his stride on "moving"
narration: "That's the picture that actually gets you moving."

**M67** · picture S10 (NEW: narrator at his desk at night, laptop showing an upload arrow, happy eyes) · camera zoom-in
narration: "Let me show you how this sounds for me."

**M68** · CODED woop (Luke's own WOOP; each answer fills on its word) · camera hold
edit: answers type in on their words · hand-drawn underline on ANYWAY on "anyway"
host: N01 "my"
WISH: 1 VIDEO **EVERY WEEK** (on "wish"). OUTCOME: A CHANNEL I'M **PROUD OF** (on "outcome"). OBSTACLE: ~~"IT'S NOT READY"~~ (on "obstacle"). PLAN: POST IT **ANYWAY** (on "plan").
narration: "My wish: post one video every week. The outcome: a channel I'm proud of, and people in the comments saying a video actually helped them. The obstacle... honestly? It's me deciding a video isn't good enough yet, and not posting it. So my plan: if I catch myself thinking "it's not ready," then I post it anyway and make the next one better."
beats: icon I13 "week" · icon I41 "comments" · pop N10 "deciding" → card ~~NOT GOOD ENOUGH~~ YET

**M69** · picture S10 · camera zoom-in
edit: snap zoom to the laptop screen on "laptop" · hand-drawn callout circle around the upload arrow on "upload" (1st occurrence) · zoom back to his happy face on "just"
narration: "And the process? I picture Sunday night. Me, the laptop, hitting upload. Not the million views. Just the upload."
beats: card "million" → NOT THE ~~MILLION VIEWS~~

**M70** · picture S37 (COPY: narrator sitting on a curb at dusk, thought bubbles) · camera zoom-in
edit: crossfade in (calm moment) · snap zoom to the thought bubbles on "dreaming" (2nd occurrence)
narration: "Here's what I keep coming back to. I don't think wanting things and dreaming big is the problem. Dreaming is where everything starts."
beats: card "dreaming" (2nd occurrence) → WHERE **IT ALL STARTS**

**M71** · picture S12 · camera zoom-in
edit: snap zoom to the trophy on "good" → whip slide to the unused sneakers on "doing"
narration: "The problem is when the dream feels so good... that it replaces the doing."

**M72** · picture S26 · camera zoom-in
edit: snap zoom to the mirror self on "version" → whip slide back to him on "doing"
narration: "Because the version of you in the daydream isn't someone you become by picturing. It's someone you become by doing the boring part, over and over."
beats: card "over" (1st occurrence) → **OVER AND OVER**

**M73** · picture S11 · camera zoom-out
edit: snap zoom to the dream bubble on "dream" · whip slide back to him at the start line on "starting" · light sweep across the sunrise on "starting"
narration: "So keep the dream. Just stop letting it be the finish line. Let it be the starting line."
beats: card "finish" → NOT THE ~~FINISH LINE~~, kinetic swap to THE **STARTING LINE** on "starting"

**M74** · CODED woop (recap) · camera hold
edit: WISH + OUTCOME light up on "want", OBSTACLE on "way", PLAN on "plan"
host: N01 "dream" → N02 "picture"
narration: "Dream big. Then get specific. Picture what you want. Then picture what's in your way. Then make a plan to get past it."

**M75** · picture S27 · camera zoom-in · crossfade in
edit: snap zoom to his hand on the door handle on "you're"
narration: "That's not as magical as the universe handing it to you. But it's a version of manifesting that actually works... and you're the one making it happen."
beats: icon I51 "magical"

**M76** · picture S29 (COPY: narrator on the right, pointing left; end screen) · camera hold · hold the last frame 5s after the narration
edit: hard cut to S28 (the stage of eyes) on "voice", and back to S29 on "made" for the end screen
narration: "Which step do you usually skip? Tell me the number in the comments. And if your biggest obstacle is that voice in your head saying everyone's watching, I made a whole video on why that's not true. I'll leave it right here."
beats: pop N08 "number" → card WHICH **NUMBER?** (finish it before "and if" so the end screen stays clean)

---

## New diagram kinds to add to `tools/build-part.mjs`

Use the same look as the existing kinds: cream background, 9px ink outlines, Nunito ExtraBold, yellow or red outlined badges. Every animation must be seek-safe on the GSAP timeline.

- **drops:** a header badge, then 2–3 rows. Each row is a big label (≥ 72px) with an arrow box on its right. The arrow (red pointing down, or sage pointing up in `up` mode) drops or rises into the box with `back.out(1.4)` and a *pop* on its own word. Options: `header`, `rows: [{label, word, occ}]`, `dir: down|up`. Used in M06, M29 and M48.
- **woop:** a tall card with 4 rows: **W** WISH, **O** OUTCOME, **O** OBSTACLE, **P** PLAN. Each row has a big round letter badge (mustard for W and O, red for OBSTACLE, sage for PLAN) and an answer slot on the right. Options: `intro` (letters pop on a word, as in M52), `active` (that row is full-color and the rest dimmed to 40%), `ticks` (rows that get a sage tick), `pulse` (a row that pulses yellow on a word), `answers: {ROW: [text, word, occ]}` (answer text types in over 0.3s on its word), `lights: [[rows, word]]` (M74 recap). Used in M52, M53, M55, M60, M61, M68 and M74.
- **grid highlight mode:** the existing `grid` kind gets `pop` (people pop in row by row on a word), `lit` (how many turn yellow, and on which word) and `dim` (the rest fade to `#E6E1D6` on a word). Used in M33 and M42.
- **split arrows:** the existing `split` kind gets `arrows: [left, right, word]` (`up` sage or `down` red arrows that pop under each side on the word) and `dimRight` (for the M40 callback). Used in M18 and M40.
- **bars:** the existing `bars` kind gets `colorA` (mustard here) and raw-number labels (140 and 84) instead of percentages, plus a `+60%` badge on `word` and a small source line. Used in M63.
- **card with two swaps:** the existing card → card swap, extended to three states (M57).

### Description sources (for Luke, not on screen)
- Oettingen & Mayer (2002), "The motivating function of thinking about the future: Expectations versus fantasies," *JPSP*
- Kappes & Oettingen (2011), "Positive fantasies about idealized futures sap energy," *JESP*
- Pham & Taylor (1999), "From thought to action: Effects of process- versus outcome-based mental simulations on performance," *PSPB*
- Duckworth, Grant, Loew, Oettingen & Gollwitzer (2011), "Self-regulation strategies improve self-discipline in adolescents," *Educational Psychology*
- Richard Wiseman (2003), *The Luck Factor*
- Gabriele Oettingen (2014), *Rethinking Positive Thinking*
