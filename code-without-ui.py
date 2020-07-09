import urllib.request, json

url = 'https://api.coinbase.com/v2/prices/BTC-USD/buy'
response = urllib.request.urlopen(url)

data = response.read()

price = float(json.loads(data)['data']['amount'])

print ('price:', price)