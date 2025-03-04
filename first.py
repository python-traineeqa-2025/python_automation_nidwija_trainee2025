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
username.click()
username.send_keys("test")
time.sleep(6)
driver.quit()
