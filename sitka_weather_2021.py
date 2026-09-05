import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path
import csv

path = Path('weather_data/sitka_weather_2021_full.csv')

with path.open('r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    try:
        date_index = header_row.index('DATE')
        highs_index = header_row.index('TMAX')
        lows_index = header_row.index('TMIN')
        prcp_index = header_row.index('PRCP')
    except ValueError:
        print('Check index values.')

    dates, highs, lows, prcps = [], [], [], []
    highest, lowest = float('-inf'), float('inf')
    highest_date, lowest_date = None, None
    
    for row in reader:
        try:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            high = int(row[highs_index])
            low = int(row[lows_index])
            prcp = float(row[prcp_index])

        except (ValueError, IndexError):
            continue
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            prcps.append(prcp)

            # Look for the highest and lowest temperature
            if high > highest:
                highest = high
                highest_date = current_date
            if low < lowest:
                lowest = low
                lowest_date = current_date
           
plt.style.use('seaborn-v0_8')
fig, (ax, ax1) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Plot the highest and lowest daily temperatures and fill the gap between them
ax.plot(dates, highs, label='highs', color='red', alpha=0.7)
ax.plot(dates, lows, label='lows', color='blue', alpha=0.7)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Plot the highest and lowest temperature of the year
ax.scatter(highest_date, highest, color='red', s=40, zorder=5)
ax.scatter(lowest_date, lowest, color='blue', s=40, zorder=5)

# Label the lowest and highest temperature
ax.annotate(
    f'High: {highest}°F', 
    xy=(highest_date, highest), 
    xytext=(15, 0), 
    textcoords="offset points",
    va='center',
    arrowprops=dict(arrowstyle='->', color='red', lw=1.5)
)

ax.annotate(
    f'Low: {lowest}°F', 
    xy=(lowest_date, lowest), 
    xytext=(15, 0), 
    textcoords="offset points",
    va='center',
    arrowprops=dict(arrowstyle='->', color='blue', lw=1.5)
)


ax.set_title('Temperature Highs and Lows', fontsize=14, fontweight='bold')
ax.set_xlabel('', fontsize=12)
ax.set_ylabel('Temperature (F)', fontsize=12, fontweight='bold')
ax.legend(loc='upper right', frameon=True)

ax1.bar(dates, prcps, color='purple', width=1)
ax1.set_title('Precipitation', fontsize=14, fontweight='bold')
ax1.set_xlabel('', fontsize=12)
ax1.set_ylabel('Precipitation (cm)', fontsize=12)


fig.autofmt_xdate()

plt.suptitle('Sikta 2021 Weather Overview', fontsize=18, fontweight='bold', x=0.52)
plt.tight_layout()
plt.show()

