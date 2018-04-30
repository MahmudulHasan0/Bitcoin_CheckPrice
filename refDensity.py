
import requests
import json
import time		
import sys		

"""[100, 0.00838564, 11805.90], [50, 0.00433082, 11314.25], [50, 0.00438647, 11170.71], 
				[0,0.001006,10154], [25, 0.00231142, 10788.87],[25, 0.00240592, 10396],
				[50, 0.00494595, 9907.10], [50, 0.00526249, 9311.18], [100,0.01046382,9461.17], [50, 0.00511541, 9750.01], 
				[50,0.00579132, 8460.94],  [50, 0.0060779400, 8205.95],
			    [25,0.0032192400,7746.42], [25,0.0032635400,7644.33]
			  	[50,0.00723745,6605.92], ,
			"""
#INPUTING MY EXCHANGES: 
investment = [ [50,0.00723745,6605.92],
				
]		
class MyProfits():
	def __init__(self):
		self.BTC = 0
		self.BTCtoUSD = 0 	#Dollars in BTC
		self.totalUSD = 0	#Everything converted to USD
		self.dollarBit = 0
		self.gainLoss = 0 
		self.gainLossArray = []
		self.gainLossPercent = 0
		self.gainLoss_prev = 0
firstTimeRunning = True
input = MyProfits()		#Object for all initial investent.
current = MyProfits()	#Current BTCtoUSD, BTC i have with the market
each = MyProfits()		#Object for each investment
count = 0

for i in range(len(investment)):
	input.BTC = input.BTC + investment[i][1]
sys.stdout.write(str(input.BTC))

# 11.1k to 11.8k  0.01710293  #sell when reached (1st)

# 10.1k to 10.8k  0.00572334  #sell then reached (1st)
# 9.3k  to 9.9k   0.02578767 


# 8.2k  to 8.5k   0.01186926   #can sell

# 7.6k  to 7.8k   0.00648278   #major profits sell last
# 6.6k+           0.00723745