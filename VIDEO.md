# Current video: "The Psychology of Self-Doubt: Where It Really Comes From"

**Topic:** self-doubt is learned, not born. Bandura's self-efficacy: belief is built from evidence. Four sources of bad evidence (no proof yet, unfair comparison, the louder critical voice, misread nerves), and five research-backed ways to collect new proof.
**Follows:** `PLAYBOOK.md` (cold open → personal story → research → 4 sources → 5 steps → emotional close). It pays off the promise in the manifestation video ("I'm making a whole video on it next") and points to the spotlight video at the end.
**Length:** the raw voice is about 1,590 words. After pause padding, the target is about **11:00**.
**Audio:** 14 clips, `audio/part1a.mp3` … (Part 1 a–c, Part 2 a–c, Part 3 a–d, Part 4 a–d). Run `python3 tools/join-clips.py` first.
**Music:** `music/track.mp3`, mixed softly. Keep it at its quietest during the cold open (D01–D05) and the final scene (D53).
**Upload kit:** `prompts/upload-package.md`.
**Spec examples:** copy the helpers from `videos/02-regret/make-specs.py`. Videos 2–4 use the same notation.

## How to read this list

- **Scene IDs (D01…) and picture files (S01.png…) are separate.** `(NEW)` = Luke makes it (`prompts/nano-banana-prompts.md`). `(COPY)` = already in `pictures/`. `CODED` = build it in code.
- **beats:** key moments with the exact trigger word in quotes: `icon Ixx "word"`, `pop Nxx "word" → content`, `card "word" → TEXT`, `step "word" → STEP n + TEXT`, `badge "word" → TEXT`. **Bold** = yellow badge, ~~struck~~ = red badge. Fill the rest per CLAUDE.md (every shot ≤ 4s, except the cold-open scenes).
- **edit:** specific moves (CLAUDE.md section 9). **host:** the narrator-host pose track; no `host:` line = full-frame.
- **narration** is for timing only and must match the audio. Never show it on screen.
- **Icons:** I06, I11, I41, I52, I63 and I67 are reused (already in `icons/`). I71–I78 are new (`prompts/icon-prompts.md`). Missing icon → skip that beat.
- **Numbers:** Whisper may write "nineteen-seventies" as "1970s", "nineteen-fifties" as "1950s", "two thousand one" as "2001", "ninety-two percent" as "92%", "twelve thousand" as "12,000". Match triggers either way.

---

## The cold open

D01–D05 are in the normal comic style, but slightly slower and calmer: shots may run up to **4.5s**, moves are snap zooms and soft pushes on words, and the music stays at its quietest. After D05, show the **title card** right away: green pill **LESSON**, big text PSYCHOLOGY OF / SELF-DOUBT, with "SELF-DOUBT" in orange, 2.5s.

## The narrator host

Same rules as before (poses from the tone tags, frame on the right, hard-cut pose changes, never animated, he stays put between host scenes). Host scenes are pictures without the narrator and coded diagrams. No host stretch longer than about 40s.

---

## PART 1: The cold open and my story (`audio/part1.mp3`)

**D01** · picture S01 (NEW: a little kid version of the narrator proudly holding a crayon drawing up high: a purple sun and a dog with six legs) · camera zoom-in
edit: snap zoom to the drawing on "picture" → whip slide to the purple sun on "purple" → whip slide to the six-legged dog on "dog"
narration: "Think about a little kid who just drew a picture. A purple sun. A dog with six legs."

**D02** · picture S01 · camera zoom-out
edit: zoom back out to the whole kid on "run" · light sweep across the drawing on "high"
narration: "Do they wonder if it's good enough? Do they compare it to anyone else's? No. They run straight to you and hold it up as high as they can."

**D03** · picture S02 (NEW: the narrator at a desk at night, hugging a sketchbook against his chest, crumpled pages on the floor) · camera zoom-in
edit: hard cut in on "now" · snap zoom to the hidden sketchbook on "hide"
narration: "Now think about the last time you made something. A drawing. A song. A business idea. A message to someone you like. Did you hold it up? Or did you hide it... until it was perfect... and then never show anyone at all?"

**D04** · picture S03 (NEW: the narrator with sad eyes, a tall soft shadow figure leaning in behind him, whispering into his ear) · camera zoom-in
edit: snap zoom to the shadow on "voice" · three speech-bubble pills pop beside the shadow, one per quote: "YOU'RE NOT READY" on "ready", "WHO DO YOU THINK YOU ARE?" on "who", "DON'T EMBARRASS YOURSELF" on "embarrass"
narration: "Somewhere between that kid and you, a voice showed up. The one that says, "You're not ready." "Who do you think you are?" "Don't embarrass yourself." And here's the part most people never stop to think about."

**D05** · picture S04 (NEW: the narrator kneeling, picking up his old childhood crayon drawing of a purple sun from the floor, the shadow fading behind him) · camera zoom-in · **reveal: at least 2s of silence after**, then the title card
edit: soft riser into the scene · snap zoom to the drawing on "born" · impact hit on "learned"
narration: "You weren't born with that voice. You learned it."
beats: card "learned" → YOU **LEARNED** IT

**D06** · picture S05 (NEW: narrator at his desk with a microphone and laptop, finger on the delete key, crumpled script pages around him) · camera zoom-in
edit: hard cut from the title card · snap zoom to his finger on the key on "deleted"
narration: "I know that voice really well. When I started this channel, I wrote my first script three times. I recorded it, listened back, and deleted it. Twice."
beats: icon I71 "recorded" · icon I72 "twice"

**D07** · picture S06 (NEW: narrator at his laptop while a small dark shadow version of himself sits on his shoulder, whispering) · camera zoom-in
edit: snap zoom to the shadow on "voice" · three speech-bubble pills pop beside the shadow, one per quote: "YOUR VOICE SOUNDS WEIRD" on "weird", "NOBODY'S GOING TO WATCH" on "nobody's", "REAL CREATORS DON'T…" on "real" · zoom out on "almost"
narration: "Every time, the voice had a new reason. "Your voice sounds weird." "Nobody's going to watch this." "Real creators don't make videos like this." I almost didn't post anything at all. And if you're watching this, you already know how that turned out."
beats: pop N05 "watching" → card YOU KNOW **HOW IT ENDED**

**D08** · picture S20 (COPY: researcher at a desk with a huge pile of notes) · camera zoom-in
edit: snap zoom to the researcher on "psychologists"
host: N06 "but" → N01 "so"
narration: "But it made me want to understand where that voice actually comes from. So I went looking at what psychologists have found."

**D09** · CODED iconRow · camera hold
host: N01 "by"
Icons: I74 on "four", I72 on "believe", I67 on "five". Labels: 4 SOURCES · WHY "BELIEVE" FAILS · 5 FIXES.
narration: "By the end of this video, you'll know the four places self-doubt really comes from, why "just believe in yourself" almost never works, and five ways to rebuild your confidence that are actually backed by research."

**D10** · icon I11 as the main picture · camera hold
edit: badge pops on "two": **2 SECONDS**
host: N01 "one"
narration: "One of them takes about two seconds, and you can use it before anything that scares you."

---

## PART 2: Where belief comes from (`audio/part2.mp3`)

**D11** · picture S20 · camera zoom-in
edit: push wipe in (time jump) on "in" · name pill ALBERT BANDURA on "Bandura" · snap zoom to the researcher on "why"
host: N01 "in" → N06 "why"
narration: "In the nineteen-seventies, a psychologist named Albert Bandura became obsessed with one question. Why do some people keep going when things get hard, while others give up before they even start?"

**D12** · CODED card, swapping to card B on "self-efficacy" · camera hold
edit: ~~TALENT~~ pops on "talent", ~~INTELLIGENCE~~ on "intelligence" · kinetic swap to card B with a ding · marker highlight
host: N01 "it" → N02 "it" (3rd occurrence)
Card A: ~~TALENT~~ ~~INTELLIGENCE~~. Card B: **SELF-EFFICACY** (small line under it: believing you can do it).
narration: "It wasn't talent. It wasn't intelligence. It was what he called self-efficacy. Your belief that you can actually do the thing in front of you."

**D13** · picture S26 (COPY: narrator facing a mirror that shows a confident version of him) · camera zoom-in
edit: snap zoom to the mirror on "mirror"
narration: "And Bandura found something surprising. That belief doesn't come from nowhere. And it doesn't come from repeating "I can do it" in the mirror."

**D14** · CODED card, swapping to card B on "wrong" · camera hold
edit: marker highlight on EVIDENCE · red stamp on card B
host: N02 "it"
Card A: IT COMES FROM **EVIDENCE**. Card B: SELF-DOUBT = ~~WRONG PROOF~~.
narration: "It comes from evidence. Your brain is constantly collecting proof about what you can and can't do. And self-doubt is what happens when your brain has collected the wrong proof."

**D15** · CODED quad · camera hold
edit: the four tiles pop on their words · all four pulse on "mind"
host: N01 "he" → N06 "keep"
Tiles: DOING IT (I52) on "doing", WATCHING OTHERS (I06) on "watching", WHAT PEOPLE SAY (I41) on "tell", YOUR BODY (I75) on "body".
narration: "He found four main places that belief comes from. Doing something yourself. Watching someone like you do it. What other people tell you. And how your body feels when you try. Keep those four in mind, because they're going to come back."

**D16** · picture S07 (NEW: a nervous stickman pressed against the wall far from a glass tank with a snake inside, a calm stickman next to the tank, a researcher with a clipboard) · camera zoom-in
edit: snap zoom to the nervous stickman on "nervous" → whip slide to the tank on "tank"
host: N01 "one" → N05 "not"
narration: "One of his most famous experiments involved people with a serious fear of snakes. Not a little nervous. Some of them couldn't even stand near one in a glass tank."
beats: icon I73 "snakes"

**D17** · picture S07 · camera zoom-in
edit: snap zoom to the calm handler on "watched" → whip slide to the nervous stickman on "step" (1st occurrence) · step pills pop top-center one by one: LOOK on "look", CLOSER on "closer", GLOVE on "glove", NO GLOVE on "without"
host: N01 "bandura"
narration: "Bandura didn't tell them to be brave, and he didn't try to talk them out of it. Instead, they watched someone else handle a snake calmly. Then, step by step, they did tiny pieces themselves. Look at the snake. Stand a little closer. Touch it with a glove. Then without one."

**D18** · CODED pie, then picture S07b (NEW: the same nervous stickman now sitting calmly with the snake resting in his lap, small proud smile) on "lap" · camera hold · **reveal: at least 2s of silence after "lap"**
edit: riser before it · pie fills 0 → 92% with a count-up on "ninety-two" · impact hit · hard cut to S07b with a ding on "lap"
host: N02 "by"
Pie label: SNAKE IN THEIR LAP: **92%**. Small line: Bandura, Blanchard & Ritter, 1969.
narration: "By the end, ninety-two percent of the people in that group could sit with a snake resting in their lap."

**D19** · picture S07b · camera zoom-in
edit: snap zoom to his small smile on "brave" (2nd occurrence)
host: N06 "they" → N01 "and" → N06 "proof" (2nd occurrence)
narration: "They didn't feel brave first. They became brave by collecting small proof that they could handle it. And a lot of them reported feeling less afraid of other things in their lives too. Proof in one area spilled into others."
beats: card "first" → THEY DIDN'T FEEL **BRAVE FIRST**

**D20** · CODED card, swapping to card B on "conclusion" · camera hold · **reveal: at least 2s of silence after**
edit: kinetic word swap FEELING → CONCLUSION · light sweep across card B
host: N02 "that's" → N06 "confidence" → N01 "it's"
Card A: CONFIDENCE ISN'T ~~A FEELING~~. Card B: IT'S A **CONCLUSION**.
narration: "That's the key to this whole video. Confidence isn't a feeling you wait for. It's a conclusion your brain reaches after enough evidence."

**D21** · picture S06 · camera zoom-in
edit: snap zoom to the shadow on "self-doubt"
narration: "So if self-belief is built from evidence... where does all the evidence for self-doubt come from?"

---

## PART 3: The 4 sources of self-doubt (`audio/part3.mp3`)

**D22** · picture S20 · camera zoom-out
host: N01 "bandura"
narration: "Bandura and the researchers who followed him point to a few main sources. Here are the four that show up the most."

**D23** · picture S08 (NEW: narrator at the start of a bridge disappearing into thick fog, he can't see the other side) · camera zoom-in
edit: snap zoom into the fog on "gap"
narration: "One. You don't have proof yet. This is the most common one, and the most fixable. If you've never done something, your brain has no evidence that you can. So it fills the gap with doubt."
beats: step "one" → SOURCE 1 + NO PROOF YET

**D24** · CODED iconRow · camera hold
host: N01 "the"
Icons: I77 on "drive", I71 on "speech", I78 on "gym". Label under the row on "guesses" (1st occurrence): YOUR BRAIN IS **GUESSING**.
narration: "The first time you drive, give a speech, or walk into a gym, your brain is basically guessing. And when it guesses, it guesses low, to keep you safe."

**D25** · CODED card, swapping to card B on "idea" · camera hold
edit: kinetic swap · light sweep on card B
host: N06 "that" → N05 "your"
Card A: NOT ~~"YOU'RE BAD AT THIS"~~. Card B: **"I HAVE NO IDEA"**.
narration: "That doesn't mean you can't do it. It means you haven't shown yourself yet. Your brain isn't saying "you're bad at this." It's saying "I have no idea.""

**D26** · picture S09 (NEW: narrator slumped at a messy desk scrolling his phone, giant glowing "highlight" cards towering over him: a finished painting, a gym photo, a trophy, a smiling crowd) · camera zoom-out
edit: snap zoom to the giant cards on "outside"
narration: "Two. You compare your inside to everyone else's outside."
beats: step "two" → SOURCE 2 + UNFAIR COMPARISON

**D27** · picture S20 · camera zoom-in
edit: name pill LEON FESTINGER on "Festinger" · push wipe in on "back"
host: N01 "back"
narration: "Back in the nineteen-fifties, a psychologist named Leon Festinger pointed out that we figure out how good we are by comparing ourselves to other people."

**D28** · picture S09 · camera pan-right
edit: tour: snap zoom to the painting card on "painting" → whip slide to the gym card on "gym" → snap zoom to his messy desk on "messy" → zoom out to everything on "highlight"
narration: "The problem is, today you're comparing yourself to millions of people... and only seeing their best moments. You see their finished painting, not the hundred bad ones before it. You see the gym photo, not the year of showing up tired. So your messy middle always looks worse than their highlight reel."
beats: badge "millions" → **MILLIONS** OF PEOPLE · card "messy" → YOUR MIDDLE VS **THEIR HIGHLIGHTS**

**D29** · picture S10 (NEW: narrator holding a balance scale: ten small gold stars on one side, one heavy dark stone on the other side pulling it all the way down) · camera zoom-in
edit: snap zoom to the heavy stone on "louder"
narration: "Three. The critical voice is louder than the kind one."
beats: step "three" → SOURCE 3 + THE LOUDER VOICE

**D30** · picture S20 · camera zoom-in
edit: name pill ROY BAUMEISTER, 2001 on "Baumeister"
host: N02 "in"
narration: "In two thousand one, a group of researchers led by Roy Baumeister reviewed hundreds of studies and came to a simple conclusion. Bad is stronger than good."
beats: card "stronger" → BAD IS **STRONGER** THAN GOOD

**D31** · picture S10 · camera zoom-in
edit: snap zoom to the stone on "harsh" → whip slide to the ten stars on "ten"
narration: "One harsh comment sticks with you longer than ten compliments."

**D32** · CODED bars · camera hold · **reveal: at least 2s of silence after**
edit: badge counts up to 12,000 DIARY ENTRIES on "twelve" · bars grow on "setback": SETBACK (red, tall) vs STEP FORWARD (sage, short) · badge **2–3×** pops with an impact hit on "two" (1st occurrence)
host: N01 "in" → N02 "a"
Small source line: Amabile & Kramer, Harvard.
narration: "In another study, researchers at Harvard collected almost twelve thousand daily diary entries from people at work. A setback hit people's mood about two to three times harder than a step forward helped it."

**D33** · picture S06 · camera zoom-in
edit: snap zoom to the whispering shadow on "louder"
narration: "So if someone once told you that you weren't good at something, that one moment might still be louder than everything good anyone's said since."

**D34** · picture S11 (NEW: narrator backstage behind a curtain before going on stage, shaky hands, a glowing heart racing in his chest, sweat drop) · camera zoom-in
edit: snap zoom to his heart on "heart" → whip slide to his shaking hands on "hands"
narration: "Four. You misread your own body. Before something big, your heart beats faster. Your hands shake a little. Your stomach drops."
beats: step "four" → SOURCE 4 + MISREAD NERVES · icon I75 "stomach"

**D35** · CODED quad (callback to D15) · camera hold
edit: the YOUR BODY tile lights up and the other three dim on "Bandura"
host: N06 "and" → N02 "bandura"
narration: "And your brain takes that feeling as a message: "See? You can't handle this." Bandura listed this as one of the main sources of self-doubt. People treat normal nerves as proof that they're not ready."
beats: pop N06 "see" → card SEE? **YOU CAN'T**

**D36** · CODED list · camera hold · **reveal: at least 2s of silence after "evidence"**
edit: four pills stack in on their words: NO PROOF YET on "proof", UNFAIR COMPARISONS on "unfair", A LOUDER VOICE on "louder", MISREAD NERVES on "misread" · red stamp **BAD EVIDENCE** across them on "bad"
host: N02 "so" → N06 "that's"
narration: "So put those four together. No proof yet. Unfair comparisons. A louder critical voice. And misread nerves. That's not the truth about who you are. That's just a lot of bad evidence."

**D37** · picture S26 · camera zoom-out
edit: snap zoom to the mirror on "believe"
narration: "And that's why "just believe in yourself" almost never works. You can't argue your brain out of something it thinks it has evidence for. But you can give it new evidence."
beats: card "new" → GIVE IT **NEW EVIDENCE**

---

## PART 4: The 5 steps and the ending (`audio/part4.mp3`)

**D38** · picture S24 (COPY: narrator at the foot of a giant mountain, one small step at his feet) · camera zoom-in
edit: snap zoom to the small step on "jump"
narration: "So here's how I actually do that now. Five steps. One. Collect tiny proof. Remember the snake study. Nobody went from terrified to holding a snake in one jump."
beats: step "one" → STEP 1 + COLLECT TINY PROOF

**D39** · picture S24 · camera zoom-in
edit: whip slide up the mountain on "next"
narration: "Pick something you doubt you can do, and break it into a step so small it's almost embarrassing. Then do that step. Then the next one. Every small step is one more piece of evidence for your brain."
beats: card "embarrassing" → **ALMOST EMBARRASSING** · icon I52 "evidence"

**D40** · picture S05 · camera zoom-in
edit: snap zoom to the microphone on "record"
narration: "For this channel, my first step wasn't "make a great video." It was "record one minute and don't delete it.""
beats: badge "record" → **1 MINUTE**. DON'T DELETE.

**D41** · CODED card, swapping to card B on "little" · camera hold
edit: kinetic swap · light sweep
host: N05 "in"
Card A: BEST DAYS ≠ ~~HUGE WINS~~. Card B: BEST DAYS = **A LITTLE PROGRESS**.
narration: "In that diary study, the days people felt best weren't the days they did something huge. They were the days they made a little progress."

**D42** · picture S12 (NEW: narrator on a hillside path looking up at another brain-head character a few steps ahead, who turns back and waves him on) · camera zoom-in
edit: snap zoom to the character ahead on "ahead" → whip slide back to the narrator on "started"
narration: "Two. Watch someone like you do it. Not the most famous person in the world. Someone a few steps ahead of you. Someone who started where you are."
beats: step "two" → STEP 2 + WATCH SOMEONE LIKE YOU

**D43** · CODED quad (callback) · camera hold
edit: the WATCHING OTHERS tile lights up on "seeing"
host: N06 "bandura"
narration: "Bandura found that seeing someone similar succeed is one of the strongest ways to build belief. Because your brain thinks, "If they can, maybe I can.""
beats: card "if" → IF THEY CAN, **MAYBE I CAN**

**D44** · picture S26 · camera zoom-in
edit: name pill ETHAN KROSS on "Kross" · snap zoom to the reflection on "own"
narration: "Three. Talk to yourself by name. Psychologist Ethan Kross found that when people talked to themselves using their own name or "you," instead of "I," they felt less anxious and actually performed better under pressure."
beats: step "three" → STEP 3 + TALK TO YOURSELF BY NAME

**D45** · CODED card, swapping to card B on "Luke" · camera hold
edit: kinetic swap · marker highlight on YOU CAN DO THIS
host: N01 "so" → N05 "it"
Card A: ~~"I CAN'T DO THIS"~~. Card B: "LUKE, **YOU CAN DO THIS**".
narration: "So instead of "I can't do this," try "Luke, you've done hard things before. You can do this too." It sounds a little strange. But it gives you a bit of distance from the panic, like advice from a friend."
beats: pop N05 "strange" → card **LIKE A FRIEND**

**D46** · picture S13 (NEW: narrator on a small karaoke stage holding a microphone, nervous-excited eyes, spotlight, a few stickmen watching) · camera zoom-in
edit: snap zoom to his face on "excited"
narration: "Four. Rename the nerves. This is the two-second one. Before something scary, say out loud, "I'm excited.""
beats: step "four" → STEP 4 + RENAME THE NERVES · icon I11 "two-second"

**D47** · picture S28 (COPY: one figure on a lit stage, a dark crowd of eyes) · camera zoom-in
edit: name pill ALISON WOOD BROOKS on "Brooks" · snap zoom to the figure on stage on "singing"
narration: "A Harvard researcher named Alison Wood Brooks had people do stressful things like singing in front of others and giving a speech. The people who said "I'm excited" first did better than the people who tried to calm down."
beats: card "better" → "I'M EXCITED" **WINS**

**D48** · CODED split · camera hold
edit: left pops on "nerves", right on "excitement", a ≈ sign pops between them on "same"
host: N06 "because"
Left: **NERVES**. Right: **EXCITEMENT**.
narration: "Because nerves and excitement feel almost the same in your body. You're just choosing which story your brain tells about it."

**D49** · picture S14 (NEW: narrator sitting on his bed smiling at his phone, the screen showing a checklist note with ticks) · camera zoom-in
edit: snap zoom to the phone on "note" · three tick pills pop top-center: SPOKE UP ✓ on "spoke", FINISHED THE WORKOUT ✓ on "finished", POSTED THE VIDEO ✓ on "posted"
narration: "Five. Keep a proof list. Get a note on your phone and every time you do something you doubted you could do, write it down. Even small things. You spoke up in class. You finished the workout. You posted the video."
beats: step "five" → STEP 5 + KEEP A PROOF LIST

**D50** · icon I76 as the main picture · camera hold
edit: the receipt unrolls downward (clip-path wipe, 0.6s) on "list"
host: N01 "then" → N05 "it's"
narration: "Then, the next time the voice says "you can't," you open the list. It's a lot harder for your brain to argue with a receipt."
beats: badge "receipt" → ARGUE WITH **A RECEIPT**

**D51** · picture S01 (the cold-open picture, callback) · camera zoom-in · crossfade in
edit: snap zoom to the drawing on "drawing" · light leak (memory) on "kid"
narration: "Here's what I keep coming back to. That little kid with the drawing didn't have more talent than you. They just didn't have any bad evidence yet. Nobody had told them it wasn't good enough. They hadn't compared it to anyone. They hadn't learned to read their nerves as a warning."

**D52** · picture S12 · camera zoom-out · crossfade in
narration: "Every confident person you've ever met was once a beginner with no proof at all."

**D53** · picture S15 (NEW: the narrator standing in warm sunlight, proudly holding his sketchbook drawing up high, exactly like the kid did, the shadow gone) · camera zoom-in · **at least 2s of silence after "used to"**
edit: iris reveal into the picture on "good" · light sweep on "hold"
narration: "And the good news is, if self-doubt was learned... it can be unlearned. Not by pretending. By collecting new proof, one small step at a time. So find one thing you've been hiding until it's perfect. And show someone. Hold it up, like you used to."

**D54** · picture S29 (COPY: narrator on the right, pointing left; end screen) · camera hold · hold the last frame 5s after the narration
narration: "What's one thing you doubted you could do, that you ended up doing anyway? Tell me in the comments. It might be exactly the proof someone else needs. And if your doubt is really about what other people will think, I made a whole video on why they're barely watching. I'll leave it right here."
beats: pop N06 "doubted" → card **YOUR PROOF?** (finish it before "and if" so the end screen stays clean)

---

## New diagram kinds to add to `tools/build-part.mjs`

Same look as before: cream background, 9px ink outlines, Nunito ExtraBold, yellow or red outlined badges, seek-safe. (If video 3/4 kinds were lost, rebuild only what this list needs.)

- **quad:** a 2×2 grid of rounded tiles, each with an icon and a label (≥ 56px). Options: `tiles: [[label, icon, word]]` (pop in on their words), `active` (one tile full-color, the rest 40%), `pulse` (word). Used in D15, D35 and D43.
- **list:** pills stacking top to bottom on their words, plus an optional red stamp across them on a word. Used in D36.
- **bars:** two vertical bars (red SETBACK, sage STEP FORWARD), no y numbers, a **2–3×** badge on a word, plus a count-up badge for 12,000. Used in D32.
- **pie, split, card → card swap, iconRow, icon-as-main-picture:** the existing kinds.

### Description sources (for Luke, not on screen)
- Bandura (1977), "Self-efficacy: Toward a unifying theory of behavioral change," *Psychological Review*
- Bandura, Blanchard & Ritter (1969), participant modeling and snake phobia, *JPSP*
- Festinger (1954), "A theory of social comparison processes," *Human Relations*
- Baumeister, Bratslavsky, Finkenauer & Vohs (2001), "Bad is stronger than good," *Review of General Psychology*
- Amabile & Kramer (2011), *The Progress Principle*
- Kross et al. (2014), "Self-talk as a regulatory mechanism," *JPSP*
- Brooks (2014), "Get excited: Reappraising pre-performance anxiety as excitement," *JEP: General*
