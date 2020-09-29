import json
import base64
import requests
import time
import hmac
import hashlib
​
api_key = 'YOUR_API_KEY' #put here your public key
secret_key = 'YOUR_SECRET_KEY' #put here your secret key
path = '/api/v1/dashboard' #put here request path. 
getParams = 'ticker=BTC&limit=15&offset=0' #request params (if any)
nonce = str(int(time.time() * 1000)) #nonce is a timestamp in miliseconds
request = '/api/v1/dashboard?ticker=BTC&limit=15&offset=0' #put here your request with base URL
baseUrl = 'https://api.bitcoin.global'  #base URL: api.bitcoin.global
​
#preparing payload
completeUrl = baseUrl + request
payload = nonce + api_key + path + getParams
signature = hmac.new(secret_key.encode('utf-8'), payload.encode('utf-8'), hashlib.sha256).hexdigest().upper()
​
#preparing headers
headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    'Apiauth-Key': api_key,
    'Apiauth-Nonce': nonce,
    'Apiauth-Signature': signature
}
​
#sending request
resp = requests.get(completeUrl, headers=headers)
​
print(resp)