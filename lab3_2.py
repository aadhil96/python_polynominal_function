import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-10,10,num=100)

fx = []
for i in range(len(x)):
	fx.append(x[i]**4 - 3*x[i]**3 - 35*x[i]**2+39*x[i]+70)


plt.plot(x,fx)
plt.grid()
plt.axvline()
plt.axhline()
plt.show()


