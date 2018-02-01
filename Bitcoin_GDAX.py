#Working Object Version
#strategy: python write to a file. get html to read from that file and refresh every second
import requests
import json
import time		
import sys		

class MyProfits(object):
	def __init__(self):
		self.BTC = 0		#total BTC i own
		self.USD = 0		#total USD i own
		self.currDollar = 0
		self.profit = 0
		self.profit_prev = 0
firstTimeRunning = True

count = 0

#MY BITCOIN: [USD, BTC, USD/BTC]
bought = [ [100, 0.00838564, 11805.90], [50, 0.00438647, 11170.71], [50, 0.00433082, 11314.25], [50, 0.00494595, 9907.10], [0, 0.001006, 10154], [50, 0.00526249, 9311.18]]	 
total = MyProfits()
exchange = list(range(0,len(bought)))  #THIS IS FOR INDIVIDUA; exchange. WILL CONTINUE LATER IN CODE.making an array as long at the elements in the bought array
for i in range(len(bought)):
	exchange[i] = MyProfits()  

def calcProfits():
	t0 = time.time()
	global firstTimeRunning
	global count
	global total
	global exchange
	print("................................................................................................................................................."+str(count))
#Calculate BTC and USD for my total profits and  individual exchange profits:	
	#Tell me the total bitcoin and USD i currently have in this market:
	for i in range(len(bought)):
		total.USD = total.USD + bought[i][0] 
		total.BTC = total.BTC + bought[i][1] 
		#Print what i have right now 
	if (firstTimeRunning == True):
		sys.stdout.write("CURRENT INVESTMENT   |    G/L DOLLARS, G/L PERCENTAGE   |   BTC/USD   |   PERCENT CHANGES   |   USD: "+ str(round(total.USD,3)) + "   BTC: "+ str(round(total.BTC,7))+"\n\n")
#GET CURRENT PRICE OF BITCOIN:
	url = 'https://api.gdax.com/products/BTC-USD/trades'
	res = requests.get(url)
	json_res = json.loads(res.text) 				#"json_res" got a ton of stuff. the price is in "json_res[0]""
	currDollarBit = float(json_res[0]['price'])     #current dollars per bitcoin. 'price' is the location in the 0th index of "jason_res" #turning to float to make calculations 
	total.currDollar = round(total.BTC * currDollarBit, 3)
	total.profit = round(total.currDollar - total.USD, 3)

#Calculate total profits:
	percent_change = abs(round(abs(total.profit)/total.USD*100, 3))
	if (total.profit == 0): 
		sys.stdout.write("$" +  str(abs(total.currDollar)) + "  |  base: $" +  str(abs(total.profit)) + " " + str(abs(percent_change)) +  "%   ")
	elif (total.profit > 0):  
		sys.stdout.write("$" +  str(abs(total.currDollar)) + "  |  gain:+$" + str(abs(total.profit)) + " +" + str(abs(percent_change)) + "%  |  ")
	elif (total.profit < 0):  	
		sys.stdout.write("$" +  str(abs(total.currDollar)) + "  |  loss:-$" + str(abs(total.profit)) + " -" + str(abs(percent_change)) +  "%  |  ")	
#Calculate Percent Change/slope  
	sys.stdout.write("BTC/USD: " + str(currDollarBit) + "   |   ")
	if (firstTimeRunning == True):
		total.profit_prev = total.profit
	if (total.profit > total.profit_prev):
		diff = abs(round(total.profit - total.profit_prev, 3))
		percent_change = abs(round(diff/total.profit_prev*100,4))
		sys.stdout.write("+$" + str(diff) + "  ")    		
		sys.stdout.write("+" + str(percent_change) + "%")
	elif (total.profit < total.profit_prev):
		diff = abs(round(total.profit_prev - total.profit, 3))
		percent_change = abs(round(diff/total.profit_prev*100, 4))
		sys.stdout.write("-$" + str(diff) + "  ")			
		sys.stdout.write("-" + str(percent_change) + "%")
	elif (total.profit == total.profit_prev):
		sys.stdout.write("NO CHANGE")			

#Tell me the bitcoin and USD i have for each individual buy i made. 
	for i in range(len(bought)):
		exchange[i].USD = bought[i][0]
		exchange[i].BTC = bought[i][1]
		exchange[i].currDollar = round(exchange[i].BTC * currDollarBit, 3)
		exchange[i].profit = round(exchange[i].currDollar - exchange[i].USD, 3)
	if (firstTimeRunning == True):
		firstTimeRunning = False
		for i in range(len(bought)):	
			exchange[i].profit_prev = exchange[i].profit
	
	print(exchange[0].profit)
	print(exchange[0].profit_prev)
	tt = 0

	for i in range(len(bought)):
	#Calculate exchange[i].profits:
		print("\n..................................................................................."+str(tt))
		print("\nprinting:")
		sys.stdout.write("USD in: ("+str(exchange[i].USD))
		sys.stdout.write(")~~~~currUSD: ("+str(exchange[i].currDollar)+") - USDin: ("+str(exchange[i].USD)+")\n")
		print(exchange[i].profit)
		print(exchange[i].profit_prev)
		print()
		percent_change = abs(round(abs(exchange[i].profit)/exchange[i].USD*100, 3))
		if (exchange[i].profit== 0): 
			sys.stdout.write("$" +  str(abs(exchange[i].currDollar)) + "  |  base: $" +  str(abs(exchange[i].profit)) + " " + str(abs(percent_change)) +  "%   ")
		elif (exchange[i].profit> 0):  
			sys.stdout.write("$" +  str(abs(exchange[i].currDollar)) + "  |  gain:+$" + str(abs(exchange[i].profit)) + " +" + str(abs(percent_change)) + "%  |  ")
		elif (exchange[i].profit< 0):  	
			sys.stdout.write("$" +  str(abs(exchange[i].currDollar)) + "  |  loss:-$" + str(abs(exchange[i].profit)) + " -" + str(abs(percent_change)) +  "%  |  ")	
	#Calculate Percent Change/slope  
		sys.stdout.write("BTC/USD: " + str(currDollarBit) + "   |   ")
		if (firstTimeRunning == True):
			firstTimeRunning = False	
			exchange[i].profit_prev = exchange[i].profit
		if (exchange[i].profit> exchange[i].profit_prev):
			diff = abs(round(exchange[i].profit- exchange[i].profit_prev, 3))
			percent_change = abs(round(diff/exchange[i].profit_prev*100,4))
			sys.stdout.write("+$" + str(diff) + "  ")    		
			sys.stdout.write("+" + str(percent_change) + "%")
		elif (exchange[i].profit< exchange[i].profit_prev):
			diff = abs(round(exchange[i].profit_prev - exchange[i].profit, 3))
			percent_change = abs(round(diff/exchange[i].profit_prev*100, 4))
			sys.stdout.write("-$" + str(diff) + "  ")			
			sys.stdout.write("-" + str(percent_change) + "%")
		elif (exchange[i].profit== exchange[i].profit_prev):
			sys.stdout.write("NO CHANGE")		
		tt +=1	





#PRINT TO HTML:
	htmlf = open('profit.html', 'w') #paste the total.profit onto the total.profit.html file!
	#htmlf.write(str(profit))
	htmlf.close()

#REFRESH+ENDING:
	total.USD = 0   #reseting calculations 
	total.BTC = 0
	count += 1
	if (count == 60):       	
		count = 0;
		firstTimeRunning = True
	t1 = time.time()
	total_time = round((t1-t0),3)
	sys.stdout.write("    |  " + str(total_time)+" sec        " + str(count) + "\n")
	time.sleep(1)	

while True:
	calcProfits()
	
