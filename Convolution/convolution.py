#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:38:46 2019

@author: aayush
"""

import numpy as np
import matplotlib.pyplot as plt
n=201
N = np.linspace(-100 ,100 , 201)
ZeroImpulse = np.zeros(201)
ZeroImpulse[100] = 1
x = 0.95**N*np.heaviside(N,0)
def delay(A,d):
    k = A.size
    l = n+d
    return  np.linspace(-(n//2) , n//2 +d , l ) , np.append(np.zeros(d) , A) 



def mas(Signal , M):
    
    k = np.zeros(n+M)
   
    for i in range(M+1):
       
     
        k=k+ np.append(np.zeros(M - i) , delay(Signal , i)[1])
        
    return k[10:]/(M+1)

h = mas(ZeroImpulse , 10)
y1 = mas(x , 10)
y2 = np.convolve(h,x , 'same')

plt.plot(N , y1)
plt.title("direct result (Moving Average System)")
plt.show()

plt.plot(N , y2)
plt.title("convolution result (Moving Average System)")
plt.show()

def BackwardDifference(Signal):
    k = Signal
    k = k[1:] - k[:k.size-1]

    return k

 



    
h = BackwardDifference(ZeroImpulse)
y1 = BackwardDifference(x)
y2 = np.convolve(h,x[1:] , 'same')

plt.plot(N[1:] , y1)
plt.title("direct result (Backward Difference)")
plt.show()

plt.plot(N[1:] , y2)
plt.title("convolution result (Backward Difference)")
plt.show()



def difference(Signal):
    k = Signal
    k = k[2:] -2*k[1:k.size-1] + k[:k.size-2]
  
    return k
    
h = difference(ZeroImpulse)
y1 = difference(x)
y2 = np.convolve(h,x[2:] , 'same')

plt.plot(N[2:] , y1)
plt.title("direct result (Backward Difference)")
plt.show()

plt.plot(N[2:] , y2)
plt.title("convolution result (Backward Difference)")
plt.show()
