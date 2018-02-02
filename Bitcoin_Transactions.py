#INDIVIDUAL TRANSACTION BTC CHECKER
#Bitcoin_GDAX.py is the main program
import requests
import json
import time		
import sys		

class MyProfits():
	def __init__(self):
		self.BTC = 0		#total BTC i own
		self.USD = 0		#total USD i own
		self.currDollar = 0
		self.change = 0
		self.change_prev = 0
		self.USD_density = 0
		self.BTC_density = 0
firstTimeRunning = True
count = 0
soldUSD = 0
soldBTC = 0

#INPUTING MY BITCOIN EXCHANGES: [USD, BTC, USD/BTC]
bought = [ [-100, 0.00838564, 11805.90], [-50, 0.00438647, 11170.71], [-50, 0.00433082, 11314.25], [-50, 0.00494595, 9907.10], [0, 0.001006, 10154], [-50, 0.00526249, 9311.18], [-50,0.00579132, 8460.94] ]	 
sold   = [ [+0, -0.0]]				 #sold my BTC (-) for USD (+)
total = MyProfits()
exchange = list(range(0,len(bought)))  #THIS IS FOR INDIVIDUAL EXCHANGES. WILL CONTINUE LATER IN CODE.making an array as long at the elements in the bought array
for i in range(len(bought)):
	exchange[i] = MyProfits()  

def calcProfits():
	t0 = time.time()
	global firstTimeRunning, count, total, exchange, soldUSD, soldBTC
#CALCULATE TOTAL NUMBER OF BTC I OWN AND THE TOTAL USDed I SPEND ON THEM + SOLD BTC:
	for i in range(len(sold)):
		soldUSD = sold[i][0]
		soldBTC = sold[i][1]
	for i in range(len(bought)):
		total.USD = total.USD + bought[i][0] 
		total.BTC = total.BTC + bought[i][1]
	total.USD = total.USD + soldUSD
	total.BTC = total.BTC + soldBTC 
#PRINT WHAT I HAVE RIGHT NOW
	if (firstTimeRunning == True):
		sys.stdout.write("CURRENT INVESTMENT   |    G/L DOLLARS, G/L PERCENTAGE   |   BTC/USD   |   PERCENT CHANGES   ||   USD: "+ str(round(total.USD,3)) + "   BTC: "+ str(round(total.BTC,8))+"   ||   USD: "+str(soldUSD) + "   BTC: "+str(soldBTC)+"\n\n")
#GET CURRENT PRICE OF BITCOIN:
	url = 'https://api.gdax.com/products/BTC-USD/trades'
	res = requests.get(url)
	json_res = json.loads(res.text) 			
	total.currDollarBit = float(json_res[0]['price'])  
#CALCULATE THE CURRENT USD VALUE OF BTC FOR EACH TRANSACTION I MADE 
	for i in range(len(bought)):
#*SUBTRACTING MY BUYS FROM THE EXCHANGES USING A RATIO OF EXCHANGE/TOTAL
		if (soldUSD == 0):		#Eliminating the "divide by 0" error when my sold array is at 0
			exchange[i].USD_density = 1
			exchange[i].BTC_density = 1

		else:
			exchange[i].USD_density = bought[i][0] / soldUSD    #(exhange USD)/(total USD) = density of exchange
			exchange[i].BTC_density = bought[i][1] / soldBTC  
		exchange[i].USD = round(abs(bought[i][0] - (exchange[i].USD_density)*soldUSD),2) #SUBTRACTING THE SELL FROM EACH EXCHANGE
		exchange[i].BTC = round(abs(bought[i][1] - (exchange[i].BTC_density)*soldBTC),8) #SUBTRACTING THE SELL FROM EACH EXCHANGE
		exchange[i].currDollar = round(exchange[i].BTC * total.currDollarBit, 2)	
		exchange[i].change = round(exchange[i].currDollar - exchange[i].USD, 2)	
#FIXING A FEW ERRORS:		
		if (exchange[i].USD == 0):	#Eliminating the "divide by 0" error when i sell and make 0 total profits
			exchange[i].USD = 1
		if (bought[i][0] == 0): 	#Print purposes only, not important, just says that when i get free BTC (meaning 0 USD) it will say 0%							
			percent_change = 0 
		else:						#Eliminating the "divide by 0" error when i sell and make 0 total profits
			percent_change = round(abs(exchange[i].change)/exchange[i].USD*100, 2)
		
#PRINT CHANGES:
		if (exchange[i].change == 0): 
			sys.stdout.write(str(i) + ": " + str(exchange[i].USD) + " / $"  + str(abs(exchange[i].change)) + "  " + str(abs(percent_change)) + "%   |   ")
		elif (exchange[i].change> 0):  
			sys.stdout.write(str(i)  + ": " + str(exchange[i].USD) + " /  $+"  + str(abs(exchange[i].change)) + " +" + str(abs(percent_change)) + "%   |   ")
		elif (exchange[i].change< 0):  	
			sys.stdout.write(str(i)  + ": " + str(exchange[i].USD) + " / $-"  + str(abs(exchange[i].change)) + " -" + str(abs(percent_change)) + "%   |   ")		
		exchange[i].USD = 0  
		exchange[i].BTC = 0
#PRINT TO HTML:
	#htmlf = open('change.html', 'w') #paste the total.change onto the total.change.html file!
	#htmlf.write(str(change))
	#htmlf.close()
	
#REFRESH+ENDING:
	total.USD = 0   
	total.BTC = 0
	count += 1
	firstTimeRunning = False
	if (count == 60):       	
		count = 0;
		firstTimeRunning = True
	t1 = time.time()
	total_time = round((t1-t0),3)
	sys.stdout.write("    " + str(total_time)+" sec     Loop:" + str(count) + "\n")
	time.sleep(1)
	
while True:
	calcProfits()
	
