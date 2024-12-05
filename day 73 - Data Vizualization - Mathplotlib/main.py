import pandas as pd
import matplotlib.pyplot as plt

# use the set_option below to not show the truncated content of each cell
pd.set_option("display.max_columns", None)

# setting the header to 0 allows to set the column names
df = pd.read_csv("QueryResults.csv", names=['DATE', 'TAG', 'POSTS'], header=0)

# print(df.head)

# convert date and time to a format
df.DATE = pd.to_datetime(df.DATE)

# print(df.head())

# TODO 1 - pivot the df DataFrame so that each row is a date and each column is a programming language

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
# print(reshaped_df.head())

# handle NaN values using .fillna() method - dont drop the rows
reshaped_df.fillna(0, inplace=True)
reshaped_df = reshaped_df.fillna(0)
# print(reshaped_df.head())
# check if there are any NaN values left
reshaped_df.isna().values.any()

# TODO 2 - how a line chart for the popularity of a programming language
#
# plt.plot(reshaped_df.index, reshaped_df['python'])
# plt.plot(reshaped_df.index, reshaped_df['java'])
# # use plt.show() method to display the chart if working with pycharm
# plt.show()

# TODO 3 - plot all the programming languages on the same chart

# adding details to the chart by setting the line width and labels based on the column name
# add a font size for the legend
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], linewidth=2, label=reshaped_df[column].name)
# use loc= attribute to set the position of the legend
plt.legend(fontsize=9, loc="upper left")
plt.show()

# TODO 4 - smooth the graph with all the programming languages on the same chart
# use rolling() and mean() methods
# rool_df = reshaped_df.rolling(window=6).mean()
# for column in rool_df.columns:
#     plt.plot(rool_df.index, rool_df[column], linewidth=2, label=rool_df[column].name)
# plt.legend(fontsize=9, loc="upper left")
# plt.show()
