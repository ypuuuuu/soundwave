# audio.py
# This module provides convenience functions for reading and writing audio WAV files.

import wave
from os.path import exists


def samples2bytes(samples):
  """
  Converts a sequence of floats in the range [-1, 1] to a bytestring suitable for writing to a WAV file.
  """
  signal = bytearray()
  for s in samples:
    signal += wave.struct.pack('h', int(5000*s))
  return signal


def read_file(filename):
  """
  Reads in a WAV file and returns it as a list of samples
  """
  w = wave.open(filename, 'rb')
  nframes = w.getnframes()
  data = w.readframes(nframes)
  w.close()
  sound = wave.struct.unpack('%ih'%(2*nframes),data)
  sound = [sound[n]/5000 for n in range(0, len(sound),2)]
  return sound


def write_file(filename, samples, samplerate, overwrite=False):
  """
  Writes tones stores as samples to a WAV file.
  """
  if exists(filename) and not overwrite:
    response = input("This file " + filename + " already exists. Would you like to overwrite it? [y/N] ").strip().lower()
    if response != 'y' and response != 'yes':
      print("No file saved")
      return
    
  w = wave.open(filename, 'wb')
  # (number of channels, samplewidth in bytes, framerate, number of frames, compression type, compression name)
  w.setparams((1, 2, samplerate, len(samples), 'NONE', 'noncompressed'))
  signal = samples2bytes(samples)
  w.writeframes(signal)


def save(filename, samples, samplerate):
  """
  Alias function for write_file().
  """
  write_file(filename, samples, samplerate)
