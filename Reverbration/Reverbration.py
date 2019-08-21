#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:56:43 2019

@author: aayush
"""

import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

fs , myrecording = read("Input.wav")

#adding zeroes to beginning and end


#adding zeroes to beginning and end
x  = myrecording.flatten()

n = np.linspace(0,100,101)
h1 = 0.999**n
h2 = np.random.random(1000)/4

y1 = np.convolve(h1 , x , 'same')
y2 = np.convolve(h2 , x , 'same')
plt.plot(n,y1[fs:fs+101])
plt.show()

plt.plot(n,x[fs:fs+101])
plt.show()


plt.plot(n,y2[fs:fs+101])
plt.show()

plt.plot(n,x[fs:fs+101])
plt.show()

write("Reverbrated1.WAV" , fs , y1)
write("Reverbrated2.WAV" , fs , y2)