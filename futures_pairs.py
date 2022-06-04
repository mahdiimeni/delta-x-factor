import pandas as pd
import requests, json, urls


class Futures_Pairs:
    def __init__(self, exchange_name):
        self.exchange = exchange_name

    def token_collector(self):
        # -- recieves exchanges futures pairs from Coingecko API
        raw_data = requests.get(urls.exchange_url(self.exchange)).text

        # -- raw data to json
        data_list = json.loads(raw_data)
        data_list = data_list["tickers"]

        # -- data frame operation
        df = pd.DataFrame(data_list)
        df = df[["base", "target"]]

        usdt_pairs = df[df["target"] == "USDT"]
        usd_pairs = df[df["target"] == "USD"]

        # -- Joins two dataframes together!
        target_pairs = pd.concat([usdt_pairs, usd_pairs])

        filtered_coin_list = (
            target_pairs["base"].drop_duplicates().to_list()
        )  # -- drop_duplicates() removes repetitive tokens

        # -- final list operation
        futures_coin_list = []
        for item in filtered_coin_list:
            futures_coin_list.append(item.lower())

        return futures_coin_list
