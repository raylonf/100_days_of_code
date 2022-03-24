from twilio.rest import Client
import smtplib
from data_uteis import ACCOUNT_SID, AUTH_TOKEN_TWILIO_KEY, PASSWORD_EMAIL


class SendMessage:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN_TWILIO_KEY)
        self.my_email = 'raylonsilva42@gmail.com'
        self.password = PASSWORD_EMAIL

    def sendSMS(self, to_phone, msg=str):
        message = self.client.messages.create(
            body= msg,
            from_='+12344054495',
            to=to_phone
        )

        return message.sid

    def sendEmail(self, email_to, msg=str):
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email, to_addrs=email_to, msg=msg)






