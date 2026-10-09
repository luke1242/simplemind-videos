# SimpleMindMotivation: Video Build Guide

You are building a faceless stickman video for the YouTube channel **SimpleMindMotivation** using **HyperFrames** (HTML/SVG → MP4). Follow this guide exactly. It has two halves:

- **Part A: Channel rules.** These apply to every video: look, characters, motion, workflow, usage limits.
- **Part B: This video.** The 4-part scene list for *"One of the Most Useful Lessons I Learned."*

The owner is Luke. He is not a developer, so keep messages to him short and plain.

---

# PART A: CHANNEL RULES

## A1. Golden rules

1. **Characters are built ONCE and never redrawn.** Every scene uses the same master character SVGs. Poses come only from rotating named limb groups. Never draw a "new version" of a character for a scene.
2. **One motion per scene**, plus an optional slow camera zoom. Nothing else moves.
3. **Data-driven, not hand-written.** Scenes live in `scenes/partN.json`. One generator script turns any part's JSON into a HyperFrames composition. Do not hand-write HTML per scene.
4. **Build one part per session.** Render it, report back, stop. Don't start the next part unless Luke asks.
5. **Check before rendering.** Run `npx hyperframes lint` and `npx hyperframes check`, and snapshot 3 to 4 frames. Do a full render only once those look right. Don't re-render whole parts to fix one scene.
6. **Save usage.** Don't load skills or docs you don't need, don't paste huge files back into chat, and reuse assets instead of creating new ones.

## A2. Repo layout

```
CLAUDE.md                     ← this guide
audio/part1.mp3 … part4.mp3   ← Luke provides (ElevenLabs voiceover)
music/                        ← optional background track (Luke provides)
assets/
  characters/brain.svg        ← master narrator (built once)
  characters/person.svg       ← master side character (built once)
  characters/poses.json       ← pose table (limb rotations)
  backgrounds/*.svg           ← one file per setting, reused
  props/*.svg                 ← small reusable props
  fonts/                      ← installed from npm (@fontsource)
  vendor/gsap.min.js          ← vendored (CDN is blocked)
scenes/part1.json … part4.json
tools/build-part.mjs          ← generator: scenes JSON → HyperFrames project
tools/timing.mjs              ← computes scene start/end from audio
parts/part1/ … part4/         ← generated HyperFrames projects
renders/part1.mp4 … part4.mp4, full.mp4
review/character-sheet.png    ← character approval image
```

## A3. Environment setup (cloud session)

Do this once per session, quietly:

- Install the HyperFrames skills with `npx hyperframes skills update` (run from the repo root, never inside a HyperFrames checkout). Read `/hyperframes-core` only when you need composition details.
- **Chrome:** Google's Chrome download is blocked. Use the preinstalled Chromium: `export HYPERFRAMES_BROWSER_PATH=$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome | head -1)`, then confirm with `npx hyperframes doctor`.
- **GSAP:** the jsDelivr CDN is blocked. `npm pack gsap@3.14.2`, extract it, and copy `dist/gsap.min.js` to `assets/vendor/`. Point every composition at that local file. Never reference a CDN URL.
- **Fonts:** `npm i @fontsource/montserrat @fontsource/bebas-neue` and load them locally. No Google Fonts URLs.
- **Audio length:** `ffprobe` is available. If `audio/partN.mp3` is missing, stop and tell Luke which file to add.

## A4. Visual style

Hand-drawn 2D doodle look: simple, clean, warm. Think "children's-book doodle," but for adults.

- **Canvas:** 1920×1080, 30 fps, MP4 (H.264 + AAC).
- **Line work:** ink color `#1A1A1A`, round caps and joins. Character outlines are 5px, limbs 7px, props and backgrounds 4px. For a subtle hand-drawn wobble, use one shared SVG filter (`feTurbulence` baseFrequency 0.02, numOctaves 2, **fixed seed 7**, then `feDisplacementMap` scale 1.5). It must be static: never animate the seed, because "line boil" looks sloppy.
- **Fills:** flat colors only. No gradients, no shadows, no 3D, no textures.
- **Palette** (use only these):

| Name | Hex | Use |
|---|---|---|
| Paper | `#F5EFE3` | default background |
| Tan | `#D9B382` | ground, floors, desks |
| Terracotta | `#C9785D` | skies, accents |
| Sage | `#8FA98A` | hills, trees, plants |
| Soft orange | `#F2A65A` | glow, highlights, spotlight, lightbulb |
| Charcoal | `#2B2B2B` | hoodie shadow areas, dark props |
| Hoodie grey | `#4A4A4A` | Brain's hoodie |
| Brain pink | `#F4A6B8` | Brain's head |
| Brain fold | `#D9788F` | fold lines on the brain |
| Night blue | `#2E3A52` | night scenes |
| Stage dark | `#141414` | dark stage / theater |
| White | `#FFFFFF` | heads of side characters, sneakers |
| Stripe red | `#D64545` | sneaker stripe, "X" marks |

- **Composition:** one idea per frame and lots of empty space. Characters stand on a ground line at y ≈ 860. The main character is roughly 420px tall, kept in the center 60% of the frame.
- **Backgrounds** are a few flat shapes: a horizon line, a wall, a door, a desk. Never busy.
- **Text overlays** (titles, numbers, labels): Montserrat ExtraBold or Bebas Neue, ink color or white on dark, with a soft orange accent for key numbers. Max 5 words on screen at once.

## A5. The narrator: "Brain" (consistency lock)

Build `assets/characters/brain.svg` **once**, render the character sheet (A9), get Luke's approval, then **never change its shapes again**. Every scene imports this file.

**Exact spec** (standing height 420px; origin at the feet center):

- **Head:** a cartoon brain silhouette, two rounded lobes with a soft center dip on top and a flat-ish bottom. 150px wide × 115px tall. Fill `#F4A6B8`, outline `#1A1A1A` 5px. Inside are exactly **4 fold lines** (stroke `#D9788F`, 4px, round caps): one gentle center line plus three short S-curves. The same 4 lines appear in every frame.
- **Eyes:** two filled black circles, r = 7px, 36px apart, centered horizontally, 52px from the bottom of the head. Group them as `#eyes` so blinks scale them.
- **Brows** (`#brows`): two short 4px strokes above the eyes. Their angle changes per expression (A7).
- **Mouth** (`#mouth`): one 4px stroke path, swapped only from the expression table in A7.
- **Neck:** none. The head sits directly on the hoodie.
- **Torso / hoodie** (`#torso`): a rounded-rectangle hoodie, 110px wide × 150px tall, fill `#4A4A4A`, 5px ink outline, with a small hood-fold arc at the collar and a kangaroo-pocket line. The hood is down.
- **Arms** (`#armL`, `#armR`): each has an upper and a lower segment (`#armL-upper`, `#armL-lower`, …), 7px ink strokes, with hoodie-sleeve fill on the upper arm only. Hands are small ink circles, r = 7. **Pivot** is at the shoulder, with an elbow pivot for the lower segment.
- **Legs** (`#legL`, `#legR`): 7px ink strokes, each with an upper and a lower segment. The pivot is at the hip, with a knee pivot.
- **Sneakers:** white rounded shoes, 5px ink outline, with one thin `#D64545` stripe on each. They are attached to the lower legs.

**Rules:**
- Proportions, colors and line widths never change. The only things that change between scenes are limb rotations (from `poses.json`), the expression (brows + mouth), position, scale, and flip (`scaleX(-1)` to face left).
- Brain must never be drawn without his hoodie or sneakers, never in another color, and never with a round head.
- **Scale:** standard 1.0 (420px tall). Close-ups scale the whole group up to at most 2.2 and crop. Never redraw a "close-up version."

## A6. Side characters: "Person" (consistency lock)

`assets/characters/person.svg` uses the **same skeleton and group names** as Brain, so the same `poses.json` works for both.

- **Head:** a plain white circle, r = 55, 5px ink outline, same eyes, brows and mouth system as Brain.
- **Clothes:** a simple flat shirt over the torso, the same shape as the hoodie but without a hood fold. The color comes from a `variant` field: `sage`, `terracotta`, `tan` or `charcoal`. Pants are ink-colored lines (the legs themselves), with simple white shoes and **no red stripe**.
- Only Brain has a brain head. Side characters never do.
- In crowd shots, use ≤ 8 people, mostly static, at scales 0.6 to 0.8, with mixed variants.

## A7. Pose and expression library

Put these in `assets/characters/poses.json` as rotation values in degrees per joint. Build all of them once and verify them on the character sheet.

**Poses:** `stand`, `stand-grip-strap`, `walk-a`, `walk-b` (the two walk frames that alternate), `point-right`, `point-left`, `think` (hand to chin), `shrug`, `facepalm`, `sit-chair`, `sit-bench`, `sit-curb`, `lie-bed`, `raise-hand-half`, `raise-hand-full`, `thumbs-up`, `hold-front` (both hands forward to hold a prop), `hold-up` (one hand holding a prop high), `curl-down`, `curl-up` (dumbbell), `kneel`, `arms-relaxed`, `roll-sleeves` (hands at the opposite forearms), `stumble` (leaning forward, one arm out).

**Expressions** (brows + mouth only): `neutral`, `smile`, `big-smile`, `worried` (brows angled up in the middle, small flat mouth), `surprised` (brows raised high, small "o" mouth), `cringe` (brows down, wavy mouth), `relieved` (soft smile, relaxed brows), `laugh` (open D-shaped mouth), `wink` (one eye becomes a curved line plus a smile), `thinking` (one brow raised, small side mouth).

**Props** (`assets/props/`, built once): backpack strap, goofy T-shirt (on a hanger and as a worn overlay), clipboard, whiteboard, lightbulb (soft-orange glow), thought bubble, speech bubble, question mark, dumbbell, lunch tray + spilled food, balance scale, magnifying glass, giant scissors, blank sign, sign-up sheet, desk lamp, spotlight cone, bed, park bench, school desk, chair, movie screen, restaurant table, locker row, gym mirror.

## A8. Motion rules (keeps it clean, not sloppy)

**Allowed motions.** Use exactly one per scene; `zoom` can combine with one other.

| Motion | Spec |
|---|---|
| `zoom-in` / `zoom-out` | whole-scene scale 1.00 ↔ 1.06 across the full scene, `sine.inOut` |
| `pan-left` / `pan-right` | background x shift ≤ 80px across the scene, `sine.inOut` |
| `pop-in` | element scale 0 → 1, 0.35s, `back.out(1.6)` |
| `fade-in` | opacity 0 → 1, 0.4s |
| `blink` | `#eyes` scaleY 1 → 0.1 → 1 over 0.16s |
| `nod` | head group rotate 0 → 6° → 0, 0.5s |
| `shrug` | pose `stand` → `shrug` → `stand`, 0.6s, `power2.inOut` |
| `pose-to` | tween limb rotations to a target pose, 0.5 to 0.7s, `power2.inOut` |
| `walk` | translate x at a steady speed while alternating `walk-a`/`walk-b` every 0.3s (with a tiny 0.08s crossfade between frames) |
| `tremble` | x ± 2px, yoyo every 0.06s (nervous only) |
| `sweat-drop` | a small drop slides 20px down and fades, 0.8s |
| `spotlight-on` | the cone fades in 0.2s with one brief 0.1s flicker |
| `shrink` | element scale 1 → 0.25, 0.8s, `power2.inOut` |
| `scale-tip` | the scale beam rotates 0 → 14°, 0.8s |

**Banned:** idle breathing or wobble, bouncing for no reason, camera shake, spinning, fast whip moves, limbs bending past natural angles, morphing shapes, more than one character moving at the same time (unless the scene says so), and animated line boil.

**Joint limits** (enforce them in `build-part.mjs`): shoulders −170° to 170°, elbows 0 to 150° (one direction only), hips −60° to 80°, knees 0 to 120° (one direction only). Clamp any pose value outside these.

**Timing:** each motion starts 0.3s after the scene begins. Leave the character still for the rest of the scene. Stillness looks clean.

**Scene transitions:** a straight cut by default. Use a 0.4s crossfade only where a scene says `transition: fade`.

## A9. Character sheet approval (first session only)

Before building any scene:

1. Build `brain.svg`, `person.svg` and `poses.json`.
2. Render `review/character-sheet.png` (1920×1080, Paper background): Brain in `stand`, `point-right`, `think`, `shrug`, `walk-a`, `sit-bench`, `raise-hand-full` and `thumbs-up`, then a row of 4 expressions, then one Person in each of the 4 color variants.
3. Show it to Luke and **stop**. Continue only once he approves. After approval, the character files are frozen. Changing them needs Luke's explicit OK.

## A10. Timing: syncing scenes to the voiceover

Each part has one audio file. Scenes must line up with what's being said.

1. Get the total duration with `ffprobe`.
2. Find the pauses: `ffmpeg -i audio/partN.mp3 -af silencedetect=noise=-35dB:d=0.35 -f null -` gives the silence gaps (ElevenLabs puts a pause at each "..." line).
3. **First estimate:** give each scene a share of the audio proportional to its narration word count.
4. **Snap:** move each scene boundary to the nearest silence midpoint, within ±1.5s. If no silence is that close, keep the estimate.
5. Save the result to `scenes/partN.timing.json` and print a short table (scene, start, end) for Luke.
6. If Luke says a scene is off, he'll give the correct time. Edit only that boundary.

## A11. Build loop for one part

1. Check that `audio/partN.mp3` exists. Run the timing step (A10).
2. Write or update `scenes/partN.json` from Part B (only once per part).
3. `node tools/build-part.mjs N` generates `parts/partN/`, with one sub-composition per scene, the audio track and the overlays. Reuse means reusing the same background and character files, not copying new drawings.
4. Run `npx hyperframes lint` and `npx hyperframes check`, and fix any errors.
5. Snapshot 4 frames: the first scene, a middle scene, a scene with overlay text, and the last scene. Look at them for character consistency and clipping.
6. `npx hyperframes render` to `renders/partN.mp4`.
7. Tell Luke in 2 to 3 lines: it's done, the file path, the runtime, and anything you weren't sure about. **Stop.**

**Optional final step** (only when Luke asks): join the parts with `ffmpeg` concat into `renders/full.mp4`, adding 1.0s of silence and a hold on the last frame between parts. If `music/track.mp3` exists, mix it under the voice at about −20 dB with a 2s fade in and a 3s fade out.

## A12. Self-check before every render

- [ ] Brain looks identical in every scene: same head shape, 4 fold lines, hoodie, red-stripe sneakers.
- [ ] Side characters all have round white heads, and none has a brain head.
- [ ] Only palette colors are used.
- [ ] Each scene has one motion (plus an optional zoom) that starts at +0.3s, and is still otherwise.
- [ ] No limb exceeds the joint limits, and nothing goes off-frame unless intended.
- [ ] Overlay text is spelled exactly as written in Part B, with ≤ 5 words.
- [ ] Audio is present and the video length equals the audio length.

---

# PART B: THIS VIDEO

**Title:** One of the Most Useful Lessons I Learned
**Topic:** the spotlight effect (people notice and judge us far less than we think)
**Target length:** about 9 to 10 minutes total across 4 parts
**Audio files:** `audio/part1.mp3`, `audio/part2.mp3`, `audio/part3.mp3`, `audio/part4.mp3`

### Backgrounds needed (build once each, in `assets/backgrounds/`)

| ID | Description |
|---|---|
| `gym-door` | Paper bg; a tan floor line; a simple open doorway frame on the left; inside, faint outlines of a bench and dumbbell rack |
| `gym-inside` | Tan floor, a sage wall stripe, a dumbbell rack, a mirror rectangle on the right |
| `stage-dark` | Full Stage dark; a wooden stage edge (tan) at the bottom; the crowd area is rows of small white dot-pairs (eyes), static |
| `stage-empty` | Same stage, lit softly; rows of simple empty seat outlines instead of eyes |
| `hallway` | Paper bg, a row of sage lockers, a tan floor line |
| `bedroom-night` | Night blue room, a window with a moon, the bed prop |
| `whiteboard-room` | Paper bg, a large blank whiteboard prop center-right |
| `university` | Terracotta sky, a sage hill, a simple building with columns on top |
| `classroom` | Paper bg, a tan floor, a row of desks, a doorway on the left |
| `restaurant` | Paper bg, a table with two plates, a hanging lamp |
| `theater` | Stage dark, a big glowing screen (Paper colored) in the top center, rows of seat backs |
| `cafeteria` | Paper bg, long tan tables, a tray-return window |
| `park` | Paper bg, a sage tree on the left, a park bench center, grass tufts |
| `curb-dusk` | Soft orange → terracotta sky as **two flat bands** (no gradient), a sidewalk curb, a streetlamp |
| `hill-sunrise` | Terracotta sky, a soft orange half-circle sun, a sage hill |
| `plain` | Paper bg only |

### Scene format

Each scene below becomes one entry in `scenes/partN.json`:
`id`, `bg`, `characters` (who, pose, expression, x position as % of width, scale, facing), `props`, `motion`, `overlay` (exact text or graphic), `transition`, `narration` (used for timing only and never shown on screen).

`REUSE Sxx` means: use the same bg, characters and props as scene xx, with only the listed motion changed. Generate nothing new.

---

## PART 1: Hook and the spotlight effect (`audio/part1.mp3`)

**S01**: bg `gym-door` · Brain `stand-grip-strap`, `worried`, x 35%, facing right toward the door · motion `zoom-in`
narration: "For a long time, there was one thought that stopped me from doing almost everything. Going to the gym. Raising my hand in class. Trying out for something. Posting anything online."

**S02**: bg `plain` · Brain close-up (head and shoulders, scale 2.0, centered), `worried` · motion `sweat-drop`
narration: "Everyone's going to be watching."

**S03**: bg `stage-dark` · Brain `stand`, `worried`, x 50%, scale 0.7 · props: spotlight cone on Brain · motion `spotlight-on` · transition `fade`
narration: "That's what it felt like. Every single time. Like I was standing alone on a giant stage, with one bright spotlight on me, and thousands of eyes in the dark."

**S04**: bg `stage-dark` · no characters · props: goofy T-shirt on a hanger, center, in the spotlight cone · motion `pop-in` (shirt)
narration: "Then I learned about one experiment, involving a really embarrassing T-shirt."

**S05**: bg `plain` · Brain `think`, `thinking`, x 50% · props: lightbulb above his head · motion `pop-in` (lightbulb) · overlay (after the narration ends, a 2.5s title card on Stage dark): **ONE OF THE MOST USEFUL LESSONS I LEARNED** (two lines, white, the word "USEFUL" in soft orange)
narration: "And it changed how I see almost everything. By the end of this video, you'll know exactly how wrong our brains are about this, by how much, and the one question I now ask myself that shuts that thought down in about three seconds."

**S06**: bg `hallway` · Brain `walk`, `neutral`, from x 15% → 60%, facing right · props: a small soft-orange spotlight circle on the floor under Brain that moves with him · motion `walk`
narration: "So here's how it used to go for me. I'd walk into a room, and I'd feel like there was a spotlight following me."

**S07**: bg `hallway` · Brain `stumble`, `cringe`, x 50% · 3 Persons `stand`, `neutral`, at x 20%, 75% and 88%, scale 0.8, each with a small thought bubble (bubbles hold one tiny icon each: a laughing face, an "!" and a "?") · motion `pop-in` (bubbles, staggered 0.4s)
narration: "If I tripped, everyone saw it. If my outfit was a little off, everyone noticed. If I said something dumb, I was sure everyone would remember it for weeks."

**S08**: bg `bedroom-night` · Brain `lie-bed`, `worried` · props: a thought bubble above showing a tiny Brain in the `stumble` pose · motion `zoom-in`
narration: "And then I'd replay it in my head that night. Over and over. Like a highlight reel of every awkward thing I'd ever done."

**S09**: REUSE S08 · motion `blink`, then the expression changes to `relieved` at the line "You're not weird"
narration: "If you've ever done that, lying in bed at night, thinking about something awkward from three years ago. You're not weird. You're not broken."

**S10**: bg `whiteboard-room` · Brain `point-right`, `smile`, x 30%, pointing at the whiteboard · overlay written on the whiteboard: **THE SPOTLIGHT EFFECT** · motion `fade-in` (overlay text)
narration: "Your brain is doing something almost everyone's brain does. And it even has a name. Psychologists call it the spotlight effect. It's the feeling that people are noticing you, and judging you, way more than they actually are. And once you understand how strong it is, it's hard to see things the same way again."

---

## PART 2: The T-shirt study (`audio/part2.mp3`)

**S11**: bg `university` · no characters · motion `pan-right` · overlay (bottom-left, small): **Cornell University, ~2000**
narration: "So here's the experiment. Around the year two thousand, a psychologist named Thomas Gilovich and his team at Cornell University ran a study with college students."

**S12**: bg `plain` · Person (variant `tan`) wearing the goofy T-shirt overlay, `cringe`, x 50% · motion `shrug`
narration: "They had one student put on a T-shirt with a big, cheesy picture of a singer on it. One that college students at the time would find really embarrassing to be seen in."

**S13**: bg `classroom` · Person in the T-shirt, `cringe`, at the doorway (x 12%) · 5 Persons `sit-chair` at desks, `neutral`, scale 0.7 · motion `walk` (the T-shirt Person takes about 2 steps in, to x 22%)
narration: "Then that student walked into a room full of other students, stayed for a moment, and walked back out."

**S14**: bg `plain` · Person in the T-shirt `stand`, `worried`, x 60% · researcher Person (variant `charcoal`) `hold-front` with a clipboard, x 35% · props: a speech bubble from the researcher with a "?" · motion `pop-in` (the "?")
narration: "Afterward, the researchers asked the student in the T-shirt one simple question. How many people in that room do you think noticed your shirt?"

**S15**: bg `plain` · Person in the T-shirt `think`, `thinking`, x 35% · overlay: a simple pie chart at x 70% (ink outline, soft-orange fill) that fills to **50%** with the label **"THEIR GUESS: 50%"** · motion `pop-in` (chart), with the fill animating 0 → 50% over 0.8s
narration: "On average, they guessed about half."

**S16**: REUSE S15 · motion: the pie fill animates 50% → **25%** over 0.8s, starting at the word "quarter"; the label changes to **"REALITY: 25%"**; the Person's expression switches to `surprised` · hold 2s after the line
narration: "The real number? Only about a quarter."

**S17**: bg `plain` · Person in the T-shirt `shrug`, `relieved`, x 50% · motion `shrug`
narration: "They thought twice as many people noticed as actually did. And remember, that was a shirt picked specifically to be embarrassing. Something designed to get noticed."

**S18**: bg `restaurant` · Brain `sit-chair`, `cringe`, at the table x 40% · waiter Person (variant `charcoal`) walking away at x 75%, facing right · motion `pose-to` (Brain → `facepalm`)
narration: "Now think about the little things you worry about every day. A bad hair day. A pimple. Saying you too when the waiter says enjoy your meal."

**S19**: REUSE S17 · motion `zoom-out`
narration: "If people barely noticed a ridiculous T-shirt, they're definitely not tracking those."

**S20**: bg `theater` · Brain `sit-chair` from behind (flip, small, scale 0.6), center bottom · the movie screen shows a big Brain head close-up, `smile` · motion `zoom-in`
narration: "So why does this happen? It's actually pretty simple. You are the main character of your own life. You see everything from inside your own head, so you're thinking about yourself all day long. And your brain quietly assumes everyone else is thinking about you too."

**S21**: bg `hallway` · 6 Persons (mixed variants), scale 0.7, spread across the frame, each `stand` with a `worried` look, slightly downward (head tilt), each with their own small spotlight cone · Brain `stand`, `surprised`, center · motion: the spotlights switch on one at a time (staggered 0.25s, using `spotlight-on`)
narration: "But here's the thing. Everyone else is the main character of their own life too."

**S22**: bg `gym-inside` · Person (variant `sage`) `curl-up`, `thinking`, looking into the mirror, x 70% · Brain `stand`, `neutral`, background x 25%, scale 0.7 · motion `pose-to` (`curl-down` → `curl-up`, once)
narration: "That guy you think is judging your workout? He's worried about his own form."

**S23**: bg `hallway` · Person (variant `terracotta`) `walk`, `cringe`, x 30% → 55% · props: a thought bubble showing a tiny Person waving awkwardly · motion `walk` (the thought bubble pops in at +1.0s; this is allowed as the second element)
narration: "That girl you think noticed you stumble over your words? She's busy replaying something she said."

**S24**: REUSE S21 (all spotlights on) · motion `zoom-out`
narration: "Everyone is walking around in their own little spotlight, so busy worrying about it that they barely notice yours."

**S25**: bg `classroom` · Brain at the front, `stand`, `worried`, x 50% · motion `tremble` (whole Brain group) + `sweat-drop`
narration: "And it's not just about how you look. Gilovich and his team found something similar with nerves. When people gave a speech, they thought their nervousness was way more obvious than it really was. The audience mostly couldn't tell."

**S26**: bg `classroom` · Brain `stand`, `neutral`, x 50% (perfectly still) · 4 Persons in the foreground `sit-chair`, seen from behind (flipped), scale 0.8 · overlay (small, above Brain): **"SEEMS FINE"** · motion `zoom-in`
narration: "They called it the illusion of transparency. It's that feeling that everyone can see right through you. They can't. The shaking you feel on the inside? From the outside, it mostly just looks like a normal person talking."

---

## PART 3: People are kinder than you think (`audio/part3.mp3`)

**S27**: bg `cafeteria` · Brain `stand`, `surprised`, x 50% · props: a lunch tray + spilled food on the floor at his feet · motion `zoom-in`
narration: "Okay. But what about when people do notice? What if you really do mess up, and someone sees it?"

**S28**: bg `plain` · Brain `point-right`, `thinking`, x 25% · props: a balance scale at x 62% · overlay: the left pan is labeled **EXPECTED** and the right pan **REALITY** · motion `scale-tip` (the EXPECTED side drops)
narration: "This is where it gets even better. Researchers tested this too. They had people imagine, or actually go through, embarrassing moments, like messing up in front of others. Then they compared how harshly people thought they'd be judged, with how harshly they actually were judged."

**S29**: REUSE S28 (tipped) · motion `zoom-in` toward the REALITY pan
narration: "Over and over, people expected to be judged way more harshly than they really were."

**S30**: bg `cafeteria` · Brain `kneel`, `relieved`, x 45% · Person (variant `sage`) `kneel`, `smile`, x 58%, holding the tray (`hold-front`) · 2 Persons in the background `stand`, `smile`, scale 0.7 · props: the tray · motion `pose-to` (the helper extends the tray toward Brain)
narration: "Because when other people see you mess up, they don't just see the mistake. They see the whole situation. They know you were nervous. They know it was a hard moment. They've been there too."

**S31**: bg `plain` · Brain `hold-up` with the magnifying glass in front of his own face, `cringe`, x 30% · 3 Persons far away on the right (scale 0.45), `smile` · motion `pose-to` (Brain lowers the glass → `hold-front`, expression → `relieved`)
narration: "You're judging yourself with a magnifying glass. They're looking at you from across the room, with a lot more kindness than you'd expect."

**S32**: bg `park` · Brain `sit-bench`, `smile`, x 42% · Person (variant `terracotta`) `sit-bench`, `smile`, x 58%, facing Brain · motion `nod` (Brain only)
narration: "And here's one that honestly surprised me. It's called the liking gap."

**S33**: bg `park` · the same two on the bench · researcher Person (variant `charcoal`) `hold-front` with a clipboard, standing at x 80% · motion `pose-to` (the researcher raises the clipboard slightly, as if writing)
narration: "Researchers paired up strangers and had them talk for a few minutes. Afterward, they asked each person two things. How much did you like the other person? And how much do you think they liked you?"

**S34**: bg `park` (no bench people) · Brain `walk`, `worried`, facing left, at x 35% · Person `walk`, `smile`, facing right, at x 65% · props: Brain's thought bubble has a small ink storm cloud, the Person's has a smiley face · motion `pop-in` (both bubbles at the same time; the characters are frozen mid-stride on `walk-a`, so there's no walking motion)
narration: "People consistently underestimated how much the other person liked them. You walk away from a conversation thinking, that was so awkward, they probably think I'm weird. And the other person walks away thinking, that was nice. I liked them."

**S35**: bg `classroom` · Brain `sit-chair` at a desk, `worried`, x 50% · motion `pose-to` (→ `raise-hand-half`)
narration: "And there's one more. Researchers call it the beautiful mess effect."

**S36**: bg `classroom` · Person (variant `sage`) `sit-chair`, `raise-hand-full`, `worried`, x 40% · Brain `sit-chair`, `smile`, behind at x 65%, scale 0.85 · motion `pose-to` (Brain → `thumbs-up`)
narration: "When people imagined themselves showing vulnerability, like admitting a mistake, asking for help, or saying how they really feel, they saw it as weak and embarrassing. But when they imagined someone else doing the exact same thing, they saw it as brave."

**S37**: REUSE S35 · motion `pose-to` (Brain `raise-hand-half` → `raise-hand-full`, expression → `smile`)
narration: "Same action. Completely different story. The thing that feels like weakness to you, often looks like courage to everyone else."

**S38**: bg `curb-dusk` · Brain `sit-curb`, `neutral`, x 45% · props: 4 small thought bubbles in an arc above him, holding a sign-up sheet, a raised hand, a phone and a waving stick figure · motion `pop-in` (the bubbles, one per sentence: at "team," "question," "post" and "person") · transition `fade`
narration: "When I finally understood all of this, I started thinking about everything I didn't do. The team I didn't try out for. The question I didn't ask. The thing I wanted to post, but deleted. The person I wanted to talk to, but didn't."

**S39**: bg `stage-empty` · Brain `stand`, `neutral`, x 50%, scale 0.55 · motion `zoom-out`
narration: "None of it was because I couldn't do it. It was because of an audience that, mostly, wasn't even watching. And the few who were, would have been a lot kinder than I imagined."

**S40**: bg `plain` · props: a sign-up sheet on a wall, centered and large, with one empty line · Brain's arm only (lower arm + hand, same stroke style) entering from the right, near the sheet · motion: the arm pulls back out of frame, 0.8s · overlay (at "Missed chances," centered below): **MISSED CHANCES** · hold 2.5s after the line
narration: "That's what the spotlight effect really costs you. Not embarrassment. Missed chances."

---

## PART 4: The 5 steps and the ending (`audio/part4.mp3`)

**S41**: bg `plain` · Brain `roll-sleeves`, `smile`, x 50% · motion `nod`
narration: "So here's how I actually use this now."

**S42**: bg `plain` · Brain `think`, `thinking`, x 35% · props: a big thought bubble at x 65% showing a tiny Person in `stumble` beside a dumbbell · overlay (top): **1. WOULD I REMEMBER THIS?** · motion `pop-in` (bubble)
narration: "One. Ask the three-second question. This is the one I promised you. When that everyone's watching thought shows up, I ask myself: Would I remember this, if someone else did it?"

**S43**: REUSE S42 · motion `shrug` (Brain; the thought bubble fades out during the shrug, which is allowed as part of the same beat), expression → `relieved`
narration: "If someone tripped at the gym, would you think about it tomorrow? Probably not. You'd forget in about five seconds. That's exactly how much they'll think about you."

**S44**: bg `plain` · Brain `hold-front` with the giant scissors, `smile`, x 35% · props: a blank sign at x 68% · overlay on the sign: **50%**, swapping to **25%** at the word "half" · overlay (top): **2. CUT IT IN HALF** · motion: the scissors snip once (blades rotate ±12°, 0.3s) right before the number swaps
narration: "Two. Cut the number in half. However many people you think will notice, cut it in half. That's literally what the T-shirt study found. Your brain overestimates by about double."

**S45**: REUSE S24 (all spotlights on) · overlay (top): **3. EVERYONE HAS A SPOTLIGHT** · motion `zoom-in`
narration: "Three. Remember, everyone has their own spotlight. Picture the room. Everyone in it is worried about themselves. You're not on a stage. You're in a crowd of people who all think they're on a stage."

**S46**: REUSE S30 (end state, tray handed over) · overlay (top): **4. PEOPLE ARE KINDER** · motion `zoom-out`
narration: "Four. Assume people are kinder than your brain says. If you do mess up, the people who saw it are probably thinking about it far less, and far more kindly, than you are. And after a conversation, assume they liked you more than you think. The research says they probably did."

**S47**: bg `gym-door` · Brain `walk`, `neutral` → `smile`, x 35% → 62% (through the doorway) · overlay (top): **5. DO IT ANYWAY** · motion `walk`
narration: "Five. Do it anyway, and watch what happens. Next time, do the thing you're nervous about. Then pay attention to how people actually react. Almost every time, it's way less than you expected."

**S48**: bg `stage-dark` · Brain `stand`, `laugh`, x 40% · props: the spotlight cone above the stage that `shrink`s and turns into a small desk lamp on a stool at x 60% · motion `shrink` (spotlight → lamp swap at the end of the shrink) · transition `fade`
narration: "And every time you see that for yourself, the spotlight gets a little dimmer."

**S49**: bg `gym-inside` · Brain `curl-up`, `smile`, x 45% · 3 Persons doing their own thing (poses `curl-down`, `stand`, `arms-relaxed`), all facing away from Brain, scale 0.75 · motion `pose-to` (Brain `curl-down` → `curl-up`, once)
narration: "So here's the lesson. People aren't watching you nearly as much as you think. And that's not sad. That's freedom."

**S50**: bg `hill-sunrise` · Brain `arms-relaxed`, `relieved`, standing on the hilltop, x 50%, scale 0.6 · motion `zoom-out` · transition `fade`
narration: "It means you can try. You can mess up. You can look a little dumb while you get better. You can ask the question. Post the video. Walk into the gym. Talk to the person."

**S51**: bg `plain` · Brain close-up (scale 2.0), `smile` → `wink` at "Hardly anyone's watching" · motion `blink`, then the wink (the expression swap counts as part of the same beat)
narration: "Because the only one keeping score that closely, is you. So go do the thing. Hardly anyone's watching."

**S52**: bg `plain` · Brain `point-left`, `smile`, at x 78%, scale 0.8 · left 55% of the frame left empty (for the YouTube end screen) · motion `pose-to` (→ `point-left`) · hold the last frame 5s after the narration (end-screen time)
narration: "And if you want to actually make that thing a habit, the sixty-six-day video breaks down exactly how long that really takes."

---

### Description sources (for Luke, not on screen)

- Gilovich, Medvec & Savitsky (2000), "The spotlight effect in social judgment," *Journal of Personality and Social Psychology*
- Gilovich, Savitsky & Medvec (1998), "The illusion of transparency," *JPSP*
- Savitsky, Epley & Gilovich (2001), "Do others judge us as harshly as we think?", *JPSP*
- Boothby, Cooney, Sandstrom & Clark (2018), "The liking gap in conversations," *Psychological Science*
- Bruk, Scholl & Bless (2018), "Beautiful mess effect," *JPSP*
