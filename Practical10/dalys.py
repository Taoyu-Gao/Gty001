import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir(r"D:\githubrep\Practical10")

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Show third and fourth columns (Year and DALYs) for first 10 rows
print(dalys_data.iloc[0:10, 2:4])

# Find which year reported the maximum DALYs across first 10 years for Afghanistan
afghanistan_data = dalys_data.loc[dalys_data.Entity == "Afghanistan", :]
afghanistan_first_10 = afghanistan_data.iloc[0:10, :]
max_dalys_idx = afghanistan_first_10['DALYs'].idxmax()
max_year_afghanistan = afghanistan_first_10.loc[max_dalys_idx, 'Year']
# COMMENT: Afghanistan max DALYs in first 10 records occurred in 1990
print(f"Afghanistan max DALYs year: {max_year_afghanistan}")

# Use Boolean indexing to show all years for Zimbabwe
zimbabwe_mask = (dalys_data.Entity == "Zimbabwe")
zimbabwe_years = dalys_data.loc[zimbabwe_mask, "Year"]
first_year_zimbabwe = zimbabwe_years.min()
last_year_zimbabwe = zimbabwe_years.max()
# COMMENT: Zimbabwe DALYs recorded from 1990 to 2019
print(f"Zimbabwe: {first_year_zimbabwe} to {last_year_zimbabwe}")

# Find countries with max and min DALYs in 2019
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
max_dalys_2019 = recent_data.loc[recent_data['DALYs'].idxmax()]
min_dalys_2019 = recent_data.loc[recent_data['DALYs'].idxmin()]
# COMMENT: Max DALYs 2019: Central African Republic, Min: Singapore
print(f"2019 Max: {max_dalys_2019['Entity']} ({max_dalys_2019['DALYs']:.2f})")
print(f"2019 Min: {min_dalys_2019['Entity']} ({min_dalys_2019['DALYs']:.2f})")

# Plot DALYs over time for country with max DALYs
max_country_data = dalys_data.loc[dalys_data.Entity == max_dalys_2019['Entity'], :]

plt.figure(figsize=(12, 6))
plt.plot(max_country_data.Year, max_country_data.DALYs, 'b-', linewidth=2)
plt.plot(max_country_data.Year, max_country_data.DALYs, 'ro', markersize=4)
plt.title(f'DALYs Over Time - {max_dalys_2019["Entity"]}', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('DALYs (per 100,000 population)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('max_dalys_country_trend.png')
plt.show()

# Custom question: How has global DALYs distribution changed from 1990 to 2019?
global_avg_by_year = dalys_data.groupby('Year')['DALYs'].agg(['mean', 'median', 'std']).reset_index()

plt.figure(figsize=(12, 6))
plt.plot(global_avg_by_year['Year'], global_avg_by_year['mean'], 'b-', linewidth=2, label='Mean', marker='o')
plt.plot(global_avg_by_year['Year'], global_avg_by_year['median'], 'r--', linewidth=2, label='Median', marker='s')
plt.fill_between(global_avg_by_year['Year'],
                 global_avg_by_year['mean'] - global_avg_by_year['std'],
                 global_avg_by_year['mean'] + global_avg_by_year['std'],
                 alpha=0.2, label='±1 SD')
plt.title('Global DALYs Trends (1990-2019)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('DALYs (per 100,000 population)', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('global_dalys_trend.png')
plt.show()

first_mean = global_avg_by_year['mean'].iloc[0]
last_mean = global_avg_by_year['mean'].iloc[-1]
change_percent = ((last_mean - first_mean) / first_mean) * 100
print(f"\nGlobal mean DALYs 1990: {first_mean:.2f}")
print(f"Global mean DALYs 2019: {last_mean:.2f}")
print(f"Change: {change_percent:.1f}%")