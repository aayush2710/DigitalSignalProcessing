from scipy.io.wavfile import *
import pyaudio

SamplingRate, Arr = read("Audio1.wav")
print(Arr)
dsr = 8

write("Audio2.wav" , int(SamplingRate/dsr) , Arr[0::dsr])