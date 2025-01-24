import numpy as np
import matplotlib.pyplot as plt

xlims = (-5,5)
ylims = (-2,2)
dx = 0.01
x = np.arange(*xlims, dx)
wave   = np.sin(10*x)
packet = np.exp(-x**2)
y = wave*packet 
plt.plot(x,y,'r')
plt.grid(True)
plt.xlim(*xlims)
plt.ylim(*ylims)
plt.show()