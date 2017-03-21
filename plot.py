import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10, 1000)
y = x**2
plt.plot(x, y, 'r-')
plt.savefig('Plot.pdf')