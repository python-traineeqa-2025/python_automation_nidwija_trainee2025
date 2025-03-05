"""
send_keys()	-> element.send_keys("text")
click()-> element.click()
clear()	_>	element.clear()
text ->	print(element.text)
get_attribute()	_> element.get_attribute("href")
"""


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.service import Service

driver_path = r"/bin/chromedriver.exe"


ser = Service(driver_path)
driver = webdriver.Chrome(service=ser)
driver.get("https://www.saucedemo.com/")

print("Page Title: ", driver.title)

list_cred=driver.find_elements(By.ID,'login_credentials')
# username.click()
# username.send_keys("jijio")
# username.clear()
print(list_cred)
login_cred_list=[]
for i in list_cred:
    print(i.text)
    login_cred_list.append(i.text)
    # i.click()
print(login_cred_list)
driver.quit()