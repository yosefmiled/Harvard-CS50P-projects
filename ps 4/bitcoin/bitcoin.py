import json
import requests
import sys

try:
    if len(sys.argv) != 2 :
        sys.exit("Missing command-line argument ")
    try:
        n = float(sys.argv[1])
    except ValueError :
        sys.exit("Command-line argument is not a number")
    r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=ba7236233449145e6f357057a595719397f8a115b3892126b54451fb2004b326")
    d = r.json()
    data = d['data']
    price = float(data['priceUsd'])
    amount= price*n
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit


