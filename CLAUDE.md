# SimpleMindMotivation: Video Build Guide

You assemble faceless explainer videos for Luke's YouTube channel **SimpleMindMotivation**, using **HyperFrames** (HTML + GSAP → MP4).

**The format:** Luke's AI-made illustrations (Nano Banana, 2K), fast cuts (a new shot every ~3s), icon cutaways, narrator pop-ups, short text cards, simple coded diagrams, an ElevenLabs voiceover and soft music.

Luke is not a developer. Keep messages to him short and plain. **Don't ask him questions about style or content.** Everything you need is in this repo.

---

## 0. What to do in a session

1. **Read `VIDEO.md`.** It's the scene list for the current video. When planning a *new* video (script, scene list, prompts, upload kit), follow `PLAYBOOK.md`.
2. **Check the inputs** against it: `audio/part1.mp3` … `part4.mp3`, every `NEW` picture in `pictures/`, and the icons in `icons/`.
   - **Missing audio:** stop and tell Luke which files are missing.
   - **Missing picture:** use a text card with that scene's key phrase, keep going, and list the missing files in the report.
   - **Missing icon:** skip that beat.
3. **Build the whole video in one go, with no check-ins:** Parts 1 → 2 → 3 → 4, then the final join with music.
   - Run your own checks and fix problems yourself.
   - Commit and push after each part, so a new session can pick up where you left off if this one runs out.
4. **Deliver** `renders/full.mp4` as a file in the chat, plus a 3-line report.
   - Also commit and push it. GitHub refuses files over 100 MB, so if it's bigger, push a copy re-encoded under 95 MB as `renders/full-small.mp4` instead.
5. **Save usage:**
   - Reuse and extend the existing tools; don't rewrite them.
   - Don't load skills or docs you don't need.
   - Don't paste big files into chat.

## 1. Repo layout

The repo root always holds the **current** video. Finished videos are archived in `videos/`.

```
CLAUDE.md                 ← this guide (channel rules, the same for every video)
VIDEO.md                  ← the current video's scene list
PLAYBOOK.md               ← titles, thumbnails, descriptions and script shape (for Luke and script writing; not needed to build)
audio/part1-4.mp3         ← Luke: ElevenLabs voiceover (or clips part1a, part1b … joined by tools/join-clips.py); padded copies go in audio/padded/
pictures/S##.jpg|png      ← scene pictures (S##b = "after" picture of a swap)
icons/I##.jpg             ← icon cutaways (16:9, off-white background)
assets/narrator/N01-N12.png ← narrator pop-up poses, transparent and ready to use
assets/sfx/  assets/vendor/gsap.min.js
music/track.mp3           ← soft background music
tools/                    ← the build pipeline (built for video 1; reuse it)
scenes/                   ← generated specs, word timestamps and timing for the current video
parts/partN/  renders/    ← HyperFrames projects and renders
reference/                ← style references (the look of coded diagrams, the narrator)
prompts/                  ← Luke's Nano Banana prompts for this video
videos/01-spotlight/      ← video 1, archived
videos/02-regret/         ← video 2, archived; its make-specs.py and scenes/ are the newest spec examples (host mode and edits)
```

## 2. Setup (once per cloud session, quietly)

- `npm i` (installs `@fontsource/nunito`).
- `npx hyperframes skills update`. Read `/hyperframes-core` only if you need composition details.
- **Chrome** (Google's download is blocked):
  - `export HYPERFRAMES_BROWSER_PATH=$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome | head -1)`
  - Then run `npx hyperframes doctor`.
- **GSAP:** use only the local `assets/vendor/gsap.min.js` (the CDN is blocked).
- **Whisper:** `pip install faster-whisper --break-system-packages`. The `small.en` model downloads from huggingface.co, which this environment allows.
- `ffmpeg` and `ffprobe` are available.

## 3. Pipeline (in `tools/`)

1. **Specs.** Write `tools/make-specs.py` for the current video from `VIDEO.md`.
   - Copy the helpers (`sc`, `icon`, `card`, `pop`, `title`, `mv`, `step`, `quote`, `iconrow`, overlays, `foci`, host tracks) from `videos/02-regret/make-specs.py`, the most recent build. It already supports host mode and the editing toolkit.
   - It outputs `scenes/partN.json` and `scenes/foci.json`.
   - Add any new diagram kinds that `VIDEO.md` asks for to `tools/build-part.mjs`.
1b. **Clips.** If the voice comes as clips (`audio/part1a.mp3`, `part1b.mp3` …), run `python3 tools/join-clips.py` to join them into `audio/partN.mp3`. Missing-audio checks apply to the joined files.
2. **Pause padding.** `tools/pad-audio.py` lengthens silences only (see section 10) and outputs `audio/padded/partN.wav`.
3. **Word timestamps.** Run `tools/transcribe.py audio/padded/partN.wav scenes/partN.words.json`.
4. **Timing.** Run `tools/timing.py N`. Each scene starts at its first word and ends right before the next scene's first word.
5. **Prepare pictures.** Run `tools/prep-pictures.py N`. It makes full-frame pictures and focus crops from the 2K sources with lanczos.
6. **Build.** Run `node tools/build-part.mjs N`. It writes `parts/partN/`, `scenes/partN.cuts.txt` and `scenes/partN.plan.json`.
7. **Check.**
   - Run `npx hyperframes lint` and `npx hyperframes check`.
   - Snapshot every beat (`tools/snap-times.py`), make contact sheets (`tools/review-sheets.py`), **look at them**, and fix problems.
8. **Render** `renders/partN.mp4` (voice only), then commit and push.
9. **Final join.** After Part 4, run `tools/final-join.py`. It joins the parts, mixes in SFX and music, and outputs `renders/full.mp4`.

## 4. Pacing (the most important rule for the feel)

- **No shot longer than 4.0s.** The target average is about **3s**.
  - Exceptions: the title card (2.5s), a quote card (up to 7s), and the end screen (its last 5s).
- Split every scene into beats that change on **sentence or phrase boundaries**, never mid-word.
- **Beat recipe** for a long scene: main picture (≤4s) → icon cutaway on the key word → punch-in crop of the main picture → text card *or* narrator pop-up *or* picture B → back to the main picture.
  - Never put two text cards in a row.
  - Never put two icons in a row.
- **Coded diagrams:** pictures, crops, icons and diagrams should fill **at least 75%** of screen time. Text cards are seasoning.

## 5. Icons

- Icons are `icons/I##.jpg`: one centered subject on off-white, 16:9. Scale them to 1920×1080 with lanczos.
- Show each one for **1.5 to 3s**, timed exactly on the word it illustrates, centered on cream.
  - It pops in over 0.2s (scale 0.92 → 1.0) with a soft *pop* SFX.
- Each icon can be used at most twice per video. `VIDEO.md` lists the key ones, and you can add more where an icon clearly fits.

## 6. Narrator pop-ups and the narrator host

- **Host mode:** if `VIDEO.md` has `host:` lines, follow its "narrator host" section. The narrator stands at the side of the scene in a host frame, and his pose hard-cuts with the tone of the voice. The rules below (poses, never animated, slide in and out) still apply.

- **The poses:** `assets/narrator/N01.png … N12.png` are transparent cut-outs, about 680px tall. Use them as-is.
- **What each pose is:**
  - N01 explain (open hand), N02 finger up (key point)
  - N03 point right (hand on hip), N04 point right (both hands)
  - N05 shrug (joke), N06 thinking (a question)
  - N07 thumbs up (a step or good news), N08 two fingers (counting)
  - N09 surprised (a reveal), N10 facepalm (embarrassment)
  - N11 arms crossed (a confident statement), N12 wave (intro or outro)
- **Layout:**
  - He's about **55 to 65% of the frame height**, in the **lower-left** corner (all the poses face right).
  - The card, icon or chart goes on the right, on cream.
  - If he must stand on the right, flip him horizontally.
- **Motion:** he is **never animated**. Allowed:
  - slide in from the edge (0.25s, ease-out) and out (0.2s)
  - a soft *swoosh* SFX
  - a hard cut to a second pose when the tone changes (at most 2 poses per pop-up)
- **Timing:** each pop-up lasts **2 to 4s** and counts as one shot. Use one about every 25 to 40 seconds, on lines where he explains, makes a point, asks a question, lists a step or reacts.

## 7. Pictures and crops

- Pictures are Luke's AI images, mostly **2K (2752×1536)**. Scale them **down** to 1920×1080 with lanczos.
  - Use them as-is: never redraw, restyle or "fix" them. Only crop or scale them to fit 16:9.
- **Swaps:** `S##` then `S##b` at the trigger word.
- **Reuse:** `SAME AS Sxx` in `VIDEO.md` means reuse that scene's picture.
- **Punch-in crops:**
  - At most **1.4×**, and at most 1 per scene.
  - **Open the picture and look at it first.** Center the crop on a real subject and keep the whole subject in frame.
  - Never crop to just legs, just background, or a cut-off head.
  - Crop from the full 2K source.

## 8. Text, labels and coded diagrams (one consistent style)

- **Look:** cream background `#FAF7F0`, **Nunito ExtraBold**, ink `#1A1A1A`. Key words and numbers go in **yellow `#F2C230` or red `#D64545` badges** with a black outline.
- **Text cards:** a maximum of 5 words, 1.5 to 2.5s, and at most **1 standalone card per scene** (a pop-up's content doesn't count). Use them only for the punchiest phrase being said at that moment.
- **Overlay labels and STEP pills:** at least **56px** text, in a solid pill with a 6px outline, placed **top-center**.
- **Diagrams** (pie, scale, grid, bars, lines and so on) use the same style: 9px ink outlines and flat palette fills.
- **Palette:**
  - Paper `#FAF7F0`, Ink `#1A1A1A`, Shadow `#E6E1D6`
  - Mustard `#F2C230`, Sky `#8EC5E8`, Sage `#9CC08B`
  - Terracotta `#D9805F`, Soft orange `#F2A65A`
  - Label green `#2F6B2F`, Red `#D64545`
- **Title card:** a green pill above two lines of big ink text, with one word in orange, held for 2.5s at the end of Part 1.

## 9. Editing toolkit: motion and transitions

**No more slow Ken Burns zooms as the main move.** They looked flat. Every shot now gets a *motivated* move: something happens on a word. Pick from this toolkit, driven by the trigger words in `VIDEO.md` (`edit:` lines) and by these defaults.

**Install from the HyperFrames registry** (`npx hyperframes add <name>`, see `/hyperframes-registry`): `motion-blur`, `whip-pan`, `cut-the-curve`, `directional-wipe`, `hw-callout-circle`, `hw-arrow`, `hw-underline`, `marker-highlight`, `count-up`, `number-wheel`, `per-word-rise`, `kinetic-type-swap`, `iris-reveal`, `focus-rack`, `light-sweep-pass`, `organic-light-leak-overlay`.
- Restyle every one to our palette and Nunito ExtraBold.
- Keep everything seek-safe.
- If an item won't install, build the same effect with GSAP plus CSS/SVG filters. Don't stop.

| Technique | What it looks like | Use it for |
|---|---|---|
| **Snap zoom** | A fast punch-in (0.25s, `expo.out`) from the full picture to a subject, then a hold with a tiny 1.5% drift | Naming a person or thing in a picture ("Office workers.") |
| **Whip slide (motion blur)** | The frame slides quickly (0.22–0.3s, `power3.inOut`) from one subject to the next with **directional motion blur** (`motion-blur` component, or an SVG `feGaussianBlur` with a horizontal-only stdDeviation of about 40 at peak speed) and a *swoosh* | Moving between people or objects in the same picture, as in a list |
| **Whip-pan cut** | A `whip-pan` or `cut-the-curve` transition between two different pictures | Fast topic changes and "but then…" moments |
| **Push / slide wipe** | A `directional-wipe`: the new picture pushes the old one off | A story moving forward in time (the student leaves, years later) |
| **Hand-drawn callout** | An `hw-callout-circle` or `hw-arrow` draws on around a subject, with a short label | Pointing at a detail ("Cornell", the 76% student, the reflection) |
| **Marker highlight / underline** | `marker-highlight` or `hw-underline` on the key word of a card | The punch word in text cards |
| **Count-up numbers** | `count-up` or `number-wheel`, so numbers roll to their value | Every statistic (75%, 77, 213, 84%, 76%) |
| **Word-by-word rise** | `per-word-rise` with words timed to the voice | Quotes and two-line cards |
| **Kinetic word swap** | `kinetic-type-swap`, one word rolling into another | Card → card swaps ("played it safe" → "tried") |
| **Focus rack** | `focus-rack`: one element sharp, the other blurred, then they switch | Comparisons (should vs want, short sting vs long what-if) |
| **Iris / light sweep** | `iris-reveal` into a picture, or a `light-sweep-pass` across it | Warm, hopeful reveals (the door opening, the sunrise) |
| **Light leak** | A soft `organic-light-leak-overlay` | Memories and "years later" moments, at most 3 times per video |
| **Impact hit** | On a big reveal number only: a 1.06 → 1.0 scale punch plus at most a **3-frame, ≤6px** shake, with a *ding* | The 4–5 biggest reveals only |

**Rules:**
- **Every shot moves on purpose.** A snap zoom, whip, callout or count-up should land on a word at least every ~3s.
  - A plain shot gets at most a subtle 1.5% drift.
  - Never use a slow 5% zoom for a whole shot.
- **Pictures with several subjects** (lineups, thought bubbles, two-person scenes) are "toured": snap zoom to the first subject on its word, then whip slide to each next subject on its word, then zoom back out to the full picture.
- **Transitions between scenes:** use a hard cut by default, a whip-pan cut for energy, and a push wipe for a time jump. Crossfades (0.25s) are only for calm, reflective moments.
- **Inside a scene:** use hard cuts between beats. Never crossfade into or out of a text card, and make sure nothing ghosts.
- **Crops and zooms** stay at **1.4× or less** of the 2K source and keep the whole subject in frame (section 7).
- **Overlays** pop in with `back.out(1.4)` over 0.3s. Swaps take 0.3s.
- **SFX for every move:** *swoosh* for whips and slides, *pop* for snap zooms and icons, *click* for cards, *ding* for reveals. Add a soft *riser* (0.6s) before the 3 biggest reveals, generated with ffmpeg in `tools/make-sfx.sh`. Stay quiet and keep about −20 dB under the voice.
- **Still banned:** moving the narrator's limbs, walk cycles, wobble or bounce on characters, constant shake, spin, and line boil.
- Everything must stay seek-safe on one paused GSAP timeline.

## 10. Audio

- **Pause padding** (do this first; never time-stretch the speech):
  - short pause (under 0.6s): **+0.25s**
  - beat pause (0.6s or longer): **+0.9s**
  - scene change: **+0.4s** extra
  - reveals marked in `VIDEO.md`: at least **2.0s** of silence after
  - Print the old and new length of each part. If the total comes out under the target in `VIDEO.md`, raise the short pad to +0.35s.
- **Sync:**
  - Every cut lands within **±0.1s of a word start**. Text cards, icons and pop-ups appear **exactly** on their word.
  - Before rendering, print the cut / word / time table and spot-check 5 random cuts.
  - Whisper may write numbers as digits ("seventy-five percent" → "75%"), so match trigger words to it either way.
- **SFX:** quiet, about −20 dB under the voice, at most about 1 every 3 seconds.
  - *pop* on icons, *click* on cards, *swoosh* on pop-ups, *ding* on swaps and reveals
  - They're in `assets/sfx/`; regenerate them with `tools/make-sfx.sh` if needed.
- **Music** (final join):
  - `music/track.mp3` at about **−24 dB**, with `sidechaincompress` ducking under the voice (threshold 0.02, ratio 8, attack 20ms, release 400ms).
  - 2s fade-in, 4s fade-out, then `loudnorm` to about −14 LUFS with no clipping.
  - If the music competes with the voice anywhere, lower it 3 dB.
  - If `music/` has no real audio file (missing, or under 50 KB), deliver the voice-only version and say so.
- **Joining the parts:** put 1.0s of silence and a held last frame between parts.

## 11. Check before every render

- [ ] No shot is over 4s (except the listed exceptions), and the average is about 3s.
- [ ] Every cut is on a word start, and cards, icons and pop-ups land on their word.
- [ ] Crops show a whole subject. There's no ghosting and no double exposure.
- [ ] Every `edit:` line in `VIDEO.md` is done, there are no slow full-shot zooms, and every move lands on its word.
- [ ] On-screen text is spelled exactly as in `VIDEO.md`, and labels are ≥ 56px.
- [ ] The narrator is never animated, and pop-up poses fit the line.
- [ ] The padded audio is used, the video length equals the audio length, and the audio is present.
- [ ] (Final) The music is soft and the voice is always clearly on top.

## 12. Narrator reference (for understanding the pictures)

The narrator is a tall, slim figure with a glowing peach **brain** for a head, two white oval eyes and **no mouth**. He wears a black hoodie, black pants and white sneakers with a red stripe. He shows emotion only through his eye shapes and his pose.

Side characters are classic stickmen with round white heads and flat-colored shirts.
