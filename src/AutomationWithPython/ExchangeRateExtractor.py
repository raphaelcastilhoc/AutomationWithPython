import requests
import json
from types import SimpleNamespace

currency = input('Type the currency: ')

baseAddrees = 'https://api.exchangerate.host/latest?base=%s' % currency

response = requests.get(baseAddrees)
response.raise_for_status()

exchangeRateData = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))

print('Value in real: %s' % exchangeRateData.rates.BRL)
print('Value in dollar: %s' % exchangeRateData.rates.USD)
print('Value in euro: %s' % exchangeRateData.rates.EUR)