import threading
import json
import requests
import csv

mainCurrencies = ['BRL', 'USD', 'EUR', 'CNY', 'JPY']
exchangeRateBaseUrl = 'https://api.exchangerate.host/latest?base=%s'
csvHeader = ['CURRENCY BASE', 'BRL', 'USD', 'EUR', 'CNY', 'JPY']

def showExchangeRate(currency):
    exchangeRateUrl = exchangeRateBaseUrl % currency
    response = requests.get(exchangeRateUrl)
    response.raise_for_status()

    exchangeRateData = json.loads(response.text)

    csvFileName = '%s.csv' % currency
    outputFile = open(csvFileName, 'w', newline='')
    outputWriter = csv.writer(outputFile, delimiter = ';')

    outputWriter.writerow(csvHeader)

    exchangeRateRow = [currency]
    for currencyName in mainCurrencies:
        exchangeRateRow.append(exchangeRateData['rates'][currencyName])

    outputWriter.writerow(exchangeRateRow)


exchangeRateThreads = []
for currency in mainCurrencies:
     exchangeRateThread = threading.Thread(target=showExchangeRate, args=(currency,))
     exchangeRateThreads.append(exchangeRateThread)
     status = exchangeRateThread.start()

for exchangeRateThread in exchangeRateThreads:
    exchangeRateThread.join()

print('Finished')

