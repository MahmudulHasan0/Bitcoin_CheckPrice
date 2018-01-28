#Working
import requests
import json
import time

#what i have:
myBTC = 0.008385640 
myDollar = 99 					#what i put in


def calcProfits():
	#getting current price:
	url = 'https://api.gdax.com/products/BTC-USD/trades'
	res = requests.get(url)
	json_res = json.loads(res.text) 		#"json_res" got a ton of stuff. the price is in "json_res[0]""
	currDollarBit = json_res[0]['price']    #current dollars per bitcoin. 'price' is the location in the 0th index of "jason_res"
	currDollarBit = float(currDollarBit)    #turning to float to make calculations


	#calculate:
	# Current: 1BTC = currentDollar
	# Bought:  0.008385640BTC = $99 
	currDollar = myBTC * currDollarBit
	#print("Current Dollar/Bitcoin: " + str(currDollar))

	profit = currDollar - 99 
	if (profit < 0):  	#if im losing money
		print("loss: $" + str(profit))
	elif (profit > 0):  #if im gaining money
		print("profit: $"+  str(profit))
	time.sleep(.6)	#program take .5s to execute. so making it refresh at .6s

while True:
	calcProfits()




