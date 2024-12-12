import pandas as pd
import plotly.express as px

# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format
# use the set_option below to show all content for all cels
pd.set_option("display.max_columns", None)

df_apps = pd.read_csv("apps.csv")

print(df_apps.shape)

# TODO 1 - Remove the columns called Last_Updated and Android_Version from the DataFrame
# create df_app_clean -  remove the last 2 columns
# df_apps.drop(["Last_Updated", "Android_Version"], axis=1, inplace=True)
# remove the Nan rows
df_apps_clean = df_apps.dropna()
print(df_apps_clean.shape)

# TODO 2  - Check and remove duplicates
# use .duplicated method
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
# print(duplicated_rows.shape) # print statement for debug values
df_apps_clean = df_apps_clean.drop_duplicates(subset=["App", "Type", "Price"])
print(df_apps_clean.shape)

# # TODO 3 - Preliminary Exploration: The Highest Ratings, Most Reviews, and Largest Size
# # these can be assigned to new variables in case of future usage
# # use collumn name to sort the whole file by those values and pull a sample out i.e. head()
# print(df_apps_clean.sort_values('Rating', ascending=False).head())
#
# # use collumn name to sort the whole file by those values and pull a sample out i.e. head()
# print(df_apps_clean.sort_values('Size_MBs', ascending=False).head())
#
# # use collumn name to sort the whole file by those values and pull a sample out i.e. head()
# # adding a param to head extends the filtering up the desired number of rows
# print(df_apps_clean.sort_values('Reviews', ascending=False).head(50))


# # TODO 4 - Make charts with plotly
# # https://plotly.com/python/
# # make a pie chart
# # init ratings as values
# ratings = df_apps_clean.Content_Rating.value_counts()
# # style the chart a bit
# # https://plotly.com/python-api-reference/generated/plotly.express.pie.html
# fig = px.pie(
#     labels=ratings.index,
#     values=ratings.values,
#     title="Content Rating",
#     names=ratings.index,
#     hole=0.4
# )
# fig.update_traces(textposition="inside", textinfo="percent + label")
# fig.show()

#  TODO 5 - How many apps had over 1 billion installations? How many apps just had a single install?
# use .groupby() and .count()
# remove the , in the numbers like 1,000 and so on
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[['App', 'Installs']].groupby('Installs').count()

# remove the $ sign
df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)

df_apps_clean.sort_values('Price', ascending=False).head(20)

# remove the one costing over 250$
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
df_apps_clean.sort_values('Price', ascending=False).head(5)


df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
print(df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10])


# TODO 6 - The Most Competitive & Popular App Categories
top10_category = df_apps_clean.Category.value_counts()[:10]
# # use bar chart model for the top 10
# bar = px.bar(x=top10_category.index,  # index = category name
#              y=top10_category.values)
#
# bar.show()

#  model by number of installations
category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)

# add orientation to change the graph orientation
# cutom title and axis labels
h_bar = px.bar(x=category_installs.Installs,
               y=category_installs.index,
               orientation='h',
               title='Category Popularity')

h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
h_bar.show()

# TODO 7 - Scatter plot
# get number of apps in each category
cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})
# merge the two data frames
cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how="inner")
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
cat_merged_df.sort_values('Installs', ascending=False)

scatter = px.scatter(cat_merged_df,  # data
                     x='App',  # column name
                     y='Installs',
                     title='Category Concentration',
                     size='App',
                     hover_name=cat_merged_df.index,
                     color='Installs')

scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))

scatter.show()

# TODO 8 - Extracting Nested Column Data using .stack()

# Split the strings on the semicolon and then .stack them.
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')

# TODO 9 - Extracting Nested Column Data using .stack()
bar = px.bar(x=num_genres.index[:15],  # index = category name
             y=num_genres.values[:15],  # count
             title='Top Genres',
             hover_name=num_genres.index[:15],
             color=num_genres.values[:15],
             color_continuous_scale='Agsunset')

bar.update_layout(xaxis_title='Genre',
                  yaxis_title='Number of Apps',
                  coloraxis_showscale=False)

bar.show()

# TODO 10 - Grouped Bar Charts and Box Plots with Plotly
df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
print(df_free_vs_paid.head())

g_bar = px.bar(df_free_vs_paid,
               x='Category',
               y='App',
               title='Free vs Paid Apps by Category',
               color='Type',
               barmode='group')

g_bar.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    xaxis={'categoryorder': 'total descending'},
                    yaxis=dict(type='log'))

g_bar.show()

# TODO 11 - Create Box Plots for the Number of Installs
box = px.box(df_apps_clean,
             y='Installs',
             x='Type',
             color='Type',
             notched=True,
             points='all',
             title='How Many Downloads are Paid Apps Giving Up?')

box.update_layout(yaxis=dict(type='log'))

box.show()

# TODO 12 - App Revenue by Category
df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']
box = px.box(df_paid_apps,
             x='Category',
             y='Revenue_Estimate',
             title='How Much Can Paid Apps Earn?')

box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Ballpark Revenue',
                  xaxis={'categoryorder': 'min ascending'},
                  yaxis=dict(type='log'))

box.show()

# TODO 13 - App Pricing by Category

print(df_paid_apps.Price.median())
box = px.box(df_paid_apps,
             x='Category',
             y="Price",
             title='Price per Category')

box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Price',
                  xaxis={'categoryorder': 'max descending'},
                  yaxis=dict(type='log'))

box.show()
