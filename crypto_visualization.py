import requests 
import pandas as pd
from pandas import DataFrame
from IPython.core.display import HTML




r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')  #to timeout on request 
r_data = r.json()
# id = []
data_list = []
image_list = []
# for i in range(len(r_data)):
#     id.append(r_data[i]["id"])

for i in range(len(r_data)):
    data_list.append((r_data[i]["id"],r_data[i]["current_price"],r_data[i]["market_cap"]))


for i in range(len(r_data)):
    image_list.append((r_data[i]["image"]))

# data_tuple = tuple(data_tuple)
#image_list = tuple(image_list)
print(image_list)


# df = DataFrame (data_tuple,columns=['id','current_price','image'])
# print (df)

# print(data_tuple)