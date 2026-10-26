# Current video: "The Psychology of Discipline" (final title TBD)

**Working title:** Psychology of Discipline: Why Motivation Never Lasts. Luke will pick the final title later; the title card just says PSYCHOLOGY OF / DISCIPLINE.
**Topic:** discipline isn't a bigger willpower tank. Disciplined people avoid the fight (Hofmann's beeper study), willpower-as-a-tank is shaky (ego depletion replication), and four reasons discipline breaks (running on motivation, temptation face to face, "I can't" rules, all-or-nothing). Five research-backed ways to build discipline that lasts.
**Follows:** `PLAYBOOK.md` (cold open with a study → personal story → research → 4 reasons → 5 steps → emotional close). It points to the procrastination video at the end.
**Length:** the raw voice is about 1,570 words. After pause padding, the target is about **11:00**.
**Audio:** 15 clips, `audio/part1a.mp3` … (Part 1 a–c, Part 2 a–b, Part 3 a–d, Part 4 a–f). Run `python3 tools/join-clips.py` first.
**Music:** `music/track.mp3`, mixed softly. Keep it at its quietest during the cold open (D01–D10) and the final scenes (D74–D75).
**Upload kit:** `prompts/upload-package.md`.
**Spec examples:** copy `videos/07-overthinking/make-specs.py` (newest build: reads narration and host tracks straight from VIDEO.md; loop, lines2, bars3, people, dots, pie, split `fs0`, red screen badges). If Whisper can't download its model, use `tools/align.py` (forced alignment; steps in `videos/06-procrastination/VIDEO.md`, "Build status").

## How to read this list

- **Scene IDs (D01…) and picture files (S01.png…) are separate.** `(NEW)` = Luke makes it (`prompts/nano-banana-prompts.md`). `(COPY)` = already in `pictures/`. `CODED` = build it in code.
- **beats:** key moments with the exact trigger word in quotes: `icon Ixx "word"`, `pop Nxx "word" → content`, `card "word" → TEXT`, `step "word" → STEP n + TEXT`, `badge "word" → TEXT`. **Bold** = yellow badge, ~~struck~~ = red badge. Fill the rest per CLAUDE.md (every shot ≤ 4s, except the cold-open scenes).
- **edit:** specific moves (CLAUDE.md section 9). **host:** the narrator-host pose track; no `host:` line = full-frame.
- **narration** is for timing only and must match the audio. Never show it on screen.
- **Icons:** I99 and I101–I108 are new (there is no I100) (`prompts/icon-prompts.md`). I78, I80, I84 and I86 are reused (already in `icons/`). Missing icon → skip that beat.
- **Numbers:** Whisper may write "two thousand twelve" as "2012", "two hundred and five" as "205", "twenty-three" as "23", "forty-three percent" as "43%", "sixty-four percent" as "64%", "eighth graders" as "8th graders". Match triggers either way.
- **Names:** Hagtvedt ("HAG-vet"), Wertenbroch ("VER-ten-brock"), Mischel ("mih-SHELL"). The forced-alignment fallback (`tools/align.py`) has pronunciations for them.

---

## The cold open

D01–D10 are in the normal comic style, but slightly slower and calmer: shots may run up to **4.5s**, moves are snap zooms and soft pushes on words, and the music stays at its quietest. After D10, show the **title card** right away: green pill **LESSON**, big text PSYCHOLOGY OF / DISCIPLINE, with "DISCIPLINE" in orange, 2.5s.

## The narrator host

Same rules as before (poses from the tone tags, frame on the right, hard-cut pose changes, never animated, he stays put between host scenes). Host scenes are pictures without the narrator, icons used as the main picture, and coded diagrams. No host stretch longer than about 40s.

---

## PART 1: The cold open and my story (`audio/part1.mp3`)

**D01** · picture S01 (NEW: midnight; the narrator sitting up in bed, lit by his phone, which shows a fiery motivational video; his eyes blaze with determination, one fist clenched) · camera zoom-in
edit: snap zoom to the glowing phone on "video" → whip slide to his blazing eyes on "fired"
narration: "It's midnight. You just watched a video that got you fired up."

**D02** · picture S01 · camera zoom-out
edit: pills top-center one by one: WAKE UP AT 5 on "five", GYM on "gym", COLD SHOWER on "cold", NO PHONE on "phone", NO JUNK FOOD on "junk"
narration: "Tomorrow, everything changes. Wake up at five. Gym. Cold shower. No phone. No junk food."

**D03** · picture S01 · camera zoom-in
edit: snap zoom to his face on "feel"
narration: "You can feel it. This time is different."
beats: card "different" → THIS TIME IS **DIFFERENT**

**D04** · picture S02 (NEW: Thursday morning; the narrator still in bed, tangled in the blanket, one hand slapping a ringing alarm clock, a half-eaten bowl of cereal on the bed, his phone glowing in his other hand, droopy eyes) · camera zoom-in
edit: whip-pan cut in on "and" · tour: snap zoom to the alarm clock on "snooze" → whip slide to the cereal on "cereal" → whip slide to the phone on "scrolled"
narration: "And then it's Thursday. You hit snooze three times, ate cereal in bed, and scrolled for two hours."
beats: icon I86 "three"

**D05** · picture S02 · camera zoom-out
edit: red badge ~~GONE~~ on "gone"
narration: "And the motivation from Monday? Gone. Like it was never there."

**D06** · picture S03 (NEW: a small research room; several stickmen sit at desks, each holding a phone that is beeping with little ring lines; one stares at a slice of cake, one at a pillow, one at a game controller; a stickman researcher with a clipboard watches) · camera zoom-in
edit: push wipe in (time jump) on "in" · name pill HOFMANN ET AL. (2012) on "researchers" · badges: **205 PEOPLE** on "people", **7 BEEPS A DAY** on "seven"
host: N02 "here's"
narration: "Here's what's strange. In two thousand twelve, a team of researchers gave two hundred and five people a phone that beeped seven times a day for a whole week."

**D07** · picture S03 · camera zoom-in
edit: tour: snap zoom to the stickman staring at the cake on "wanted" → whip slide to the stickman staring at the controller on "resist"
host: N02 "every"
narration: "Every time it beeped, they reported what they wanted right then, and whether they were trying to resist it."

**D08** · CODED card · camera hold
host: N06 "you'd"
Card: MOST DISCIPLINED = / **FIGHTING ALL DAY?**
narration: "You'd expect the most disciplined people to be fighting temptation all day long."

**D09** · CODED bars3 · camera hold
edit: bars grow on "resist" · impact hit on "less"
host: N02 "they"
Bars (no numbers), title HOW OFTEN THEY TRIED TO RESIST: HIGH SELF-CONTROL (sage, short) vs EVERYONE ELSE (sky, tall).
narration: "They weren't. They tried to resist less often than everyone else."

**D10** · picture S07 (NEW: a sunny street with a bakery; one stickman is pressed against the bakery window drooling at the cakes, while across the street a calm stickman in a sage shirt simply walks past on the other sidewalk, not even looking) · camera zoom-in · **reveal: at least 2s of silence after**, then the title card
edit: soft riser · snap zoom to the drooling stickman on "willpower" → whip slide to the calm walker on "fewer" · impact hit on "fewer"
host: N02 "their" → N06 "they"
narration: "Their secret wasn't more willpower. They just had fewer fights to begin with."

**D11** · picture S04 (NEW: the narrator proudly taping a huge hand-written hourly schedule to his bedroom wall, lots of neat lines and boxes, no readable words) · camera zoom-in
edit: hard cut from the title card · snap zoom to the schedule on "schedule" · zoom out on "wall"
narration: "I've made the midnight plan more times than I can count. One time, I wrote out a whole schedule on a piece of paper. Every hour of the day, planned out. I even taped it to my wall."

**D12** · picture S04b (NEW, edit of S04: the same wall, but the schedule hangs half off, one corner torn, sunlight high in the window; the narrator stands in front of it in pajamas with guilty, droopy eyes) · camera zoom-in
edit: push wipe in on "it" · badge **2 DAYS** on "two" · snap zoom to his face on "ruined"
narration: "It lasted two days. On day three, I woke up late, felt like I'd already ruined it, and never looked at that paper again."

**D13** · picture S04b · camera zoom-out
narration: "I didn't need a better plan. I needed to understand why my plans kept falling apart."
beats: pop N06 "understand" → card WHY PLANS **FALL APART**

**D14** · icon I108 as the main picture · camera hold
edit: snap zoom into the lightning bolt on "motivation"
host: N06 "so"
narration: "So what is discipline, really? And why does motivation always run out right when you need it?"

**D15** · CODED iconRow · camera hold
host: N01 "by"
Icons: I101 on "willpower", I84 on "four", I105 on "five". Labels: THE WILLPOWER MYTH · 4 REASONS · 5 WAYS THAT LAST.
narration: "By the end of this video, you'll know why willpower isn't what you think it is, the four reasons your discipline keeps breaking, and five research-backed ways to build discipline that actually lasts."

**D16** · CODED card · camera hold
edit: marker highlight on DAY 3 on "three"
host: N01 "and"
Card: THE **DAY 3** MISTAKE.
narration: "And the last one fixes the exact mistake that killed my schedule on day three."

---

## PART 2: The willpower myth (`audio/part2.mp3`)

**D17** · picture S06 (NEW: the narrator straining to carry a big glass fuel tank on his back like a backpack; the tank is labeled with a fuel gauge drawing (no numbers) and the liquid inside is low; little temptations (a donut, a phone, a pillow) float around him like magnets) · camera zoom-in
edit: badge **LIKE A MUSCLE** on "muscle" · snap zoom to the fuel gauge on "tired"
narration: "For years, psychologists believed willpower worked like a muscle. Use it too much, and it gets tired."

**D18** · picture S05 (NEW: a stickman sitting at a table, longingly staring at a plate of fresh warm cookies while sadly chewing a radish from a bowl of radishes; a stickman researcher watches from behind a two-way mirror) · camera zoom-in
edit: push wipe in on "in" · name pill ROY BAUMEISTER on "psychologist" · snap zoom to the cookies on "cookies" → whip slide to the radishes on "radishes"
host: N01 "in"
narration: "In the late nineteen-nineties, psychologist Roy Baumeister ran a famous study. People who had to resist a plate of fresh cookies and eat radishes instead gave up faster on an impossible puzzle afterward."
beats: icon I99 "famous"

**D19** · picture S06 · camera zoom-in
edit: badge **EGO DEPLETION** on "ego" · snap zoom to the floating temptations on "temptation"
narration: "The idea was called ego depletion. Your willpower is a tank, and every temptation drains it."

**D20** · CODED card · camera hold
host: N01 "it"
Card: ONE OF THE / **MOST FAMOUS IDEAS**.
narration: "It became one of the most famous ideas in all of psychology."

**D21** · picture S20 (COPY: researcher at a desk with a huge pile of notes) · camera zoom-in
edit: push wipe in on "but" · badges: **23 LABS** on "twenty", **2,000+ PEOPLE** on "people"
host: N02 "but"
narration: "But in two thousand sixteen, twenty-three labs around the world tried to repeat a version of the effect, with more than two thousand people."

**D22** · CODED card · camera hold
edit: impact hit on "nothing"
host: N02 "they"
Card: THEY FOUND / ~~ALMOST NOTHING~~.
narration: "They found almost nothing."

**D23** · picture S20 · camera zoom-in
edit: name pill CAROL DWECK on "dweck" · snap zoom to the researcher on "interesting"
host: N06 "and"
narration: "And in another set of studies, Carol Dweck and her colleagues found something interesting."

**D24** · CODED split · camera hold
edit: right side pops on "believed", left side on "didn't" (1st occurrence)
host: N06 "the"
Right (red): BELIEVED IT RUNS OUT → ~~WORN OUT~~. Left (yellow): DIDN'T BELIEVE IT → **MOSTLY FINE**.
narration: "The people who believed willpower runs out were the ones who got worn out. The people who didn't believe it mostly didn't."

**D25** · icon I101 as the main picture · camera hold
edit: snap zoom into the battery on "clear" · red badge ~~NOT A RELIABLE TANK~~ on "reliable"
host: N06 "scientists"
narration: "Scientists are still arguing about it. But one thing is clear. Willpower isn't a reliable tank you can count on all day."

**D26** · picture S07 · camera zoom-in
edit: snap zoom to the drooling stickman on "bigger" → whip slide to the calm walker on "remember" · name pill WILHELM HOFMANN on "hofmann"
host: N01 "so"
narration: "So if disciplined people aren't running on a bigger tank, what are they doing? Remember the beeper study. Wilhelm Hofmann and his team found that people with high self-control had just as many desires as everyone else."

**D27** · CODED list · camera hold
edit: items pop on their words
host: N02 "but"
Items: 1 WEAKER DESIRES on "weaker", 2 LESS TORN on "torn", 3 FEWER FIGHTS on "fight".
narration: "But their desires were weaker, they felt less torn, and they had to fight them less often."

**D28** · picture S07 · camera zoom-in
edit: whip slide to the calm walker on "picking"
host: N06 "they"
narration: "They weren't winning more battles. They were picking fewer of them."
beats: card "fewer" → PICK **FEWER BATTLES**

**D29** · picture S08 (NEW: a classroom of eighth-grade stickman students at desks during a test; one student in a sage shirt sits focused and calm with a neat planner open, while others look distracted) · camera zoom-in
edit: push wipe in on "in" · name pill DUCKWORTH & SELIGMAN (2005) on "duckworth" · snap zoom to the focused student on "graders"
host: N01 "and"
narration: "And it matters a lot. In two thousand five, Angela Duckworth and Martin Seligman followed eighth graders through a school year."
beats: icon I102 "year"

**D30** · CODED bars3 · camera hold
edit: bars grow on "explained" · impact hit on "twice"
host: N02 "self-discipline"
Bars, title WHAT PREDICTED THEIR GRADES: SELF-DISCIPLINE (sage, tall, 2×) vs IQ (sky, short, 1×).
narration: "Self-discipline explained about twice as much of the difference in their grades as IQ did."

**D31** · picture S08 · camera zoom-out
edit: snap zoom to the focused student on "smart"
host: N02 "so" → N06 "it"
narration: "So discipline isn't just a nice extra. It might matter more than how smart you are."

**D32** · CODED card · camera hold
host: N06 "which"
Card: WHY IS IT / **SO HARD TO KEEP?**
narration: "Which raises the big question. If it's that important... why is it so hard to keep?"

---

## PART 3: Why discipline keeps breaking (`audio/part3.mp3`)

**D33** · icon I84 as the main picture · camera hold
edit: badge **4 REASONS** on "four"
host: N01 "there"
narration: "There are four reasons discipline keeps breaking."

**D34** · picture S09 (NEW: a gym packed shoulder to shoulder with stickmen on every machine, a "new year" party banner hanging from the ceiling (no letters), the narrator squeezed in the middle with a water bottle, excited eyes) · camera zoom-in
edit: snap zoom to the narrator on "motivation" (2nd occurrence)
narration: "One. You're running on motivation. Motivation is a feeling. And feelings come and go."
beats: step "one" → REASON 1 + RUNNING ON MOTIVATION · icon I108 "feeling"

**D35** · picture S20 · camera zoom-in
edit: name pill DAI, MILKMAN & RIIS (2014) on "researchers" · pills top-center: SEMESTER on "semester", BIRTHDAY on "birthday", MONDAY on "monday"
host: N01 "researchers"
narration: "Researchers at Wharton found that students were much more likely to hit the gym right after a fresh start, like the beginning of a semester, their birthday, or even just a Monday."

**D36** · picture S09, swapping to S09b on "empty" (NEW, edit of S09: the same gym a few weeks later, almost completely empty; the narrator is gone; one lonely stickman on a treadmill, the banner drooping) · camera zoom-in
edit: hard swap to S09b on "empty", with a ding
narration: "Think about how packed the gym is in the first week of January, and how empty it gets a few weeks later."

**D37** · picture S09b · camera zoom-in
edit: snap zoom to the lonely treadmill on "spark" · badge **A SPARK, NOT AN ENGINE** on "spark"
narration: "That burst of motivation is real. But it's a spark, not an engine."

**D38** · CODED card, swapping to card B on "mood" · camera hold
host: N05 "if"
Card A: ONLY WORKS WHEN MOTIVATED? Card B: THAT'S A ~~MOOD~~.
narration: "If your plan only works on the days you feel motivated, it's not a plan. It's a mood."

**D39** · picture S10 (NEW: a small, plain room; a young stickman kid sits at a table staring hard at a single fluffy marshmallow on a plate, sweating, gripping the table edge; a little bell on the table) · camera zoom-in
edit: name pill WALTER MISCHEL on "mischel's" · snap zoom to the marshmallow on "treat"
narration: "Two. You're fighting temptation face to face. In the famous marshmallow experiments, Walter Mischel's team left young kids alone with a treat. If they could wait, they'd get two."
beats: step "two" → REASON 2 + TEMPTATION FACE TO FACE · icon I103 "wait"

**D40** · picture S10, swapping to S10b on "covered" (NEW, edit of S10: the same kid, but the marshmallow is now hidden under an upside-down metal cake tin; the kid sits relaxed, humming, swinging his legs, eyes closed happily) · camera zoom-in
edit: snap zoom to the kid's straining face on "see" · hard swap to S10b on "covered", with a ding
narration: "Kids who could see the treat gave up much faster than kids who couldn't. When the treat was covered up, waiting got way easier."

**D41** · picture S02 · camera zoom-in
edit: snap zoom to the phone on "phone" · whip slide to the cereal on "snacks"
narration: "Most of us do the opposite. We leave the phone on the desk and the snacks on the counter, and then wonder why we keep giving in."
beats: icon I80 "wonder"

**D42** · picture S11 (NEW: the narrator standing in front of a glowing vending machine full of candy bars, his hand hovering over the button, torn eyes; a small stern rule-book sticks out of his hoodie pocket) · camera zoom-in
edit: speech pills: "I CAN'T HAVE SUGAR." on "sugar", "I CAN'T SKIP THE GYM." on "skip"
narration: "Three. Your rules feel like punishment. Listen to how you talk about your goals. "I can't have sugar." "I can't skip the gym.""
beats: step "three" → REASON 3 + RULES FEEL LIKE PUNISHMENT

**D43** · picture S20 · camera zoom-in
edit: name pill PATRICK & HAGTVEDT (2012) on "researchers"
host: N01 "researchers"
narration: "Researchers Vanessa Patrick and Henrik Hagtvedt found that the words you use matter."

**D44** · CODED bars3 · camera hold
edit: bars grow on "sixty" · impact hit on "thirty"
host: N01 "in"
Bars, title CHOSE THE HEALTHY SNACK: SAID "I DON'T" (sage, 64%) vs SAID "I CAN'T" (red, 39%).
narration: "In one study, people told to say "I don't" when tempted chose the healthy snack sixty-four percent of the time. People told to say "I can't"? Only thirty-nine percent."
beats: icon I107 "snack"

**D45** · CODED split · camera hold
edit: right side pops on "rule", left side on "who" · focus rack from right to left on "who"
host: N06 "i"
Right (red): "I CAN'T" → ~~A RULE~~. Left (yellow): "I DON'T" → **WHO YOU ARE**.
narration: ""I can't" sounds like a rule someone forced on you. "I don't" sounds like who you are."

**D46** · picture S12 (NEW: the narrator sitting on the floor next to a torn-up wall calendar; one day has a big red X, and the rest of the pages are ripped and scattered around him; defeated eyes) · camera zoom-in
edit: snap zoom to the red X on "miss" · zoom out on "quit"
narration: "Four. All or nothing. You miss one day, and suddenly the whole thing feels ruined. So you quit."
beats: step "four" → REASON 4 + ALL OR NOTHING

**D47** · picture S12 · camera zoom-in
edit: badge ~~1 SKIP → A WEEK~~ on "week" · thought-bubble pill "WHATEVER, I'LL START AGAIN MONDAY" on "whatever"
narration: "One skipped workout turns into a skipped week. One cheat meal turns into "whatever, I'll start again on Monday.""

**D48** · picture S20 · camera zoom-in
edit: name pill UNIVERSITY COLLEGE LONDON on "university" · badge **1 MISSED DAY = FINE** on "missing"
host: N01 "but"
narration: "But in a habit study at University College London, missing a single day didn't really slow down how fast people built their habit."

**D49** · CODED card, swapping to card B on "tell" · camera hold
host: N06 "it's"
Card A: NOT ~~THE MISS~~. Card B: WHAT YOU **TELL YOURSELF**.
narration: "It's not the miss that breaks you. It's what you tell yourself after it."

**D50** · picture S04b · camera zoom-in · crossfade in
edit: snap zoom to the torn schedule on "schedule"
narration: "That's exactly what happened to my schedule on the wall."

**D51** · CODED list · camera hold
edit: items pop on their words
host: N02 "so"
Items: 1 WAITING FOR MOTIVATION on "waiting", 2 TEMPTATION FACE TO FACE on "fighting", 3 RULES AS PUNISHMENT on "rules", 4 QUITTING AFTER ONE DAY on "quitting".
narration: "So put those four together. Waiting for motivation. Fighting temptation face to face. Rules that feel like punishment. And quitting after one bad day."

**D52** · CODED card, swapping to card B on "strategy" · camera hold
host: N06 "that's" → N01 "that's" (2nd occurrence)
Card A: NOT ~~WILLPOWER~~. Card B: A **STRATEGY** PROBLEM.
narration: "That's not a lack of willpower. That's a strategy problem. And strategies can be fixed."

---

## PART 4: Five ways to build discipline that lasts (`audio/part4.mp3`)

**D53** · CODED card · camera hold
edit: count-up 5 on "five"
host: N01 "so"
Card: **5** STEPS.
narration: "So here's how to build discipline that lasts. Five steps."

**D54** · picture S13 (NEW: a view through a doorway: in the far kitchen, the narrator's phone sits charging on the counter; in the near room, the narrator works at his desk, focused and calm, with nothing tempting around him) · camera zoom-in
edit: snap zoom to the phone in the kitchen on "temptation" → whip slide to the narrator at his desk on "avoid"
narration: "One. Make temptation hard to reach. Do what the disciplined people in the beeper study do. Avoid the fight before it starts."
beats: step "one" → STEP 1 + MAKE IT HARD TO REACH

**D55** · picture S13 · camera zoom-out
edit: pills top-center one by one: ANOTHER ROOM on "room", NO JUNK FOOD on "junk", DELETE THE APP on "delete"
narration: "Put your phone in another room while you work. Don't keep junk food in the house. Delete the app for a week."
beats: icon I104 "app"

**D56** · picture S13 · camera zoom-in
edit: snap zoom to the narrator on "distance" · zoom out on "need"
narration: "Every bit of distance gives you a few seconds to choose. And a few seconds is often all you need."

**D57** · icon I80 as the main picture · camera hold
edit: badge **PHONE IN THE KITCHEN** on "kitchen"
host: N01 "for"
narration: "For me, the biggest one was my phone. When it charged in the kitchen instead of next to my bed, I stopped scrolling at midnight without even trying."

**D58** · CODED card · camera hold
edit: marker highlight on TESTING on "testing"
host: N05 "you"
Card: STOP **TESTING** IT.
narration: "You don't need more willpower when you stop testing it."

**D59** · picture S14 (NEW: the narrator in bed reading a book under a warm lamp, calm content eyes; on the nightstand, a toothbrush in a cup next to the book's empty spot, showing the routine) · camera zoom-in
edit: snap zoom to the book on "same" (1st occurrence)
narration: "Two. Same time, same place."
beats: step "two" → STEP 2 + SAME TIME, SAME PLACE

**D60** · CODED pie · camera hold
edit: name pill WENDY WOOD on "psychologist" · pie fills with a count-up to **43%** on "forty" · impact hit on "forty"
host: N01 "psychologist"
Pie label: DONE ALMOST EVERY DAY:
narration: "Psychologist Wendy Wood found that about forty-three percent of the things people did each day were things they did almost every day, usually in the same place."

**D61** · picture S20 · camera zoom-in
edit: pills top-center one by one: EXERCISING on "exercising", SLEEPING WELL on "sleeping", STUDYING on "studying"
host: N01 "and"
narration: "And Angela Duckworth's team found that people with more self-control tend to have stronger good habits, like exercising, sleeping well and studying."

**D62** · picture S14 · camera zoom-in
edit: snap zoom to his face on "forcing" · snap zoom to the book on "reading" · badge **BORING & AUTOMATIC** on "boring"
narration: "They aren't forcing themselves every day. The habit does the work. So pick one time and one place. The gym right after work. Reading right after you brush your teeth. Make it boring and automatic."
beats: icon I78 "gym"

**D63** · picture S15 (NEW: the narrator calmly and confidently pushing away a plate of glazed donuts with one hand, the other hand in his hoodie pocket, relaxed half-closed eyes, totally unbothered) · camera zoom-in
edit: snap zoom to the hand pushing the plate on "don't"
narration: "Three. Say "I don't," not "I can't." Remember the snack study."
beats: step "three" → STEP 3 + SAY "I DON'T"

**D64** · CODED bars3 · camera hold
edit: bars grow on "eight" · impact hit on "only"
host: N01 "in"
Bars, title STUCK WITH THEIR GOAL FOR 10 DAYS: SAID "I DON'T" (sage, 8 OF 10) vs SAID "I CAN'T" (red, 1 OF 10).
narration: "In another part of that research, women with a personal health goal used one of the strategies for ten days. Eight out of ten who used "I don't" stuck with their goal the whole time. Only one out of ten using "I can't" did."

**D65** · picture S15 · camera zoom-out
edit: speech pills: "I DON'T SKIP WORKOUTS." on "skip", "I DON'T SCROLL IN BED." on "scroll"
narration: ""I don't skip workouts." "I don't scroll in bed." It turns a rule into part of who you are. And people protect who they are."
beats: card "protect" → PEOPLE **PROTECT** WHO THEY ARE

**D66** · picture S16 (NEW: night; the narrator packing a gym bag by the front door, sneakers and a water bottle ready beside it, his phone showing a sent text bubble with a thumbs-up reply) · camera zoom-in
edit: name pill ARIELY & WERTENBROCH (2002) on "economists" · snap zoom to the bag on "decide"
narration: "Four. Decide before you're tempted. Behavioral economists Dan Ariely and Klaus Wertenbroch gave people three proofreading jobs to finish."
beats: step "four" → STEP 4 + DECIDE IN ADVANCE

**D67** · CODED split · camera hold
edit: right side pops on "some", left side on "others"
host: N01 "some"
Right (red): ONE DEADLINE → **AT THE END**. Left (yellow): THEIR OWN DEADLINES → **SET IN ADVANCE**.
narration: "Some had one deadline at the very end. Others set their own deadlines for each one, in advance."

**D68** · CODED card · camera hold
edit: marker highlight on BETTER WORK on "better"
host: N02 "the"
Card: SET YOUR OWN DEADLINES = / **BETTER WORK**.
narration: "The people who set their own deadlines did better work, and turned it in late less often, than the people with one big deadline at the end."

**D69** · picture S16 · camera zoom-in
edit: snap zoom to the bag on "pack" → whip slide to the phone on "friend"
narration: "In the moment, you're weaker. So make the decision now, while you're thinking clearly. Pack the gym bag tonight. Tell a friend you'll be there at six."
beats: icon I106 "tonight"

**D70** · picture S17 (NEW: the narrator walking along a path of round stepping stones across a calm pond; one stone in the path is missing, and he simply steps over the gap onto the next stone, steady and calm) · camera zoom-in
edit: snap zoom to the gap in the stones on "miss" (2nd occurrence)
narration: "Five. Never miss twice. You're going to miss days. Everyone does. And the habit study showed that one miss doesn't ruin anything."
beats: step "five" → STEP 5 + NEVER MISS TWICE

**D71** · picture S17 · camera zoom-in
edit: badge **MISS TODAY? NOT TOMORROW.** on "today" · snap zoom to his steady step on "rule"
narration: "A bad day isn't the end of the habit. It's just a bad day. So make one simple rule. If you miss today, you don't miss tomorrow."

**D72** · picture S04b · camera zoom-in · crossfade in
edit: light leak (memory) on "schedule" · snap zoom to his face on "next" (1st occurrence)
narration: "That's what I should have done with my schedule on day three. Not wait for Monday to start over. Just do the next thing, the next day."

**D73** · picture S07 · camera zoom-in · crossfade in
edit: snap zoom to the calm walker on "disciplined" · zoom out on "easy"
narration: "Here's what I keep coming back to. The most disciplined people you know aren't superheroes with endless willpower. They're just people who made the right thing easy, and the wrong thing hard."

**D74** · picture S18 (NEW: early morning sunrise; the narrator walks out of his front door with a gym bag on his shoulder, calm happy eyes; through the window behind him, his phone sits charging on the kitchen counter) · camera zoom-in
edit: iris reveal into the picture on "discipline" · light sweep on "building"
narration: "Discipline isn't about fighting yourself every single day. It's about building a life where you don't have to. Motivation gets you started. Your setup keeps you going."

**D75** · picture S18 · camera zoom-out · **at least 2s of silence after "two"**
edit: pills top-center one by one: MOVE ONE TEMPTATION on "move", ONE TIME, ONE PLACE on "pick", NEVER MISS TWICE on "miss"
narration: "So you don't need another midnight plan. You need one small change that makes tomorrow a little easier. Move one temptation out of reach. Pick one time and one place. And if you miss a day, just don't miss two."

**D76** · picture S29 (COPY: narrator on the right, pointing left; end screen) · camera hold · hold the last frame 5s after the narration
narration: "What's one temptation you're going to move out of reach this week? Tell me in the comments. And if you keep putting things off before you even start, I made a whole video on the psychology of procrastination. I'll leave it right here."
beats: pop N06 "what's" → card YOUR **ONE TEMPTATION?** (finish it before "and if" so the end screen stays clean)
