import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ✅ Manually creating sample time series data
dates = pd.date_range(start="2016-05-09", periods=1300, freq="D")
page_views = np.random.randint(10000, 200000, size=len(dates))
df = pd.DataFrame({"date": dates, "value": page_views})
df.set_index("date", inplace=True)

# ✅ Cleaning the data (Removing top and bottom 2.5%)
lower_bound = df["value"].quantile(0.025)
upper_bound = df["value"].quantile(0.975)
df = df[(df["value"] >= lower_bound) & (df["value"] <= upper_bound)]

# ✅ Function to draw line plot
def draw_line_plot():
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["value"], color='tab:red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.show()

# ✅ Function to draw bar plot
def draw_bar_plot():
    df_bar = df.copy()
    df_bar["Year"] = df_bar.index.year
    df_bar["Month"] = df_bar.index.strftime('%B')
    df_bar = df_bar.groupby(["Year", "Month"]).mean().unstack()
    df_bar.plot(kind="bar", figsize=(12, 6))
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.title("Monthly Average Page Views")
    plt.legend(title="Months", labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.show()

# ✅ Function to draw box plot
def draw_box_plot():
    df_box = df.copy()
    df_box["Year"] = df_box.index.year
    df_box["Month"] = df_box.index.strftime('%b')
    plt.figure(figsize=(12, 6))
    sns.boxplot(x="Year", y="value", data=df_box)
    plt.title("Year-wise Box Plot (Trend)")
    plt.xlabel("Year")
    plt.ylabel("Page Views")
    plt.show()

# ✅ Display individual plots
if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
