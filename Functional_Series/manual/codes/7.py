from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-1,1,1e-3)
x1=np.arange(-0.999,0.9999,1e-1)
f=np.arctan(x)
f1=[]
for x2 in x1:
	y=0
	for j in range(1,1000):
		y=y+((-1)**(j+1))*(x2**j/(2*j-1))
	f1.append(y)
plt.plot(x,f)
plt.plot(x1,f1,'o')
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.savefig('../figs/7.eps')
plt.show()

