
from selenium import webdriver #to naivate web

#1) OPEN BROWSER:
chromeDriver_path = r"C:\Users\Mahmudul\Downloads\chromedriver_win32\chromedriver.exe" #do need to add an "r" for it to work for some reason
driver = webdriver.Chrome(chromeDriver_path)  #this will open up chrome with address: "data:;"

"""#2) GO TO PAGE:
driver.get("https://www.google.com/") 
#setup
search_box = driver.find_element_by_id("lst-ib") #FINDIGN BOX
search_box.send_keys("bitcoin to usd") #ENTERING TEXT
search_box.submit() #ENTERING SUBMIT"""
driver.get("https://www.google.com/search?source=hp&ei=2OhsWvKLGMO4zwK58aGQDQ&q=bitcoin+to+usd&oq=&gs_l=") 

#entering my stuff
myBTC = str(0.008385640000)  #myBTC need to be a string not a float
search_box = driver.find_element_by_id("pair_base_input") #bitcoin entering box
search_box.send_keys(myBTC) #ENTERING my bTC, no need to enter
newestDollar = 99
currentURL = driver.current_url




"""import urllib2
req = urllib2.Request('http://www.voidspace.org.uk')
response = urllib2.urlopen(req)
the_page = response.read()

from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup 
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=gpu'

#3) opening up connection, grabbing page
uClient = uReq(my_url) #opens up the connection. grabs the webpage and downloads it
page_html = uClient.read() #will read it will dump everything into "page_html". 
uClient.close() #for any web client. this this is a open internet connection, i want to close it when im done with it

#4) parch it b(break it up into html sections)
page_soup = soup(page_html, "html.parser") 
#calling "soup" will call the "BeautifulSoup" function, within the bs4 package
#soup of my page "page_html" and will tell it to parse it at a html file. then equal it to "page_soup" so i dont lose the data

#print("printing urls")
print(page_soup.h1) #should print the header in HTML. Which it does! :)
print(page_soup.body.span)"""





#driver.close()