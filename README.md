# Official Documentation of Bitcoin Global API

## Public API

[Public General API](./Public/websocket.md) - General purpose endpoints

[Public Ads API](./Public/http-v1.md) - Ads management

[Public Wallet API](./Public/http-v2.md) - Wallet management

___

## Private API

[Private Ads API](./Private/http-auth.md) - Ads management

[Private Wallet API](./Private/http-v1.md) - Wallet management

[Private Trade API](./Private/http-trade-v4.md) - Private trading endpoints (in progress)

---

## Info HTTP

1. WhiteBIT API supports `private` and `public` methods.
2. Available API versions: `V1`.
3. Using **Public endpoints**:
    1. Public endpoints are cached. You can find specific cache refresh interval for each particular request in API documentation.
    2. Use HTTP method `GET` method when making a request.
    3. Use `query string` if you need to send additional params.
4. Using **Private endpoints**:
    1. To make private API calls:
        1. Go to your account on [Bitcoin Global](https://bitcoin.global).
        2. Click on the Settings -> API tab.
        3. Generate a new key or use an existing one.
    2. Auth request should include:
        1. `'Content-type': 'application/json'`
        2. `'X-TXC-APIKEY': api_key` - where api_key is your public Bitcoin Global API key
        3. `'X-TXC-PAYLOAD': nonce'` - where nonce is a timestamp in miliseconds
        4. `'X-TXC-SIGNATURE': signature` - where signature is `hmac.new(secret_key, payload, hashlib.sha256).hexdigest().upper()`
            1. **payload** should be created based on the following values:
                - `'nonce'` - where nonce is a timestamp in miliseconds
                - `'api_key'` - where api_key is your public Bitcoin Global API key
                - `'path'` - where path is method path without base URL (e.g. `'/api/v1/dashboard'`)
                - `'params'` - where params are urlencoded params of your request (e.g. `'ticker=BTC&limit=15&offset=0'`)
    3. To help you get started with our API, we've created the [API Quick start helper](./quick-start) library. It supports the following languages:
        1. [Python](./quick-start/python_auth.py)