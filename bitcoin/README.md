Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

This program :
1) Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy. If that argument cannot be converted to a float, the program exits via sys.exit with an error message.
2) Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. The CoinCap API returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
3) Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places, using , as a thousands separator.

Make sure to install requests library by passing the command - pip install requests
Also generate an api key by visting https://pro.coincap.io/signup and paste the api key in code in place of 'YourAPIKey'
