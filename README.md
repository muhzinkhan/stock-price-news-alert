# Stock Price Alert News

## Overview

The Stock Price Alert News script is a Python application that monitors a specific stock (default: Tesla) and sends an SMS alert to the user when the stock price changes by a fixed percentage (default: 5%) compared to the previous two days' closing prices.

## Features

- Monitors the stock price of a specified company (default: Tesla).
- Sends an SMS alert when the stock price changes by a set percentage (default: 5%).
- Provides valuable information for timely decision-making in the stock market.

## Requirements

- [Python 3.x](https://www.python.org/downloads/)
- [Twilio API credentials](https://www.twilio.com/docs/usage/api) (For SMS service)
- [News API](https://newsapi.org/docs) (For delivering the related news)
- [Alpha Vantage API](https://www.alphavantage.co/) (A Stock market API)

## Installation

1. Clone or download the repository to your local machine.
2. Ensure you have Python 3.x installed on your system.
3. Sign up for a [Twilio](https://www.twilio.com/docs/usage/api)
account and obtain your Account SID, Auth Token, and Twilio phone number.
4. Sign up for access to [Alpha Vantage](https://www.alphavantage.co/)
and obtain the API key.
5. Create a `.env` file with your API credentials.

## Usage

1. Open/create the `.env` file and populate the following environment variable.
   - `NEWS_API_KEY`
   - `STOCK_API_KEY`
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `RECIPIENT_NUMBER`
   - `MY_TWILIO_NUMBER`

2. Run the `stock_price_alert.py` script.

## Configuration

You can customize the following parameters in `config.py`:

- `STOCK_NAME`: The stock symbol you want to monitor (e.g., TSLA for Tesla).
- `NEWS_QUERY`: The search query for the new articles from *newsapi.org*
- `PRICE_CHANGE_PERCENTAGE`: The percentage change threshold for triggering an alert.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Twilio](https://www.twilio.com/) for their SMS service.
- [Alpha Vantage](https://www.alphavantage.co/) for providing stock market data.

## Contributing

If you'd like to contribute, please fork the repository and create a pull request. Please make sure to update tests as appropriate.

## Support

If you encounter any issues or have suggestions, please [open an issue](https://github.com/muhzinkhan/stock-price-news-alert/issues).

## Roadmap

- [ ] Implement support for monitoring multiple stocks.
- [ ] Add option for email alerts in addition to SMS.
- [ ] Create a web interface for easy setup and configuration.

## Authors

- [Muhsin Khan](https://github.com/muhzinkhan)

## Disclaimer

This script is provided as-is, without any warranty or guarantee of any kind. Use at your own risk.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
