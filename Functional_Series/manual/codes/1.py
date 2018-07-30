from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3.0001,3.0001,1e-3)
y1=[]
for x1 in x:
	z=0
	for i in range(1,10):
		z=z+(i**3/3**i)*(x1**i)
	y1.append(z)
plt.plot(x,y1)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
# # # #Comment the following line
plt.savefig('../figs/1.eps')
plt.show()

