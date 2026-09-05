import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E', 'F']
a_values = [1, 2, 3, 4, 5, 6]
b_values = [4, 3, 6, 4, 5, 3]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

ax1.bar(categories, a_values, label='a_values', color='red', alpha=0.7)
ax1.bar(categories, b_values, bottom=a_values, label='b_values', color='blue', alpha=0.7)
ax1.set_title('Basic Stacked Bar Graph', fontsize=14, fontweight='bold')
ax1.set_xlabel('Categories', fontsize=12)
ax1.set_ylabel('Values', fontsize=12)

ax1.legend(loc='upper left', frameon=True)

ax2.bar(categories, a_values, color='green', alpha=0.7)
ax2.set_title('Basic Bar Graph', fontsize=14, fontweight='bold')
ax2.set_xlabel('Categories', fontsize=12)
ax2.set_ylabel('a_values', fontsize=12)

fig.suptitle('Basic Bar Graphs', fontsize=18, fontweight='bold')

plt.style.use('seaborn-v0_8-whitegrid')
plt.tight_layout()
plt.show()

