import requests
import sys

# Missing argument
try:
    arg = sys.argv[1]
except IndexError:
    sys.exit("Missing command-line argument")

# Invalid
try:
    n = float(arg)
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")
    data = response.json()

    price = float(data["data"]["priceUsd"])
    total = n * price

    print(f"${total:,.4f}")

except requests.RequestException:
    sys.exit("API request failed")
