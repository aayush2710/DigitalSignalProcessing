import numpy as np
import matplotlib.pyplot as plt

Samples = 100
fs = 8


def plot(fs, Samples):
    N = np.linspace(-Samples, Samples, 2*Samples)
    N = np.array(N)

    Y1 = np.sin(2 * (np.pi / fs) * N)
    Y2 = np.sin(4 * (np.pi / fs) * N)

    Y3 = np.sin(6 * (np.pi / fs) * N)

    Y4 = np.sin(7 * (np.pi / fs) * N)
    Y5 = np.sin(8 * (np.pi / fs) * N)
    Y6 = np.sin(10 * (np.pi / fs) * N)
    Y7 = np.sin(12 * (np.pi / fs) * N)
    Y8 = np.sin(14 * (np.pi / fs) * N)

 
    plt.plot(N, Y1)
    plt.show()
  
    plt.plot(N, Y2)
    plt.show()
 
    plt.plot(N, Y3)
    plt.show()
   
    plt.plot(N, Y4)
    plt.show()
 
    plt.plot(N, Y5)
    plt.show()
   
    plt.plot(N, Y6)
    plt.show()
 
    plt.plot(N, Y7)
    plt.show()
 
    plt.plot(N, Y8)
    plt.show()


plot(8, 10)
plot(80, 100)
