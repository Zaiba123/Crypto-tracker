import requests 
import pandas as pd
from pandas import DataFrame


r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')  #to timeout on request 
r_data = r.json()
# id = []
data_tuple = []
# for i in range(len(r_data)):
#     id.append(r_data[i]["id"])

for i in range(len(r_data)):
    data_tuple.append((r_data[i]["id"],r_data[i]["current_price"],r_data[i]["market_cap"]))
data_tuple = tuple(data_tuple)


df = DataFrame (data_tuple,columns=['id','current_price','market_cap'])
print (df)

# print(data_tuple)