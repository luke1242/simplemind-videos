import sys, json
from faster_whisper import WhisperModel
m = WhisperModel("small.en", device="cpu", compute_type="int8")
src, out = sys.argv[1], sys.argv[2]
import wave, numpy as np
w=wave.open(src); a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
segs, info = m.transcribe(a, word_timestamps=True, language="en")
words=[]
for s in segs:
    for w in s.words: words.append({"w":w.word.strip(),"s":round(w.start,3),"e":round(w.end,3)})
json.dump({"duration":info.duration,"words":words}, open(out,"w"), indent=0)
print(len(words), info.duration)
