#Working
import requests
import json
import time		
import sys		

class MyProfits:
	def __init__(self):
		self.BTC = 0		#total BTC i own
		self.USD = 0		#total USD i own
		self.profit = 0
		self.profit_prev = 0
firstTimeRunning = True
count = 0

#MY BITCOIN: [USD, BTC, USD/BTC]
market = [ [100, 0.00838564, 11805.90], [50, 0.00438647, 11170.71], [50, 0.00433082, 11314.25], [50, 0.00474367, 10329.55]  ]	 

def calcProfits():
	t0 = time.time()
	global firstTimeRunning
	global count

#Calculate BTC and USD for exchanges and total:
	total = MyProfits()
	for i in range(len(market)):
		total.USD = total.USD + market[i][0] 
		total.BTC = total.BTC + market[i][1] 
	"""exchanges = list(range(0,len(market)))  #making an array as long at the elements in the market array
	for i in range(len(market)):
					exchanges[i] = MyProfits()  
					exchanges[i].USD = exchanges[i].USD + market[i][0] 
					exchanges[i].BTC = exchanges[i].BTC + market[i][1] """
	
	if (firstTimeRunning == True):
		sys.stdout.write("CURRENT INVESTMENT   |    G/L DOLLARS, G/L PERCENTAGE   |   BTC/USD   |   PERCENT CHANGES   |   MY_TOTAL_BTC: "+ str(round(total.BTC,4))+"\n\n")
#GET CURRENT PRICE OF BITCOIN:
	url = 'https://api.gdax.com/products/BTC-USD/trades'
	res = requests.get(url)
	json_res = json.loads(res.text) 				#"json_res" got a ton of stuff. the price is in "json_res[0]""
	currDollarBit = float(json_res[0]['price'])     #current dollars per bitcoin. 'price' is the location in the 0th index of "jason_res" #turning to float to make calculations 
	currDollar = round(total.BTC * currDollarBit, 3)
	total.profit = round(currDollar - total.USD, 3)

#Calculate total.profits:
	percent_change = abs(round(abs(total.profit)/total.USD*100, 3))
	if (total.profit == 0): 
		sys.stdout.write("$" +  str(abs(currDollar)) + "  |  base: $" +  str(abs(total.profit)) + "   " + str(abs(percent_change)) +  "%  |  ")
	elif (total.profit > 0):  
		sys.stdout.write("$" +  str(abs(currDollar)) + "  |  gain: +$" + str(abs(total.profit)) + "  +" + str(abs(percent_change)) + "%  |  ")
	elif (total.profit < 0):  	
		sys.stdout.write("$" +  str(abs(currDollar)) + "  |  loss: -$" + str(abs(total.profit)) + "  -" + str(abs(percent_change)) +  "%  |  ")	

#Calculate Percent Change/slope  --> Make with constructor next time
	sys.stdout.write("BTC/USD: " + str(currDollarBit) + "   |   ")
	if (firstTimeRunning == True):
		firstTimeRunning = False
		total.profit_prev = total.profit
		print("\nChanged Last total.profit")

	print("\nprof:  "+str(total.profit_prev))
	print()

	if (total.profit > total.profit_prev):
		diff = abs(round(total.profit - total.profit_prev, 3))
		percent_change = abs(round(diff/total.profit_prev*100,4))
		sys.stdout.write("+$" + str(diff) + "    ")    		
		sys.stdout.write("+" + str(percent_change) + "%")
	elif (total.profit < total.profit_prev):
		diff = abs(round(total.profit_prev - total.profit, 3))
		print(diff)
		print()

		percent_change = abs(round(diff/total.profit_prev*100, 4))
		sys.stdout.write("-$" + str(diff) + "    ")			
		sys.stdout.write("-" + str(percent_change) + "%")
	elif (total.profit == total.profit_prev):
		sys.stdout.write("NO CHANGE")			

#PRINT TO HTML:
	htmlf = open('total.profit.html', 'w') #paste the total.profit onto the total.profit.html file!
	#htmlf.write(str(total.profit))
	htmlf.close()

#REFRESH:
	count += 1
	if (count == 60):       	
		count = 0;
		firstTimeRunning = True
	t1 = time.time()
	total = round((t1-t0),3)
	sys.stdout.write("    |  " + str(total)+" sec")
	print()
	time.sleep(.6)	

while True:
	calcProfits()
	
