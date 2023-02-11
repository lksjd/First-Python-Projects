from requests import get

BASE_URL = "https://free.currconv.com/"
API_KEY = "da7c6bf30119ea0eea06"

def get_currencies():
    end_point = f"api/v7/currencies?apiKey={API_KEY}"
    
    url = BASE_URL + end_point
    data = get(url).json()['results']
    
    data = list(data.items())
    data.sort()
    
    return data
def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get('currencySymbol', '')
        print(f'{_id} - {name} - {symbol}')

def exchange_rate(currency1, currency2):
    end_point = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + end_point
    data = get(url).json()
    
    if len(data) == 0:
        print('Invalid currencies')
        return
    
    rate = list(data.values())[0]
    
    print(f'{currency1} -> {currency2} = {rate}')
    return rate
    

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    
    if rate is None:
        return
    
    try:
        amount = float(amount)
    except:
        print('Invalid amount')
        return
    
    converted_amount = rate * amount
    print(f'{amount} {currency1} is equal {converted_amount} {currency2}')
    return converted_amount

def main():
    currencies = get_currencies()
    
    print('Welcome to the currency converter!')
    print('List - lists the different currencies')
    print('Convert - convert from one currency to another')
    print('Rate - get the exchange rate ot two currencies')
    print()
    
    while True:
        command = input('Enter a command (q to quit): ').lower()
        
        if command == 'q':
            break
        elif command == 'list':
            print_currencies(currencies)
        elif command == 'convert':
            currency1 = input('Enter a base currency: ').upper()
            amount = input(f'Enter an amount in {currency1}: ')
            currency2 = input('Enter a currency to convert to: ').upper()
            convert(currency1, currency2, amount)
        elif command == 'rate':
            currency1 = input('Enter a base currency: ').upper()
            currency2 = input('Enter a currency to convert to: ').upper()
            exchange_rate(currency1, currency2)
        else:
            print('Unrecognized command!')

main()
    
