import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)
intensities = np.random.rand(50)

plt.scatter(x, y, c=intensities, cmap='viridis')
plt.colorbar()
plt.show()
