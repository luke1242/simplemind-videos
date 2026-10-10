#!/usr/bin/env python3
"""Writes scenes/partN.json (v2 beat specs: icons, cards, narrator pop-ups, overlays) and scenes/foci.json."""
import json
def icon(word, ic, occ=1, dur=1.8): return {"kind":"icon","icon":ic,"word":word,"occ":occ,"dur":dur}
def card(word, parts, occ=1, dur=1.8, back=0.0): return {"kind":"card","parts":[{"t":p[0],**({"badge":p[1]} if len(p)>1 else {})} for p in parts],"word":word,"occ":occ,"dur":dur,"back":back}
def pop(word, pose, content, occ=1, dur=3.0):
    c = {"type":"icon","icon":content} if isinstance(content,str) else {"type":"card","parts":[{"t":p[0],**({"badge":p[1]} if len(p)>1 else {})} for p in content]}
    return {"kind":"pop","pose":pose,"content":c,"word":word,"occ":occ,"dur":dur}
def title(): return {"kind":"title","dur":2.5}
def sc(id, narr, picture=None, camera="zoom-in", ev=None, **kw):
    d = {"id":id,"camera":camera,"narration":narr,"events":ev or []}
    if picture: d["picture"]=picture
    d.update(kw); return d
Y,R="yellow","red"
P1=[
 sc("S01","For a long time, there was one thought that stopped me from doing almost everything. Going to the gym. Raising my hand in class. Trying out for something. Posting anything online.","S01",ev=[icon("posting","I05")]),
 sc("S02","Everyone's going to be watching.","S02",transition="cut"),
 sc("S03","That's what it felt like. Every single time. Like I was standing alone on a giant stage, with one bright spotlight on me, and thousands of eyes in the dark.","S03","zoom-out",ev=[icon("eyes","I06",dur=1.6)]),
 sc("S04","Then I learned about one experiment, involving a really embarrassing T-shirt.","S04",ev=[icon("learned","I09",dur=1.6),icon("shirt","I08",dur=1.6)]),
 sc("S05","And it changed how I see almost everything. By the end of this video, you'll know exactly how wrong our brains are about this, by how much, and the one question I now ask myself that shuts that thought down in about three seconds.","S05","hold",ev=[card("question",[("THE",),("3-SECOND",Y),("QUESTION",)],dur=1.5),icon("three","I11",dur=1.5),title()]),
 sc("S06","So here's how it used to go for me. I'd walk into a room, and I'd feel like there was a spotlight following me.","S06","pan-right",ev=[pop("spotlight","N03","I07",dur=3.0)]),
 sc("S07","If I tripped, everyone saw it. If my outfit was a little off, everyone noticed. If I said something dumb, I was sure everyone would remember it for weeks.","S07",ev=[icon("tripped","I12"),icon("weeks","I13",dur=1.6)]),
 sc("S08","And then I'd replay it in my head that night. Over and over. Like a highlight reel of every awkward thing I'd ever done.","S08",ev=[icon("night","I14",dur=1.6),pop("highlight","N10","I15",dur=3.0)]),
 sc("S09","If you've ever done that, lying in bed at night, thinking about something awkward from three years ago. You're not weird. You're not broken.","S08","zoom-out",pictureB="S08b",swap={"word":"weird"},continues=True),
 sc("S10","Your brain is doing something almost everyone's brain does. And it even has a name. Psychologists call it the spotlight effect. It's the feeling that people are noticing you, and judging you, way more than they actually are. And once you understand how strong it is, it's hard to see things the same way again.","S10","hold",
    ev=[card("name",[("IT HAS A",),("NAME",Y)],dur=1.5),pop("feeling","N02","I06",dur=3.2)],
    overlays=[{"type":"board","text":["THE","SPOTLIGHT","EFFECT"],"word":"spotlight","occ":1,"box":{"x":0.50,"y":0.12,"w":0.42,"h":0.43}}]),
]
P2=[
 sc("S11","So here's the experiment. Around the year two thousand, a psychologist named Thomas Gilovich and his team at Cornell University ran a study with college students.","S11","pan-right",ev=[pop("so","N01",[("THE",),("EXPERIMENT",Y)],dur=3.0),icon("cornell","I16")],
    overlays=[{"type":"label","text":"Cornell University, ~2000","word":"cornell"}]),
 sc("S12","They had one student put on a T-shirt with a big, cheesy picture of a singer on it. One that college students at the time would find really embarrassing to be seen in.","S12",ev=[icon("shirt","I08"),card("really",[("REALLY",),("EMBARRASSING",R)],dur=1.6)]),
 sc("S13","Then that student walked into a room full of other students, stayed for a moment, and walked back out.","S13","pan-left"),
 sc("S14","Afterward, the researchers asked the student in the T-shirt one simple question. How many people in that room do you think noticed your shirt?","S14",ev=[pop("simple","N06","I17",dur=3.0)]),
 sc("S15","On average, they guessed about half.",None,"hold",diagram={"kind":"pie","pct":50,"label":"THEIR GUESS:","badge":Y,"value":"50%"},
    foci=[[0.5,0.42,1.3],[0.5,0.82,1.3]]),
 sc("S16","The real number? Only about a quarter.",None,"zoom-in",diagram={"kind":"pie","pct":50,"label":"THEIR GUESS:","badge":Y,"value":"50%"},
    diagramB={"kind":"pie","pct":25,"label":"REALITY:","badge":R,"value":"25%"},swap={"word":"quarter"},continues=True,
    foci=[[0.5,0.42,1.3],[0.5,0.82,1.3]]),
 sc("S17","They thought twice as many people noticed as actually did. And remember, that was a shirt picked specifically to be embarrassing. Something designed to get noticed.","S17","zoom-out",ev=[pop("twice","N09",[("TWICE",Y),("AS MANY",)],dur=3.0)]),
 sc("S18","Now think about the little things you worry about every day. A bad hair day. A pimple. Saying you too when the waiter says enjoy your meal.","S18"),
 sc("S19","If people barely noticed a ridiculous T-shirt, they're definitely not tracking those.","S17",ev=[icon("barely","I18")]),
 sc("S20","So why does this happen? It's actually pretty simple. You are the main character of your own life. You see everything from inside your own head, so you're thinking about yourself all day long. And your brain quietly assumes everyone else is thinking about you too.","S20",
    ev=[icon("main","I19"),pop("inside","N06",[("INSIDE YOUR",),("OWN HEAD",Y)],dur=3.0)]),
 sc("S21","But here's the thing. Everyone else is the main character of their own life too.","S21","zoom-out"),
 sc("S22","That guy you think is judging your workout? He's worried about his own form.","S22",ev=[icon("workout","I20")]),
 sc("S23","That girl you think noticed you stumble over your words? She's busy replaying something she said.","S23","pan-right"),
 sc("S24","Everyone is walking around in their own little spotlight, so busy worrying about it that they barely notice yours.","S21",ev=[card("own",[("THEIR OWN",),("SPOTLIGHT",Y)],dur=1.6),icon("barely","I18")]),
 sc("S25","And it's not just about how you look. Gilovich and his team found something similar with nerves. When people gave a speech, they thought their nervousness was way more obvious than it really was. The audience mostly couldn't tell.","S25",ev=[pop("speech","N10","I21",dur=3.0)]),
 sc("S26","They called it the illusion of transparency. It's that feeling that everyone can see right through you. They can't. The shaking you feel on the inside? From the outside? It mostly just looks like a normal person talking.","S26",ev=[icon("transparency","I22")],
    overlays=[{"type":"pill","text":"SEEMS FINE","word":"can't"}]),
]
P3=[
 sc("S27","Okay. But what about when people do notice? What if you really do mess up, and someone sees it?","S27",ev=[pop("but","N06",[("WHAT IF PEOPLE",),("DO NOTICE?",Y)],dur=3.0),icon("mess","I23")]),
 sc("S28","This is where it gets even better. Researchers tested this too. They had people imagine, or actually go through, embarrassing moments, like messing up in front of others. Then they compared how harshly people thought they'd be judged, with how harshly they actually were judged.",None,"hold",
    diagram={"kind":"scale"},foci=[[0.25,0.62,1.35],[0.75,0.5,1.35]],
    overlays=[{"type":"badge","badge":R,"text":"EXPECTED","word":"thought","box":{"x":0.115,"y":0.72,"w":0.26,"h":0.14}},
              {"type":"badge","badge":Y,"text":"REALITY","word":"actually","occ":2,"box":{"x":0.625,"y":0.53,"w":0.26,"h":0.14}}]),
 sc("S29","Over and over, people expected to be judged way more harshly than they really were.",None,"zoom-in",diagram={"kind":"scale","labels":True},continues=True,zoomTo=1.12,camOrigin="75% 45%",
    foci=[[0.25,0.62,1.35],[0.75,0.5,1.35]]),
 sc("S30","Because when other people see you mess up, they don't just see the mistake. They see the whole situation. They know you were nervous. They know it was a hard moment. They've been there too.","S30","zoom-out",ev=[pop("been","N07",[("THEY'VE BEEN",),("THERE TOO",Y)],dur=3.0)]),
 sc("S31","You're judging yourself with a magnifying glass. They're looking at you from across the room, with a lot more kindness than you'd expect.","S31","hold",pictureB="S31b",swap={"word":"kindness"},ev=[icon("magnifying","I25"),icon("kindness","I24")]),
 sc("S32","And here's one that honestly surprised me. It's called the liking gap.","S32",ev=[icon("liking","I26")]),
 sc("S33","Researchers paired up strangers and had them talk for a few minutes. Afterward, they asked each person two things. How much did you like the other person? And how much do you think they liked you?","S33","zoom-out"),
 sc("S34","People consistently underestimated how much the other person liked them. You walk away from a conversation thinking, that was so awkward, they probably think I'm weird. And the other person walks away thinking, that was nice. I liked them.","S34","hold",
    ev=[card("underestimated",[("UNDER-",),("ESTIMATED",R)],dur=1.5,back=0.1),icon("awkward","I27"),pop("nice","N07","I27",dur=3.0)]),
 sc("S35","And there's one more. Researchers call it the beautiful mess effect.","S35",ev=[card("beautiful",[("THE BEAUTIFUL",),("MESS EFFECT",Y)],dur=1.6,back=0.2)]),
 sc("S36","When people imagined themselves showing vulnerability, like admitting a mistake, asking for help, or saying how they really feel, they saw it as weak and embarrassing. But when they imagined someone else doing the exact same thing, they saw it as brave.","S36",ev=[pop("same","N07",[("SEEN AS",),("BRAVE",Y)],dur=3.0)]),
 sc("S37","Same action. Completely different story. The thing that feels like weakness to you, often looks like courage to everyone else.","S35","zoom-out",pictureB="S35b",swap={"word":"courage"}),
 sc("S38","When I finally understood all of this, I started thinking about everything I didn't do. The team I didn't try out for. The question I didn't ask. The thing I wanted to post, but deleted. The person I wanted to talk to, but didn't.","S38",ev=[pop("finally","N06","I09",dur=2.8)],
    overlays=[{"type":"bubble","icon":"sheet","word":"team","box":{"x":0.105,"y":0.122,"w":0.11,"h":0.195}},
              {"type":"bubble","icon":"hand","word":"question","box":{"x":0.225,"y":0.022,"w":0.11,"h":0.195}},
              {"type":"bubble","icon":"phone","word":"post","box":{"x":0.485,"y":0.03,"w":0.11,"h":0.195}},
              {"type":"bubble","icon":"wave","word":"person","box":{"x":0.625,"y":0.032,"w":0.11,"h":0.195}}]),
 sc("S39","None of it was because I couldn't do it. It was because of an audience that, mostly, wasn't even watching. And the few who were, would have been a lot kinder than I imagined.","S39","zoom-out",ev=[icon("wasn't","I29")]),
 sc("S40","That's what the spotlight effect really costs you. Not embarrassment. Missed chances.","S40",ev=[icon("really","I30",dur=2.0)],
    overlays=[{"type":"board","text":["MISSED","CHANCES"],"color":"#D64545","bg":"#FAF3E3","word":"missed","box":{"x":0.24,"y":0.56,"w":0.52,"h":0.32}}]),
]
P4=[
 sc("S41","So here's how I actually use this now.",None,"hold",diagram={"kind":"card","parts":[{"t":"HOW I USE"},{"t":"THIS","badge":Y}]}),
 sc("S42","One. Ask the three-second question. This is the one I promised you. When that everyone's watching thought shows up, I ask myself: Would I remember this, if someone else did it?","S42","hold",ev=[icon("three","I11"),pop("would","N06",[("WOULD I",),("REMEMBER THIS?",Y)],dur=3.0)],
    overlays=[{"type":"step","step":"STEP 1","text":"WOULD I REMEMBER THIS?","word":"ask"}]),
 sc("S43","If someone tripped at the gym, would you think about it tomorrow? Probably not. You'd forget in about five seconds. That's exactly how much they'll think about you.","S43","zoom-out",ev=[icon("tripped","I12"),card("five",[("FIVE",Y),("SECONDS",)],dur=1.4,back=0.1)]),
 sc("S44","Two. Cut the number in half. However many people you think will notice, cut it in half. That's literally what the T-shirt study found. Your brain overestimates by about double.",None,"hold",
    diagram={"kind":"stepPie","step":"STEP 2","title":"CUT IT IN HALF","pct":50,"badge":Y,"value":"50%"},
    diagramB={"kind":"stepPie","step":"STEP 2","title":"CUT IT IN HALF","pct":25,"badge":R,"value":"25%"},swap={"word":"half"},
    foci=[[0.33,0.65,1.35],[0.78,0.65,1.35],[0.5,0.2,1.3]],ev=[icon("cut","I31"),pop("literally","N02",[("THE T-SHIRT",),("STUDY",Y)],dur=3.0)]),
 sc("S45","Three. Remember, everyone has their own spotlight. Picture the room. Everyone in it is worried about themselves. You're not on a stage. You're in a crowd of people who all think they're on a stage.","S21","zoom-in",ev=[card("stage",[("YOU'RE NOT",),("ON A STAGE",R)],dur=1.6,back=0.5)],
    overlays=[{"type":"step","step":"STEP 3","text":"EVERYONE HAS A SPOTLIGHT","word":"three"}]),
 sc("S46","Four. Assume people are kinder than your brain says. If you do mess up, the people who saw it are probably thinking about it far less, and far more kindly, than you are. And after a conversation, assume they liked you more than you think. The research says they probably did.","S30","zoom-in",
    ev=[icon("kinder","I24"),card("kindly",[("FAR MORE",),("KINDLY",Y)],dur=1.5,back=0.3),pop("liked","N07",[("THEY LIKED",),("YOU MORE",Y)],dur=3.0)],
    overlays=[{"type":"step","step":"STEP 4","text":"PEOPLE ARE KINDER","word":"four"}]),
 sc("S47","Five. Do it anyway, and watch what happens. Next time, do the thing you're nervous about. Then pay attention to how people actually react. Almost every time, it's way less than you expected.","S47","zoom-in",ev=[card("way",[("WAY LESS",Y),("THAN EXPECTED",)],dur=1.5,back=0.2)],
    overlays=[{"type":"step","step":"STEP 5","text":"DO IT ANYWAY","word":"five"}]),
 sc("S48","And every time you see that for yourself, the spotlight gets a little dimmer.","S48","hold",pictureB="S48b",swap={"word":"dimmer"}),
 sc("S49","So here's the lesson. People aren't watching you nearly as much as you think. And that's not sad. That's freedom.","S49","zoom-out",ev=[pop("so","N11",[("THE",),("LESSON",Y)],dur=2.5),card("freedom",[("THAT'S",),("FREEDOM",Y)],dur=1.8,back=0.4)]),
 sc("S50","It means you can try. You can mess up. You can look a little dumb while you get better. You can ask the question. Post the video. Walk into the gym. Talk to the person.","S50","zoom-out"),
 sc("S51","Because the only one keeping score that closely, is you. So go do the thing. Hardly anyone's watching.","S51","zoom-in",pictureB="S51b",swap={"word":"hardly"}),
 sc("S52","And if you want to actually make that thing a habit, the sixty-six-day video breaks down exactly how long that really takes.","S52","hold",ev=[pop("sixty","N12","I13",dur=3.0)],holdEnd=True),
]
for n,sc_ in ((1,P1),(2,P2),(3,P3),(4,P4)):
    json.dump({"part":n,"audio":f"audio/padded/part{n}.wav","scenes":sc_}, open(f"scenes/part{n}.json","w"), indent=1)
FOCI = {
"S01":[[.37,.36,1.3],[.72,.55,1.3]],"S02":[[.5,.33,1.3],[.55,.42,1.2]],"S03":[[.3,.5,1.35],[.75,.8,1.3]],"S04":[[.33,.45,1.35],[.75,.8,1.3]],
"S05":[[.5,.3,1.35]],"S06":[[.5,.36,1.3],[.3,.45,1.35]],"S07":[[.4,.5,1.25],[.22,.45,1.35]],"S08":[[.62,.385,1.3]],"S08b":[[.5,.72,1.3]],"S10":[[.58,.38,1.2]],
"S11":[[.35,.3,1.3],[.5,.72,1.3]],"S12":[[.5,.38,1.3]],"S13":[[.22,.45,1.3],[.65,.5,1.3]],"S14":[[.5,.45,1.25],[.3,.5,1.35],[.7,.5,1.35]],
"S17":[[.5,.42,1.3]],"S18":[[.3,.4,1.3],[.78,.5,1.35]],"S20":[[.5,.55,1.25],[.5,.3,1.35]],"S21":[[.5,.4,1.3],[.2,.5,1.35],[.8,.55,1.35]],
"S22":[[.45,.45,1.25],[.82,.55,1.35]],"S23":[[.62,.42,1.25],[.2,.5,1.35]],"S25":[[.32,.42,1.3],[.75,.7,1.35]],"S26":[[.35,.42,1.3],[.7,.7,1.35]],
"S27":[[.5,.5,1.2],[.18,.5,1.35],[.82,.5,1.35]],"S30":[[.45,.5,1.3],[.7,.45,1.35]],"S31":[[.3,.45,1.3],[.85,.55,1.35]],"S31b":[[.3,.5,1.3],[.8,.8,1.35]],
"S32":[[.52,.45,1.3]],"S33":[[.6,.45,1.3],[.15,.5,1.35]],"S34":[[.2,.38,1.3],[.82,.45,1.35]],"S35":[[.5,.45,1.3]],"S35b":[[.5,.45,1.3]],"S36":[[.45,.45,1.3]],
"S38":[[.66,.55,1.3]],"S39":[[.5,.55,1.35]],"S40":[[.5,.5,1.2]],"S42":[[.3,.35,1.3],[.7,.35,1.35]],"S43":[[.5,.35,1.3]],"S47":[[.38,.45,1.3],[.75,.45,1.3]],
"S48":[[.45,.55,1.3]],"S48b":[[.45,.55,1.3]],"S49":[[.45,.5,1.3],[.78,.5,1.35]],"S50":[[.3,.45,1.35]],"S51":[[.5,.4,1.2]],"S51b":[[.5,.4,1.2]],"S52":[[.78,.4,1.3]]}
json.dump(FOCI, open("scenes/foci.json","w"))
print("specs written")
