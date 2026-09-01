from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt 

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

# file path for saving figure
output_dir = Path("visualizations")
file_path = output_dir / "deathvalley_highs_lows.png"

reader = csv.reader(lines)
header_row = next(reader)

for index, header in enumerate(header_row):
    if header == "TMAX":
        min = index
    if header == "TMIN":
        max = index
        
# Extract dates, and highs and low temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[max])
        low = int(row[min])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
# plot the high and low  temps
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# format plot.
ax.set_ylim(10, 140)
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.savefig(file_path, dpi=300, bbox_inches="tight")
plt.show()
