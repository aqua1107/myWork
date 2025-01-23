import numpy as np
import matplotlib.pyplot as plt

x_i = np.arange(10)
softmax = np.exp(x_i)/np.sum(np.exp(x_i))

plt.plot(softmax)
plt.xlim(0, 9)
plt.ylim(0, 1.0)
plt.show()