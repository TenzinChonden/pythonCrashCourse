from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract percipitation and dates
prcps, dates = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        prcp = float(row[5])
    except ValueError:
        print(f"Percipitation format error on date {current_date}")
    else:
        dates.append(current_date)
        prcps.append(prcp)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcps, color='purple', alpha=0.5)

# Format plots
ax.set_title('Daily Percipitation in Sirka, 2021', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Percipitation Level', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
