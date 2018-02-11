#input BTC CHECKER: input profit/loss calculator
import requests
import json
import time		
import sys		

class MyProfits():
	def __init__(self):
		self.USD = 0 			
		self.BTC = 0	
		self.dollarBit = 0
		self.gainLoss = 0
		self.gainLossArray = []
		self.gainLossPercent = 0
		self.gainLoss_prev = 0
firstTimeRunning = True
input = MyProfits()		#object for all initial investment. USD i inputted to system
current = MyProfits()	#current USD, BTC i have with the market
each = MyProfits()		#object for each investment
count = 0
soldUSD = 0
soldBTC = 0
#inputING MY BITCOIN EXCHANGES: investment = [USD, BTC, USD/BTC]. SOLD = [USD, BTC]
investment = [ [-100, 0.00838564, 11805.90], [-50, 0.00433082, 11314.25], [-50, 0.00438647, 11170.71], [-50, 0.00494595, 9907.10], [-50, 0.00526249, 9311.18], [-50, .00579132, 8460.94], [-50, 0.00723745, 6605.92], [0, 0.001006, 10154], [-50, 0.00511541, 9750.01] ]
sold = [[0,0,0]] #ignore this array
for i in range(len(investment)):
	input.USD = input.USD + investment[i][0] 
	input.BTC = input.BTC + investment[i][1]
for i in range(len(sold)):
	soldUSD = sold[i][0]
	soldBTC = sold[i][1]

def calcProfits():
	t0 = time.time()

	global firstTimeRunning, count, input, current, each, soldUSD, soldBTC
#1) PRINT THE input I HAVE input TO SYSTEM (investment), AND input I HAVE SOLD
	if (firstTimeRunning == True):
		sys.stdout.write("CURRENT INVESTMENT   |    G/L DOLLARS, G/L PERCENTAGE   |   BTC/USD   |   PERCENT CHANGES   ||input:   USD:"+ str(round(input.USD,3)) + "   BTC:+"+ str(round(input.BTC,9))+"   ||SOLD:   USD:+"+str(soldUSD) + "   BTC:"+str(soldBTC)+"\n\n")

#2) GET CURRENT PRICE OF BITCOIN:
	url = 'https://api.gdax.com/products/BTC-USD/trades'
	res = requests.get(url)
	json_res = json.loads(res.text) 					 
	current.dollarBit = float(json_res[0]['price'])     

#3) CALCULATE CURRENT USD AND BTC AND CURRENT LOSSES/GAINS:
	for i in range(len(investment)):
		each.USD = investment[i][1]*current.dollarBit
		each.gainLossArray.append(investment[i][0]+each.USD) #CALCULATE THE GAIN/LOSS OF EACH INVESTMENT, AND PUT IT IN ARRAY (WILL BE USED TO EVALUATES GAINS/LOSSES OF EACH INVESTMENT)
		input.gainLoss = input.gainLoss + each.gainLossArray[i] #gain loss using the inputs
	current.BTC = 0.04416541#input.BTC
	current.USD = round(current.BTC * current.dollarBit,3)
	current.gainLoss = round(input.USD + current.USD,3)
	current.gainLossPercent = round(current.gainLoss/450*100,3)

#4) PRINT THE USD AND BTC I HAVE IN MY WALLET RIGHT NOW:	
	if (firstTimeRunning == True):
		sys.stdout.write("REMAINING IN WALLET: BTC: " + str(round(current.BTC,9)) + "    in USD:    $" + str(current.USD) +"\n\n")
		sys.stdout.write("CURRENTLY HAVE: (in BTC to USD) \n")

#5) PRINT PERCENT CHANGES
	if (current.gainLoss == 0): 
		sys.stdout.write("$*" +  str(abs(current.USD)) + "  |  base: $" + str(abs(current.gainLoss)) + " " + str(abs(current.gainLossPercent)) + "%  |  ")
	elif (current.gainLoss > 0):  
		sys.stdout.write("$" +  str(abs(current.USD)) + "  |  gain:+$" + str(abs(current.gainLoss)) + " +" + str(abs(current.gainLossPercent)) + "%  |  ")
	elif (current.gainLoss < 0):  	
		sys.stdout.write("$" +  str(abs(current.USD)) + "  |  loss:-$" + str(abs(current.gainLoss)) + " -" + str(abs(current.gainLossPercent)) + "%  |  ")	

#Calculate Percent Change SINCE 60TH READING
	sys.stdout.write("BTC/USD: " + str(current.dollarBit) + "   |  ")

	if (firstTimeRunning == True):
		firstTimeRunning = False	
		current.gainLoss_prev = current.gainLoss
	if (current.gainLoss > current.gainLoss_prev):
		diff = abs(round(current.gainLoss - current.gainLoss_prev, 3))
		current.gainLossPercent = abs(round(diff/current.gainLoss_prev*100,2))
		sys.stdout.write("+$" + str(diff) + "  ")    		
		sys.stdout.write("+" + str(current.gainLossPercent) + "%")
	elif (current.gainLoss < current.gainLoss_prev):
		diff = abs(round(current.gainLoss_prev - current.gainLoss, 3))
		current.gainLossPercent = abs(round(diff/current.gainLoss_prev*100, 2))
		sys.stdout.write("-$" + str(diff) + "  ")			
		sys.stdout.write("-" + str(current.gainLossPercent) + "%")
	elif (current.gainLoss == current.gainLoss_prev):
		sys.stdout.write("NO CHANGE")			

	current.USD = 0
	current.BTC = 0
	current.gainLoss = 0
	current.gainLossPercent = 0

	count += 1
	if (count == 60):
		count = 0;
		firstTimeRunning = True

	t1 = time.time()
	input_time = round((t1-t0),3)
	sys.stdout.write("  |            " + str(input_time)+" sec        " + str(count) + "\n")
	time.sleep(2)	

while True:
	calcProfits()

	
