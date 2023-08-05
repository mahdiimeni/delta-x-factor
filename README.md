# Crypto X-Factor

Crypto X-Factor is a Python-based tool for tracking and analyzing cryptocurrency market data over time. It focuses on calculating a custom "X-Factor" metric to identify potential "gainer" coins based on trading volume versus market capitalization.

## Overview

The X-Factor is calculated as:

```python
X-Factor = Total Trading Volume / Market Capitalization
```

Coins with a higher X-Factor have high trading volume relative to their market cap. This may indicate increased interest and potential upside for the coin.

The tool currently fetches current market data from the CoinGecko API, including:

- Current price
- 24 hour trading volume  
- Market capitalization

It then filters the coins by futures trading pairs on a specified exchange, ranks them by X-Factor, and displays the top results in a table.

## Features

- Fetch market data for top coins from CoinGecko API
- Calculate custom X-Factor metric (Volume/Market Cap)
- Filter results to futures trading pairs on selected exchange 
- Rank coins by X-Factor and display leaderboard
- Modular design using classes for data fetching and processing

## Getting Started

### Prerequisites

- Python 3.6+
- `requests` module
- API keys for CoinGecko (free)

### Usage

- Clone the repo
- Install dependencies
- Get CoinGecko API keys 
- Run `python main.py`
- Input desired parameters when prompted
- View ranked X-Factor results

## Roadmap

Planned future features:

- Historical data storage and comparison
- Automated, scheduled runs  
- Expand exchange and coin coverage
- More metrics and visualizations
- Web interface or dashboard

## Contributing

Contributions are welcome! Open an issue or PR for enhancements or fixes.

## License

This project is MIT licensed. See `LICENSE` for details.
