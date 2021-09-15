import selenium
import requests
import bs4
from bs4 import BeautifulSoup as bs
import qrtools as q
import requests
import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/Caretek/Downloads/chromedriver_win32/chromedriver') 
def open_CCM():
    print("sample test case started 1")   
    driver.maximize_window()  
    #navigate to the url  
    driver.get("https://stagingccm.com/")
    time.sleep(5)
    print("sample test case successfully completed 1")
    

def click_on_href():
    # Click  to Proceed to Login
    driver.find_element_by_partial_link_text("Proceed").click()
    time.sleep(5)



def username_password():
    # id="Email"
    # id="Password"
    driver.find_element_by_xpath('//*[@id="Email"]').send_keys("adele.testing@caretek.com")
    driver.find_element_by_xpath('//*[@id="Password"]').send_keys("*Testings9#I5139#")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@value="Login"]').click()
    
    time.sleep(5)
    driver.close()  
    # element = driver.find_elements_by_class_name("login-form")
    # print(len(element))

open_CCM()
click_on_href()
username_password()
