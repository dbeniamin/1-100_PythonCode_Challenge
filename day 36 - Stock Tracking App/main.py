import os
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
THE_TRADING_KEY = os.environ["ALPHAVANTAGE_KEY"]
NEWS_API = os.environ["THE_NEWS_KEY"]
TWILIO_SID = "enter your sid"
TWILIO_AUTH_TOKEN = "enter your own token"

# # STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# print(THE_KEY) # print statement used to see if the key was added to virtual env.

# add the params requested by the platform
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": THE_TRADING_KEY
}

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()
print(stock_data)  # print statement to check the extracted data

# navigate dict keys to extract data for the specific key i.e. = "Time Series (Daily)"
data_daily = stock_data["Time Series (Daily)"]

# list comprehension required to transfrom the extracted dict in to a list
data_list = [value for (key, value) in data_daily.items()]
# tap in to new created list and extract the required index  i.e 0 = yesterday , 1 = the day before yesterday and so on
yesterday_data = data_list[0]
# once you get the data for the given day
yesterday_closing_price = yesterday_data["4. close"]

print(yesterday_closing_price)  # check value print statement

# TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)  # check value print statement

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp

# abs() function will return the positiv value of a number ie abs(-11) => 11
diff_days_value = abs(float(day_before_yesterday_closing_price) - float(yesterday_closing_price))
print(diff_days_value)  # check value print statement
up_down = None
if diff_days_value > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"


# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.

# get the percentage that the diffrence means for each day
# personal preference is to round at 2 decimals for ease of view

percentage_yesterday = round(diff_days_value * 100 / float(yesterday_closing_price), 2)
percentage_day_before_yesterday = round(diff_days_value * 100 / float(day_before_yesterday_closing_price), 2)
print(percentage_yesterday)  # check value print statement
print(percentage_day_before_yesterday)  # check value print statement

# TODO 5. - If TODO4 percentage is greater than (a value you get on the test day) then print("Get News").
if percentage_yesterday > 2 and percentage_day_before_yesterday > 2:
    # print("Get News")  # check value print statement
    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_params = {
        "apiKey": NEWS_API,
        "qInTitle": COMPANY_NAME,
        "pageSize": 3,
    }

    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint:
    #  https://stackoverflow.com/questions/509211/understanding-slice-notation
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    # first_three_articles = news_data[:3]
    # print(first_three_articles)  # print the slice
    # print(news_data)  # check value print statement

"""you can use the slice method to get the first three articles or you can pass the "pageSize": 3 param that will
fetch the first 3 articles"""

# # STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.
# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_article_list = [(f"{STOCK_NAME}: {up_down} {percentage_yesterday} % Headline: {article['title']}. "
                           f"\nBrief: {article['description']}") for article in news_data]
print(formatted_article_list)  # check value print statement

# TODO 9. - Send each article as a separate message via Twilio.
# client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
#
# for article in formatted_article_list:
#     message = client.messages \
#         .create(
#         body=article,
#         from_='twilio dummy number',
#         to='Your number'
#     )

# Optional TODO: Format the message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus
market crash."""
