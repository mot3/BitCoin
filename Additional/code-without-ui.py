import json, requests, urllib

#currency = input('ENTER a currency = ')

url = f'https://api.coinbase.com/v2/prices/BTC-USD/sell'

response = urllib.request.urlopen(url)

data = response.read()

price = float(json.loads(data)['data']['amount'])

print ('price:', price)

key = 'JFGN2c6leJDktgSkIbrXezvEOa0ZxrS2'
url = f'http://api.navasan.tech/latest/?api_key={key}'

r = requests.get(url)

data = r.json()

price = data["usd_sell"]["value"]
print('USD TO IRI : ', price)