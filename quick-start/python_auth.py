import json
import base64
import requests
import time
import hmac
import hashlib
​
#general, ads, trade
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


#wallet
api_key = 'YOUR_API_KEY'
secret_key = 'YOUR_SECRET_KEY'
data = {'id': 435}
nonce = int(time.time())
if data:
    dumped = json.dumps(data, ensure_ascii=False)
else:
    dumped = ''
signature = hmac.new(secret_key.encode('utf-8'),
                "{}{}".format(nonce, dumped)
                .encode('utf-8'), hashlib.sha256).hexdigest()
headers = {
    'Content-Type': 'application/json',
    'X-API-KEY': api_key,
    'X-ACCESS-SIGN': signature,
    'X-ACCESS-TIMESTAMP': str(nonce)
}
resp = requests.post('https://api.bitcoin.global/api/simple-wallet/wallet/transaction', 
                     data=json.dumps(data),
                     headers=headers)
print(resp.json())  