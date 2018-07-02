
import base64
import requests
from datetime import datetime
import hashlib
import json

access_token_path = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

consumer_key="ELaBRaUrjYBJPeN8ImXC5rb7yQCxmsJA"
consumer_password="4AhsWhDLYHxJyAuP"
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
response = requests.get(access_token_path, auth=(consumer_key, consumer_password)).text
res=json.loads(response)
access_token = "access-token"

headers = {"Authorization": "Bearer %s" % access_token}
request = {
    "BusinessShortCode": "174379",
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwNzAyMTMxNzQ1",
    "Timestamp": "20180702131745",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA": "254726226149",
    "PartyB": "174379",
    "PhoneNumber": "254726226149",
    "CallBackURL": "http://requestbin.fullcontact.com/rae028ra",
    "AccountReference": "test",
    "TransactionDesc": "test"
    }

def get_access_token(self):
        url = self.api_url + self.access_token_path
        response = self.requests.get(url, auth=(self.consumer_key, self.consumer_password))
        if response.status_code == 200:
           data = response.json()
           self.access_token = "access-token"
           return self.access_token
        else:
           return None
response = requests.post(api_url, json = request, headers=headers)
print (response.text)


def get_password(self):
        pass


