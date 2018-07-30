from __future__ import division
import numpy as np
import math as m
import matplotlib.pyplot as plt

x = np.linspace(0,1,1000)
y1=[]
x1=np.array(x)
x=np.linspace(0,1,10)
x2=np.array(x)
y=np.exp(x1)
for x in x:
	z=1
	for i in range(1,6):
		z=z+x**i/m.factorial(i)
	y1.append(z)

plt.plot(x1,y)
plt.plot(x2,y1,'o')
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
# # # #Comment the following line
plt.savefig('../figs/3.eps')
plt.show()

