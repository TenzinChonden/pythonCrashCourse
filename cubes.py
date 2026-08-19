import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set title and axis labels
ax.set_title("Cube Numbers", fontsize=14)
ax.set_xlabel("Values", fontsize=9)
ax.set_ylabel("Cube of Values", fontsize=9)

# Set size of tick labels
ax.tick_params(labelsize=14)

plt.show()
