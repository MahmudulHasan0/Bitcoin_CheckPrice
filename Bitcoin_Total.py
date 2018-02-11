#TOTAL BTC CHECKER: Total profit/loss calculator
import requests
import json
import time		
import sys		

class MyProfits():
	def __init__(self):
		self.USD = 0 		# total USD i own in wallet
		self.BTC = 0		# total BTC i own in wallet
		self.currDollar = 0
		self.change = 0
		self.change_prev = 0
		self.USD_input = 0	#USD i inputted in system
		self.BTC_input = 0	#BTC i inputted in system
firstTimeRunning = True
total = MyProfits()
count = 0
soldUSD = 0
soldBTC = 0

#INPUTING MY BITCOIN EXCHANGES: investment = [USD, BTC, USD/BTC]. SOLD = [USD, BTC]
investment = [ [-99, 0.00838564, 11805.90], [-49, 0.00433082, 11314.25], [-49, 0.00438647, 11170.71], [-49, 0.00494595, 9907.10], [-47.81, 0.00723745, 6605.92], [0, 0.001006, 10154], [-49.875, 0.00511541, 9750.01] ]
sold = [[0,0,3]] #ignore this array
for i in range(len(investment)):
	total.USD_input = total.USD_input + investment[i][0] 
	total.BTC_input = total.BTC_input + investment[i][1]
def calcProfits():
	t0 = time.time()
	global firstTimeRunning, count, total, soldUSD, soldBTC
#CALCULATE TOTAL NUMBER OF BTC I OWN AND THE TOTAL USDed I SPEND ON THEM + SOLD BTC:
	for i in range(len(sold)):
		soldUSD = sold[i][0]
		soldBTC = sold[i][1]
	for i in range(len(investment)):
		total.USD = total.USD + investment[i][0] 
		total.BTC = total.BTC + investment[i][1]
	total.USD = total.USD_input 
	total.BTC = total.BTC_input 

#PRINT THE TOTAL I HAVE INPUT TO SYSTEM (investment), AND TOTAL I HAVE SOLD
	if (firstTimeRunning == True):
		sys.stdout.write("CURRENT INVESTMENT   |    G/L DOLLARS, G/L PERCENTAGE   |   BTC/USD   |   PERCENT CHANGES   ||INPUT:   USD:"+ str(round(total.USD_input,3)) + "   BTC:+"+ str(round(total.BTC_input,9))+"   ||SOLD:   USD:+"+str(soldUSD) + "   BTC:"+str(soldBTC)+"\n\n")
#PRINT THE USD AND BTC I HAVE IN MY WALLET RIGHT NOW:	
	if (firstTimeRunning == True):
		sys.stdout.write("REMAINING IN WALLET: BTC: " + str(round(total.BTC,9)) + "    in USD:    $" + str(-total.USD) +"\n\n")
		sys.stdout.write("CURRENT (in BTC to USD): \n")
#GET CURRENT PRICE OF BITCOIN:
	url = 'https://api.gdax.com/products/BTC-USD/trades'
	res = requests.get(url)
	json_res = json.loads(res.text) 					 
	total.currDollarBit = float(json_res[0]['price'])     
#CALCULATE THE TOTAL CHANGES 
	total.currDollar = round(total.BTC * total.currDollarBit, 3) # the total usd in bitcoins i have currently
	total.change = round(total.currDollar + total.USD, 3)
	if (total.USD == 0): 								
		percent_change = 0
	else:		# If i do sell enough to make 0 profit, this if-else statement will get rid of the "divide by 0 error"
		percent_change = abs(round(abs(total.change)/total.USD*100, 3))
#PRINT CHANGES
	if (total.change == 0): 
		sys.stdout.write("$*" +  str(abs(total.currDollar)) + "  |  base: $" + str(abs(total.change)) + " " + str(abs(percent_change)) + "%  |  ")
	elif (total.change > 0):  
		sys.stdout.write("$" +  str(abs(total.currDollar)) + "  |  gain:+$" + str(abs(total.change)) + " +" + str(abs(percent_change)) + "%  |  ")
	elif (total.change < 0):  	
		sys.stdout.write("$" +  str(abs(total.currDollar)) + "  |  loss:-$" + str(abs(total.change)) + " -" + str(abs(percent_change)) + "%  |  ")	
#Calculate Percent Change SINCE 60TH READING
	sys.stdout.write("BTC/USD: " + str(total.currDollarBit) + "   |  ")
	if (firstTimeRunning == True):
		firstTimeRunning = False	
		total.change_prev = total.change
	if (total.change > total.change_prev):
		diff = abs(round(total.change - total.change_prev, 3))
		percent_change = abs(round(diff/total.change_prev*100,2))
		sys.stdout.write("+$" + str(diff) + "  ")    		
		sys.stdout.write("+" + str(percent_change) + "%")
	elif (total.change < total.change_prev):
		diff = abs(round(total.change_prev - total.change, 3))
		percent_change = abs(round(diff/total.change_prev*100, 2))
		sys.stdout.write("-$" + str(diff) + "  ")			
		sys.stdout.write("-" + str(percent_change) + "%")
	elif (total.change == total.change_prev):
		sys.stdout.write("NO CHANGE")			
	total.USD = 0   
	total.BTC = 0
	count += 1
	if (count == 60):
		count = 0;
		firstTimeRunning = True
	t1 = time.time()
	total_time = round((t1-t0),3)
	sys.stdout.write("  |            " + str(total_time)+" sec        " + str(count) + "\n")
	time.sleep(1)	

while True:
	calcProfits()