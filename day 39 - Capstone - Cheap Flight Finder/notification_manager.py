from twilio.rest import Client

TWILIO_SID = "Your twilio account SID"
TWILIO_AUTH_TOKEN = "Your Twilio Auth Token"
TWILIO_VIRTUAL_NUMBER = "Your Twilio Virtual Number"
TWILIO_VERIFIED_NUMBER = "Your Twilio number that will get the SMS"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )

        print(message.sid)  # print to check if the sms was sent succesfull
