import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from pathlib import Path

data_dir = Path('gen_datasets')
apple_path = data_dir / 'apple_stock_prices.csv'
mango_path = data_dir / 'mango_stock_prices.csv'

apple_bs_path = data_dir / 'apple_balance_sheet.json'
mango_bs_path = data_dir / 'mango_balance_sheet.json'

with open(apple_bs_path, 'r', encoding='utf-8') as f:
    apple_bs = json.load(f)

with open(mango_bs_path, 'r', encoding='utf-8') as f:
    mango_bs = json.load(f)

df1 = pd.read_csv(apple_path)
df2 = pd.read_csv(mango_path)
df3 = pd.DataFrame({
    'Metrics': [
        'Total Assets', 
        'Total Liabilities', 
        'Total Equity'
    ], 
    apple_bs['name']: [
        apple_bs['assets']['total_assets'], 
        apple_bs['liabilities']['total_liabilities'], 
        apple_bs['equity']['total_equity']
    ], 
    mango_bs['name']: [
        mango_bs['assets']['total_assets'], 
        mango_bs['liabilities']['total_liabilities'], 
        mango_bs['equity']['total_equity']
    ]
})

# convert the 'Dates' column values for df1 to datetime objects
df1['Dates'] = pd.to_datetime(df1['Dates'])

fig, axes = plt.subplot_mosaic(
    [['top', 'top'], 
    ['bottom_left', 'bottom_right']], 
    figsize=(12, 10)
)

# Plot both companies on the same axis
ax_top = axes['top']
ax_top.plot(df1['Dates'], df1['Prices'], label='Apple Corp.', color='red', alpha=0.7)
ax_top.plot(df1['Dates'], df2['Prices'], label='Mango Ltd.', color='blue', alpha=0.7)

# Format the x axis for monthly ticks
ax_top.xaxis.set_major_locator(mdate.MonthLocator())
ax_top.xaxis.set_major_formatter(mdate.DateFormatter('%b %Y'))

ax_top.set_xmargin(0)

plt.suptitle('Apple Corp. vs Mango Ltd.', x=0.52, fontsize=18, fontweight='bold')
ax_top.set_title('Stock Prices For The Year 2025', fontsize=14, color='grey')
ax_top.set_ylabel('Price ($)', fontsize=12)
ax_top.set_xlabel('', fontsize=12)
ax_top.grid(True, alpha=0.4)
ax_top.legend(loc='upper left', frameon=True)
ax_top.set_facecolor('lightgrey')

ax_bl = axes['bottom_left']
ax_bl.pie(
    df3[apple_bs['name']], 
    labels=df3['Metrics'], 
    autopct='%1.1f%%', 
    colors=['#4C72B0', '#55A868'], 
    startangle=140
)
ax_bl.set_title('Apple Corp. Balance Sheet', fontsize=12, fontweight='bold')

ax_br = axes['bottom_right']
ax_br.pie(
    df3[mango_bs['name']], 
    labels=df3['Metrics'], 
    autopct='%1.1f%%', 
    colors=['#DD8452', '#C44E52'],
    startangle=140
)
ax_br.set_title('Mango Ltd. Balance Sheet', fontsize=12, fontweight='bold')

fig.autofmt_xdate()
plt.tight_layout()
plt.show()
