#input BTC CHECKER: input profit/loss calculator
import requests
import json
import time		
import sys		

#INPUTING MY BITCOIN EXCHANGES: investment = [BTCtoUSD, BTC, BTCtoUSD/BTC]
investment = [ [-100, 0.00838564, 11805.90], [-50, 0.00433082, 11314.25], [-50, 0.00438647, 11170.71], [-50, 0.00494595, 9907.10], [-50, 0.00526249, 9311.18], [-50, .00579132, 8460.94], [-50, 0.00723745, 6605.92], [0, 0.001006, 10154], [-50, 0.00511541, 9750.01] ]
sold = [[0,0,0]]						 
inWallet = [107.56, 0.04416541-.01270184]  #What I have in my wallets right now:  [current BTCtoUSD from selling BTC, current BTC]

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
input = MyProfits()		#object for all initial investment. BTCtoUSD i inputted to system
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
		sys.stdout.write("CURRENT INVESTMENT   |    G/L DOLLARS, G/L PERCENTAGE   |   BTC/BTCtoUSD   |   PERCENT CHANGES   ||input:   USD:"+ str(round(input.totalUSD,3)) + "   BTC:+"+ str(round(input.BTC,9))+"   ||SOLD:   BTCtoUSD:+"+str(soldUSD) + "   BTC:"+str(soldBTC)+"\n\n")
#GET CURRENT PRICE OF BITCOIN:
	url = 'https://api.gdax.com/products/BTC-USD/trades'
	res = requests.get(url)
	json_res = json.loads(res.text) 			
	current.currDollarBit = float(json_res[0]['price'])  
	print(current.currDollarBit)
	time.sleep(1)
	
while True:
	calcProfits()
	
