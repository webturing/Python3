import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(0, 10*math.pi, 501)
print(x)
plt.plot(x, np.cos(x))
plt.show()
plt.plot(x, np.sin(x))
plt.show()
plt.plot(x, np.tan(x))
plt.show()
