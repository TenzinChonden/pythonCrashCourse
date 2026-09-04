
import csv
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/San_Francisco_weather_2021_simple.csv')

# Select a directory to save the visualization
output_dir = Path('visualizations')

# Make the directory if it doesn't already exist
output_dir.mkdir(parents=True, exist_ok=True)
file_path = output_dir / 'San_Francisco_Precipitation_2021.png'

with path.open(mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header_row = next(reader)

    try:
        date_index = header_row.index('DATE')
        precipitation_index = header_row.index('PRCP')
    except ValueError:
        print("Check for header indexes.")
        date_index, precipitation_index = 2, 3

    dates, precipitations = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            precipitation = float(row[precipitation_index])
        except (ValueError, IndexError):
            continue
        else:
            if current_date.month == 1:
                dates.append(current_date)
                precipitations.append(precipitation)

# Choose the general style of the visualization
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(dates, precipitations, color='purple', alpha=.7, width=1)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Precipitation (mm)')

plt.show()


