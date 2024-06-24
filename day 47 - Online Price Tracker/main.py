import smtplib
import requests
from bs4 import BeautifulSoup

# https://stackoverflow.com/questions/6260457/using-headers-with-the-python-requests-librarys-get-method
# http://myhttpheader.com/
# scraped a different seller site just because amazon captcha does not worth the effort to bypass captcha

""" If you get an error that says "bs4.FeatureNotFound: Couldn't find a tree builder with the features you 
requested: html-parser." Then it means you're not using the right parser"""

""" Additional google setup steps required """
"""    1-> go to manage google account.
       2-> turn on 2-step verification.
       3-> now just below 2-step verification you will see App passwords.
       4-> Follow the steps given there and paste the app password in your password variable inside your code."""

URL = ("https://www.emag.ro/procesor-amd-ryzentm-9-7950x3d-144mb-4-5-5-7ghz-max-boost-socket-am5-radeon-graphic-100"
       "-100000908wof/pd/D8NDH6MBM/")
BUY_PRICE = 4000  # set a large price to check the loop
MY_EMAIL = "test_email@gmail.com"
MY_PASS = "test_pass"
SMTP_ADDRESS = "smtp.gmail.com"

response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())  # self check print statement

title = soup.find("h1", class_="page-title").get_text()
print(title)  # self check print statement

# get price by class
# after first run captcha might get activated and the script won't work for a while
price = soup.find("p", class_="product-new-price")
extracted_price = price.text.strip()
print(extracted_price)  # self check print statement

# extract the number part without the float
integer_price = extracted_price.split(',')[0]

# remove the . in the price and convert to integer
cleaned_string = int(''.join(filter(str.isdigit, integer_price)))

print(cleaned_string)  # self check print statement

if cleaned_string < BUY_PRICE:
    message = f"{title} is now {cleaned_string} RON"
    print(message)  # self check print statement

    # send email part of the scrip can be used as a notification
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:EMAG Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
