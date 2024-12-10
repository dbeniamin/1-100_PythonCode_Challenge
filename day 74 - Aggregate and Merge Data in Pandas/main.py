import pandas as pd
import matplotlib.pyplot as plt

# use the set_option below to not show the truncated content of each cell
pd.set_option("display.max_columns", None)

# open colors file
colors = pd.read_csv("../../OneDrive/Desktop/day 74 - Aggregate and Merge Data in Pandas/data/colors.csv")
# open sets csv
sets = pd.read_csv("../../OneDrive/Desktop/day 74 - Aggregate and Merge Data in Pandas/data/sets.csv")
# open themes csv
themes = pd.read_csv("../../OneDrive/Desktop/day 74 - Aggregate and Merge Data in Pandas/data/themes.csv")
# print(colors.head)

# # How many unique colors you have for lego sets?
# print(colors['name'].nunique())
#
# # In which year were the first LEGO sets released and what were these sets called?
# print(sets.sort_values("year").head)
#
# # How many different products did the LEGO company sell in their first year of operation?
# print([sets["year"]] == 1949)

# # What are the top 5 LEGO sets with the most number of parts?
# print(sets.sort_values("num_parts", ascending=False).head())

# # How many sets the LEGO company has published year-on-year?
sets_by_year = sets.groupby("year").count()
# # print(sets_by_year["set_num"].head()) # print to show the actual data
# plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
# # plt.legend(fontsize=9, loc="upper left") # use this line if you have multiple data sets to configure a legend
# plt.show()

# # Number of Themes per Calendar Year?
# # use .agg() method
# # the .agg() method takes a dictionary as an argument.
# # In this dictionary, we specify which operation we'd like to apply to each column.
# # In our case, we just want to calculate the number of unique entries in the theme_id
# # column by using our old friend, the .nunique() method.
themes_by_year = sets.groupby("year").agg({"theme_id": pd.Series.nunique})
# # Change the mane of the columns
themes_by_year.rename(columns={"theme_id": "nr_themes"}, inplace=True)
# # print(themes_by_year.head())
#
#
# # Create a line plot of the number of themes released year-on-year.
# # Only include the full calendar years in the dataset (1949 to 2019).
# plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
# plt.show()
# Configure and plot the data on two separate axes on the same chart.
# # get current axes
# axis_1 = plt.gca()
# # create another axis objectd axis_2 and use twinx() method that allows axis_1 and axis_2 to share the same x-axis.
# axis_2 = axis_1.twinx()
#
# axis_1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color="g")
# axis_2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color="b")
# # add styling for clarity
# axis_1.set_xlabel("Year")
# axis_1.set_ylabel("number of sets", color="green")
# axis_2.set_ylabel("number of themes", color="blue")
# # plot the newly pimped graph
# plt.legend(fontsize=9, loc="upper left")
# plt.show()
#

# # Create a Pandas Series called parts_per_set that has the year as the index and contains the average number of parts
# # user groupby() method and pass in the agg() method a dict
# parts_per_set = sets.groupby("year").agg({"num_parts": pd.Series.mean})
#
# # use scatter plot
# plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
# plt.show()


# Count the number of sets per Theme we can use the .value_counts() method on our theme_id column.
set_theme_count = sets["theme_id"].value_counts()
print(set_theme_count[:5])

# To display an image in a Text (aka Markdown) cell => use the HTML <img> tag.
# <img src="https://i.imgur.com/Sg4lcjx.png">

# How is the themes.csv structured?
# Search for the name 'Star Wars'. How many ids correspond to the 'Star Wars' name in the themes.csv?

print(themes[themes.name == "Star Wars"])
print(sets.theme_id == 18)
print(sets[sets.theme_id == 209])


# Combine data on theme names with the number sets per theme
set_theme_count = pd.DataFrame({
    "id": set_theme_count.index,
    "set_count": set_theme_count.values
})

# To .merge() two DataFrame along a particular column,
# Provide our two DataFrames and then the column name on which to merge.
merged_df = pd.merge(set_theme_count, themes, on="id")


# styling required to make sure the details on the bar don't overlap
plt.figure(figsize=(14,8))
plt.xticks(fontsize=9, rotation=9)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=11)
plt.xlabel('Theme Name', fontsize=11)
# map it to a bar chart
plt.bar(merged_df.name[:10], merged_df.set_count[:10])

plt.show()
