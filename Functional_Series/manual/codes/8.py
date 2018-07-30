from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

k=np.pi
t = np.arange(0,2*np.pi,1e-3)
x=4*(t-np.sin(t))
y=4*(1-np.cos(t))
b=[]
plt.plot(x,y)
plt.grid()
# # # #Comment the following line
plt.savefig('../figs/8.eps')
plt.show()

