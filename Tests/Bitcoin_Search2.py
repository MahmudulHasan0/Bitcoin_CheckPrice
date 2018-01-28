#runing headless chrome driver
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display #download this 
import os

chromeDriver_path = r"C:\Users\Mahmudul\Downloads\chromedriver_win32\chromedriver.exe" #do need to add an "r" for it to work for some reason
os.environ['webdriver.chrome.driver'] = chromeDriver_path 
display = Display(visible=0, size=(800, 600))
"""display.start()

driver = webdriver.Chrome(chromeDriver_path)
driver.get("http://google.com")

q=driver.find"""