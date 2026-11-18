"""Estimate the beat period from microphone PCM or a WAV recording."""
import wave
from serve import page
INTERVAL=2
def detect(samples,rate):
    import numpy as np
    hop=max(1,round(rate/100));n=len(samples)//hop
    if n<350:return None
    audio=np.asarray(samples[:n*hop],dtype=float).reshape(n,hop)
    energy=np.sqrt(np.mean(audio*audio,axis=1))
    onset=np.maximum(0,np.diff(energy,prepend=energy[0]))
    if onset.max()<0.0005 or np.count_nonzero(onset>onset.max()*.15)<3:return None
    onset=np.maximum(0,onset-np.mean(onset));periods=range(30,101)
    scores=[np.dot(onset[k:],onset[:-k])/(len(onset)-k) for k in periods]
    peak=max(scores)
    if peak<=0:return None
    local=[(s,k) for i,(s,k) in enumerate(zip(scores,periods)) if s>=.86*peak and s>=scores[max(0,i-1)] and s>=scores[min(i+1,len(scores)-1)]]
    if not local:return None
    lag=min(k for s,k in local)
    return round(60*rate/(hop*lag))
def snapshot(o,m):
    import numpy as np
    if o.get("wav"):
        with wave.open(o["wav"],"rb") as w:
            if w.getsampwidth()!=2:raise ValueError("Choose 16-bit PCM WAV")
            rate=w.getframerate();raw=w.readframes(rate*8);samples=np.frombuffer(raw,"<i2").reshape(-1,w.getnchannels()).mean(axis=1)/32768
    else:
        import sounddevice as sd
        rate=int(o.get("sample_rate",22050));samples=sd.rec(rate*6,samplerate=rate,channels=1,device=o.get("device"),dtype="float32",blocking=True).ravel()
    bpm=detect(samples,rate)
    return dict(state="Audio onset estimate",key=str(bpm),pages=[page("SONG TEMPO",f"{bpm} BPM" if bpm else "Listening","Microphone" if not o.get("wav") else "WAV recording","6-second mic window","Range 60-200 BPM")])
