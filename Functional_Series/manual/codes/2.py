import numpy as np
import matplotlib.pyplot as plt

n=1e5
x = np.arange(0,1,1e-3) #for some x less than 1 can be changed.
fx=(x-1/n)**2
 	
plt.plot(x,fx)
plt.grid()
plt.xlabel('$n$')
plt.ylabel('$f_n$')
# # # #Comment the following line
plt.savefig('../figs/2.eps')
plt.show()

