#In a file called bitcoin.py, implement a program that:
#Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
#Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
#import requests
#try:
#    ...
#except requests.RequestException:
#    ...
#Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places, using , as a thousands separator.

import requests
import sys
import json

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bt = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument ")
        
    get_bitcoin_price(bt)

def get_bitcoin_price(bt_):
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=9691234f8d6f006119d32d4e336c88bd99ca34b34b6b991d87640ffbaa36ed17")

        #print(json.dumps(response.json(), indent=2))#print the response in json format

        data = response.json()["data"]
        price = float(data["priceUsd"])

        total = price * bt_
        print(f"${total:,.4f}")

    except (requests.RequestException, KeyError):
        print("Please try a bit later")

main()