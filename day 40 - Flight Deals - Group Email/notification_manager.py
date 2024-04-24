import smtplib

from twilio.rest import Client

TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR TWILIO VIRTUAL NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR TWILIO VERIFIED NUMBER"
MAIL_PROVIDER_SMTP = "Your provider smtp adress"
MY_EMAIL = "Your email"
MY_PASS = "Your Password"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # setu-up func to send sms to yourself or the created twilio account
    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    """https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in
    -position-20#answer-9942885 - codec encode documentation"""

    ### set -up func to send emails to the previouslly created list ###
    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASS)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight \n\n{message}".encode("utf-8")
                )
