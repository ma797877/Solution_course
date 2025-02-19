import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# ✅ Manually creating sample sea level data
years = np.arange(1880, 2015)
sea_levels = 0.02 * (years - 1880) + np.random.normal(0, 1, len(years))
df = pd.DataFrame({"Year": years, "CSIRO Adjusted Sea Level": sea_levels})

# ✅ Function to draw scatter plot with regression lines
def draw_sea_level_plot():
    plt.figure(figsize=(10, 5))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Observed Data")
    
    # First regression (1880 to 2050)
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = np.arange(1880, 2051)
    plt.plot(years_extended, slope * years_extended + intercept, 'r', label='Fit: 1880-2050')
    
    # Second regression (2000 to 2050)
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent_extended = np.arange(2000, 2051)
    plt.plot(years_recent_extended, slope_recent * years_recent_extended + intercept_recent, 'g', label='Fit: 2000-2050')
    
    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.show()

# ✅ Display the plot
if __name__ == "__main__":
    draw_sea_level_plot()


