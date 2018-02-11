#latest. testing buy/sell array 
#current BTC WALLET CHECKER
#Next Strategies: python write to a file. get html to read from that file and refresh every second
import requests
import json
import time		
import sys		

class MyProfits():
	def __init__(self):
		self.USD = 0 		
		self.BTC = 0		
		self.buyUSD = 0
		self.buyBTC = 0
		self.sellUSD = 0
		self.sellBTC = 0		

		self.currDollar = 0
		self.change = 0
		self.change_prev = 0
firstTimeRunning = True
inPut = MyProfits()		#USD and BTC i entered
current = MyProfits()	#USD and BTC in my wallet right now
total = MyProfits()		#Just an object used to create current.USD and current.BTC
count = 0
x = 0
y = 0
#INPUTING MY BITCOIN EXCHANGES: BOUGHT = [USD, BTC, USD/BTC]. sell= [USD, BTC]
#bought = [ [-100, 0.00838564, 11805.90], [-50, 0.00438647, 11170.71], [-50, 0.00433082, 11314.25], [-50, 0.00494595, 9907.10], [0, 0.001006, 10154], [-50, 0.00526249, 9311.18], [-50,0.00579132, 8460.94] ]	 
#With cointotal $1 free:
bought = [[0.00838564, 11805.9, -99], [0.00433082, 11314.25, -49], [0.00438647, 11170.71, -49], [0.00494595, 9907.1, -49], [0.00526249, 9311.18, -49], [0.00579132, 8460.94, -49], [0.00511541, 9750.01, -50], [0.001006, 10154, 0]]
#0:BTC BOUGHT 	#1:ratio USD/BTC	#2:usd input for MEMORYv
buy = [[0.00511541, 9750.01], [0.00449406, 8523.29, -38.4], [0.00577656, 8565.01, -49.6], [0.00290492, 9374.96], [.003,9375], [0.00541882, 9147.01], [0.00539200, 9100.01], [0.00539200, 9100.01], [0.00536428, 9217.71], [0.00540155,9095.00]]
sell  = [[-0.00438647, 8777.94, 38.4], [-.002,8585.00], [-0.00279132, 8585.00], [-0.00577656, 8875.01], [-0.00544134, 9155.00], [-0.00541882, 9100.00], [-0.00539200, 9217.75], [-0.00100000, 9205.00], [-0.00253276, 9204.62], [-0.00183152,9202.94] ]    
#0: BTC sell	#1: ratio USD/BTC 	#2: USD gained for memory
fee = .002494 #GDAX Transaction Fee Percentage
u=0
#MAKING total CALCULATIONS (didnt incluse in the repeated function below so that program runs faster):
for i in range(len(bought)):
	inPut.USD = inPut.USD + bought[i][2] 
	inPut.BTC = inPut.BTC + bought[i][0]

for i in range(len(bought)):
	total.BTC = total.BTC + bought[i][0]
	x = x + bought[i][0]
for i in range(len(buy)):
	total.BTC = total.BTC + buy[i][0] 			#will multiply this by the ratio of USD/BTC to get USD
	#total.buyBTC = total.buyBTC + buy[i][0]

"""for i in range(len(sell)):
	total.sellBTC = total.sellBTC + (-sell[i][0])  #will dmultiple this by the ratio of USD/BTC to get USD
"""
def calcProfits():
	t0 = time.time()
	global firstTimeRunning, count, inPut, current, total
#GET CURRENT PRICE OF BITCOIN:
	url = 'https://api.gdax.com/products/BTC-USD/trades'
	res = requests.get(url)
	json_res = json.loads(res.text) 					# "json_res" got a ton of stuff. the price is in "json_res[0]""
	current.dollarBit = float(json_res[0]['price'])     # current dollars per bitcoin. 'price' is the location in the 0th index of "jason_res" #turning to float to make calculations 
  	
	for i in range(len(buy)):
		total.buyUSD = total.buyUSD + buy[i][0]*buy[i][1]
	for i in range(len(sell)):
		feedBTC = -sell[i][0] + sell[i][0]*fee
		total.sellUSD = total.sellUSD +feedBTC*sell[i][1]  #will dmultiple this by the ratio of USD/BTC to get USD

#439.2882614973
#-329.10698015739996
#CALCULATE current NUMBER OF BTC I OWN AND THE current USDed I SPEND ON THEM + sellBTC:
	print("ssssssss:")
	print(total.buyUSD)
	print(total.sellUSD)
	print
	#print(total.sellBTC*current.dollarBit - total.buyBTC*current.dollarBit )
	print()

	sellUSD = round(-total.sellBTC*current.dollarBit,3)
	sellUSD = round(sellUSD - (sellUSD*fee),4) #When i sellmy bitcoins, how much USD did i get back? Applying the fee because from BTC to USD a fee is applied
	sellBTC = round(total.sellBTC,8)

	current.USD = round(-total.BTC*current.dollarBit,3) #From USD to BTC, a fee is applied. Here, im directly converting BTC to USD so no need to apply the fee
	current.BTC = round(total.BTC,8)
	#current.USD = (current.USD + sellUSD )
	#current.BTC = (current.BTC + sellBTC)
	z = (-x*current.dollarBit)+(-y*current.dollarBit)

	print(total.sellBTC*fee*current.dollarBit)
	print(u)
	print(current.USD)
	print(sellUSD)
	print(current.USD+sellUSD)
	print()
	print(inPut.USD-current.USD+(u))
	print()
	sys.stdout.write("net USD :  "+str(current.USD))

#PRINT THE current I HAVE INPUT TO SYSTEM (BOUGHT), AND current I HAVE sell
	if (firstTimeRunning == True):
		sys.stdout.write("CURRENT INVESTMENT   |    G/L DOLLARS, G/L PERCENTAGE   |   BTC/USD   |   PERCENT CHANGES   ||INPUT:   USD:"+ str(round(inPut.USD,3)) + "   BTC:+"+ str(round(inPut.BTC,9))+"   ||sell:   USD:+"+str(sellUSD) + "   BTC:"+str(sellBTC)+"\n\n")
#PRINT THE USD AND BTC I HAVE IN MY WALLET RIGHT NOW:	
	if (firstTimeRunning == True):
		sys.stdout.write("REMAINING IN WALLET: USD:    $" + str(current.USD) + "   BTC: " + str(round(current.BTC,9))+"\n\n")
		sys.stdout.write("CURRENT: \n")
#CALCULATE THE current CHANGES 
	current.currDollar = round(current.BTC * current.dollarBit, 3) # the current usd in bitcoins i have currently
	
	sys.stdout.write("\ncurrDollar:  "+str(current.currDollar))
	print()
	sys.stdout.write("current change_2:  "+str(current.currDollar))
	print()
	print()

	current.change = round(current.currDollar + current.USD, 3)
	if (current.USD == 0): 								
		percent_change = 0
	else:		# If i do sell enough to make 0 profit, this if-else statement will get rid of the "divide by 0 error"
		percent_change = abs(round(abs(current.change)/current.USD*100, 3))
#PRINT CHANGES
	if (current.change == 0): 
		sys.stdout.write("$*" +  str(abs(current.currDollar)) + "  |  total: $" + str(abs(current.change)) + " " + str(abs(percent_change)) + "%  |  ")
	elif (current.change > 0):  
		sys.stdout.write("+$" +  str(abs(current.currDollar)) + "  |  gain:+$" + str(abs(current.change)) + " +" + str(abs(percent_change)) + "%  |  ")
	elif (current.change < 0):  	
		sys.stdout.write("-$" +  str(abs(current.currDollar)) + "  |  loss:-$" + str(abs(current.change)) + " -" + str(abs(percent_change)) + "%  |  ")	
#Calculate Percent Change SINCE 60TH READING
	sys.stdout.write("BTC/USD: " + str(current.dollarBit) + "   |  ")
	if (firstTimeRunning == True):
		firstTimeRunning = False	
		current.change_prev = current.change
	if (current.change > current.change_prev):
		diff = abs(round(current.change - current.change_prev, 3))
		percent_change = abs(round(diff/current.change_prev*100,2))
		sys.stdout.write("+$" + str(diff) + "  ")    		
		sys.stdout.write("+" + str(percent_change) + "%")
	elif (current.change < current.change_prev):
		diff = abs(round(current.change_prev - current.change, 3))
		percent_change = abs(round(diff/current.change_prev*100, 2))
		sys.stdout.write("-$" + str(diff) + "  ")			
		sys.stdout.write("-" + str(percent_change) + "%")
	elif (current.change == current.change_prev):
		sys.stdout.write("NO CHANGE")			
#PRINT TO HTML:
	#htmlf = open('change.html', 'w') #paste the current.change onto the current.change.html file!
	#htmlf.write(str(change))
	#htmlf.close()
#REFRESH+ENDING:
	current.USD = 0   
	current.BTC = 0
	count += 1
	if (count == 60):
		count = 0;
		firstTimeRunning = True
	t1 = time.time()
	current_time = round((t1-t0),3)
	sys.stdout.write("  |            " + str(current_time)+" sec        " + str(count) + "\n---------------------------------------------------------------------------\n")
	time.sleep(1)	

while True:
	calcProfits()

	
