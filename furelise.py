# furelise.py
# This program creates SoundWave objects for the song Fur Elise by Beethoven, saved as furelise.wav. This tests whether the extend() function in the SoundWave class is working.

import soundwave


dur = 0.3

song = soundwave.SoundWave()
a = soundwave.SoundWave(9, dur)
b = soundwave.SoundWave(11, dur)
c = soundwave.SoundWave(12, dur)
d = soundwave.SoundWave(14, dur)
ds = soundwave.SoundWave(15, dur)
e = soundwave.SoundWave(16, dur)

song.extend(e)
song.extend(ds)
song.extend(e)
song.extend(ds)
song.extend(e)
song.extend(b)
song.extend(d)
song.extend(c)
song.extend(a)
song.extend(a)
song.extend(a)

song.save("furelise.wav")
