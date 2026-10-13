# Current video: "Psychology of Regret: Why Playing It Safe Haunts You Later"

**Topic:** regrets of inaction. Over time, people regret what they *didn't* do far more than what they did.
**Follows:** `PLAYBOOK.md` (hook → personal story → research → 4 reasons → 5 steps → emotional close). It calls back to the spotlight video twice.
**Length:** the raw voice is about 1,710 words. After pause padding, the target is about **11:30–12:00**.
**Audio:** `audio/part1.mp3` … `audio/part4.mp3` (ElevenLabs, from Luke).
**Music:** `music/track.mp3`, mixed softly as before.
**Upload kit** (title, thumbnail, description, tags): `prompts/upload-package.md`.

## How to read this list

- **Scene IDs (R01…) and picture files (S01.png…) are separate.** The `picture:` field names the exact file in `pictures/` (or an icon in `icons/`). The same picture can be used by several scenes.
  - `(NEW)` means Luke makes it (prompt in `prompts/nano-banana-prompts.md`).
  - `(COPY)` means it's already in `pictures/` (reused from video 1).
  - `CODED` means you build it in code (see "New diagram kinds" at the bottom).
- **beats:** the key moments, with the exact trigger word in quotes. Fill the remaining time with crops, cards, icons and pop-ups as the CLAUDE.md pacing rules say (every shot ≤ 4s).
  - `icon Ixx "word"` is an icon cutaway.
  - `pop Nxx "word" → content` is a narrator pop-up.
  - `card "word" → TEXT` is a text card. **Bold** words go in a yellow badge and ~~struck~~ words in a red badge.
  - `step "word" → STEP n + TEXT` is the top-center step pill.
  - `crop "word" → subject` is a punch-in crop of the main picture.
- **edit:** lines are the specific edits for that scene (snap zoom, whip slide, callout, count-up…). See the editing toolkit, CLAUDE.md section 9. Every scene without an `edit:` line still gets motivated moves from the toolkit defaults.
- **narration** is used for timing only and must match the audio. Never show it on screen.
- **Icons:** I06–I30 are reused from video 1. I40–I50 are new (Luke makes them; prompts in `prompts/icon-prompts.md`). If an icon file is missing, skip that beat.

---

## The narrator host (new for this video)

The narrator **stands at the side of scenes and "explains" them** for most of the video. His pose changes with the tone of the voice, even inside one scene.

- **`host:` lines** list his pose track for that scene: a pose, then the word where he hard-cuts to the next pose. The tracks come from the tone tags in Luke's script:
  - calm or storytelling → N01
  - curious, thoughtful or reflective → N06
  - serious, emphatic or a key number → N02
  - wry or light → N05
  - upbeat or a step → N07
  - counting a numbered reason → N08
  - a reveal → N09
  - embarrassed → N10
  - a confident statement → N11
  - the outro → N12
  - You may add one more swap where the tone clearly shifts (at most 3 poses per scene, and each pose held at least 2s).
- **Layout ("host frame"):**
  - Cream background. The scene's picture, diagram, card or icon goes in a **rounded frame on the right** (about 74% of the width, 6px ink outline, radius 28px, vertically centered).
  - The narrator stands in the **lower-left**, about 60% of the frame height, overlapping the frame edge slightly, with a soft ground shadow.
  - Crops and camera moves happen *inside* the frame.
- **Motion:**
  - He slides in from the left (0.25s, ease-out) when a host stretch starts and slides out (0.2s) when it ends.
  - When consecutive host scenes join, **he stays put** across the cut and only the frame content changes.
  - Pose changes are **hard cuts, never animated**.
- **When he's off:** scenes **without** a `host:` line are shown full-frame as before. Those are mostly pictures that already show the narrator, so he's never on screen twice.
  - Alternate between host stretches and full-frame stretches so the video breathes. Aim for about **50–60% of screen time with the host**, and no host stretch longer than about 40s without a full-frame scene.
- **Pop-up events inside a host scene** don't add a second narrator. Their content (card or icon) is shown in the frame, and his pose switches to the pop's pose for that moment.
- **Triggers:** numbers in host lines (e.g. "seventy") may appear as digits in the transcript ("75%"). Match them either way.

---

## PART 1: The hook and my story (`audio/part1.mp3`)

**R01** · picture S59 (NEW: narrator frozen at the edge of a high diving board) · camera zoom-in
edit: start wide, then snap zoom to his scared face on "trying" · impact hit on "stupid"
narration: "Most people think the choice they'll regret is the risky one. Saying the wrong thing. Trying and failing. Looking stupid in front of everyone."
beats: card "risky" → THE **RISKY** ONE?

**R02** · picture S03 (NEW: researcher sorting notes into a small and a huge pile) · camera zoom-in
host: N02 "but"
narration: "But when researchers actually asked people about their biggest regrets... that's not what they found."
beats: pop N09 "not" → card THAT'S ~~NOT~~ IT

**R03** · picture S02 (NEW: lineup of 4 people) · camera pan-right
edit: tour: full lineup → snap zoom to the student on "college" → whip slide to the office worker on "office" → whip slide to the professor on "retired" → whip slide to the elderly woman on "nursing" → zoom back out to all four on "one" (replaces the crop beat)
host: N06 "they"
narration: "They asked college students. Office workers. Retired professors. People living in nursing homes, looking back on almost their whole lives. One simple question."

**R04** · picture S01 (NEW: researcher interviewing an elderly man) · camera zoom-in
host: N06 "what's" → N02 "and" → N06 "they" (2nd occurrence)
narration: "What's the biggest regret of your life? And most people's biggest regrets... weren't about the things they did. They were about the things they didn't do."
beats: icon I17 "what's" · card "didn't" → WHAT THEY ~~DIDN'T~~ DO

**R05** · picture S04 (NEW: elderly man in a rocking chair with 4 thought bubbles) · camera zoom-in
edit: tour of the thought bubbles: snap zoom to the book bubble on "class" → whip slide to the waving person on "person" → whip to the airplane on "trip" → whip to the guitar on "thing" → zoom back out on "because"
host: N06 "the"
narration: "The class they never took. The person they never talked to. The trip they kept putting off. The thing they always wanted to try... but never did, because it felt too risky, too embarrassing, or like it just wasn't the right time."
beats: crop "trip" → the thought bubbles · card "right" → NOT THE **RIGHT TIME**

**R06** · picture S05 (COPY: narrator close-up, worried) · camera zoom-in
narration: "When I first read that, it hit me pretty hard. Because I had a whole list of those."
beats: pop N10 "whole" → card A WHOLE **LIST**

**R07** · picture S06 (COPY: sign-up sheet, hand pulling away) · camera zoom-in
host: N01 "there"
narration: "There was a tryout I talked myself out of. I had the date written down. I even bought the shoes."
beats: icon I49 "shoes"

**R08** · picture S58 (NEW: narrator on the edge of his bed in the morning, new sneakers by the door) · camera zoom-in
edit: slow push only on "sat" (8% over 2s; the one allowed slow move), then a hard cut to the shoes crop on "next" (1st occurrence)
narration: "And the morning of, I just sat on the edge of my bed... and didn't go. I told myself I wasn't good enough yet. That I'd try next year. Next year, I didn't go either."
beats: icon I13 "year" (1st occurrence) · card "either" → NEXT YEAR: ~~DIDN'T GO~~

**R09** · picture S07 (NEW: narrator in bed at night holding a glowing phone) · camera zoom-in
narration: "There was a message I typed out three times... and deleted three times."
beats: card "deleted" → ~~DELETED~~ 3 TIMES

**R10** · picture S08 (COPY: narrator at a classroom desk, hand half raised) · camera zoom-in
narration: "There was a question I didn't ask in class, and then heard someone else ask five minutes later. And the teacher said, "Great question.""
beats: icon I17 "question" (1st occurrence) · pop N10 "great" → card "GREAT **QUESTION**."

**R11** · picture S09 (NEW: narrator at a closed door with light under it) · camera zoom-in
narration: "Every time, my brain had a really good reason. "You'll look dumb." "It's not worth it." "Maybe next time." And every time, it felt like the safe choice."
overlays (speech bubbles from his head, one by one): YOU'LL LOOK DUMB on "dumb" · NOT WORTH IT on "worth" · MAYBE NEXT TIME on "next"
beats: card "safe" → THE **SAFE** CHOICE

**R12** · picture S10 (NEW: narrator holding a ridiculously long bill) · camera zoom-in
edit: whip slide down the unrolling bill on "bill"
narration: "But here's what the research shows. The safe choice isn't always safe. It just sends you the bill later."
beats: pop N02 "safe" (2nd occurrence) → card ISN'T ALWAYS ~~SAFE~~ · the main picture should be on screen for "bill later"

**R13** · picture S04 · camera zoom-out
host: N01 "by"
narration: "By the end of this video, you'll know exactly what those researchers found, why the things we don't do stay with us so much longer than our mistakes, and the five steps I now use whenever I'm about to talk myself out of something. The first one takes about ten seconds. And it's changed a lot of my decisions."
beats: pop N08 "found" → card WHAT THEY **FOUND** · icon I43 "longer" · pop N07 "five" → card **5** STEPS · icon I11 "ten" · **title card** at the end (2.5s): green pill **LESSON**, big text PSYCHOLOGY OF / REGRET, with "REGRET" in orange

---

## PART 2: The research (`audio/part2.mp3`)

**R14** · picture S12 (COPY: university campus) · camera pan-right
edit: hand-drawn callout circle around the building with the label "Cornell" on "psychologists"
host: N01 "in"
narration: "In the mid nineteen-nineties, two psychologists, Thomas Gilovich and Victoria Medvec, started studying regret."
overlays: label "Cornell University, 1994" on "nineties"
beats: icon I16 "psychologists"

**R15** · picture S13 (COPY: the T-shirt student) · camera zoom-in
host: N05 "if"
narration: "If those names sound familiar, they're two of the same researchers behind the embarrassing T-shirt study from my last video. They spent a lot of their careers figuring out how our brains trick us."
beats: icon I08 "shirt" · pop N05 "trick" → card HOW OUR BRAINS **TRICK US**

**R16** · CODED grid · camera hold
edit: the grid draws in row by row · "60" counts up on "sixty"
host: N06 "first"
60 small person icons (6 rows × 10), all plain, with the label **60** ADULTS.
narration: "First, they kept it simple. They asked sixty adults one question."

**R17** · picture S15 (NEW: a path splitting at a blank two-way signpost) · camera hold
edit: snap zoom to the left sign on "did" (1st occurrence) → whip slide to the right sign on "didn't" → zoom out on "wish" (2nd occurrence)
narration: "When you look back on your life, what do you regret more? The things you did, and wish you hadn't? Or the things you didn't do, and wish you had?"
overlays (text on the two signs; measure the boxes from the picture): THINGS I DID on "did" · THINGS I DIDN'T DO on "didn't"

**R18** · CODED grid (same as R16) · camera hold · **reveal: at least 2s of silence after**
edit: count-up 0 → 75% while the people turn red · impact hit on "seventy"
host: N02 "seventy"
45 of the 60 people turn red, row by row over 0.6s, starting on "seventy-five". Label: ~~75%~~ DIDN'T DO.
narration: "Seventy-five percent said the things they didn't do."

**R19** · picture S02 · camera pan-left
edit: tour: snap zoom to the student on "college" → whip slide to the professor on "professors" → whip slide to the elderly woman on "nursing" → zoom out on "asked"
host: N01 "then"
narration: "Then they went deeper. They interviewed seventy-seven people, from college students, to retired professors, to people in nursing homes, and asked them to list their biggest regrets."
beats: card "seventy-seven" → **77** PEOPLE

**R20** · picture S03 · camera zoom-in
edit: "213" rolls up with the number wheel on "two"
host: N06 "over"
narration: "Over two hundred regrets in total."

**R21** · CODED bars · camera hold
edit: the bars grow with count-ups to 63% and 37%
host: N02 "and"
"DIDN'T ACT" (red, 63%) vs "ACTED" (grey, 37%), growing on "outnumbered".
narration: "And the regrets about not acting outnumbered the regrets about acting... almost two to one."
beats: badge ALMOST **2 TO 1** on "two"

**R22** · CODED card, swapping to card B on "choice" · camera hold
edit: card A: "10" in a marker circle · kinetic word swap to card B on "choice"
host: N06 "and" → N02 "almost"
Card A: ONLY **10 OF 213**, with the small line "were bad luck" under it. Card B: ALMOST ALL: ~~A CHOICE~~.
narration: "And here's a detail I didn't expect. Out of all those regrets, only about ten were about things outside their control. Bad luck. Things that just happened to them. Almost everything else... was a choice. Their own."
beats: pop N09 "detail" → card I DIDN'T **EXPECT THIS**

**R23** · picture S20 (COPY: cafeteria, dropped tray) · camera zoom-in
narration: "But here's where it gets really interesting. They also asked people to think about two different time frames. First: what's your biggest regret from just this past week? For that one, it was basically a coin flip. About half the people picked something they did. A dumb comment. A bad decision. Something they'd messed up."
beats: pop N02 "two" → card **TWO** TIME FRAMES · icon I13 "week" · icon I42 "coin" · card "half" → ABOUT **HALF** · the main picture should be on screen for "a dumb comment…"

**R24** · picture S04 · camera zoom-in
host: N06 "then"
narration: "Then they asked: what's the biggest regret of your whole life?"

**R25** · CODED pie (the existing pie kind) · camera hold · **reveal: at least 2s of silence after**
edit: the pie fills 0 → 84% with a count-up · riser before it, then impact hit on "eighty"
host: N02 "eighty"
Pie at 84%, label "WHOLE LIFE:" with ~~84%~~.
narration: "Eighty-four percent... picked something they didn't do."

**R26** · picture S23 (COPY: bedroom at night, replaying) · camera zoom-in
narration: "So in the short term, our mistakes hurt more. That part is real. If you say something awkward today, you'll probably feel it tonight."
beats: card "short" → SHORT TERM: ~~MISTAKES~~ HURT · icon I14 "tonight"

**R27** · CODED lines ("REGRET OVER TIME") · camera hold · **reveal: at least 2s of silence after**
edit: the lines draw on with a light sweep at the crossing point
host: N02 "but" → N06 "the" (2nd occurrence)
narration: "But over the years, that flips. The mistakes fade. And the missed chances... grow."
beats: the lines draw on "flips" · FADE tag on "fade" · GROW tag on "grow"

**R28** · picture S25 (NEW: two unhappy students on college steps) · camera zoom-in
host: N01 "they"
narration: "They even tested this with a little story. Two college students, both unhappy at their school."

**R29** · picture S26 (NEW: one student leaves with a moving box, the other stays) · camera pan-right
edit: push wipe to the left as the student walks away on "transfers"
host: N01 "one"
narration: "One of them transfers to a new school. The other one stays. And it turns out, both of them made the wrong choice."
beats: card "both" → **BOTH** CHOICES WERE ~~WRONG~~

**R30** · picture S26 · camera zoom-in
edit: hand-drawn arrow plus a "76%" badge to the leaving student · count-up
host: N06 "so"
narration: "So who feels worse? Right after the decision, most people said the one who transferred. Seventy-six percent. He took the risk, and it didn't work out."
overlays: a yellow badge "76%" over the leaving student on "seventy-six"
beats: pop N06 "who" → card WHO FEELS **WORSE?** · crop "transferred" → the leaving student

**R31** · picture S28 (NEW: the student who stayed, years later, alone on the steps) · camera zoom-in · hold 1.5s at the end of the part
edit: light-leak overlay plus a push wipe in on "years" (time jump)
host: N06 "but"
narration: "But years later? Most people said the one who stayed. The one who never found out."
overlays: pill "YEARS LATER" top-center on "years"

---

## PART 3: Why it happens (`audio/part3.mp3`)

**R32** · picture S09 · camera zoom-out
narration: "So why does this happen? Why do the things we don't do follow us around for so much longer? The researchers pointed to a few reasons. And once you see them, it's hard to unsee them."
beats: pop N06 "why" → card **WHY?** · pop N08 "few" → card **4** REASONS

**R33** · picture S30 (NEW: narrator gluing a broken vase) · camera zoom-in
narration: "One. When you make a mistake, you do something about it. You apologize. You fix it. You laugh about it later. Or you find the silver lining. "Well, at least I learned something." Your brain does a lot of quiet repair work on the things you did."
beats: step "one" → REASON 1 + YOU REPAIR MISTAKES · icon I44 "fix" · icon I09 "learned" · crop "repair" → narrator and vase

**R34** · picture = icon I45 (dusty unopened gift box) full-frame · camera zoom-in (slow)
host: N06 "but"
narration: "But there's nothing to repair when nothing happened. So it just... sits there."

**R35** · picture = icon I46 (closed book) full-frame · camera zoom-in
host: N08 "two" → N01 "if"
narration: "Two. A mistake has an ending. A missed chance doesn't. If you try something and it goes badly, you know exactly how bad it was. The story is over."
beats: step "two" → REASON 2 + A MISTAKE HAS AN ENDING · pop N01 "badly" → card THE STORY IS **OVER**

**R36** · picture S33 (NEW: glowing open book with dream scenes rising) · camera zoom-in
edit: snap zoom to the dream scenes on "imagination" → whip slide across them on "maybe" (1st occurrence)
narration: "But if you never try, the story stays open. And your imagination keeps writing new endings. Maybe it would have worked. Maybe it would have changed everything."
beats: crop "changed" → the dream scenes

**R37** · picture S34 (NEW: narrator carrying a giant question-mark load uphill) · camera zoom-in
narration: "You'll never know. And "I'll never know" is a heavy thing to carry."
beats: card "never" (1st occurrence) → YOU'LL ~~NEVER~~ KNOW · the main picture should be on screen for "heavy thing to carry"

**R38** · picture S35 (NEW), swapping to S35b on "small" · camera zoom-in
edit: impact hit on "huge" · the swap to S35b is an iris reveal on "small"
narration: "Three. Over time, you forget why you were scared. In the moment, the fear feels huge. Like the most important thing in the room. But ten years later, you can barely remember it. You remember the reasons you had to go. You just can't remember the reasons you had to stay. And from far away, the thing that stopped you looks... kind of small."
beats: step "three" → REASON 3 + YOU FORGET THE FEAR · card "huge" → THE FEAR FEELS **HUGE** · icon I43 "ten"

**R39** · picture S36 (COPY: empty stage, empty seats) · camera zoom-out
host: N05 "which"
narration: "Which, if you saw my last video, makes a lot of sense. Most of the time, the fear was about people watching... who weren't really watching."
beats: icon I06 "watching" (1st occurrence) · icon I29 "weren't" (with the main picture between the two icons)

**R40** · picture S37 (NEW: narrator awake in bed, thinking of a closed door) · camera zoom-in
edit: snap zoom to the door bubble on "door"
narration: "Four. Unfinished things stay on your mind. Your brain is good at letting go of things that are done. It's much worse at letting go of things that never got finished, or never even got started. So the door you never opened... keeps coming back."
beats: step "four" → REASON 4 + UNFINISHED THINGS STAY · icon I47 "finished" · crop "door" → the thought bubble

**R41** · picture S03 · camera zoom-out
edit: hand-drawn underline under the label on "Davidai"
host: N02 "and" → N01 "gilovich"
narration: "And there's one more study, from two thousand eighteen, that I think is the most important part of all of this. Gilovich and another researcher, Shai Davidai, asked people about their regrets again. But this time, they sorted them differently."
overlays: label "Davidai & Gilovich, 2018" on "Davidai"
beats: pop N02 "important" → card THE **MOST IMPORTANT** PART

**R42** · picture S39 (NEW: narrator in a tie carrying a wobbly stack of boxes) · camera zoom-in
narration: "Were they about who you felt you should be? Your duties. Your responsibilities."
beats: card "should" → WHO YOU **SHOULD** BE

**R43** · picture S40 (NEW: narrator at a mirror; his reflection is his ideal self) · camera zoom-in
edit: snap zoom to the reflection on "become" with a light sweep across the mirror
narration: "Or were they about who you wanted to be? Your dreams. Your goals. The person you hoped you'd become."
beats: crop "become" → the reflection

**R44** · CODED bars · camera hold · **reveal: at least 2s of silence after**
edit: focus rack: WHO I SHOULD BE sharp first, then WHO I WANTED TO BE on "seventy" · count-up to 76% · riser plus impact hit
host: N02 "seventy"
"WHO I WANTED TO BE" (red, 76%) vs "WHO I SHOULD BE" (grey, 24%).
narration: "Seventy-six percent of people said their single biggest regret was about not becoming the person they wanted to be."

**R45** · picture S40 · camera zoom-out
narration: "Think about that. The regrets that last the longest aren't about the times you messed up. They're about the version of you that never got a chance to show up."
beats: pop N02 "version" → card NEVER GOT **A CHANCE**

**R46** · picture S42 (NEW: a kind nurse beside an elderly patient) · camera zoom-in · hold 1.5s at the end of the part
edit: the quote rises word by word (per-word-rise) timed to the voice · marker highlight on "courage" (2nd occurrence)
host: N06 "a" → N02 "notice"
narration: "A nurse named Bronnie Ware spent years caring for people in the last weeks of their lives, and she wrote down what they told her. The regret she heard most often was this: "I wish I'd had the courage to live a life true to myself, not the life others expected of me." Notice what that regret is about. It's not about a mistake. It's about courage."
beats: CODED quote card on "wish", up until "notice" · then the main picture · card "courage" (2nd occurrence) → IT'S ABOUT **COURAGE**

---

## PART 4: The 5 steps and the ending (`audio/part4.mp3`)

**R47** · CODED card · camera hold
host: N01 "so"
HOW I USE **THIS**
narration: "So here's how I actually use this now. Five steps."
beats: pop N08 "five" → card **5** STEPS

**R48** · picture S44 (NEW: old narrator in a rocking chair), swapping to S44b on "annoyed" · camera zoom-in
edit: snap zoom to old-me's face on "obvious" · the swap to S44b is a hard cut with a pop on "annoyed"
narration: "One. The rocking chair test. When I'm about to talk myself out of something, I picture myself old, sitting in a rocking chair, looking back on my life. And I ask: will that version of me care that this was awkward? Or will he care that I never tried? Almost every time, the answer is obvious. Old me does not care about the awkward part. Old me is annoyed that I didn't go."
beats: step "one" → STEP 1 + THE ROCKING CHAIR TEST · icon I40 "rocking" (1st occurrence) · pop N06 "awkward" (1st occurrence) → card **AWKWARD?** · card "never" → OR ~~NEVER TRIED?~~ · crop "obvious" → old narrator's face

**R49** · CODED lines (same chart as R27) · camera hold
host: N07 "two" → N02 "if" (2nd occurrence)
narration: "Two. Remember which regret fades. If you try and it goes badly, it'll sting for a few days. Maybe a few weeks. Then it fades, and your brain turns it into a lesson, or a funny story. If you don't try, that one doesn't fade. It grows."
beats: step "two" → STEP 2 + REMEMBER WHICH ONE FADES · icon I44 "sting" · icon I48 "grows" (cut back to the chart between the icons)

**R50** · CODED split · camera hold · **reveal: at least 2s of silence after**
edit: focus rack between A SHORT STING and A LONG WHAT IF
host: N01 "so"
Left: A SHORT **STING** (on "short"). Right: A LONG ~~WHAT IF~~ (on "long").
narration: "So you're not choosing between pain and no pain. You're choosing between a short sting... and a long "what if.""

**R51** · picture S47 (NEW: narrator facing a giant mountain, one small step at his feet), swapping to S47b (NEW: the door from S09, now slightly open) on "open" · camera zoom-in
edit: whip slide up the mountain on "too big" · iris reveal from the door gap into S47b on "open"
narration: "Three. Make it smaller. A lot of the time, we don't act because the thing feels too big. So shrink it. Don't plan to become a runner. Go for one run. Don't write the perfect message. Send a simple one. You don't have to change your whole life today. You just have to open the door a little."
beats: step "three" → STEP 3 + MAKE IT SMALLER · icon I49 "run" · icon I41 "message" · card "change" → NOT YOUR **WHOLE LIFE**

**R52** · picture S40 · camera zoom-out
narration: "Four. Ask yourself: is this a should, or a want? Remember that last study. The regrets that hit hardest aren't about what you were supposed to do. They're about who you wanted to be. So if something keeps pulling at you, the guitar, the business idea, the person you want to talk to... that pull is worth listening to."
beats: step "four" → STEP 4 + A SHOULD, OR A WANT? · CODED icon row (I50 on "guitar", I09 on "business", I26 on "person") · pop N02 "pull" → card WORTH **LISTENING TO**

**R53** · picture S35 (the big fear, not S35b) · camera zoom-in
narration: "Five. Decide before the fear shows up. Fear is loudest in the moment. So make the decision earlier, when you're calm. Sign up tonight. Put it on the calendar. Tell a friend you're doing it. Then when the nerves show up later, the hard part is already done."
beats: step "five" → STEP 5 + DECIDE BEFORE THE FEAR · icon I30 "sign" · icon I13 "calendar" · pop N07 "hard" → card HARD PART: **DONE**

**R54** · picture S50 (COPY: narrator on a curb at dusk) · camera zoom-in
edit: hand-drawn underline on JUST FUNNY NOW
narration: "Here's the thing I keep coming back to. Every mistake I've ever made, I can tell you exactly what happened. The story's over. Most of them are just funny now."
beats: icon I46 "story's" · pop N05 "funny" → card JUST **FUNNY** NOW

**R55** · picture S37 · camera zoom-in
narration: "But the things I didn't do? I still wonder about those."

**R56** · picture S10 (the long bill: a callback to "sends you the bill later") · camera zoom-out
edit: whip slide down the long bill on "charging"
narration: "And if you've got a list like mine, that doesn't mean you're a coward. It means your brain was doing exactly what it was built to do. Protecting you from a little bit of pain today... by charging you a lot more later. You can stop paying that."
beats: pop N01 "built" → card BUILT TO **PROTECT YOU** · card "stop" → YOU CAN **STOP PAYING**

**R57** · picture S04 · camera zoom-out
host: N01 "so"
narration: "So the next time your brain says, "It's safer not to"... remember what all those people said, looking back on their whole lives."
beats: card "safer" → "IT'S ~~SAFER~~ NOT TO"

**R58** · CODED card, swapping to card B on "tried" · camera hold · **reveal: at least 2s of silence after**
edit: kinetic word swap: PLAYED IT SAFE → TRIED on "tried" · light sweep across TRIED
host: N01 "they" → N06 "they" (2nd occurrence)
Card A: THEY DIDN'T WISH THEY'D ~~PLAYED IT SAFE~~. Card B: THEY WISHED THEY'D **TRIED**.
narration: "They didn't wish they'd played it safer. They wished they'd tried."

**R59** · picture S54 (COPY: narrator walking confidently through a doorway) · camera zoom-in
narration: "So go try. Send the message. Sign up."
beats: icon I41 "message"

**R60** · picture S55 (COPY: narrator with his hand fully raised, happy) · camera zoom-in
narration: "Ask the question."

**R61** · picture S56 (COPY: hilltop sunrise) · camera zoom-out · **at least 2s of silence after "wonder"**
edit: iris reveal into the sunrise on "best"
narration: "Worst case, you get a funny story. Best case... you never have to wonder."
beats: pop N05 "worst" → card WORST CASE: **A FUNNY STORY** · the main picture should be on screen from "best case" on

**R62** · picture S57 (COPY: narrator on the right, pointing left; end screen) · camera hold · hold the last frame 5s after the narration
narration: "Which of the five steps do you need most? Tell me the number in the comments. And if the thing stopping you is that feeling that everyone's watching, my last video breaks down exactly why that's not true. I'll leave it right here."
beats: pop N08 "number" → card WHICH **NUMBER?** (finish it before "and if" so the end screen stays clean)

---

## New diagram kinds to add to `tools/build-part.mjs`

Use the same look as the existing pie and scale: cream background, 9px ink outlines, Nunito ExtraBold, and yellow or red outlined badges. Every animation must be seek-safe on the GSAP timeline.

- **grid:** 60 simple person icons (round head plus rounded body, ink outline, white fill) in 6 rows × 10. Options: `fill` (how many turn red), `word` (when they turn, row by row over 0.6s), `label` (badge text under the grid). Used in R16 and R18.
- **bars:** two vertical bars side by side, labels under them, and percentages in badges on top. They grow from 0 over 0.6s (`power2.out`) on `word`. The first bar is red and the second is Shadow grey `#E6E1D6`. Used in R21 and R44.
- **lines:** a chart titled "REGRET OVER TIME" with an x-axis from TODAY to YEARS LATER and no y numbers. Line A, "THINGS I DID" (terracotta), starts high and falls. Line B, "THINGS I DIDN'T DO" (red), starts low, rises and crosses A at about 40%. Draw both lines with a stroke-dashoffset tween over 1.5s on `word`. FADE and GROW tags pop next to the line ends on their words. Used in R27 and R49.
- **split:** two halves with a thin vertical ink divider. Each side holds a short line of badge text and appears on its own word. Used in R50.
- **quote:** a large opening quote mark in soft orange, then the quote in sentence case at about 64px, centered and max 1500px wide, with "courage" and "true to myself" in yellow badges. It may stay on screen up to **7s** (the one exception to the 4s rule). Small text under it: "Bronnie Ware, palliative care nurse". Used in R46.
- **iconRow:** three icons from `icons/` in a row on cream, each popping in (0.2s, 0.92 → 1.0) on its own word. It counts as one shot. Used in R52.
- **card → card swap:** like `diagramB` for the pie, a hard cut to card B on the trigger word. Used in R22 and R58.
- **Icon as main picture (R34, R35):** prepare it like a picture (scale the 16:9 icon to 1920×1080 with lanczos).

### Description sources (for Luke, not on screen)
- Gilovich & Medvec (1994), "The temporal pattern to the experience of regret," *JPSP*
- Gilovich & Medvec (1995), "The experience of regret: What, when, and why," *Psychological Review*
- Davidai & Gilovich (2018), "The ideal road not taken," *Emotion*
- Bronnie Ware (2011), *The Top Five Regrets of the Dying*
