import pandas as pd

# use the set_option below to not show the truncated content of each cell
pd.set_option("display.max_columns", None)
df = pd.read_csv("salaries_by_college_major.csv")

# print the first 5 rows
# print(df.head())

# To see the number of rows and columns we can use the shape attribute
# print(df.shape)

# get columns name by suing columns attribute
# print(df.columns)

# use the .isna method to find NaN's - not a number - in order to avoid later problems
df.isna()

# cleaning the df - deleting the 50th row
clean_df = df.dropna()

# print last 5 rows to check it the 50th row was removed
# print(clean_df.tail())

# to acces specific column use [] -  these can be attributed to any variable for work purposes
# add .max() to get the highest value only
# .idmax() -  returns the row index of the max value
# print(clean_df["Starting Median Salary"].max())

# get an entire row by using .loc[22]
# using a column name and loc gives the value of the specific cell
# print(clean_df.loc[22])
# print(clean_df["Undergraduate Major"][22])

# TODO 1 - The Highest Mid-Career Salary
print(clean_df["Mid-Career Median Salary"].max())
print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
var1 = clean_df['Undergraduate Major'][8]
print(var1)

# TODO 2 - Sorting Values & Adding Columns
var2 = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
# insert() method used to create another column and save the data
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
print(clean_df.head())
# smallest spread, we can use the .sort_values() method.
# use below reference for sorting documentation
# --- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html ---

# TODO 3 -  Degrees with the Highest Potential

highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())
