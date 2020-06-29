**A program that calculates your gains/losses from the bitcoin market**
* **Bitcoin_Total.py** is the main program/.
* **Bitcoin_Individual.py** is a test program. Is not very important.
* Both programs will scrape the current bitcoin price from GDAX every few seconds and then calculate how much money in US dollars I'm gaining or losing. 

**A) Bitcoin_Total.py will:**

![Bitcoin_total Example](bitcoin_checker_example.PNG "Bitcoin_Total Example")
The above picture is converting The amount of bitcoins and other cryptocurrencies that I own into USD and calculating how much I'm losing or gaining, the percentage of my investment that I'm gaining or losing and if the market is going up of down since the nth reading. 

1) output how much USD I currently have in bitcoins.
2) output how much money (in USD) I'm gaining/losing in the current bitcoin market.
3) outputs the percent gain/loss (USD).
4) output the current USD per bitcoin rate.
5) store the current bitcoin price in a variable and will calculate the percent gain/loss from this amount. 
The variable will reset after 60 runs. After 60 runs, this variable will then be reassigned to the newest price. 
Will eventually use this to make a graph and store that graph in a database. 
6) When I sell bitcoins, it will take in dollars I have gained and the bitcoins I have lost and then recalculate the total USD and bitcoin I currently have

**B) Bitcoin.Individual.py will:** (Will Need To Fix)

1) output how much money in USD I traded in for bitcoin for each exchange.
2) outputs how much money (in USD) I'm gaining/losing per exchange.
3) outputs the percent gain/loss (USD) of that exchange.
4) When I sell bitcoins for USD, the program will calculate how much of the current exchange makes up the total USD and total BTC in my wallet.

For example, If I first buy bitcoins with $100 (this will be the first exchange), and I inputted a total of $300 into the market (this is sum of all exchanges)
Then the density of the first exchange is 1/3. Using this I will subtract the total USD gained from selling bitcoins from each exchange.
This will help me recalculate how much USD and bitcoins I have in my wallet

**C) INPUTTING YOUR DATA: For Bitcoin_Total.py:**
* Gains/losses are calculated using the **investment** and **inWallet** arrays. 
* The **investment** array is what you initially put into the market. It takes in three factors: The amount of money in USD you put into the system (this is the initial investment. It's not need anymore), the number of bitcoins you have bought with that initial investment, and the USD per one BTC price you bought the bitcoins for. The number of bitcoins bought, USD per one Bitcoin price, and the GDAX or Coinbase fees can calculate the initial USD investment (thats why the USD investment index isn't really needed, will get rid of it in the future).
* The **inWallet** array is how much bitcoins and US dollars you have in your account. The program will turn the bitcoins into dollars and will then calculate your gain/loss from your initial investment (in dollars).

```
investment = [ [<USD you put into system>, <bought bitcoins>, <USD per one BTC price you bought bitcoins for>] ]
```
```
inWallet = [ [<USD in your account>, <Bitcoins in your account>] ]
```
