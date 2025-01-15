import numpy as np
import matplotlib.pylab as plt

# 시그모이드 activation function numpy로 분해해
def sigmoid(x):
    return 1 / (1 + np.exp(-x))    

X = np.arange(-5.0, 5.0, 0.1) #X의 범위
Y = sigmoid(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1) #Y의 범위
plt.show()
