#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:23:39 2019

@author: aayush
"""

import numpy as np
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
  
# Read Images 
img = mpimg.imread('img12.png' ) 
plt.imshow(img) 
m,n = img.shape
def quantize(Array , N):
    a = np.min(Array)
    b = np.max(Array)
    print(a,b)
    m,n = Array.shape
    Array1 = np.zeros([m,n])
    
    Array1 = (np.around((((Array - a)/(b-a)) *(2**N - 1)))*((b-a) / (2**N - 1))) + a
            
    return Array1
# Output Images 



img1 = quantize(img , 2)
plt.imshow(img1) 