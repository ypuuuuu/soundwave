# surprise.py
# This program creates SoundWave objects for a song that is saved as surprise.wav. This tests whether the plus function in the SoundWave class is working.

import soundwave


dur = 0.3
    
song = soundwave.SoundWave()
c53  = soundwave.SoundWave(0, 3*dur)
db53 = soundwave.SoundWave(1, 3*dur)
eb52 = soundwave.SoundWave(3, 2*dur)
eb53 = soundwave.SoundWave(3, 3*dur)
f53  = soundwave.SoundWave(5, 3*dur)
gb52 = soundwave.SoundWave(6, 2*dur)
gb53 = soundwave.SoundWave(6, 3*dur)
ab52 = soundwave.SoundWave(8, 2*dur)
ab53 = soundwave.SoundWave(8, 3*dur)
bb63 = soundwave.SoundWave(10, 3*dur)
c63  = soundwave.SoundWave(12, 3*dur)
db63 = soundwave.SoundWave(13, 3*dur)
eb63 = soundwave.SoundWave(15, 3*dur)
f63  = soundwave.SoundWave(17, 3*dur)
f61  = soundwave.SoundWave(17, 1*dur)
gb6h = soundwave.SoundWave(18, dur/2)
ab6h = soundwave.SoundWave(20, dur/2)

ch1 = db53 + gb53 + bb63 + db63
ch2 = eb53 + ab53 + c63 + eb63
ch3 = eb52 + gb52 + ab52
ch4 = c53 + f53 + ab53 + c63 + eb63
ch5 = f53 + bb63 + db63 + f63
ch6 = db53 + gb53 + bb63 + db63
ch7 = c53 + eb53 + gb53 + ab53

song.extend(ch1)
song.extend(ch2)
song.extend(ch3)
song.extend(ch4)
song.extend(ch5)
song.extend(ab6h)
song.extend(gb6h)
song.extend(f61)
song.extend(ch6)
song.extend(ch2)
song.extend(ch7)

song.save("surprise.wav")
