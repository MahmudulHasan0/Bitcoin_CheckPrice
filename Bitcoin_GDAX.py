#Working
import requests
import json
import time		#to refresh scans, repeat function
import sys		#to print in one line

#MY BITCOIN:
myBTC = 0.01710293
myDollar = 197				
profit = 0
profit_past = 0
firstTimeRunning = True
count = 0
sys.stdout.write("CURRENT INVESTMENT   |    G/L DOLLARS, G/L PERCENTAGE   |   BTC/USD   |   PERCENT CHANGES\n\n")

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
	percent_change = abs(round(abs(profit)/myDollar, 4))
	if (profit == 0): 
		
		sys.stdout.write("$" +  str(abs(currDollar)) + "   |   base:    $" +  str(abs(profit)) + "    " + str(abs(percent_change)) +  "%   |   ")
	elif (profit > 0):  
		sys.stdout.write("$" +  str(abs(currDollar)) + "   |   gain:    +$" + str(abs(profit)) + "   +" + str(abs(percent_change)) + "%   |   ")
	elif (profit < 0):  	
		sys.stdout.write("$" +  str(abs(currDollar)) + "   |   loss:    -$" + str(abs(profit)) + "   -" + str(abs(percent_change)) +  "%   |   ")	

#Calculate Percent Change/slope  --> Make with constructor next time
	sys.stdout.write("BTC/USD: " + str(currDollarBit) + "   |   ")
	if (firstTimeRunning == True):
		firstTimeRunning = False
		profit_past = profit
		print("\nChanged Last Profit")
	if (profit > profit_past):
		diff = abs(round(profit - profit_past, 4))
		percent_change = abs(round(diff/profit_past,4))
		sys.stdout.write("+$" + str(diff) + "    ")    		
		sys.stdout.write("+" + str(percent_change) + "%\n")
	elif (profit < profit_past):
		diff = abs(round(profit_past - profit, 4))
		percent_change = abs(round(diff/profit_past, 4))
		sys.stdout.write("-$" + str(diff) + "    ")			
		sys.stdout.write("-" + str(percent_change) + "%\n")
	elif (profit == profit_past):
		sys.stdout.write("NO CHANGE" + '\n')			

#PRINT TO HTML:
	htmlf = open('profit.html', 'w') #paste the profit onto the profit.html file!
	#htmlf.write(str(profit))
	htmlf.close()

#REFRESH:
	count += 1
	if (count == 60):       	
		count = 0;
		firstTimeRunning = True
	time.sleep(1)	

while True:
	calcProfits()
	
