#!/usr/bin/env python3

#REFERENCE: https://www.youtube.com/watch?v=txKBWtvV99Y&list=PLRwV8PM4b0OAOn-ayvzv4lNcbQyhovnFI&index=7&t=165s

from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "4b5990cbe8cd0cc07067"

printer = PrettyPrinter()

def get_currency():
    endpoint = f'api/v7/currencies?apiKey={API_KEY}'
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())
    data.sort()

    return data

def print_currency(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f'{_id} - {name} - {symbol}')

def exchange_rate(currency1, currency2):
    endpoint = f'api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}'
    url = BASE_URL + endpoint
    data = get(url).json()

    if len(data) == 0:
        print("Invalid Currency(s).")
        return

    rate = list(data.values())[0]
    print(f'{currency1} --> {currency2} = {rate}')
    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print("Invalid Amount.")
        return

    converted = rate * amount
    print(f'{amount} {currency1} is equal to {converted} {currency2}')
    return converted

def main():
    currencies = get_currency()

    print("COMMANDS:")
    print("List - lists all currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        com = input("Enter a command (q to quit):  ").lower()

        if com == "q":
            break
        elif com == "list":
            print_currency(currencies)
        elif com == "convert":
            currency1 = input("Enter a base currency:  ").upper()
            amount = input("Enter amount in {currency1}:  ")
            currency2 = input("Enter currency to convert to:  ").upper()
            convert(currency1, currency2, amount)
        elif com == "rate":
            currency1 = input("Enter a base currency:  ").upper()
            currency2 = input("Enter currency to convert to:  ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognised Command!")

main()