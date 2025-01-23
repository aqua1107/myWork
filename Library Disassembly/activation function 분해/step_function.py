import numpy as np
import matplotlib.pylab as plt

# 계단함수(step function)분해
def step_function(x):
    return np.array(x > 0, dtype=np.float32) # 실수형으으로 시각화

X = np.arange(-5.0, 5.0, 0.1) # x축의 범위 지정정
Y = step_function(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)  # y축의 범위 지정
plt.show()
