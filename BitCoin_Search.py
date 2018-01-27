from selenium import webdriver #to naivate web
import requests #most downloaded package. make HTML requests
from urllib.request import urlopen as uReq #urllib.request.urlopen(...) = uReq(...); importing "urlopen" from "urllib.request. Naming this as "uReq" so i can refer to it easily.
from bs4 import BeautifulSoup as soup #bs4.BeautifulSoup = soup

#1) OPEN BROWSER:
chromeDriver_path = r"C:\Users\Mahmudul\Downloads\chromedriver_win32\chromedriver.exe" #do need to add an "r" for it to work for some reason
driver = webdriver.Chrome(chromeDriver_path)  #this will open up chrome with address: "data:;"
#driver = webdriver.PhantomJS() #using a virtual browser:

#open page
driver.get("https://www.google.com/search?source=hp&ei=2OhsWvKLGMO4zwK58aGQDQ&q=bitcoin+to+usd&oq=&gs_l=") 

#entering my stuff
myBTC = str(0.008385640000)  #myBTC need to be a string not a float
search_box = driver.find_element_by_id("pair_base_input") #bitcoin entering box
search_box.send_keys(myBTC) #ENTERING my bTC, no need to enter
myDollar = 99 #what i put in
currentURL = driver.current_url #getting current URL
print(currentURL)

"""r = requests.get(currentURL) #package the request, send the requesnt, and capture the respond in a single function: request.get()
text = r.text #turn it into text
page_soup = soup(r, "html.parser") 
"""

#get the current price
newDollar = driver.find_element_by_id("pair_targ_input")
print(newDollar.text)
#calculate profits


