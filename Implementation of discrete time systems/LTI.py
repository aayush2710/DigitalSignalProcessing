#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 22:22:06 2019

@author: aayush
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg
from math import ceil , floor
n=101
N = np.linspace(-(n//2) , n//2 , n)
zeropointer = n/2
#Signal = np.random.normal(0 , 2 , n)
Signal = 0.95**N*np.heaviside(N,0)

plt.plot(N , Signal)
plt.title("Signal")
plt.show()

#y[n] = x[-n]
def Inv(Signal):
    return Signal[::-1]

plt.plot(N , Inv(Signal))
plt.title("Inverted Signal")
plt.show()

#Generating even part
def Even(Signal):
    return (Inv(Signal) + Signal)/2


plt.plot(N , Even(Signal))
plt.title("Even")
plt.show()

#Generating odd part
def Odd(Signal):
    return (-Inv(Signal) + Signal)/2

plt.plot(N , Odd(Signal))
plt.title("Odd")
plt.show()


#Time delayed
def delay(A,d):
    k = A.size
    l = n+d
    return  np.linspace(-(n//2) , n//2 +d , l ) , np.append(np.zeros(d) , A) 

Delay = 0    
k = n+Delay
N1 , Delayed = delay(Signal , 30)
plt.plot(N1 , Delayed)
plt.title("Delayed")
plt.show()

def mas(signal , m):
    s = signal.size + m 
   
    y = np.zeros(s)
    for i in range(m):
        
        sig = delay(signal,i)[1]
       
        sig = np.pad(sig,(m-i,0),mode='constant',constant_values=0)
        
        y += sig
    
    y *= 1/(m+1)
    return y[m::]



M = mas(Signal , 10)
plt.plot(N , M , 'r')
plt.plot(N , Signal , 'blue')
plt.title("Moving Average System")
plt.show()        
        

def BackwardDifference(Signal):
    k = Signal
    k = k[1:] - k[:k.size-1]
        
    return k

plt.plot(N[1:] , BackwardDifference(Signal))
plt.title("BackwardDifference")
plt.show()   


def difference(Signal):
    k = Signal
    k = k[2:] -2*k[1:k.size-1] + k[:k.size-2]
    return k
    
plt.plot(N[2:] , difference(Signal))
plt.title("Difference")
plt.show()  

def squarer(Signal):
    k = Signal
    k = k**2
    return k
    
plt.plot(N , squarer(Signal))
plt.title("Squarer")
plt.show()  

def system(Signal):
    k = Signal
    k = k + k[::-1]
    return k
    
plt.plot(N - 2 , system(Signal))
plt.title("y[n] = x[n-2] + x[2-n]")
plt.show()  