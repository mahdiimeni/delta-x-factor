def data_url(page):
    URL = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page={page+1}&sparkline=false"
    return URL


def historical_data_url(token_id, date):
    URL = f"https://api.coingecko.com/api/v3/coins/{token_id}/history?date={date}&localization=false"
    return URL


def exchange_url(exchange):
    URL = f"https://api.coingecko.com/api/v3/derivatives/exchanges/{exchange}?include_tickers=all%2C%20unexpired"
    return URL
