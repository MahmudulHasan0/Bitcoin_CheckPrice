
#Working
import requests
import json

#getting current price:
url = 'https://api.gdax.com/products/BTC-USD/trades'
res = requests.get(url)
json_res = json.loads(res.text)
currDollarBit = json_res[0]['price'] #current dollars per bitcoin
currDollarBit = float(currDollarBit)    #turning to float to make calculations

#what i have:
myBTC = 0.008385640 
myDollar = 99 					#what i put in

#calculate:
# Current: 1BTC = currentDollar
# Mine:    0.008385640BTC = $99 
currDollar = myBTC * currDollarBit
print("Current Dollar/Bitcoin: " + str(currDollar))

profit = currDollar - 99 

if (profit < 0):  	#if im losing money
	print("loss: $" + str(profit))
elif (profit > 0):  #if im gaining money
	print("profit: $"+  str(profit))




