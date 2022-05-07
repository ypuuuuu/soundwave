# middlec.py
# This program creates a single SoundWave object that is middle C and saves it to a WAV file called middlec.wav

import soundwave

note = soundwave.SoundWave(0, 2, 1)

note.save("middlec.wav")
