#input BTC CHECKER: input profit/loss calculator
import requests
import json
import time		
import sys		

#INPUTING MY BITCOIN EXCHANGES: investment = [BTCtoUSD, BTC, BTCtoUSD/BTC]
investment = [ [100, 0.00838564, 11805.90], [50, 0.00433082, 11314.25], [50, 0.00438647, 11170.71], [50, 0.00494595, 9907.10], [50, 0.00526249, 9311.18], [50, .00579132, 8460.94], [50, 0.00723745, 6605.92], [0, 0.001006, 10154], [50, 0.00511541, 9750.01] ]
sold = [[0,0,0]]						 
inWallet = [130.04, 0.02852339]  #What I have in my wallets right now:  [current BTCtoUSD from selling BTC, current BTC]

class MyProfits():
	def __init__(self):
		self.BTC = 0
		self.BTCtoUSD = 0 	#$ in BTC
		self.totalUSD = 0	#everything converted to USD
		self.dollarBit = 0
		self.gainLoss = 0
		self.gainLossArray = []
		self.gainLossPercent = 0
		self.gainLoss_prev = 0
firstTimeRunning = True
input = MyProfits()		#object for all initial investent. BTCtoUSD i inputted to system
current = MyProfits()	#current BTCtoUSD, BTC i have with the market
each = MyProfits()		#object for each investment
count = 0
soldBTCtoUSD = 0
soldBTC = 0

for i in range(len(investment)):
	input.totalUSD = input.totalUSD + investment[i][0] 
	input.BTC = input.BTC + investment[i][1]
for i in range(len(sold)):
	soldUSD = sold[i][0]
	soldBTC = sold[i][1]


def calcProfits():
	t0 = time.time()
	global firstTimeRunning, count, input, current, each, soldUSD, soldBTC, inWallet
#1) PRINT THE input I HAVE input TO SYSTEM (investment), AND input I HAVE SOLD
	if (firstTimeRunning == True):
		sys.stdout.write("CURRENT INVESTMENT   |    G/L DOLLARS, G/L PERCENTAGE   |   BTC/BTCtoUSD   |   PERCENT CHANGES   ||input:   USD:"+ str(round(input.totalUSD,3)) + "   BTC:"+ str(round(input.BTC,9))+"   ||SOLD:   BTCtoUSD:+"+str(soldUSD) + "   BTC:"+str(soldBTC)+"\n\n")
#2) GET CURRENT PRICE OF BITCOIN:
	url = 'https://api.gdax.com/products/BTC-USD/trades'
	res = requests.get(url)
	json_res = json.loads(res.text) 			
	current.dollarBit = float(json_res[0]['price'])  

	
#$373.86  
#-$76.14
#3) CALCULATE CURRENT BTCtoUSD AND BTC AND CURRENT LOSSES/GAINS:
	for i in range(len(investment)):
		each.BTCtoUSD = investment[i][1]*current.dollarBit
		each.gainLossArray.append(investment[i][0]-each.BTCtoUSD) 	#CALCULATE THE GAIN/LOSS OF EACH INVESTMENT, AND PUT IT IN ARRAY (WILL BE USED TO EVALUATES GAINS/LOSSES OF EACH INVESTMENT)
		input.gainLoss = input.gainLoss + each.gainLossArray[i] 	#Gain/loss using the inputs
	current.BTCtoUSD = round(inWallet[1] * current.dollarBit,3)		#Turning the BTC to USD
	current.totalUSD = inWallet[0] + current.BTCtoUSD 				#Basically turning everything in wallet to USD
	current.gainLoss = -round(input.totalUSD - current.totalUSD,3)
	current.gainLossPercent = round(current.gainLoss/input.totalUSD*100,3)


#4) PRINT THE BTCtoUSD AND BTC I HAVE IN MY WALLET RIGHT NOW:	
	if (firstTimeRunning == True):
		sys.stdout.write("REMAINING IN WALLET:    BTC: " + str(round(inWallet[1],9)) + "--> $" + str(current.BTCtoUSD) + "         USD: "+str(inWallet[0])+"\n\n")
		sys.stdout.write("CURRENTLY HAVE: (all converted to USD) \n")

#5) PRINT PERCENT CHANGES
	if (current.gainLoss == 0): 
		sys.stdout.write("$*" +  str(abs(current.totalUSD)) + "  |  base: $" + str(abs(current.gainLoss)) + " " + str(abs(current.gainLossPercent)) + "%  |  ")
	elif (current.gainLoss > 0):  
		sys.stdout.write("$" +  str(abs(current.totalUSD)) + "  |  gain:+$" + str(abs(current.gainLoss)) + " +" + str(abs(current.gainLossPercent)) + "%  |  ")
	elif (current.gainLoss < 0):  	
		sys.stdout.write("$" +  str(abs(current.totalUSD)) + "  |  loss:-$" + str(abs(current.gainLoss)) + " -" + str(abs(current.gainLossPercent)) + "%  |  ")	

#Calculate Percent Change SINCE 60TH READING
	sys.stdout.write("BTC/USD: $" + str(current.dollarBit) + "   |  ")
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
	current.totalUSD = 0
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
	time.sleep(4)	

while True:
	calcProfits()
