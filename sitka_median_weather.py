from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

# Output path for saving the figure
output_dir = Path('visualizations')
file_path = output_dir / 'Sitka_Median_Temperature_2021.png'

reader = csv.reader(lines)
header_row = next(reader)

for index, header in enumerate(header_row):
    if header == 'DATE':
        date_col = index

    if header == 'TMIN':
        low_col = index

    if header == 'TMAX':
        high_col = index

dates, medians = [], []

for row in reader:
    current_date = datetime.strptime(row[date_col], '%Y-%m-%d')
    try:
        high = int(row[high_col])
        low = int(row[low_col])
        median = low + ((high-low)/2)
    except ValueError:
        print(f'Missing value on {current_date}.')
    else:
        dates.append(current_date)
        medians.append(median)

# Plot the data
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, medians, color='purple', alpha=0.5)

ax.set_title('Median Temperature in Sitka 2021', fontsize=24)
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()

plt.savefig(file_path, dpi=300, bbox_inches='tight')
plt.show()
