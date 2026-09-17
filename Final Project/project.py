#A small command-line tool that  calls a free public API and prints the results in a clean format

import requests
import sys
import json


def main():
    if len(sys.argv) != 2:
        sys.exit("Coin denomination missed or incorrect number of arguments")

    price, change = get_coin_data(sys.argv[1])
    price_formated = format_price(price)
    change_data = parse_change(change)
    print(price_formated)
    print(change_data)

def get_coin_data(coin_id):
    try:
        response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd&include_24hr_change=true")
        data = response.json()
        if coin_id not in data:
            sys.exit("Unknown coin")
        return data[coin_id]["usd"], data[coin_id]["usd_24h_change"]

    except (requests.RequestException):
        sys.exit("Please try a bit later")


def format_price(number):
    return f"${number:,.2f}"

def parse_change(change):
    if change >= 0:
        return f"▲ {change:.2f}% (up)"
    else:
        return f"▼ {abs(change):.2f}% (down)"


if __name__ == "__main__":
    main()
