exchanges_names = {
    "1": "binance_futures",
    "2": "coinex_futures",
    "3": "okex_swap",
    "4": "kumex",
    "5": "ftx",
}


def exchange_selector():
    user_choice = input(
        """Enter your exchange number: [1]-Binance / [2]-CoinEx / [3]-OKX / [4]-KuCoin / [5]-FTX 

                                      >>>  """
    ).lower()
    selected_exchange = exchanges_names[user_choice]
    return selected_exchange
