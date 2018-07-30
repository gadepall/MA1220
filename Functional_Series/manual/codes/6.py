from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-1,1,1e-3)
x1=np.arange(-1,1,1e-1)
f=1/(1+x**2)
f1=[]
for x2 in x1:
	y=0
	for j in range(0,100):
		y=y+((-1)**j)*(x2**(2*j))
	f1.append(y)
plt.plot(x,f)
plt.plot(x1,f1,'o')
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.savefig('../figs/6.eps')
plt.show()

