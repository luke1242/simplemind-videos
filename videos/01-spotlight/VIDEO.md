# Video 1: "One of the Most Useful Lessons I Learned" (spotlight effect)

Published. This is the archived scene list. The pictures, icons and audio for it are in this folder. `make-specs.py` and `scenes/` are the specs the build used, kept as working examples of the spec format.


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
