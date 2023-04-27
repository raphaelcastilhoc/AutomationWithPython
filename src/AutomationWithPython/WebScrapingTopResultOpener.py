import requests, webbrowser, bs4

searchTerm = input('Type the search term: ')
seacrhSiteBaseUrl = 'https://pypi.org'
maxQuantityTopResult = 5

print('Searching...')

response = requests.get('%s/search/?q=%s' % (seacrhSiteBaseUrl, searchTerm))
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, 'html.parser')
linkElements = soup.select('.package-snippet')
linksQuantity = min(maxQuantityTopResult, len(linkElements))

for i in range(linksQuantity):
    urlToOpen = seacrhSiteBaseUrl + linkElements[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

print('Links opened on browser.')
