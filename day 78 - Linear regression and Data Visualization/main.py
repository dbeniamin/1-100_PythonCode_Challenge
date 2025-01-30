import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from pandas.plotting import register_matplotlib_converters

pd.options.display.float_format = '{:,.2f}'.format

register_matplotlib_converters()

data = pd.read_csv('cost_revenue_dirty.csv')

# TODO 1 - How many rows and columns we have, NaN, Duplicated rows, Data Types.

# # check for NaN values
# print(data.isna().values.any())
#
# # check for duplicates
# print(data.duplicated().values.any())

# getting False as returned by the check-ups means there are no values with the searched attributes
# i.e. NaN and Duplicates
duplicated_rows = data[data.duplicated()]
# print(len(duplicated_rows))

# TODO 2 - Convert the USD_Production_Budget, USD_Worldwide_Gross, and USD_Domestic_Gross columns to a numeric format.

chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget',
                    'USD_Worldwide_Gross',
                    'USD_Domestic_Gross']

for col in columns_to_clean:
    for char in chars_to_remove:
        # replace each character that needs to be removed with an empty string
        data[col] = data[col].astype(str).str.replace(char, "")
    # convert column to a numeric data type
    data[col] = pd.to_numeric(data[col])

# TODO 3 - Convert the Release_Date column to a Pandas Datetime type.

data.Release_Date = pd.to_datetime(data.Release_Date)

# # use the .info() to access the conversion status of the Release_Date collumn.
# print(data.Release_Date.info())

# TODO 4 - Investigate the films that had 0 revenue.

# use the .describe() method
# print(data.describe())

# getting the 0 domestic revenue movie
zero_domestic = data[data.USD_Domestic_Gross == 0]
print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
zero_domestic.sort_values('USD_Production_Budget', ascending=False)

# getting the 0 worldwide revenue movies
zero_worldwide = data[data.USD_Worldwide_Gross == 0]
# print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
zero_worldwide.sort_values('USD_Production_Budget', ascending=False)

# TODO 5 - Filter on Multiple Conditions: International Films

# filtering the movies that made 0 domestic revenue and that made more than 0 worldwide revenue.
# method 1 - use .loc[] property
international_releases_method1 = data.loc[(data.USD_Domestic_Gross == 0) &
                                          (data.USD_Worldwide_Gross != 0)]

# method 2 - use pandas .querry() function - Hint - needs the usage of "and" keyword
international_releases_method2 = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
# print(f'Number of international releases: {len(international_releases_method2)}')
# print(international_releases_method2.tail())

# get what films are not yet released
scrape_date = pd.Timestamp("2018-5-1")
future_releases = data[data.Release_Date >= scrape_date]

data_clean = data.drop(future_releases.index)

# TODO 6 - Find films that lost money

# method 1 - use .loc[]
money_losing_method_1 = data_clean.loc[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
# print(len(money_losing_method_1)/len(data_clean))

# method 2 - use .query() function
money_losing_method_2 = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
result = money_losing_method_2.shape[0] / data_clean.shape[0]
# print(result)

# TODO 7 - Seaborn Data Visualisation: Bubble Charts

# # scatter plot
# # add the axis description - use the ax
# plt.figure(figsize=(8, 4), dpi=200)
# ax = sns.scatterplot(data=data_clean,
#                      x='USD_Production_Budget',
#                      y='USD_Worldwide_Gross')
# ax.set(ylim=(0, 3000000000),
#        xlim=(0, 450000000),
#        ylabel='Revenue in $ billions',
#        xlabel='Budget in $100 millions')
#
# plt.show()


# # bubble chart
# plt.figure(figsize=(8, 4), dpi=200)
# ax = sns.scatterplot(data=data_clean,
#                      x='USD_Production_Budget',
#                      y='USD_Worldwide_Gross',
#                      hue='USD_Worldwide_Gross',  # colour
#                      size='USD_Worldwide_Gross', )  # dot size
#
# ax.set(ylim=(0, 3000000000),
#        xlim=(0, 450000000),
#        ylabel='Revenue in $ billions',
#        xlabel='Budget in $100 millions',)
#
# plt.show()


# # bubble chart with styling
# plt.figure(figsize=(8, 4), dpi=200)
#
# # set styling on a single chart
# with sns.axes_style('darkgrid'):
#     ax = sns.scatterplot(data=data_clean,
#                          x='USD_Production_Budget',
#                          y='USD_Worldwide_Gross',
#                          hue='USD_Worldwide_Gross',
#                          size='USD_Worldwide_Gross')
#
#     ax.set(ylim=(0, 3000000000),
#            xlim=(0, 450000000),
#            ylabel='Revenue in $ billions',
#            xlabel='Budget in $100 millions')
#
# plt.show()


# movie budgets over time
plt.figure(figsize=(8, 4), dpi=200)

with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=data_clean,
                         x='Release_Date',
                         y='USD_Production_Budget',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross', )

    ax.set(ylim=(0, 450000000),
           xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
           xlabel='Year',
           ylabel='Budget in $100 millions')

plt.show()

# TODO 8 - Floor Division: A Trick to Convert Years to Decades

dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year

decades = years // 10 * 10
data_clean['Decade'] = decades

old_films = data_clean[data_clean.Decade <= 1960]
new_films = data_clean[data_clean.Decade > 1960]

# print(old_films.sort_values("USD_Production_Budget", ascending=False).head())


# TODO 9 - Plotting Linear Regressions with Seaborn

# sns.regplot(data=old_films,
#             x='USD_Production_Budget',
#             y='USD_Worldwide_Gross')
#
# plt.figure(figsize=(8,4), dpi=200)
# with sns.axes_style("whitegrid"):
#     sns.regplot(data=old_films,
#             x='USD_Production_Budget',
#             y='USD_Worldwide_Gross',
#             scatter_kws = {'alpha': 0.4},
#             line_kws = {'color': 'black'})


# ploting a regression against the newer films.

# plt.figure(figsize=(8, 4), dpi=200)
# with sns.axes_style('darkgrid'):
#     ax = sns.regplot(data=new_films,
#                      x='USD_Production_Budget',
#                      y='USD_Worldwide_Gross',
#                      color='#2f4b7c',
#                      scatter_kws={'alpha': 0.3},
#                      line_kws={'color': '#ff7c43'})
#
#     ax.set(ylim=(0, 3000000000),
#            xlim=(0, 450000000),
#            ylabel='Revenue in $ billions',
#            xlabel='Budget in $100 millions')
#
# plt.show()

# TODO 10 - Use scikit-learn to Run Your Own Regression.

regression = LinearRegression()

# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])

# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross'])

# Find the best-fit line
regression.fit(X, y)

# R-squared
regression.score(X, y)

budget = 350000000
revenue_estimate = regression.intercept_[0] + regression.coef_[0, 0] * budget
revenue_estimate = round(revenue_estimate, -6)
print(f'The estimated revenue for a $350 milion film is around ${revenue_estimate}')
