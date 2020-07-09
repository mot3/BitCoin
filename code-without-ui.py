import urllib.request, json

currency = input('ENTER a currency = ')

url = f'https://api.coinbase.com/v2/prices/BTC-{currency}/buy'

response = urllib.request.urlopen(url)

data = response.read()

price = float(json.loads(data)['data']['amount'])

print ('price:', price)