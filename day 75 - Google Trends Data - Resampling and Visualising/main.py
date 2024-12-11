import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter("%Y")

# TODO 1 - pass column name to extract data from data frame that has a csv data read
# min() and max() methods can be passed over the specified collumn of data frame to extract values
print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()} ')
print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')
print('Largest value for "Unemployemnt Benefits" '
      f'in Web Search: {df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}')

# TODO 2 - Investigate all 4 DataFrames and find if there are any missing values
# Solution 1 - use .isna() method and check.
print(f"Missing values? for BTC price?:{df_btc_price.isna().values.any()}")
# number of missing values can be found by using .sum() to add up the number of occurrences of True in the series.
print(f"Number of missing values: {df_btc_price.isna().values.sum()}")
test = df_btc_price[df_btc_price.CLOSE.isna()]
test2 = df_btc_price.dropna(inplace=True)

# Solution 2 - see below - chain .values.any() to see if any value in the series is True.
print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')
print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}')

# TODO 3 - Convert any strings you find in month or date columns into datetime objects
# Solution - To convert strings into a datetime object use Pandas .to_datetime() function
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)
# Resampling Time Series Data
# use .resample() function - use "M" for monthly
# for more details on date and time functions see the below link
#  https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects

# get the last available price at month end
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()

# average price over the month
df_btc_monthly_average = df_btc_price.resample('M', on='DATE').mean()

# TODO 4 - Plot the Tesla stock price against the Tesla search volume using a line chart and two different axes
# Solution

# increases size and resolution
plt.figure(figsize=(9, 6), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)

ax1 = plt.gca()  # get current axis
ax2 = ax1.twinx()

# Also, increase fontsize and linewidth for larger charts
ax1.set_ylabel('TSLA Stock Price', color="blue", fontsize=14)
ax2.set_ylabel('Search Trend', color="red", fontsize=14)

# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

# adding the formaters from TODO 5
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color="blue", linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color="red", linewidth=3)
plt.show()

# TODO 5 - Adding Locator Tick Marks
# add the objects needed to find years and months
# look at the top of the file

# TODO 6 - Charting Bitcoin

plt.figure(figsize=(12, 6), dpi=120)

plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=0, top=15000)
ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])

# linestyle and markers
ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE,
         color='#F08F2E', linewidth=3, linestyle='--')
ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH,
         color='skyblue', linewidth=3, marker='o')
plt.show()

# TODO 7 - How to use Grids
plt.figure(figsize=(10, 6), dpi=120)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])

# set color for the grid lines as dark grey lines
ax1.grid(color='grey', linestyle='--')

# add new data set
ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE,
         color='purple', linewidth=3, linestyle='--')
ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH,
         color='skyblue', linewidth=3)

plt.show()

# TODO 8 - The Effect of New Data
# Read the data in the 'UE Benefits Search vs UE Rate 2004-20.csv' into a DataFrame.
# Convert the MONTH column to Pandas Datetime objects and then plot the chart

df_ue_2020 = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)

plt.figure(figsize=(10, 6), dpi=120)
plt.yticks(fontsize=11)
plt.xticks(fontsize=11, rotation=45)
plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=14)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.set_xlim([df_ue_2020.MONTH.min(), df_ue_2020.MONTH.max()])

ax1.plot(df_ue_2020.MONTH, df_ue_2020.UNRATE, 'purple', linewidth=3)
ax2.plot(df_ue_2020.MONTH, df_ue_2020.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)

plt.show()
