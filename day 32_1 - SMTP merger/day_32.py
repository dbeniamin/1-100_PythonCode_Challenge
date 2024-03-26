### datetime - helps with date format and date manipulations ###
### SMTP - Simple mail transfer protocol ###

import smtplib
import datetime as dt
import random

""" addresses and password are made up just for the purpose of the class """
""" In order to really use this follow the steps provided  below """
""" 1. Make sure you've got the correct smtp address for your email provider:
Gmail: smtp.gmail.com
Hotmail: smtp.live.com
Outlook: outlook.office365.com
Yahoo: smtp.mail.yahoo.com """

""" 2. Go to https://myaccount.google.com/
Select Security on the left and scroll down to How you sign in to Google.
Enable 2-Step Verification
3. Click on 2-Step Verification again, and scroll to the bottom.
There you can add an App password.
Select Other from the dropdown list and enter an app name, e.g. Python Mail, then click Generate.
COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.
Use this App password in your Python code instead of your normal password.
4. Add a port number by changing your code to this:
smtplib.SMTP("smtp.gmail.com", port=587)"""

MY_EMAIL = "coding_class_notreal@gmail.com"
MY_PASSWORD = "coding_class_notreal_pass_123"

with smtplib.SMTP("smtp.gmail.com") as connection:
    # setting up the secured communication - encrypts the mail
    connection.starttls()
    # login
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    # send the e-mail from my adrees to the desired addres
    # use the subject parameter and add the body using \n\n
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="codding_class@yahoo.com",
                        msg="Subject:Hello \n\n This is the actual body of the email that will be sent using this "
                            "automated script")
# close the connection
connection.close()

now = dt.datetime.now()
# the value can be used to tap in to some attributes like year, month, day, hour, minute etc.
year = now.year
print(year)

# can use the datetime module to create a new date
date_of_birth = dt.datetime(year=1900, month=4, day=11, hour=23)
print(date_of_birth)


now = dt.datetime.now()
weekday = now.weekday()

# weekday can be taped to get the index for the specific day of the week
# monday = 0 , tuesday = 1, wednesday = 2 , etc.
if weekday == 0:
    with open("day_32_quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivation \n\n {quote}")
