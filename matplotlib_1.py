import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2.0*np.pi, 2.0*np.pi, 0.1*np.pi)   # start,stop,step
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y, marker='o', markerfacecolor='black', label="sinus")
plt.scatter(x, z, label="cosinus")

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sinus & Cosinus')
plt.legend()
plt.show()