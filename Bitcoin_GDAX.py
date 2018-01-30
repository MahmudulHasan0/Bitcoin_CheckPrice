#Working
import requests
import json
import time		#to refresh scans, repeat function
import sys		#to print in one line

myBTC = 0		#0.01710293 
myDollar = 0	#200#197				
profit = 0
profit_past = 0
firstTimeRunning = True
count = 0
#MY BITCOIN: [USD, BTC, USD/BTC]
bitcoins = [ [100, 0.00838564, 11805.90], [50, 0.00438647, 11170.71], [50, 0.00433082, 11314.25] ]	 
for i in range(len(bitcoins)):
	myDollar = myDollar + bitcoins[i][0] 
	myBTC = myBTC + bitcoins[i][1] 

sys.stdout.write("CURRENT INVESTMENT   |    G/L DOLLARS, G/L PERCENTAGE   |   BTC/USD   |   PERCENT CHANGES\n\n")
def calcProfits():
	t0 = time.time()
	global firstTimeRunning
	global profit
	global profit_past
	global count
#GET CURRENT PRICE OF BITCOIN:
	url = 'https://api.gdax.com/products/BTC-USD/trades'
	res = requests.get(url)
	json_res = json.loads(res.text) 		#"json_res" got a ton of stuff. the price is in "json_res[0]""
	currDollarBit = float(json_res[0]['price'])    #current dollars per bitcoin. 'price' is the location in the 0th index of "jason_res" #turning to float to make calculations
	currDollar = round(myBTC * currDollarBit, 3)
	profit = round(currDollar - myDollar, 3)


#Calculate Profits:
	percent_change = abs(round(abs(profit)/myDollar*100, 3))
	if (profit == 0): 
		sys.stdout.write("$" +  str(abs(currDollar)) + "  |  base: $" +  str(abs(profit)) + "   " + str(abs(percent_change)) +  "%  |  ")
	elif (profit > 0):  
		sys.stdout.write("$" +  str(abs(currDollar)) + "  |  gain: +$" + str(abs(profit)) + "  +" + str(abs(percent_change)) + "%  |  ")
	elif (profit < 0):  	
		sys.stdout.write("$" +  str(abs(currDollar)) + "  |  loss: -$" + str(abs(profit)) + "  -" + str(abs(percent_change)) +  "%  |  ")	

#Calculate Percent Change/slope  --> Make with constructor next time
	sys.stdout.write("BTC/USD: " + str(currDollarBit) + "   |   ")
	if (firstTimeRunning == True):
		firstTimeRunning = False
		profit_past = profit
		print("\nChanged Last Profit")
	if (profit > profit_past):
		diff = abs(round(profit - profit_past, 3))
		percent_change = abs(round(diff/profit_past*100,4))
		sys.stdout.write("+$" + str(diff) + "    ")    		
		sys.stdout.write("+" + str(percent_change) + "%")
	elif (profit < profit_past):
		diff = abs(round(profit_past - profit, 4))
		percent_change = abs(round(diff/profit_past, 4))
		sys.stdout.write("-$" + str(diff) + "    ")			
		sys.stdout.write("-" + str(percent_change) + "%")
	elif (profit == profit_past):
		sys.stdout.write("NO CHANGE")		
#PRINT TO HTML:
	htmlf = open('profit.html', 'w') #paste the profit onto the profit.html file!
	#htmlf.write(str(profit))
	htmlf.close()

#REFRESH:
	count += 1
	if (count == 60):       	
		count = 0;
		firstTimeRunning = True
	t1 = time.time()
	total = round((t1-t0),3)
	sys.stdout.write("    " + str(total)+" sec")
	print()
	time.sleep(.5)	

while True:
	calcProfits()
	
