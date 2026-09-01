import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path
import csv

path = Path('weather_data/San_Francisco_weather_2021_simple.csv')
lines = path.read_text().splitlines()

output_dir = Path('visualizations')
file_path = output_dir / 'San_Francisco_highs_lows.png'

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing value on {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temps
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format the plot
ax.set_ylim(10, 140)
ax.set_title('San-Francisco Daily High and Low Temperatures, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.savefig(file_path, dpi=300, bbox_inches="tight")
plt.show()
