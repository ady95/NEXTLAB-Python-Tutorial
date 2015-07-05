import numpy as np
import matplotlib.pyplot as plt
import smooth

# 1. generate data
t = np.linspace(-4, 4, 500)
y = np.exp( -t**2 ) + np.random.normal(0, 0.05, t.shape)

# 2. smooth data
ysg = smooth.savitzky_golay(y, window_size=31, order=4)

# 3. graph
plt.plot(t, y, label='Noisy signal')
plt.plot(t, np.exp(-t**2), 'k', lw=1.5, label='Original signal')
plt.plot(t, ysg, 'r', label='Smooth signal')
plt.legend()
plt.show()