import requests
import json
import datetime


def stock_price(symbol, api_key):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-statistics"

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    return float(requests.request("GET", url, headers=headers, params={"symbol": symbol}).json()["price"]["postMarketPrice"]["fmt"].replace(',', ''))


def stock_history(symbol, api_key, timespan_start=None, timespan_end=None, input_date_format="%b %d, %Y", output_date_format="%b %d, %Y"):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"

    querystring = {"symbol": symbol, "region": "US"}

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    if timespan_start is not None:
        start_strptime = datetime.datetime.strptime(timespan_start, input_date_format)
    if timespan_end is not None:
        end_strptime = datetime.datetime.strptime(timespan_end, input_date_format)

    prices = requests.request("GET", url, headers=headers, params=querystring).json()["prices"]
    if timespan_start is None and timespan_end is None:
        return {
            datetime.datetime.fromtimestamp(price["date"]).strftime(output_date_format): price for price in prices}
    elif timespan_start is None:
        return {datetime.datetime.fromtimestamp(price["date"]).strftime(output_date_format): price for price in prices if datetime.datetime.fromtimestamp(price["date"]) <= end_strptime}
    elif timespan_end is None:
        return {datetime.datetime.fromtimestamp(price["date"]).strftime(output_date_format): price for price in prices if datetime.datetime.fromtimestamp(price["date"]) >= start_strptime}
    else:
        return {datetime.datetime.fromtimestamp(price["date"]).strftime(output_date_format): price for price in prices if start_strptime <= datetime.datetime.fromtimestamp(price["date"]) <= end_strptime}
