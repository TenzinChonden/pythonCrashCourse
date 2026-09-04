import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E', 'F']
values_a = [1, 2, 3, 4, 5, 6]
values_b = [6, 5, 4, 3, 2, 1]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

fig.suptitle('Basic Bar Graphs', fontsize=28)

ax1.bar(categories, values_a, label='A Values', color='teal', edgecolor='black', linewidth=1.5)
ax1.bar(categories, values_b, bottom=values_a, label='B Values', color='Blue', edgecolor='black', linewidth=1.5)
ax1.set_title('Basic Bar Chart')
ax1.set_xlabel('Categories')
ax1.set_ylabel('Values')
ax1.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=2)

ax2.bar(categories, values_a, color='blue', edgecolor='black', linewidth=1.5)
ax2.set_title('Basic Bar Chart 2')
ax2.set_xlabel('Categories')
ax2.set_ylabel('Values')

plt.tight_layout()
plt.show()
