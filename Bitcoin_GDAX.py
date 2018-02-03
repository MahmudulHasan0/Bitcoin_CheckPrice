#TOTAL BTC WALLET CHECKER
#Next Strategies: python write to a file. get html to read from that file and refresh every second
import requests
import json
import time		
import sys		

class MyProfits():
	def __init__(self):
		self.USD = 0 		# total USD i own
		self.BTC = 0		# total BTC i own
		self.currDollar = 0
		self.change = 0
		self.change_prev = 0
firstTimeRunning = True
total = MyProfits()
count = 0
soldUSD = 0
soldBTC = 0

#INPUTING MY BITCOIN EXCHANGES: BOUGHT = [USD, BTC, USD/BTC]. SOLD = [USD, BTC]
#bought = [ [-100, 0.00838564, 11805.90], [-50, 0.00438647, 11170.71], [-50, 0.00433082, 11314.25], [-50, 0.00494595, 9907.10], [0, 0.001006, 10154], [-50, 0.00526249, 9311.18], [-50,0.00579132, 8460.94] ]	 
#With no coinbase $1 free:
bought = [ [-99, 0.00838564, 11805.90], [-49, 0.00438647, 11170.71], [-49, 0.00433082, 11314.25], [-49, 0.00494595, 9907.10],  [-49, 0.00526249, 9311.18], [-49,0.00579132, 8460.94], [0, 0.001006, 10154],   [-38.40, 0.00449406, 8523.29] ]	 #x#buy when smaller
sold   = [ [38.40, -.00438647, 8777.94]]#+38.42,-0.00449406,8579.95]]				 #sell when higher ratio   #sold my BTC (-) for USD (+)


def calcProfits():
	t0 = time.time()
	global firstTimeRunning, count, total, soldUSD, soldBTC
#CALCULATE TOTAL NUMBER OF BTC I OWN AND THE TOTAL USDed I SPEND ON THEM + SOLD BTC:
	for i in range(len(sold)):
		soldUSD = sold[i][0]
		soldBTC = sold[i][1]
	for i in range(len(bought)):
		total.USD = total.USD + bought[i][0] 
		total.BTC = total.BTC + bought[i][1]
	total.USD = total.USD + soldUSD
	total.BTC = total.BTC + soldBTC

#PRINT THE TOTAL I HAVE INPUT TO SYSTEM (BOUGHT), AND TOTAL I HAVE SOLD
	if (firstTimeRunning == True):
		sys.stdout.write("CURRENT INVESTMENT   |    G/L DOLLARS, G/L PERCENTAGE   |   BTC/USD   |   PERCENT CHANGES   ||BOUGHT:   USD:"+ str(round(total.USD,3)) + "   BTC:+"+ str(round(total.BTC,9))+"   ||SOLD:   USD:+"+str(soldUSD) + "   BTC:"+str(soldBTC)+"\n\n")
#PRINT THE USD AND BTC I HAVE IN MY WALLET RIGHT NOW:	
	
	if (firstTimeRunning == True):
		sys.stdout.write("REMAINING IN WALLET: USD:    $" + str(total.USD) + "   BTC: " + str(round(total.BTC,9))+"\n\n")
		sys.stdout.write("CURRENT: \n")

#GET CURRENT PRICE OF BITCOIN:
	url = 'https://api.gdax.com/products/BTC-USD/trades'
	res = requests.get(url)
	json_res = json.loads(res.text) 					  # "json_res" got a ton of stuff. the price is in "json_res[0]""
	total.currDollarBit = float(json_res[0]['price'])     # current dollars per bitcoin. 'price' is the location in the 0th index of "jason_res" #turning to float to make calculations 
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
		sys.stdout.write("+$" +  str(abs(total.currDollar)) + "  |  gain:+$" + str(abs(total.change)) + " +" + str(abs(percent_change)) + "%  |  ")
	elif (total.change < 0):  	
		sys.stdout.write("-$" +  str(abs(total.currDollar)) + "  |  loss:-$" + str(abs(total.change)) + " -" + str(abs(percent_change)) + "%  |  ")	
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
#PRINT TO HTML:
	#htmlf = open('change.html', 'w') #paste the total.change onto the total.change.html file!
	#htmlf.write(str(change))
	#htmlf.close()
#REFRESH+ENDING:
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

	
