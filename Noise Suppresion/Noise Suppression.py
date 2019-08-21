import sounddevice as sd
from scipy.io.wavfile import read , write
import numpy as np

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

fs , myrecording = read("Original.wav")

#adding zeroes to beginning and end
myrecording  = myrecording.flatten()
FW = 10
s= [0 for x in range(FW)]
e= [3*fs for x in range(FW)]
Enhanced = np.insert(myrecording, s+e, [0 for x in range(2*FW)])


#applying function
def MovingAverageSystem(Enhanced):
    
   
    for i in range(FW, 3*fs+FW):
        Enhanced[i] = sum(Enhanced[i-FW:i+1])/(FW+1)
        l_Enhanced = np.array(Enhanced[FW:FW+3*fs])
    
    
 
    write('Enhanced_mean.wav', fs, l_Enhanced) 

   

def MovingMedianSystem(Enhanced):
    
   
    for i in range(FW, 3*fs+FW):
        Enhanced[i] = np.median(Enhanced[i-FW:i+FW+1])
        l_Enhanced = np.array(Enhanced[FW:FW+3*fs])

   
    write('Enhanced_median.wav', fs, l_Enhanced) 



  
MovingAverageSystem(Enhanced)  



