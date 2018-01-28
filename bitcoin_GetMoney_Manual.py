from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

url = 'https://www.gdax.com/trade/BTC-USD'
html = """<span class="MarketInfo_market-num_1lAXs">11,560.00 USD</span>"""
#program need to retrieve this by itself uReq(url).read()
soup = BeautifulSoup(html, "html.parser") 

spans=soup.find_all('span', {'class': 'MarketInfo_market-num_1lAXs'})
for span in spans:
	print(span.text.replace('USD','').strip())
