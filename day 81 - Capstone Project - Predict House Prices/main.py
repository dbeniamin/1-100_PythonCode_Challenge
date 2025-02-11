import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# format and load the data
pd.options.display.float_format = '{:,.2f}'.format
data = pd.read_csv('boston.csv', index_col=0)

# # prelim data exploration
# print(data.shape)
# print(data.columns)
# print(data.count)
#
# # check for nan and duplicated values
# print(f'Any NaN values? {data.isna().values.any()}')
# print(f'Any duplicates? {data.duplicated().values.any()}')

# TODO 1 - display house prices and distance to employment
# house price chart
g_1 = sns.displot(data['PRICE'],
                  bins=50,
                  aspect=2,
                  kde=True,
                  color='#2196f3')
# add adjust top to fit the title to screen
plt.subplots_adjust(top=0.85)
plt.title(f'1970s Home Values in Boston. Average: ${(1000 * data.PRICE.mean()):.6}', fontsize=12)
plt.xlabel('Price in 000s')
plt.ylabel('Nr. of Homes')

plt.show()

# distance to employment chart
g_2 = sns.displot(data.DIS,
                  bins=50,
                  aspect=2,
                  kde=True,
                  color='darkblue')

plt.subplots_adjust(top=0.85)
plt.title(f'Distance to Employment Centres. Average: {(data.DIS.mean()):.2}', fontsize=12)
plt.xlabel('Weighted Distance to 5 Boston Employment Centres')
plt.ylabel('Nr. of Homes')

plt.show()

# TODO 2 -  number of rooms and access to highway
# number of rooms
g_3 = sns.displot(data.RM,
                  aspect=2,
                  kde=True,
                  color='#00796b')

plt.subplots_adjust(top=0.85)
plt.title(f'Distribution of Rooms in Boston. Average: {data.RM.mean():.2}', fontsize=12)
plt.xlabel('Average Number of Rooms')
plt.ylabel('Nr. of Homes')

plt.show()

# access to highway
plt.figure(figsize=(8, 4), dpi=200)

plt.hist(data['RAD'],
         bins=24,
         ec='black',
         color='#7b1fa2',
         rwidth=0.5)

plt.xlabel('Accessibility to Highways')
plt.ylabel('Nr. of Houses')
plt.show()

# TODO 3 - river access challenge
# access to river for properties
river_access = data['CHAS'].value_counts()

bar = px.bar(x=['No', 'Yes'],
             y=river_access.values,
             color=river_access.values,
             color_continuous_scale=px.colors.sequential.haline,
             title='Next to Charles River?')

bar.update_layout(xaxis_title='Property Located Next to the River?',
                  yaxis_title='Number of Homes',
                  coloraxis_showscale=False)
bar.show()

# TODO 4 - pollution graphs
# Compare DIS (Distance from employment) with NOX (Nitric Oxide Pollution)
with sns.axes_style('darkgrid'):
    sns.jointplot(x=data['DIS'],
                  y=data['NOX'],
                  height=8,
                  kind='scatter',
                  color='deeppink',
                  joint_kws={'alpha': 0.5})

plt.show()

# Compare INDUS (the proportion of non-retail industry i.e., factories) with NOX (Nitric Oxide Pollution)
with sns.axes_style('darkgrid'):
    sns.jointplot(x=data.NOX,
                  y=data.INDUS,
                  # kind='hex',
                  height=7,
                  color='darkgreen',
                  joint_kws={'alpha': 0.5})
plt.show()

# TODO 5 - lower income population statistics
# Compare LSTAT (proportion of lower-income population) with RM (number of rooms)
with sns.axes_style('darkgrid'):
    sns.jointplot(x=data['LSTAT'],
                  y=data['RM'],
                  # kind='hex',
                  height=7,
                  color='orange',
                  joint_kws={'alpha': 0.5})
plt.show()

# % of Lower Income Population versus Home Price
with sns.axes_style('darkgrid'):
    sns.jointplot(x=data.LSTAT,
                  y=data.PRICE,
                  # kind='hex',
                  height=7,
                  color='crimson',
                  joint_kws={'alpha': 0.5})
plt.show()

# TODO 6 - Split Training & Test Dataset
target = data['PRICE']
features = data.drop('PRICE', axis=1)

X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size=0.2,
                                                    random_state=10)

# % of training set
train_pct = 100 * len(X_train) / len(features)
print(f'Training data is {train_pct:.3}% of the total data.')

# % of test data set
test_pct = 100 * X_test.shape[0] / features.shape[0]
print(f'Test data makes up the remaining {test_pct:0.3}%.')

# TODO 7 - Multivariable Regression


# run regression on the data set
regr = LinearRegression()
regr.fit(X_train, y_train)
rsquared = regr.score(X_train, y_train)
print(f'Training data r-squared: {rsquared:.2}')

# evaluate the coeficient of the model
regr_coef = pd.DataFrame(data=regr.coef_, index=X_train.columns, columns=['Coefficient'])
# Premium for having an extra room
premium = regr_coef.loc['RM'].values[0] * 1000  # i.e., ~3.11 * 1000
print(f'The price premium for having an extra room is ${premium:.5}')

# TODO 8 - Analyse the Estimated Values & Regression Residuals

predicted_vals = regr.predict(X_train)
residuals = (y_train - predicted_vals)

# Original Regression of Actual vs. Predicted Prices
plt.figure(dpi=100)
plt.scatter(x=y_train, y=predicted_vals, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Actual vs Predicted Prices', fontsize=10)
plt.xlabel('Actual prices', fontsize=10)
plt.ylabel('Prediced prices', fontsize=14)
plt.show()

# Residuals vs Predicted values
plt.figure(dpi=100)
plt.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
plt.title('Residuals vs Predicted Values', fontsize=10)
plt.xlabel('Predicted Prices', fontsize=10)
plt.ylabel('Residuals', fontsize=10)
plt.show()

# TODO 9 - Regression with Log Prices & Residual Plots
new_target = np.log(data['PRICE'])  # Use log prices
features = data.drop('PRICE', axis=1)

X_train, X_test, log_y_train, log_y_test = train_test_split(features,
                                                            new_target,
                                                            test_size=0.2,
                                                            random_state=10)

log_regr = LinearRegression()
log_regr.fit(X_train, log_y_train)
log_rsquared = log_regr.score(X_train, log_y_train)

log_predictions = log_regr.predict(X_train)
log_residuals = (log_y_train - log_predictions)

print(f'Training data r-squared: {log_rsquared:.2}')
# Graph of Actual vs. Predicted Log Prices
plt.scatter(x=log_y_train, y=log_predictions, c='navy', alpha=0.6)
plt.plot(log_y_train, log_y_train, color='cyan')
plt.title(f'Actual vs Predicted Log Prices:  {log_rsquared:.2}', fontsize=17)
plt.xlabel('Actual Log Prices', fontsize=8)
plt.ylabel('Prediced Log Prices', fontsize=8)
plt.show()

# Original Regression of Actual vs. Predicted Prices
plt.scatter(x=y_train, y=predicted_vals, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Original Actual vs Predicted Prices {rsquared:.3}', fontsize=17)
plt.xlabel('Actual prices X 1000', fontsize=14)
plt.ylabel('Prediced prices X 1000', fontsize=14)
plt.show()

# Residuals vs Predicted values (Log prices)
plt.scatter(x=log_predictions, y=log_residuals, c='navy', alpha=0.6)
plt.title('Residuals vs Fitted Values for Log Prices', fontsize=12)
plt.xlabel('Predicted Log Prices', fontsize=10)
plt.ylabel('Residuals', fontsize=10)
plt.show()

# Residuals vs Predicted values
plt.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
plt.title('Original Residuals vs Fitted Values', fontsize=12)
plt.xlabel('Predicted Prices', fontsize=10)
plt.ylabel('Residuals', fontsize=10)
plt.show()
