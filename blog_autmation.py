from os import O_APPEND
import bs4
import requests
from bs4 import BeautifulSoup as bs
import Selenium
from selenium import webdriver
# from Selenium import webdriver  
# import time  
# from Selenium.webdriver.common.keys import Keys
def google_test():
    print("sample test case started")  
    driver = webdriver.Chrome('/Applications/Google Chrome.app')  
    #driver=webdriver.firefox()  
    #driver=webdriver.ie()  
    #maximize the window size  
    driver.maximize_window()  
    #navigate to the url  
    driver.get("https://www.google.com/")  
    #identify the Google search text box and enter the value  
    driver.find_element_by_name("q").send_keys("javatpoint")  
    time.sleep(3)  
    #click on the Google search button  
    driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
    time.sleep(3)  
    #close the browser  
    driver.close()  
    print("sample test case successfully completed")
    


#pip3 install opencv-python qrcode numpy
def open_url_fun():
    url = "http://azeezullah.hussnainconsultants.com/index.php"
    open_url = requests.get(url)
    page = bs(open_url.content, "html.parser")
    fin = page.findAll(class_="card-description")
    for i in range(len(fin)):
        print(fin[i].text)
        open_url.close()
        
def qr_code_crack():
    data_here = imread("img.png")
    
    
def open_staging():
    url = "https://stagingccm.com/Account/DisplayMessage?ReturnUrl=%2F"
    open_url = requests.get(url)
    page = bs(open_url.content, "html.parser")
    print(li_a)
    open_url.close()
    
