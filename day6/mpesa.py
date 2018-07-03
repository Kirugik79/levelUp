
import base64
import requests
from datetime import datetime
import hashlib
import json

access_token_path = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

consumer_key="ELaBRaUrjYBJPeN8ImXC5rb7yQCxmsJA"
consumer_password="4AhsWhDLYHxJyAuP"
shortcode = 174379
passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
Timestamp = 20180702131745



api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
response = requests.get(access_token_path, auth=(consumer_key, consumer_password)).text
res=json.loads(response)
access_token = res['access_token']


Amount=int(input("Enter Amount: "))
phone_number=input("Enter Phone Number: ")

def get_access_token(self):
        url = self.api_url + self.access_token_path
        response = self.requests.get(url, auth=(self.consumer_key, self.consumer_password))
        if response.status_code == 200:
           data = response.json()
           self.access_token = "access-token"
           return self.access_token
        else:
           return None



def payload(self):
  string = self.shortcode + self.passPhrase + timestamp
  return base64.b64encode(string)


headers = {"Authorization": "Bearer %s" % access_token}
request = {
    "BusinessShortCode": "174379",
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwNzAyMTMxNzQ1",
    "Timestamp": "20180702131745",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA": "254710471328",
    "PartyB": "174379",
    "PhoneNumber": "254710471328",
    "CallBackURL": "http://requestbin.fullcontact.com/rae028ra",
    "AccountReference": "test",
    "TransactionDesc": "test"
    }
response = requests.post(api_url, json = request, headers=headers)

print (response.text)


