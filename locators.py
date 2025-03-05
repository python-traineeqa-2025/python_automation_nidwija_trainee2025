"""

ID (find_element(By.ID, "element_id"))
Name (find_element(By.NAME, "element_name"))
Class Name (find_element(By.CLASS_NAME, "class_name"))
Tag Name (find_element(By.TAG_NAME, "tag_name")) ,input>
Link Text / Partial Link Text (find_element(By.LINK_TEXT, "link text"))
CSS Selectors (find_element(By.CSS_SELECTOR, "css_selector"))
XPath (find_element(By.XPATH, "//tagname[@attribute='value']"))

xpath::

//{tag}[@attribute='']
eg: //div//input[@data-test='username']
//div//input[contains(@data-test,'username')]
parameterization
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.service import Service

driver_path =r"D:\Users\nidwija.bhatta\Documents\PYTHON\python_automation_nidwija_trainee2025\bin\chromedriver.exe"


ser = Service(driver_path)
driver = webdriver.Chrome(service=ser)
driver.get("https://www.saucedemo.com/")
print("Page Title: ", driver.title)

username=driver.find_element(By.XPATH,"//div//input[@data-test='username']")
driver.find_elements()
username.click()
username.send_keys("test")
time.sleep(6)
driver.quit()
