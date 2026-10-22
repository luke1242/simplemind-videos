# Brain Guy Psychology: Upload Playbook

This is how every new video is packaged: the title, thumbnail, description, tags and script shape. It's based on a breakdown of **PsychToons** (171K subscribers, +52% in 30 days, Oct 2026), the closest faceless psychology channel to ours.

Claude Code doesn't need this file to build a video. It's for writing scripts and preparing uploads.

---

## 1. Titles: the "Psychology of" franchise

Every title gives a **search term** and a **curiosity hook** at the same time. Pick one of these formulas:

| Formula | Example (theirs → ours) |
|---|---|
| **Psychology of [X] (And How to [fix / trick it])** | "Psychology of Discipline (And How to Trick Your Brain Into Craving It)" → 2.8M views |
| **Psychology of [X]: [Do Y] So [extreme] It [Feels Illegal / Is Almost Unfair / Makes People Nervous]** | "Psychology of Intelligence: Learn Anything So Fast It's Almost Unfair" → 2.9M |
| **Psychology of [X]: Why [surprising truth]** | "Psychology of Polymaths: Why Having Multiple Interests Is an Unfair Advantage" → 2.7M |
| **Psychology of People Who [relatable behavior]** | "Psychology of People Who Go Quiet When They're Hurt" → 2.4M (but it spiked once and died) |

**Rules:**
- Prefer **how-to topics people search every day** (discipline, procrastination, confidence, overthinking, learning). They keep getting views for months. Identity topics ("signs you are…") spike and die, or flop.
- **Avoid edgy titles** (swearing, "manipulate", "seduction"). They got mixed results and don't fit our brand.
- Keep the title under about 70 characters if possible, with the keyword in the first 4 words.

## 2. Thumbnails: one system, every time

**What PsychToons does (from their top 12 thumbnails):**
- **A 2–3 word ALL-CAPS hook** across the top in a heavy bold font: "LEARN ANYTHING", "DO IT ANYWAY", "BE SCARY CALM", "CHARISMA IS EASY", "YOU'RE ADDICTED".
  - **One word in red or yellow**, the rest white (on black) or black (on white).
  - The hook **never repeats the title**. It's an order, a promise or a "this is you" line.
- **One character, big and centered**, the same bald cartoon guy every time, holding **one symbolic prop** (a glowing green brain, octopus arms for "too many interests").
- **Only two background modes:** solid black (most hits) or plain white or cream.
- **Three elements at most:** the hook, the character and the prop, with lots of empty space. It reads instantly at phone size.
- The same character, font and layout on every video, so the channel is recognizable in the feed.

**Our version:**
- **The narrator is our character.** His glowing peach brain pops on black, which is a built-in advantage.
- **Layout:** the hook text across the top third. The narrator centered and big (about 60–70% of the height), from the waist up or full body, with **one prop that *is* the topic**.
- **Background:** solid near-black `#111111` for emotional or "dark truth" topics, and warm cream `#FAF7F0` for light, upbeat topics.
- **Hook text:**
  - 2–3 words, ALL CAPS, heavy font (Montserrat Black or Anton)
  - white on black or black on cream
  - **one word** in red `#D64545` or yellow `#F2C230`
  - numbers are great ("84% REGRET THIS")
- **His eyes carry the emotion** (worried, surprised, half-closed and annoyed), since he has no mouth.
- **Never:** busy scenes, multiple characters, small details, more than 3 words, or text that repeats the title.

**Thumbnail prompt template (Nano Banana, attach `reference/characters/narrator.png`):**

```
YouTube thumbnail, 16:9, 2K. Bold, minimal, high contrast. Clean thick black outlines, flat colors, comic style.
BACKGROUND: solid plain [near-black #111111 | warm cream #FAF7F0], nothing else.
CHARACTER: the narrator from the attached image, exactly the same design (glowing peach brain head, two white oval eyes, no mouth, black hoodie, white sneakers with a red stripe), BIG and centered, filling about 65% of the image height, [pose], eyes [emotion]. The brain glows softly.
PROP: [one simple object that represents the topic], large and easy to read.
TEXT: across the top, in huge heavy bold all-caps sans-serif letters: "[HOOK]". The word "[KEY WORD]" is [red #D64545 | yellow #F2C230], the other words are [white | black]. Nothing else written anywhere.
Lots of empty space. No other characters, no small details. Must be readable at phone size.
```

If the text comes out wrong, ask for the same image **with no text**, then add the hook in Canva (Montserrat Black, the same colors).

**Test it:** in YouTube Studio, use **Test & Compare** on 2–3 thumbnails (for example black vs cream, or two different hooks).

**Style test running (video 6, procrastination):** two thumbnails in a dark, drawn, semi-realistic style (like PsychToons' moodier ones, but original compositions) vs our comic narrator, with the same hook. Keep whichever style wins for the next videos.

## 3. Description template

```
[Video title]

[One paragraph: what the video breaks down, naming the researchers, years and journals. Then "Then [N] [steps/reasons/traps] …"]

[One warm line that speaks to the viewer, e.g. "If you've ever deleted a message three times, this one's for you."]

Which of the [N] [steps] do you need most? Tell me the number in the comments.

You were watching Brain Guy Psychology. I'll see you in the next one.

#psychology #selfimprovement #[topic] #[topic] #psychologyexplained #brainguypsychology

---

Research referenced:
- [Author(s) (Year)]: [what it found, in one line]
- …

---

Disclaimer: This video is for educational purposes only and is not professional psychological or medical advice. If you're struggling, please reach out to a licensed professional.
```

**Pinned comment:** "Which of the [N] [steps] do you need most? Drop the number 👇"

## 4. Tags

Use 12–20 tags: the exact title keyword first, then how-to variations, then the researchers' names, then the base tags.

**Base tags (every video):** psychology explained, psychology, self improvement, personal growth, personal development, psychology facts, mental health, brain guy psychology

From vidIQ, Oct 2026: "psychology explained" gets ~470K searches a month with **low competition (33)**. "Personal development" (345K) and "personal growth" (261K, rising) are also low competition.

## 5. Script shape (for writing new scripts)

1. **Hook (0:00–0:45):** a surprising study result that breaks a common belief, plus "by the end of this video you'll know…".
2. **Personal story:** first person, relatable and specific. This is **our edge** over lecture-style channels.
3. **The research:** 2–3 studies with real numbers (fact-checked against the papers).
4. **Why the brain does it:** 3–4 numbered reasons or traps.
5. **What to do:** 5 numbered steps, each with one concrete action.
6. **Emotional close:** "you were never broken"-style reassurance, then a call back to a related video.

- **Length:** aim for **12–14 minutes** after padding (about 1,750–1,900 raw words). Their hits run 13–16 minutes.
- **Numbered lists** make the "which number?" comment question work.

## 6. Topic queue (keyword-backed, Oct 2026)

| Topic idea | Keyword | Monthly searches | Competition |
|---|---|---|---|
| Psychology of Procrastination (And How to Trick Your Brain Out of It) | how to stop procrastinating | 204K (↑28%) | 54 |
| Psychology of Overthinking (video 7, in progress) | overthinking | 426K | 61 |
| Psychology of Confidence (low-competition angle: "How to Be Confident") | how to be confident | 96K | 39 |
| Psychology of Social Anxiety: Why Nobody's Watching You | how to overcome social anxiety | 38K (↑123%) | 48 |
| Psychology of Habits: How Long It Really Takes (ties into the 66-day video) | how to build discipline | 83K (↑35%) | 45 |
| Psychology of Learning: Remember Everything You Study | learn anything fast | 57K (↑137%) | 45 |

## 7. Posting rhythm

- **One long video a week,** plus **2–3 Shorts** cut from it. PsychToons posts no Shorts, so that lane is open.
- **Don't judge a video in its first 48 hours.** Their first big hit had 1,200 views after two weeks before it took off.
