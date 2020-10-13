# Private Ads Endpoints

## Private endpoints V1

* [My ads](#my-ads)
* [Single ad](#my-ads)
    
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
### My ads

```
[GET] /api/v1/ads
```
Returns all advertisements of the authenticated user.

**Response is cached for:**
_1 second_

**Parameters:**
Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
countrycode | String | **Yes** | Requested country. Example: US
currency | String | **Yes** | Requested currency Example: USD
trade_type | String | **Yes** | Sell or buy orders. Example: ONLINE_SELL, ONLINE_BUY

**Response:**
```json5
{
    "data": {
        "ad_list": {
            "data": [
                {
                    "ad_id": "6112eb2e-62e4-4d20-5015-as3b92d33823",
                    "countrycode": "RU",
                    "currency": "RUB",
                    "max_amount": null,
                    "min_amount": null,
                    "max_amount_available": "0",
                    "online_provider": "SPECIFIC_BANK",
                    "profile": {
                        "username": "username",
                        "feedback_score": "100",
                        "trade_count": 27,
                        "last_online": "2020-09-30T11:51:05+00:00",
                        "name": "username (27; 100%)"
                    },
                    "bank_name": "Any bank",
                    "trade_type": "ONLINE_SELL",
                    "payment_window_minutes": null,
                    "display_reference": true,
                    "created_at": "2020-08-10T13:52:33+00:00",
                    "require_feedback_score": 0,
                    "msg": "description",
                    "account_info": "ad info",
                    "volume_coefficient_btc": "5",
                    "temp_price": "302592.77881299",
                    "temp_price_usd": "302592.77881299",
                    "hidden_by_opening_hours": false,
                    "require_identification": false,
                    "is_local_office": false,
                    "first_time_limit_btc": "0",
                    "city": "",
                    "location_string": "Russia",
                    "opening_hours": null,
                    "lon": 0,
                    "sms_verification_required": false,
                    "require_trade_volume": "0",
                    "limit_to_fiat_amounts": null,
                    "require_trusted_by_advertiser": false,
                    "track_max_amount": false,
                    "lat": 0,
                    "price_equation": "btc_in_usd*usd_in_uah",
                    "visible": false,
                    "atm_model": null,
                    "reference_code": "YTliNzM2",
                    "reference_type": "SHORT"
                },
                {
                    ...
                }
            ]
        },
        "ad_count": 2
    }
}
```
___
### Single Ad

```
[GET] /api/v1/ad-get/{id}
```
Returns a specific advertisement of the authenticated user.

**Response is cached for:**
_1 second_

**Parameters:**
Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
id | String | **Yes** | Requested ad id. Example: 6112eb2e-62e4-4d20-5015-as3b92d33823

**Response:**
```json5
{
    "data": {
        "ad_id": "6112eb2e-62e4-4d20-5015-as3b92d33823",
        "countrycode": "RU",
        "currency": "RUB",
        "max_amount": null,
        "min_amount": null,
        "max_amount_available": "0",
        "online_provider": "SPECIFIC_BANK",
        "profile": {
            "username": "username",
            "feedback_score": "100",
            "trade_count": 27,
            "last_online": "2020-09-30T11:51:05+00:00",
            "name": "username (27; 100%)"
        },
        "bank_name": "Any bank",
        "trade_type": "ONLINE_SELL",
        "payment_window_minutes": null,
        "display_reference": true,
        "created_at": "2020-08-10T13:52:33+00:00",
        "require_feedback_score": 0,
        "msg": "description",
        "account_info": "ad info",
        "volume_coefficient_btc": "5",
        "temp_price": "302592.77881299",
        "temp_price_usd": "302592.77881299",
        "hidden_by_opening_hours": false,
        "require_identification": false,
        "is_local_office": false,
        "first_time_limit_btc": "0",
        "city": "",
        "location_string": "Russia",
        "opening_hours": null,
        "lon": 0,
        "sms_verification_required": false,
        "require_trade_volume": "0",
        "limit_to_fiat_amounts": null,
        "require_trusted_by_advertiser": false,
        "track_max_amount": false,
        "lat": 0,
        "price_equation": "btc_in_usd*usd_in_uah",
        "visible": false,
        "atm_model": null,
        "reference_code": "YTliNzM2",
        "reference_type": "SHORT"
    }
}
```

### Сomma-separated list of ad id(s)

```
[GET] /api/v1/ad-get/{id}
```
Returns all advertisements from a comma-separated list of ad IDs.

**Response is cached for:**
_1 second_

**Parameters:**
Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
id(s) | String | **Yes** | Requested ad id(s). Example: 6112eb2e-62e4-4d20-5015-as3b92d33823,6112eb2e-62e4-4d20-5015-as3b92d33864

**Response:**
```json5
**Response:**
```json5
{
    "data": {
        "ad_list": {
            "data": [
                {
                    "ad_id": "6112eb2e-62e4-4d20-5015-as3b92d33823",
                    "countrycode": "RU",
                    "currency": "RUB",
                    "max_amount": null,
                    "min_amount": null,
                    "max_amount_available": "0",
                    "online_provider": "SPECIFIC_BANK",
                    "profile": {
                        "username": "username",
                        "feedback_score": "100",
                        "trade_count": 27,
                        "last_online": "2020-09-30T11:51:05+00:00",
                        "name": "username (27; 100%)"
                    },
                    "bank_name": "Any bank",
                    "trade_type": "ONLINE_SELL",
                    "payment_window_minutes": null,
                    "display_reference": true,
                    "created_at": "2020-08-10T13:52:33+00:00",
                    "require_feedback_score": 0,
                    "msg": "description",
                    "account_info": "ad info",
                    "volume_coefficient_btc": "5",
                    "temp_price": "302592.77881299",
                    "temp_price_usd": "302592.77881299",
                    "hidden_by_opening_hours": false,
                    "require_identification": false,
                    "is_local_office": false,
                    "first_time_limit_btc": "0",
                    "city": "",
                    "location_string": "Russia",
                    "opening_hours": null,
                    "lon": 0,
                    "sms_verification_required": false,
                    "require_trade_volume": "0",
                    "limit_to_fiat_amounts": null,
                    "require_trusted_by_advertiser": false,
                    "track_max_amount": false,
                    "lat": 0,
                    "price_equation": "btc_in_usd*usd_in_uah",
                    "visible": false,
                    "atm_model": null,
                    "reference_code": "YTliNzM2",
                    "reference_type": "SHORT"
                },
                {
                    "ad_id": "6112eb2e-62e4-4d20-5015-as3b92d33864",
                    ...
                }
            ]
        },
        "ad_count": 2
    }
}
```

### Create an ad

```
[POST] /api/v1/ad-create
```
Create a new advertisement.

**Response is cached for:**
_1 second_

**Parameters:**
Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
countrycode | string | **Yes** | Selected country for advertising. Example: RU
currency | string | **Yes** | Selected currency for advertising. Example: RUB
trade_type | string | **Yes** | Trade type. Example: ONLINE_SELL or ONLINE_BUY
coefficient | float | **Yes** | Margin. Example: 1
price_equation | string | **Yes** | Price equation formula. Example: btc_in_usd*BTC_in_UAH
account_info | string | **Yes** | Information for traders. Example: random text 
online_provider | string | **Yes** | Trade payment method. Example: NATIONAL_BANK
payment_method_name | string | **Yes** | Selected payment method. Example: payment_method_name
payment_window_minutes | integer | **Yes** | Payment window for traders, only for ONLINE_BUY ads. Example: 90
bank_name | string | **No** | Payment method additional information. Example: Random bank name
min_amount | integer | **No** | Min trade amount for this ad. Example: 10
max_amount | integer | **No** | Max trade amount for this ad. Example: 100
msg | string | **No** | Message displayed on ad page. Example: random text
volume_coefficient_btc | integer | **No** | Increased volume of the next trade with the same user. Example: 1
track_max_amount | boolean | **No** | Ad is bound to the max amount available on account. Example: false
first_time_limit_btc | integer | **No** | Limit amount for first trade of user. Example: 0
require_trade_volume | integer | **No** | Required past trade amount for starting trade. Example: 1
require_feedback_score | integer | **No** | Min feedback score required for starting trade. Example: 0
reference_type | string | **No** | Type of reference message. Example: SHORT
display_reference | boolean | **No** | Turn on/off displaying reference message for an ad. Example: true
visible | boolean | **No** | Turn on/off displaying an ad. Example: true
floating | boolean | **No** | Deprecated, but can be accessed for old libraries. Example: false
lat | integer | **No** | Deprecated, but can be accessed for old libraries. Example: 0
lon | integer | **No** | Deprecated, but can be accessed for old libraries. Example: 0
city | string | **No** | Deprecated, but can be accessed for old libraries. Example: city
location_string | string | **No** | Deprecated, but can be accessed for old libraries. Example: location_string
sms_verification_required | boolean | **No** | Deprecated, but can be accessed for old libraries. Example: false
require_trusted_by_advertiser | boolean | **No** | Deprecated, but can be accessed for old libraries. Example: false
require_identification | boolean | **No** | Deprecated, but can be accessed for old libraries. Example: false
opening_hours | array | **No** | Not implemented yet. Example: []