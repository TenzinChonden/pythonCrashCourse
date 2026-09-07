import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.dates as mdates

sony_file_path = Path('gen_datasets/Sony_corp_stock_prices.csv')
beaver_file_path = Path('gen_datasets/Beaver_corp_stock_prices.csv')

df1 = pd.read_csv(sony_file_path)
df2 = pd.read_csv(beaver_file_path)

# convert the 'Dates' column values to datetime objects
df1['Dates'] = pd.to_datetime(df1['Dates'])

fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

ax1.plot(df1['Dates'], df1['Prices'], label='Sony Corp.', color='blue', alpha=0.7)
ax1.set_ylabel('Price ($)', fontsize=12)
ax1.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(df1['Dates'], df2['Prices'], label='Beaver Corp.', color='red', alpha=0.7)
ax2.tick_params(axis='y', labelcolor='red')

plt.title('Sony Corp. vs Beaver Corp. 2025 Stock Price Analysis')
plt.style.use('seaborn-v0_8')
plt.tight_layout()
plt.show()
