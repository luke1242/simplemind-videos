import sys, json, re
from faster_whisper import WhisperModel
m = WhisperModel("small.en", device="cpu", compute_type="int8")
src, out = sys.argv[1], sys.argv[2]
import subprocess, numpy as np
a = np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",src,"-f","f32le","-ac","1","-ar","16000","-"],capture_output=True,check=True).stdout, dtype=np.float32)  # whisper wants 16 kHz mono
segs, info = m.transcribe(a, word_timestamps=True, language="en", beam_size=5, condition_on_previous_text=False)
ONES="zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS="","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"
def card(n):
    if n < 20: return ONES[n]
    if n < 100: return TENS[n//10] + ("" if n % 10 == 0 else " " + ONES[n%10])
    if n < 1000: return ONES[n//100] + " hundred" + ("" if n % 100 == 0 else " " + card(n%100))
    return card(n//1000) + " thousand" + ("" if n % 1000 == 0 else " " + card(n%1000))
def year(n):
    if 2000 <= n <= 2099: return card(n)
    a, b = divmod(n, 100)
    return card(a) + (" hundred" if b == 0 else " " + ("oh " + ONES[b] if b < 10 else card(b)))
def spell(tok):
    t = tok.strip(); mm = re.fullmatch(r"\$?([\d,]+)(%|s)?([.,!?\"]*)", t)
    if not mm: return t
    n = int(mm.group(1).replace(",", "")); suf = mm.group(2)
    s = year(n) if 1100 <= n <= 2099 and suf != "%" else card(n)
    if suf == "s": s = s[:-1] + "ies" if s.endswith("y") else s + "s"
    if suf == "%": s += " percent"
    return s + mm.group(3)
words=[]
for s in segs:
    for w in s.words:
        sp = spell(w.word).split(); n = len(sp); d = (w.end - w.start) / n
        for i, p in enumerate(sp): words.append({"w":p,"s":round(w.start + i*d,3),"e":round(w.start + (i+1)*d,3)})
# whisper sometimes gives a word zero length and the word before it a too-long one: spread them over the same span
i = 1
while i < len(words) - 1:
    if words[i]["e"] - words[i]["s"] < 0.04 and words[i-1]["e"] - words[i-1]["s"] > 0.4:
        j = i + 1 if (words[i+1]["e"] - words[i+1]["s"] < 0.25 and words[i+1]["s"] - words[i]["e"] < 0.05) else i
        grp = words[i-1:j+1]; t0, t1 = grp[0]["s"], grp[-1]["e"]; ln = [max(1, len(re.sub(r"[^a-z0-9]", "", g["w"].lower()))) for g in grp]; tot = sum(ln); c = t0
        for g, l in zip(grp, ln): g["s"] = round(c, 3); c += (t1 - t0) * l / tot; g["e"] = round(c, 3)
        i = j + 1
    else: i += 1
json.dump({"duration":info.duration,"words":words}, open(out,"w"), indent=0)
print(len(words), info.duration)
