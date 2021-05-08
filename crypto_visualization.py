import requests 
import pandas as pd

r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')  #to timeout on request 
r_data = r.json()
id = []
for i in range(len(r_data)):
    id.append(r_data[i]["id"])

print(id)
