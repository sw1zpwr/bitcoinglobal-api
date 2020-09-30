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
### My ads

```
[GET] /api/v1/ad-get/{id}
```