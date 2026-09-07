import numpy as np
import pandas as pd
from pathlib import Path

# define output file path for generated data
output_dir = Path('gen_datasets')
output_dir.mkdir(parents=True, exist_ok=True)

file_name = input('What should the file be named? (.csv)')
file_path = output_dir / f'{file_name}.csv'

if file_path.is_file():
    make_file = input(f"Dataset already exists in {file_path}.\nContinue with the data generation? ('n' to cancel) ")

    if make_file == 'n':
        exit()

seed = input('Enter the seed for the data (press Enter for default of 42): ')
if seed == '':
    rng = np.random.default_rng(seed=42)
else:
    rng = np.random.default_rng(seed=int(seed))

days = 365

# Generate a normal distribution noise around zero
daily_changes = rng.normal(loc=0.05, scale=1.0, size=days)

start_price = input('What should the price start at (press Enter for default of $100): ')
if start_price == '':
    # Cumulative sum turns daily steps into a continious path
    values = np.round(100 + np.cumsum(daily_changes), 2) 
else:
    values = np.round(int(start_price) + np.cumsum(daily_changes), 2)
    
dates = pd.date_range(start='2025-01-01', periods=days)

df = pd.DataFrame({'Dates': dates, 'Prices': values})

df.to_csv(file_path, index=False)
