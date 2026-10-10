# SimpleMindMotivation: Video Build Guide

You are building a faceless explainer video for the YouTube channel **SimpleMindMotivation**, using **HyperFrames** (HTML/SVG → MP4).

**The format is simple on purpose: a sequence of clean illustrated pictures** with slow camera moves, a few **B-roll clips**, text callouts, a voiceover and soft music. There is no character animation. This keeps the video clean, consistent and cheap to build.

The guide has two halves:

- **Part A: Channel rules.** These apply to every video.
- **Part B: This video.** The scene list for *"One of the Most Useful Lessons I Learned."*

The owner is Luke. He is not a developer, so keep messages to him short and plain. **Don't stop to ask him questions about style or characters.** Everything you need is in this repo.

---

# PART A: CHANNEL RULES

## A1. Golden rules

1. **Pictures, not animation.** Each scene is one still illustration (sometimes two: a "before" and an "after"). Only the camera moves (A8). Characters never move their limbs on screen.
2. **Characters are built once from Luke's reference and reused.** Every picture uses the same master character files. A character's pose is chosen from a fixed pose set. Never draw a "new version" of a character.
3. **Match the style references exactly** (A4). If this guide and the reference images disagree, the images win.
4. **Data-driven.** Scenes live in `scenes/partN.json`, and one generator script builds any part. Don't hand-write HTML per scene.
5. **One part per session.** Build it, render it, report back in 2 to 3 lines, then stop. After Part 4, do the final join and music automatically (A11).
6. **Check before rendering:** run `npx hyperframes lint` and `npx hyperframes check`, and snapshot 4 frames. Don't re-render a whole part to fix one scene.
7. **Save usage.** Reuse pictures wherever the scene list says REUSE. Don't load skills or docs you don't need, and don't paste big files into chat.

## A2. Repo layout

```
CLAUDE.md                      ← this guide
reference/
  characters/narrator.png      ← Luke: THE narrator, source of truth
  characters/*.png             ← Luke: other characters (optional)
  style/*.png|jpg              ← Luke: style examples to match
audio/part1.mp3 … part4.mp3    ← Luke: ElevenLabs voiceover
music/track.mp3                ← Luke: background music (.mp3/.wav/.m4a)
broll/S01.mp4, S06.mp4 …       ← B-roll clips by scene ID (picked by you via Pexels, or added by Luke)
assets/
  characters/*.svg             ← master characters + poses (built once)
  pictures/S01.svg …           ← one illustration per scene (built once each)
  fonts/  vendor/gsap.min.js
scenes/part1.json … part4.json
tools/build-part.mjs           ← scenes JSON → HyperFrames project
tools/timing.mjs               ← scene times from the audio
parts/part1/ … part4/
renders/part1.mp4 … part4.mp4, full.mp4
review/character-sheet.png     ← self-check image
```

## A3. Environment setup (cloud session)

Do this once per session, quietly:

- `npx hyperframes skills update` (from the repo root). Read `/hyperframes-core` only if you need composition details.
- **Chrome** (Google's download is blocked): `export HYPERFRAMES_BROWSER_PATH=$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome | head -1)`, then confirm with `npx hyperframes doctor`.
- **GSAP** (the CDN is blocked): `npm pack gsap@3.14.2`, then copy `dist/gsap.min.js` to `assets/vendor/`. Use only that local file.
- **Fonts:** `npm i @fontsource/montserrat @fontsource/bebas-neue` and load them locally. No Google Fonts URLs.
- `ffmpeg`/`ffprobe` are available. If an audio file is missing, stop and tell Luke which one.

## A4. Visual style

**First, open and look at every image in `reference/style/` and `reference/characters/`.** They are the target. The main style reference is the **character-sheet image** (a stick figure with curly brown hair and a yellow shirt, shown in front view, turnaround, expressions and explainer poses). **Copy that drawing style.**

**The style in words:**
- **Clean, modern explainer-doodle look.** Crisp, smooth, uniform black outlines (about 4 to 5px at 1080p) with round caps and joins. Lines are clean, **not sketchy**, with no wobble filter.
- **Characters:** a big round head with a simple face; **thin straight black stick limbs**; small rounded black hands and feet; one simple flat-colored shirt/tunic shape for the torso; a **soft light-grey ellipse shadow** under the feet.
- **Faces:** two black vertical-oval eyes (each with a tiny white highlight dot); simple short eyebrows only when needed for the expression; one simple mouth line. Happy and surprised mouths are filled black with a small red-orange tongue.
- **Colors:** flat fills only, no gradients and no textures. Bright but soft: mustard yellow, sky blue, sage green, terracotta, pink, with lots of **white / off-white space**.
- **Settings:** minimal. Off-white background, a ground line, and 1 to 3 simple props or flat shapes that say where we are. Never busy.
- **Text:** Montserrat ExtraBold or Bebas Neue in dark ink, with **one** accent color (dark green `#2F6B2F` or orange `#F2A65A`). Rounded green label pills are allowed, like the "Stage 1" tags in the reference. Max 5 words on screen.

**Canvas:** 1920×1080, 30 fps, MP4 (H.264 + AAC).

**Palette:**

| Name | Hex | Use |
|---|---|---|
| Paper | `#FAF7F0` | default background |
| Ink | `#1A1A1A` | all outlines, limbs, text |
| Shadow | `#E6E1D6` | ground shadow ellipses |
| Mustard | `#F2C230` | shirts, highlights |
| Sky | `#8EC5E8` | skies, shirts |
| Sage | `#9CC08B` | grass, hills, plants, shirts |
| Terracotta | `#D9805F` | shirts, accents |
| Soft orange | `#F2A65A` | spotlight, glow, key numbers |
| Pink | `#F4A6B8` | shirts, accents |
| Brain peach | `#F7C4AE` | narrator brain head (folds `#E39A82`, glow) |
| Hoodie black | `#2B2B2B` | narrator hoodie, pants, hands |
| Label green | `#2F6B2F` | title pills and accents |
| Night | `#2E3A52` | night scenes |
| Stage dark | `#1C1C1C` | dark stage / theater |
| Red | `#D64545` | "X" marks, tongue |

## A5. The narrator (consistency lock)

**Source of truth: `reference/characters/narrator.png`.** It's a character turnaround on a dark background showing the narrator front, walking, pointing and arms-crossed. Rebuild him once as a master SVG (`assets/characters/narrator.svg`), then write the real hex colors you used as a comment at the top of the file.

**His design** (match the reference image; where they differ, the image wins):
- **Head:** a large, smooth cartoon brain, two rounded lobes, warm peach-pink (≈ `#F7C4AE`) with soft curved fold lines in a slightly darker peach (≈ `#E39A82`), and a thin outline. A **soft peach glow** surrounds the brain (a blurred peach halo around the head only, at about 35% opacity). Keep it subtle on light backgrounds.
- **Face:** **two small glowing white oval eyes** on the front of the brain. **No mouth.** No other facial features.
- **Neck:** a short, slim black neck.
- **Body:** a slim, tall build (head ≈ 22% of total height; standing height about 440px at scale 1.0). Black hoodie (≈ `#2B2B2B`) with the hood down, two drawstrings and a pocket line; slim black pants; black hands.
- **Limbs:** slim but **filled** (like the reference), **not** thin stick lines. This makes the narrator stand out from the stick-figure side characters on purpose.
- **Shoes:** white sneakers with a thin red (`#D64545`) stripe along the sole.
- **Outlines:** in clean light scenes, use the same crisp 4 to 5px ink outlines as the rest of the style. A faint warm rim line (like the reference) is allowed on dark backgrounds.

**Narrator expressions** (eyes only, because he has no mouth):
- `neutral`: two ovals
- `happy` / `relieved`: upward arcs (^ ^)
- `surprised`: bigger round eyes
- `worried` / `cringe`: smaller eyes with a short slanted brow line drawn on the brain above each eye
- `thinking`: one eye narrowed into a flat oval
- `laugh`: upward arcs plus 2 tiny sparkle lines
- `wink`: one oval, one arc
- `sweat-drop` is an allowed extra prop for nervous scenes.

- If `narrator.png` is missing, use the curly-haired, yellow-shirt character from the style reference as the narrator, and tell Luke in one line.
- The narrator is the **only** character with his particular look. Other characters must look clearly different (A6).
- Never change his shapes, colors or proportions between pictures. Only the **pose** (A7), the **expression** (A7), the position, the scale, and a horizontal flip change.

**The narrator is NEVER animated.** He's a still picture in every frame. Nothing about him moves: no limbs, no blinking, no breathing, no bobbing. He only changes by **switching to a different still picture** (a new pose and/or expression) with a quick 0.2s crossfade.

**Match his pose to the tone of the voice.** The voiceover has a mood in every line. Pick the narrator's pose and expression to fit it, using the scene list as the starting point. Inside a long scene, swap him to a new still pose when the tone clearly shifts, at most once every ~4 seconds and at most 3 poses per scene. Use this guide:

| Voice tone | Narrator pose | Expression |
|---|---|---|
| calm, explaining, storytelling | `present` or `explain` | `neutral` |
| curious, asking a question | `think` | `thinking` |
| serious, firm, emphatic | `stand` (or `explain` with a raised finger) | `neutral` |
| anxious, nervous, embarrassed | `stand` gripping a strap, or `facepalm` | `worried` / `cringe` |
| surprised, a reveal | `stand` | `surprised` |
| relieved, warm, reassuring | `arms-relaxed` | `relieved` |
| upbeat, confident, a list step | `explain`, `thumbs-up` or `present` | `happy` |
| amused, playful, dry joke | `shrug` | `happy` |
| reflective, quiet, sad | `sit-curb`, `sit-bench` or `stand` | `neutral` / `worried` |
| ending, call to action | `point-left` or `wave` | `happy` / `wink` |

Each of these is just another **pre-built still** from the pose set (A7). Never draw an in-between frame.

## A6. Other characters

- If Luke added other images in `reference/characters/`, build each as its own master SVG (named after the file, e.g. `friend.png` → `friend.svg`) and use them for the matching roles (researcher, friend, waiter, and so on).
- Fill any other roles with a **generic person**: the same style and build, a round white head, simple short hair in a dark color (no hair is also fine), and a flat shirt in **sky, sage or terracotta** (not mustard, which stays special for the main characters). Keep 3 to 4 variants and reuse them.
- In crowds, use 8 people at most, at scales 0.6 to 0.8.

## A7. Pose and expression set (built once)

Build every pose as a separate SVG arrangement of the master character's parts (`assets/characters/narrator-<pose>.svg`, `person-<variant>-<pose>.svg`). Copy the head and face exactly from the master. Only the stick limbs change.

**Poses:** `stand`, `wave`, `think` (hand to chin), `present` (one arm out, palm up), `explain` (one finger raised), `point-left`, `point-right`, `shrug`, `facepalm`, `walk` (mid-stride, one frame), `sit-chair`, `sit-bench`, `sit-curb`, `lie-bed`, `raise-hand`, `thumbs-up`, `hold-front` (holding a prop in front), `hold-up` (holding a prop high), `kneel`, `stumble` (leaning, one arm out), `lift` (holding a dumbbell), `arms-relaxed`.

**Expressions:** `happy`, `neutral`, `surprised`, `worried`, `cringe`, `relieved`, `laugh`, `thinking`, `wink`.

**Props** (built once, in the same style): goofy T-shirt (on a hanger and as worn), clipboard, whiteboard, lightbulb, thought bubble, speech bubble, question mark, dumbbell, lunch tray + spilled food, balance scale, magnifying glass, giant scissors, blank sign, sign-up sheet, desk lamp, spotlight cone, bed, park bench, school desk, chair, movie screen, restaurant table, lockers, gym mirror, simple pie chart.

## A8. Motion: camera only

Every picture gets **one** camera move across its full duration:

| Move | Spec |
|---|---|
| `zoom-in` | scale 1.00 → 1.06, `sine.inOut` |
| `zoom-out` | scale 1.06 → 1.00 |
| `pan-left` / `pan-right` | x shift ≤ 60px at scale 1.04 |
| `hold` | no move (use for text-heavy frames) |

Allowed extras, which are not character motion:
- **Picture swap:** a scene can have a picture A and a picture B, with a 0.3s crossfade at a given word (e.g. the pie chart going from 50% to 25%).
- **Overlay pop-in:** text, labels, a thought bubble or an "X" can appear with a 0.3s fade or scale pop (`back.out(1.4)`).
- **Scene transitions:** a 0.4s crossfade between scenes by default, and a straight cut where the scene says `cut`.

**Banned:** moving limbs, walking cycles, wobble, bounce, shake, spin, fast whips, and line boil.

## A9. Character self-check (first session only; no stopping)

1. Build the master narrator, any other characters, the generic persons, and all poses.
2. Render `review/character-sheet.png`: `narrator.png` on the left, your narrator in `stand` beside it at the same size, then your narrator in 8 poses and 4 expressions, then every other character in `stand`.
3. Compare them carefully against the references (shape, face, colors, line weight, proportions) and fix any differences. **Two fix rounds max**, then continue.
4. Check every pose: no broken joints, no limbs through the body, no gaps at the shoulders or hips.
5. Freeze the character files. Mention the character sheet in your first report so Luke can look at it whenever he wants.

## A10. B-roll (you pick it)

**You choose and fetch the B-roll yourself.** Part B marks the scenes that use B-roll and what each should show. Treat those as suggestions: you may swap the subject, skip one, or add B-roll to another scene where real footage clearly helps. Stay within the 15% limit below.

**How to get clips, in this order:**
1. **A clip Luke already added** in `broll/` named by scene ID (e.g. `broll/S06.mp4`) always wins.
2. **The Pexels API**, if the environment variable `PEXELS_API_KEY` is set:
   - Search `https://api.pexels.com/videos/search?query=<terms>&orientation=landscape&size=medium&per_page=10`, with header `Authorization: $PEXELS_API_KEY`.
   - Pick the clip that best fits the line being spoken: calm, no on-screen text, no big brand logos, no one staring into the camera, and a warm or neutral look.
   - Prefer 1920×1080, or 1280×720 if that's all there is. Download it from the `video_files` link into `broll/S##.mp4`. Keep downloads small (at most about 40 MB each), and trim to 8s with `ffmpeg` right away.
   - Log each clip in `broll/CREDITS.txt` (scene, Pexels URL, creator name).
3. **If the network blocks Pexels or there's no key:** skip B-roll and use the scene's picture. Don't stop, and don't try workarounds. Mention it in one line in your report.

**Using a clip:**
- Show it for the part of the scene marked `broll`, **muted** (the voiceover keeps playing), using its best 4 to 6 seconds. Fit it 16:9 (center-crop if needed) and apply a slow `zoom-in`.
- **Look:** apply a consistent soft, warm grade with `ffmpeg` (`eq=saturation=0.85:contrast=0.95`, plus a slight warm `colorbalance`) so the clips sit nicely next to the clean illustrations. Crossfade 0.4s in and out.
- **If no clip is available:** show the scene's picture instead.
- B-roll should take up at most about 15% of any part.

## A11. Timing, audio and the final join

**Longer pauses (do this first, every part).** The raw voiceover runs fast, about 7.5 minutes total, and Luke wants 8.5 to 9+ minutes. Fix it by **lengthening the silences only**. Never slow down or time-stretch the speech itself.

1. Detect every pause: `ffmpeg -i audio/partN.mp3 -af silencedetect=noise=-35dB:d=0.25 -f null -`.
2. Cut the audio at the middle of each pause and insert extra silence (generated with `anullsrc`, matching the sample rate and channels):
   - **Short pause** (under 0.6s, between sentences): add **+0.25s**
   - **Beat pause** (0.6s or longer, the "..." moments): add **+0.9s**
   - **Scene change** (the pause closest to each scene boundary, from the timing step): add **+0.4s** on top of the above
   - **Big reveals** ("Only about a quarter," "Missed chances," "Hardly anyone's watching"): make sure at least **2.0s** of silence follows
3. Join the pieces in order into `audio/padded/partN.wav` (keep the originals untouched). Use **the padded file** for timing, rendering and the final join.
4. Print the old and new length of each part. The expected total is about **8.5 to 9.5 minutes** for all 4 parts. If the total comes out under 8:30, raise the short-pause padding to +0.35s and redo it.
5. Listen-check 20 seconds: it should sound like a calm, confident speaker, not robotic gaps. If the pauses feel unnatural, lower the short-pause padding.

**Timing (per part):**
1. Get the duration with `ffprobe audio/padded/partN.wav`.
2. Find the pauses: `ffmpeg -i audio/padded/partN.wav -af silencedetect=noise=-35dB:d=0.35 -f null -`.
3. Estimate each scene's length from its narration word count, then snap each boundary to the nearest silence within ±1.5s.
4. For in-scene cues ("swap at the word X"), estimate the position by word count inside the scene.
5. Save to `scenes/partN.timing.json` and print a short scene/start/end table.
6. If Luke corrects a time, edit only that boundary.

**Build loop (per part):** pad pauses → timing → `scenes/partN.json` → build any missing pictures (skip REUSE scenes) → `node tools/build-part.mjs N` → lint and check → snapshot 4 frames → render `renders/partN.mp4` (**voice only**) → report → stop.

**Final join** (automatically right after Part 4, or when Luke asks):
1. Concat the parts into `renders/full-voice.mp4`, with 1.0s of silence and a held last frame between parts.
2. Take the music from `music/`. Loop it with `-stream_loop -1` if it's shorter than the video, and trim it to length.
3. **Mix it softly:** music at about **−24 dB** (roughly 6 to 8% volume), with `sidechaincompress` ducking keyed to the voice (threshold 0.02, ratio 8, attack 20ms, release 400ms), a 2s fade-in and a 4s fade-out. The voice stays untouched. Final `loudnorm` to about −14 LUFS, with no clipping.
4. Output `renders/full.mp4`. Listen-check the first 20 seconds and one pause point. If the music competes with the voice anywhere, lower it 3 dB and re-mix (audio only).
5. If `music/` has no real audio file (missing, or under 50 KB, which means a broken upload), deliver the voice-only version and tell Luke.

## A12. Self-check before every render

- [ ] The narrator matches `reference/characters/narrator.png` and is identical in every picture.
- [ ] Pictures match the character-sheet style: clean uniform outlines, oval eyes, stick limbs, flat colors, lots of white space.
- [ ] Only palette colors are used.
- [ ] Only camera moves, swaps and overlay pop-ins; no character motion. The narrator is a still picture whose pose fits the tone of each line.
- [ ] On-screen text is spelled exactly as in Part B, with ≤ 5 words.
- [ ] B-roll is graded, muted and ≤ 15% of the part; missing clips fall back to the picture.
- [ ] The padded audio is used, video length equals audio length, and the audio is present.
- [ ] (Final) The music is soft and the voice is always clearly on top.

---

# PART B: THIS VIDEO

**Title:** One of the Most Useful Lessons I Learned
**Topic:** the spotlight effect: people notice and judge us far less than we think
**Length:** raw voice ≈ 7.5 min (part 1 1:27, part 2 2:02, part 3 2:12, part 4 1:52). After pause padding (A11), the target is about **8.5 to 9.5 minutes**.
**Audio:** `audio/part1.mp3` … `audio/part4.mp3`, padded into `audio/padded/`
**Music:** `music/track.mp3` (a dark ambient track, about 12.5 min, so no looping is needed). Keep it very soft.

**Scene format** (each becomes one entry in `scenes/partN.json`): `id`, `picture` (what to draw: setting, characters with pose + expression, props), `camera`, `swap` (optional picture B + the word that triggers it), `overlay` (exact text), `broll` (optional: which part of the scene), `transition`, `narration` (used for timing only and never shown on screen).

`REUSE Sxx` means: use picture Sxx again. Draw nothing new.

---

## PART 1: Hook and the spotlight effect (`audio/part1.mp3`)

**S01**
picture: off-white; a simple gym doorway (frame plus a glimpse of a dumbbell rack inside). The narrator stands outside it, `stand`, `worried`, one hand gripping a backpack strap.
camera: `zoom-in`
broll: **first 4s**, a person walking toward or into a gym entrance → `broll/S01.mp4`
narration: "For a long time, there was one thought that stopped me from doing almost everything. Going to the gym. Raising my hand in class. Trying out for something. Posting anything online."

**S02**
picture: a close-up of the narrator's head and shoulders, `worried`, with a small sweat drop. Plain off-white.
camera: `zoom-in` · transition `cut`
narration: "Everyone's going to be watching."

**S03**
picture: Stage dark background; the narrator small and alone on a stage edge, `worried`, lit by one soft-orange spotlight cone; the dark crowd area is rows of small white oval eye-pairs.
camera: `zoom-out`
narration: "That's what it felt like. Every single time. Like I was standing alone on a giant stage, with one bright spotlight on me, and thousands of eyes in the dark."

**S04**
picture: the same dark stage, empty; a goofy T-shirt (big silly cartoon face on it) on a hanger, in the spotlight.
camera: `zoom-in`
narration: "Then I learned about one experiment, involving a really embarrassing T-shirt."

**S05**
picture: off-white; the narrator `think`, `thinking`; a glowing lightbulb above his head.
camera: `hold`
overlay: after the narration, a 2.5s title card: a green pill reading **LESSON** above big ink text **ONE OF THE MOST USEFUL LESSONS I LEARNED** (two lines), with "USEFUL" in orange.
narration: "And it changed how I see almost everything. By the end of this video, you'll know exactly how wrong our brains are about this, by how much, and the one question I now ask myself that shuts that thought down in about three seconds."

**S06**
picture: a school hallway (row of sky-blue lockers); the narrator `walk`, `neutral`, with a soft-orange spotlight circle on the floor under him.
camera: `pan-right`
broll: **first 4s**, students walking down a school hallway → `broll/S06.mp4`
narration: "So here's how it used to go for me. I'd walk into a room, and I'd feel like there was a spotlight following me."

**S07**
picture: the hallway; the narrator `stumble`, `cringe`, center; 3 generic persons nearby in `stand`, `neutral`.
camera: `zoom-in`
overlay: thought bubbles pop in over the 3 persons one by one (0.4s apart), each holding one tiny icon: a laughing face, "!" and "?".
narration: "If I tripped, everyone saw it. If my outfit was a little off, everyone noticed. If I said something dumb, I was sure everyone would remember it for weeks."

**S08**
picture: a night bedroom (Night background, window with a moon); the narrator `lie-bed`, `worried`; a thought bubble above shows a tiny narrator in `stumble`.
camera: `zoom-in`
narration: "And then I'd replay it in my head that night. Over and over. Like a highlight reel of every awkward thing I'd ever done."

**S09**
picture: REUSE S08
swap: picture B, the same bedroom with the narrator `relieved` and no thought bubble, at the word "weird"
camera: `zoom-out`
narration: "If you've ever done that, lying in bed at night, thinking about something awkward from three years ago. You're not weird. You're not broken."

**S10**
picture: off-white; a whiteboard on the right; the narrator `present`, `happy`, gesturing at it.
camera: `hold`
overlay: on the whiteboard, **THE SPOTLIGHT EFFECT** fades in at the words "spotlight effect"
narration: "Your brain is doing something almost everyone's brain does. And it even has a name. Psychologists call it the spotlight effect. It's the feeling that people are noticing you, and judging you, way more than they actually are. And once you understand how strong it is, it's hard to see things the same way again."

---

## PART 2: The T-shirt study (`audio/part2.mp3`)

**S11**
picture: a sky-blue sky, a sage hill, a simple university building with columns.
camera: `pan-right`
broll: **first 5s**, a university campus with students walking → `broll/S11.mp4`
overlay: small, bottom-left: **Cornell University, ~2000**
narration: "So here's the experiment. Around the year two thousand, a psychologist named Thomas Gilovich and his team at Cornell University ran a study with college students."

**S12**
picture: off-white; a generic student wearing the goofy T-shirt, `shrug`, `cringe`.
camera: `zoom-in`
narration: "They had one student put on a T-shirt with a big, cheesy picture of a singer on it. One that college students at the time would find really embarrassing to be seen in."

**S13**
picture: a classroom with rows of desks and seated generic students (`sit-chair`, `neutral`, scale 0.7); the T-shirt student in the doorway, `walk`, `cringe`.
camera: `pan-left`
narration: "Then that student walked into a room full of other students, stayed for a moment, and walked back out."

**S14**
picture: off-white; a researcher (generic, sage shirt) `hold-front` with a clipboard, and the T-shirt student `stand`, `worried`; a speech bubble from the researcher with a big "?".
camera: `zoom-in`
narration: "Afterward, the researchers asked the student in the T-shirt one simple question. How many people in that room do you think noticed your shirt?"

**S15**
picture: off-white; the T-shirt student `think`, `thinking`, on the left; on the right, a simple pie chart filled **50%** in orange, labeled **THEIR GUESS: 50%**.
camera: `hold`
narration: "On average, they guessed about half."

**S16**
picture: REUSE S15
swap: picture B, the student now `surprised`, the pie at **25%**, label **REALITY: 25%**, at the word "quarter"
camera: `zoom-in` (starts after the swap) · hold 2s after the line
narration: "The real number? Only about a quarter."

**S17**
picture: off-white; the T-shirt student `shrug`, `relieved`.
camera: `zoom-out`
narration: "They thought twice as many people noticed as actually did. And remember, that was a shirt picked specifically to be embarrassing. Something designed to get noticed."

**S18**
picture: a simple restaurant table; the narrator seated at the table in `facepalm`, `cringe`; a generic waiter walking away.
camera: `zoom-in`
narration: "Now think about the little things you worry about every day. A bad hair day. A pimple. Saying you too when the waiter says enjoy your meal."

**S19**
picture: REUSE S17
camera: `zoom-in`
narration: "If people barely noticed a ridiculous T-shirt, they're definitely not tracking those."

**S20**
picture: a dark theater; the narrator seen from behind, small, in a seat; the big screen shows a huge close-up of the narrator's own `happy` face.
camera: `zoom-in`
broll: **first 4s**, an empty movie theater with a glowing screen → `broll/S20.mp4`
narration: "So why does this happen? It's actually pretty simple. You are the main character of your own life. You see everything from inside your own head, so you're thinking about yourself all day long. And your brain quietly assumes everyone else is thinking about you too."

**S21**
picture: the hallway; 6 generic persons (scale 0.7), each `stand`, `worried`, each under their **own** small soft-orange spotlight; the narrator in the middle, `surprised`.
camera: `zoom-out`
overlay: the spotlights fade in one at a time, 0.25s apart
narration: "But here's the thing. Everyone else is the main character of their own life too."

**S22**
picture: a gym with a mirror; a generic person `lift`, `thinking`, checking his form in the mirror; the narrator small in the background, ignored.
camera: `zoom-in`
broll: **first 4s**, a person lifting weights and looking in a gym mirror → `broll/S22.mp4`
narration: "That guy you think is judging your workout? He's worried about his own form."

**S23**
picture: the hallway; a generic person (terracotta shirt) `walk`, `cringe`, with a thought bubble showing herself waving awkwardly.
camera: `pan-right`
narration: "That girl you think noticed you stumble over your words? She's busy replaying something she said."

**S24**
picture: REUSE S21 (all spotlights on)
camera: `zoom-in`
broll: **first 4s**, a crowd of people walking on a busy street, all on their own way → `broll/S24.mp4`
narration: "Everyone is walking around in their own little spotlight, so busy worrying about it that they barely notice yours."

**S25**
picture: a classroom; the narrator at the front `present`, `worried`, with small sweat drops and little "nervous" shake lines drawn next to his knees (static lines).
camera: `zoom-in`
narration: "And it's not just about how you look. Gilovich and his team found something similar with nerves. When people gave a speech, they thought their nervousness was way more obvious than it really was. The audience mostly couldn't tell."

**S26**
picture: the same classroom from the audience's side: the backs of 4 seated students in the foreground, and the narrator at the front looking calm, `neutral`.
camera: `zoom-in`
overlay: a small green pill above the narrator: **SEEMS FINE**
narration: "They called it the illusion of transparency. It's that feeling that everyone can see right through you. They can't. The shaking you feel on the inside? From the outside, it mostly just looks like a normal person talking."

---

## PART 3: People are kinder than you think (`audio/part3.mp3`)

**S27**
picture: a cafeteria; the narrator `stand`, `surprised`, with a dropped lunch tray and spilled food at his feet.
camera: `zoom-in`
narration: "Okay. But what about when people do notice? What if you really do mess up, and someone sees it?"

**S28**
picture: off-white; the narrator `explain`, `thinking`, on the left; a big balance scale on the right, its left pan heavy and low, its right pan light and high.
camera: `hold`
overlay: pan labels **EXPECTED** (left) and **REALITY** (right)
narration: "This is where it gets even better. Researchers tested this too. They had people imagine, or actually go through, embarrassing moments, like messing up in front of others. Then they compared how harshly people thought they'd be judged, with how harshly they actually were judged."

**S29**
picture: REUSE S28
camera: `zoom-in` toward the REALITY pan
narration: "Over and over, people expected to be judged way more harshly than they really were."

**S30**
picture: the cafeteria; the narrator `kneel`, `relieved`; a generic person (sage shirt) `kneel`, `happy`, handing him the tray; 2 people in the background `stand`, `happy`.
camera: `zoom-out`
narration: "Because when other people see you mess up, they don't just see the mistake. They see the whole situation. They know you were nervous. They know it was a hard moment. They've been there too."

**S31**
picture: off-white; the narrator `hold-up`, `cringe`, holding a giant magnifying glass to his own face; far away on the right, 3 small generic persons `happy`.
swap: picture B, the narrator lowering the glass (`hold-front`, `relieved`), at the word "kindness"
camera: `hold`
narration: "You're judging yourself with a magnifying glass. They're looking at you from across the room, with a lot more kindness than you'd expect."

**S32**
picture: a park with a sage tree and a bench; the narrator and a generic person (terracotta shirt) both `sit-bench`, `happy`, facing each other.
camera: `zoom-in`
broll: **first 4s**, two people talking and laughing on a park bench → `broll/S32.mp4`
narration: "And here's one that honestly surprised me. It's called the liking gap."

**S33**
picture: the same park bench; a researcher (sage shirt) `hold-front` with a clipboard, standing beside them.
camera: `zoom-out`
narration: "Researchers paired up strangers and had them talk for a few minutes. Afterward, they asked each person two things. How much did you like the other person? And how much do you think they liked you?"

**S34**
picture: the park, no bench people; the narrator `walk` facing left, `worried`, with a thought bubble holding a small grey storm cloud; the other person `walk` facing right, `happy`, with a thought bubble holding a smiley face.
camera: `hold`
overlay: both bubbles pop in together
narration: "People consistently underestimated how much the other person liked them. You walk away from a conversation thinking, that was so awkward, they probably think I'm weird. And the other person walks away thinking, that was nice. I liked them."

**S35**
picture: a classroom; the narrator `sit-chair` at a desk, `worried`, his hand half raised.
camera: `zoom-in`
narration: "And there's one more. Researchers call it the beautiful mess effect."

**S36**
picture: a classroom; a generic person (sage shirt) `raise-hand`, `worried`, in front; the narrator behind, `thumbs-up`, `happy`.
camera: `zoom-in`
narration: "When people imagined themselves showing vulnerability, like admitting a mistake, asking for help, or saying how they really feel, they saw it as weak and embarrassing. But when they imagined someone else doing the exact same thing, they saw it as brave."

**S37**
picture: REUSE S35
swap: picture B, the narrator `raise-hand` (fully up), `happy`, at the word "courage"
camera: `zoom-out`
narration: "Same action. Completely different story. The thing that feels like weakness to you, often looks like courage to everyone else."

**S38**
picture: a dusk street (flat orange and terracotta sky bands, a curb, a streetlamp); the narrator `sit-curb`, `neutral`.
camera: `zoom-in`
broll: **first 4s**, a quiet street at sunset → `broll/S38.mp4`
overlay: 4 small thought bubbles in an arc pop in one at a time at "team," "question," "post" and "person": a sign-up sheet, a raised hand, a phone, and a waving person.
narration: "When I finally understood all of this, I started thinking about everything I didn't do. The team I didn't try out for. The question I didn't ask. The thing I wanted to post, but deleted. The person I wanted to talk to, but didn't."

**S39**
picture: a wide empty stage, softly lit, with rows of empty seats; the narrator small in the middle, `neutral`.
camera: `zoom-out`
narration: "None of it was because I couldn't do it. It was because of an audience that, mostly, wasn't even watching. And the few who were, would have been a lot kinder than I imagined."

**S40**
picture: off-white; a sign-up sheet on a wall with one empty line; the narrator's arm (one stick arm plus a hand) pulling away at the edge.
camera: `zoom-in`
overlay: **MISSED CHANCES** fades in at those words · hold 2.5s after the line
narration: "That's what the spotlight effect really costs you. Not embarrassment. Missed chances."

---

## PART 4: The 5 steps and the ending (`audio/part4.mp3`)

**S41**
picture: off-white; the narrator `explain`, `happy`, center.
camera: `zoom-in`
narration: "So here's how I actually use this now."

**S42**
picture: off-white; the narrator `think`, `thinking`, on the left; a big thought bubble on the right showing a tiny person `stumble` next to a dumbbell.
camera: `hold`
overlay: a green pill **STEP 1** + **WOULD I REMEMBER THIS?**
narration: "One. Ask the three-second question. This is the one I promised you. When that everyone's watching thought shows up, I ask myself: Would I remember this, if someone else did it?"

**S43**
picture: off-white; the narrator `shrug`, `relieved`, with no thought bubble.
camera: `zoom-out`
narration: "If someone tripped at the gym, would you think about it tomorrow? Probably not. You'd forget in about five seconds. That's exactly how much they'll think about you."

**S44**
picture: off-white; the narrator `hold-front` with giant scissors, `happy`; a blank sign on the right.
camera: `hold`
overlay: a green pill **STEP 2** + **CUT IT IN HALF**; on the sign, **50%**, which changes to **25%** at the word "half"
narration: "Two. Cut the number in half. However many people you think will notice, cut it in half. That's literally what the T-shirt study found. Your brain overestimates by about double."

**S45**
picture: REUSE S21 (all spotlights on)
camera: `zoom-in`
overlay: a green pill **STEP 3** + **EVERYONE HAS A SPOTLIGHT**
narration: "Three. Remember, everyone has their own spotlight. Picture the room. Everyone in it is worried about themselves. You're not on a stage. You're in a crowd of people who all think they're on a stage."

**S46**
picture: REUSE S30
camera: `zoom-in`
overlay: a green pill **STEP 4** + **PEOPLE ARE KINDER**
narration: "Four. Assume people are kinder than your brain says. If you do mess up, the people who saw it are probably thinking about it far less, and far more kindly, than you are. And after a conversation, assume they liked you more than you think. The research says they probably did."

**S47**
picture: the gym doorway from S01; the narrator `walk` through the doorway, `happy`.
camera: `zoom-in`
broll: **last 4s**, a person walking confidently into a gym → `broll/S47.mp4`
overlay: a green pill **STEP 5** + **DO IT ANYWAY**
narration: "Five. Do it anyway, and watch what happens. Next time, do the thing you're nervous about. Then pay attention to how people actually react. Almost every time, it's way less than you expected."

**S48**
picture: the dark stage; the narrator `laugh`; a giant spotlight cone.
swap: picture B, the same stage with the spotlight replaced by a tiny desk lamp on a stool and the narrator still `laugh`, at the word "dimmer"
camera: `hold`
narration: "And every time you see that for yourself, the spotlight gets a little dimmer."

**S49**
picture: a gym; the narrator `lift`, `happy`; 3 generic persons doing their own thing (`lift`, `stand`, `arms-relaxed`), all facing away.
camera: `zoom-out`
broll: **first 4s**, people working out in a gym, each focused on their own workout → `broll/S49.mp4`
narration: "So here's the lesson. People aren't watching you nearly as much as you think. And that's not sad. That's freedom."

**S50**
picture: a sky-blue sky, a soft-orange sun, a sage hill; the narrator small on top, `arms-relaxed`, `relieved`.
camera: `zoom-out`
broll: **first 4s**, a sunrise over hills or a person on a hilltop at sunrise → `broll/S50.mp4`
narration: "It means you can try. You can mess up. You can look a little dumb while you get better. You can ask the question. Post the video. Walk into the gym. Talk to the person."

**S51**
picture: off-white; a close-up of the narrator, `happy`.
swap: picture B, the narrator `wink`, at the word "Hardly"
camera: `zoom-in`
narration: "Because the only one keeping score that closely, is you. So go do the thing. Hardly anyone's watching."

**S52**
picture: off-white; the narrator `point-left`, `happy`, on the right side (x ≈ 78%), with the left 55% left empty for the YouTube end screen.
camera: `hold` · hold the last frame 5s after the narration
narration: "And if you want to actually make that thing a habit, the sixty-six-day video breaks down exactly how long that really takes."

---

### Description sources (for Luke, not on screen)

- Gilovich, Medvec & Savitsky (2000), "The spotlight effect in social judgment," *Journal of Personality and Social Psychology*
- Gilovich, Savitsky & Medvec (1998), "The illusion of transparency," *JPSP*
- Savitsky, Epley & Gilovich (2001), "Do others judge us as harshly as we think?", *JPSP*
- Boothby, Cooney, Sandstrom & Clark (2018), "The liking gap in conversations," *Psychological Science*
- Bruk, Scholl & Bless (2018), "Beautiful mess effect," *JPSP*
