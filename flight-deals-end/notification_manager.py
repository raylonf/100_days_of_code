from twilio.rest import Client
from data_uteis import AUTH_TOKEN_TWILIO_KEY, ACCOUNT_SID, PHONE_TWILIO

TWILIO_SID = ACCOUNT_SID
TWILIO_AUTH_TOKEN = AUTH_TOKEN_TWILIO_KEY
TWILIO_VIRTUAL_NUMBER = PHONE_TWILIO
TWILIO_VERIFIED_NUMBER = '+5534991676814'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
