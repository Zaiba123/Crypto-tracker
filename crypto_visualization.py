import requests 
import pandas as pd
from pandas import DataFrame
from IPython.core.display import HTML




r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')  #to timeout on request 
r_data = r.json()

data_list = []
image_list = []

for i in range(len(r_data)):
    data_list.append((r_data[i]["id"],r_data[i]["current_price"],r_data[i]["market_cap"]))


for i in range(len(r_data)):
    image_list.append((r_data[i]["image"]))

df = DataFrame (data_list,columns=['id','current price','market cap'])
df['Images'] = image_list
print (df)

