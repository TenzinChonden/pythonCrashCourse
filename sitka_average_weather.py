from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().split_lines()
