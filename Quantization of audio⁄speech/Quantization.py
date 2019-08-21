import numpy as np
import matplotlib.pyplot as plt
import math as mp
import sounddevice as sd
from scipy.io.wavfile import read , write

SR , Array = read("16bit.wav")

Array = myrecording.flatten()

def quantize(Array , N):
    a = np.min(Array)
    b = np.max(Array)
    print(a,b)
    m = Array.shape
    Array1 = np.zeros(m)
    Array1 = (np.around((((Array - a)/(b-a)) *(2**N - 1)))*((b-a) / (2**N - 1))) + a
            
    return Array1
Array1 = quantize(Array  , 4)
Array2 = quantize(Array , 3)
Array3 = quantize(Array , 2)

write('16bit.wav' , SR , Array)
write('4bit.wav' , SR , Array1)
write('3bit.wav' , SR , Array2)
write('2bit.wav' , SR , Array3)
write('4bitdiff.wav' , SR , Array1 - Array)
write('3bitdiff.wav' , SR , Array2 - Array)
write('2bitdiff.wav' , SR , Array3 - Array)
