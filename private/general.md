# Private General Endpoints

## Private endpoints V1

* [Payment Methods](#payment-methods)
* [Country Payment Methods](#country-payment-methods)
* [Countrycodes](#countrycodes)
* [Currencies](#currencies)
    
Base URL is https://api.bitcoin.global

Endpoint example: https://api.bitcoin.global/api/v1/{endpoint}

All endpoints return time in Unix-time format.

All endpoints return either a __JSON__ object or array.

For receiving responses from API calls please use http method __GET__

If an endpoint requires parameters you should send them as `query string`

___
#### Error messages V1 format:

```json5
{
    "error_message": "ERROR MESSAGE"
}
```
___
### Payment Methods

```
[GET] /api/v1/payment_methods
```
Returns a list of valid payment methods. Also contains name and code for payment methods, and possible limitations in currencies and bank name choices.

**Response is cached for:**
_1 second_

**Parameters:**
NONE

**Response:**
```json5
{
  "data": {
        "methods": {
            "bank": {
                "code": "BANK",
                "name": "Bank",
                "currencies": [
                    "USD",
                    "RUB",
                    ...
                ]
            },
            {
                ...
            }
        }
    }
}
```
___

### Country Payment Methods

```
[GET] /api/v1/payment_methods/{country_code}
```
List of valid payment methods in the specific country.

**Response is cached for:**
_1 second_

**Parameters:**
NONE

**Response:**
```json5
{
  "data": {
        "methods": {
            "bank": {
                "code": "BANK",
                "name": "Bank",
                "currencies": [
                    "USD",
                    "RUB",
                    ...
                ]
            },
            {
                ...
            }
        }
    }
}
```
___

### Countrycodes

```
[GET] /api/v1/countrycodes
```
List of valid countrycodes on Bitcoin Global.

**Response is cached for:**
_1 second_

**Parameters:**
NONE

**Response:**
```json5
{
    "data": {
        "cc_list": [
            "BY",
            "MR",
            "LT",
            "BD",
            ...
        ]
    }
}
```
___


### Currencies

```
[GET] /api/v1/currencies
```
List of valid fiat currencies on Bitcoin Global.

**Response is cached for:**
_1 second_

**Parameters:**
NONE

**Response:**
```json5
{
    "currencies": {
        "collection": {
            "USDT": {
                "name": "USD Tether",
                "altcoin": true
            },
            "XAR": {
                "name": "XAR",
                "altcoin": false
            },
            ...
        }
    }
}
```