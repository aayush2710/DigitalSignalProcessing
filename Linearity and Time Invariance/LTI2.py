#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:58:21 2019

@author: aayush
"""

import numpy as np
import matplotlib.pyplot as plt

N = np.linspace(-100 ,100 , 201)

x1 = 0.9**N * np.heaviside(N , 0)
x2 = np.sin(np.pi*N/20)

#y[n] = x[-n]
def Inv(Signal):
    return Signal[::-1]



#Generating even part
def Even(Signal):
    return (Inv(Signal) + Signal)/2



#Generating odd part
def Odd(Signal):
    return (-Inv(Signal) + Signal)/2




#Time delayed
def delay(A,d):
    k = A.size
    n=201
    l = n+d
    if d>=0:
        return  np.linspace(-(n//2) , n//2 +d , l ) , np.append(np.zeros(d) , A) 
    else:
        return  np.append(A[abs(d):] , np.zeros(abs(d) ))



def mas(m , signal):
    s = signal.size + m 
   
    y = np.zeros(s)
    for i in range(m):
        
        sig = delay(signal,i)[1]
       
        sig = np.pad(sig,(m-i,0),mode='constant',constant_values=0)
        
        y += sig
    
    y *= 1/(m+1)
    return y[m::]

      
        

def BackwardDifference(Signal):
    k = Signal
    k = k[1:] - k[:k.size-1]
    k = np.append(Signal[0] , k)
    return k

 


def difference(Signal):
    k = Signal
    k = k[2:] -2*k[1:k.size-1] + k[:k.size-2]
    k = np.append([Signal[0] , Signal[1] - 2*Signal[0]] , k)
    return k
    
 

def squarer(Signal):
    k = Signal
    k = k**2
    return k
    
def system(Signal):
    k = Signal
    k = k + k[::-1]
    return delay(k,-2)



    
L =  [Inv(x1) , Even(x1) , Odd(x1) , delay(x1,5)[1][:201] , mas(10 , x1) , BackwardDifference(x1) , difference(x1) , squarer(x1) , system(x1)]
L2 =  [Inv(x2) , Even(x2) , Odd(x2) , delay(x2,5)[1][:201] , mas(10 , x2) , BackwardDifference(x2) , difference(x2) , squarer(x2) , system(x2) ]
L3 =  [Inv(2*x1 + 3*x2) , Even(2*x1 + 3*x2) , Odd(2*x1 + 3*x2) , delay(2*x1 + 3*x2,5)[1][:201] , mas(10 , 2*x1 + 3*x2) , BackwardDifference(2*x1 + 3*x2) , difference(2*x1 + 3*x2) , squarer(2*x1 + 3*x2) , system(2*x1 + 3*x2)]
L4 = [Inv(delay(x1,-4)) , Even(delay(x1,-4)) , Odd(delay(x1,-4)) , delay(delay(x1,-4),5)[1][:201] , mas(10 , delay(x1,-4)) , BackwardDifference(delay(x1,-4)) , difference(delay(x1,-4)) , squarer(delay(x1,-4)) , system(delay(x1,-4))]
L5 = ["Inverter" , "EvenPart" , "OddPart" , "Delay" , "MovingAverageSystem" , "BackwardDifference" , "y[n] = x[n] − 2x[n − 1] + x[n − 2]" , "Square" , "y[n] = x[n − 2] + x[2 − n]"]

for i in range(len(L)):
    
    y1 = L[i]
    y2 = L2[i]
    y3 = L3[i]
    y4 = L4[i]
    print()
    print(L5[i])
    
    plt.plot(N,y3)
    plt.title("Output of 2*x1 + 3*x2")
    plt.show()
    plt.plot(N , 2*y1 + 3*y2)
    plt.title("2*y1 + 3*y2")
    plt.show()
    print()
    
    if np.array_equal(np.around(y3,4) , np.around(2*y1 + 3*y2 , 4)):
        print("Linear")
    else:
        print("Not Linear")
        
       
    plt.plot(N,y4)
    plt.title("Output for x[n+4]")
    plt.show()
    plt.plot(N,delay(y1,-4))
    plt.title("y[n+4]")
    plt.show()
    print()
    
    if np.array_equal(np.around(y4,4) , np.around(delay(y1,-4) , 4)):
            print("Time Invariant")
    