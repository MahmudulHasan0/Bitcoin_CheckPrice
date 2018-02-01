#Individual Exchange BTC CHECKER
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
bought = [ [100, 0.00838564, 11805.90], [50, 0.00438647, 11170.71], [50, 0.00433082, 11314.25], [0, 0.001006, 10154], [50, 0.00526249, 9311.18]]	 
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
#Calculate BTC and USD for my total profits and  individual exchange profits:	
	for i in range(len(bought)):
		total.USD = total.USD + bought[i][0] 
		total.BTC = total.BTC + bought[i][1] 
#Print what i have right now 
	if (firstTimeRunning == True):
		sys.stdout.write("CURRENT INVESTMENT   |    G/L DOLLARS, G/L PERCENTAGE   |   BTC/USD   |   PERCENT CHANGES   |   USD: "+ str(round(total.USD,3)) + "   BTC: "+ str(round(total.BTC,7))+"\n\n")
#GET CURRENT PRICE OF BITCOIN:
	url = 'https://api.gdax.com/products/BTC-USD/trades'
	res = requests.get(url)
	json_res = json.loads(res.text) 			
	currDollarBit = float(json_res[0]['price'])   	
#Tell me the bitcoin and USD i have for each individual buy i made. 
	for i in range(len(bought)):
		exchange[i].USD = bought[i][0]
		exchange[i].BTC = bought[i][1]
		exchange[i].currDollar = round(exchange[i].BTC * currDollarBit, 3)
		exchange[i].profit = round(exchange[i].currDollar - exchange[i].USD, 3)	
		if (bought[i][0] == 0):
			exchange[i].USD = 1
		percent_change = abs(round(abs(exchange[i].profit)/exchange[i].USD*100, 3))
		if (exchange[i].profit == 0): 
			sys.stdout.write(str(i) + ": " + str(exchange[i].USD) + " / $"  + str(abs(exchange[i].currDollar)) + "  " + str(abs(percent_change)) + "%   |   ")
		elif (exchange[i].profit> 0):  
			sys.stdout.write(str(i)  + ": " + str(exchange[i].USD) + " /  $"  + str(abs(exchange[i].currDollar)) + " +" + str(abs(percent_change)) + "%   |   ")
		elif (exchange[i].profit< 0):  	
			sys.stdout.write(str(i)  + ": " + str(exchange[i].USD) + " / $"  + str(abs(exchange[i].currDollar)) + " -" + str(abs(percent_change)) + "%   |   ")		
		exchange[i].USD = 0   #reseting calculations 
		exchange[i].BTC = 0
#PRINT TO HTML:
	htmlf = open('profit.html', 'w') #paste the total.profit onto the total.profit.html file!
	#htmlf.write(str(profit))
	htmlf.close()
#REFRESH+ENDING:
	total.USD = 0   #reseting calculations 
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
	
