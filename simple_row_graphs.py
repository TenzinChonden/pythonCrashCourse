import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# Top-Left (Row 0, Col 0)
axes[0, 0].plot(x, x)
axes[0, 0].set_title('Linear')

# Top-Right (Row 0, Col 1)
axes[0, 1].plot(x, x**2, color='orange')
axes[0, 1].set_title('Quadratic')

# Bottom-Left (Row 1, Col 0)
axes[1, 0].plot(x, np.sqrt(x), color='green')
axes[1, 0].set_title('Square Root')

# Bottom-Right (Row 1, Col 1)
axes[1, 1].plot(x, np.exp(x/2), color='purple')
axes[1, 1].set_title('Exponential')

plt.tight_layout()
plt.show()
