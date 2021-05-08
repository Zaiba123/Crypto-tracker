import requests 

r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')  #to timeout on request 

r_data = r.json()
to_find = input("Enter the name of the crypto: ")
#print(r_dict['form'])
for i in range(len(r_data)):
    if r_data[i]["id"] == to_find:
        print("The price of {} is {} and the marketcap is {}.".format(r_data[i]["id"], r_data[i]["current_price"],r_data[i]["market_cap"]))
        # print("The marketcap of {} is {}.".format(r_data[i]["id"], r_data[i]["market_cap"]))
