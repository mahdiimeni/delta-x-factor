import exchanges
import pandas as pd
import data_class as dc
import futures_pairs as coin


def pair_list():
    """Lists futures pairs by exchange."""
    exchange = exchanges.exchange_selector()
    pair_object = coin.Futures_Pairs(exchange)
    futures_pairs = pair_object.token_collector()

    return futures_pairs


def x_factor(pages: int):
    """Calculates vol/mktCap & returns a DataFrame."""
    data = dc.Data(pages)
    df = pd.DataFrame(data.instant_data())
    df = df[
        [
            "market_cap_rank",
            "id",
            "symbol",
            "current_price",
            "total_volume",
            "market_cap",
        ]
    ]

    volume = df["total_volume"]
    mktCap = df["market_cap"]

    x_factor = volume / mktCap
    df["X Factor"] = x_factor

    # --- collects futures pairs
    futures_pairs = pair_list()
    for _ in df.symbol:
        if _ not in futures_pairs:
            df = df[df["symbol"] != _]

    watchlist = df[
        [
            "market_cap_rank",
            "id",
            "symbol",
            "X Factor",
        ]
    ]

    # --- index editing block
    watchlist.reset_index(inplace=True, drop=True)
    watchlist.index += 1

    return watchlist


# TODO - pd.options.display.float_format = "{:.2f}".format
