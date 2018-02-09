**Two Programs: "Bitcoin_Total.py" and "Bitcoin.Individual.py"**

Both programs will scrape the current bitcoin price from GDAX every second and then calculate how much money in US dollars and bitcoin I'm gaining/losing. 

**"Bitcoin_Total.py" will:**
(main program)
1) output how much USD I currently have in bitcoins.
2) output how much money (in USD) I'm gaining/losing in the current bitcoin market.
3) outputs the percent gain/loss (USD).
4) output the current bitcoin/USD rate.
5) store the current bitcoin price in a variable and will calculate the percent gain/loss from this amount. 
The variable will reset after 60 runs. After 60 runs, this variable will then be reassigned to the newest price. 
Will eventually use this to make a graph and store that graph in a database. 
6) When I sell bitcoins, it will take in dollars I have gained and the bitcoins I have lost and then recalculate the total USD and bitcoin I currently have

**"Bitcoin.Individual.py" will:**

1) output how much money in USD I traded in for bitcoin for each exchange.
2) outputs how much money (in USD) I'm gaining/losing per exchange.
3) outputs the percent gain/loss (USD) of that exchange.
4) When I sell bitcoins for USD, the program will calculate how much of the current exchange makes up the total USD and total BTC in my wallet.

For example, If I first buy bitcoins with $100 (this will be the first exchange), and I inputted a total of $300 into the market (this is sum of all exchanges)
Then the density of the first exchange is 1/3. Using this I will subtract the total USD gained from selling bitcoins from each exchange.
This will help me recalculate how much USD and bitcoins I have in my wallet


