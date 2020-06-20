# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import datetime
import time
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACa68a3f94df7173c0abfe989cdad8b54b'
auth_token = 'a96cdfae589757b08afa1e8cd9131efd'
client = Client(account_sid, auth_token)
while True:
  x=datetime.datetime.now()
  message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body="Today is " + str(x.date()) + "& Current time is " + str(x.time()),
                                  to='whatsapp:+918982067673'
                              )
  print(message.sid)
  time.sleep(24.0 * 60.0 * 60.0)  # 24 hours in seconds
