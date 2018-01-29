#Working
import requests
import json
import time		#to refresh scans, repeat function
import sys		#to print in one line
#MY BITCOIN:
myBTC = 0.012716460
myDollar = 148					
profit = 0
profit_past = 0
firstTimeRunning = True
count = 0
sys.stdout.write("CURRENT INVESTMENT,    GAIN/LOSS    |   BTC/USD   |   CHANGES\n")
def calcProfits():
	global firstTimeRunning
	global profit
	global profit_past
	global count
#GET CURRENT PRICE OF BITCOIN:
	url = 'https://api.gdax.com/products/BTC-USD/trades'
	res = requests.get(url)
	json_res = json.loads(res.text) 		#"json_res" got a ton of stuff. the price is in "json_res[0]""
	currDollarBit = json_res[0]['price']    #current dollars per bitcoin. 'price' is the location in the 0th index of "jason_res"
	currDollarBit = float(currDollarBit)    #turning to float to make calculations
	currDollar = round(myBTC * currDollarBit, 3)
	profit = round(currDollar - myDollar, 3)
    
#Calculate Profits:
	if (profit == 0):  #if im gaining money
		sys.stdout.write("base: $" +  str(abs(currDollar)) + "   $" +  str(abs(profit)) + "   |   ")
	elif (profit > 0):  #if im gaining money
		sys.stdout.write("gain: $" +  str(abs(currDollar)) + "   +$" + str(abs(profit)) + "   |   ")
	elif (profit < 0):  	#if im losing money
		sys.stdout.write("loss: $" +  str(abs(currDollar)) + "   -$" + str(abs(profit)) + "   |   ")
#Calculate My Current Profit:
	
#Calculate Percent Change/slope
	sys.stdout.write("BTC/USD: " + str(currDollarBit) + "   |   ")  #current BTC/USD
	if (firstTimeRunning == True):
		firstTimeRunning = False
		profit_past = profit
		print("\nChanged Last Profit")
	if (profit != profit_past):
		if (profit > profit_past):
			diff = abs(round(profit - profit_past, 4))
			sys.stdout.write("+$" + str(diff) + "    ")    		#print $ +rounded change 
			percent_change = abs(round(diff/profit_past,4))
			sys.stdout.write("+" + str(percent_change) + "%\n")	#print % +rounded change
			
		if (profit < profit_past):
			diff = abs(round(profit_past - profit, 4))
			sys.stdout.write("-$" + str(diff) + "    ")			#print $ -rounded change 
			percent_change = abs(round(diff/profit_past, 4))
			sys.stdout.write("-" + str(percent_change) + "%\n")	#print % -rounded change
	if (profit == profit_past):
			sys.stdout.write("NO CHANGE" + '\n')			
#PRINT TO HTML:
	htmlf = open('profit.html', 'w') #paste the profit onto the profit.html file!
	htmlf.write(str(profit))
	htmlf.close()
#REFRESH:
	count += 1
	if (count == 60):       	#after 60 repeats, reset the past profit
		count = 0;
ss		firstTimeRunning = True
	time.sleep(1)	#program take .5s to execute. so making it refresh at .9s
while True:
	calcProfits()
	
