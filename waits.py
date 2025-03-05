"""
implicit wait:
driver.implicitly_wait(10)

explicit wait:
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))

fluent wait:
wait = WebDriverWait(driver, 10, poll_frequency=1)
element = wait.until(EC.presence_of_element_located((By.ID, "dynamic-element")))
"""

import time
from selenium.webdriver.support import expected_conditions as ec

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver.chrome.service import Service

driver_path =r"D:\Users\nidwija.bhatta\Documents\PYTHON\python_automation_nidwija_trainee2025\bin\chromedriver.exe"


ser = Service(driver_path)
driver = webdriver.Chrome(service=ser)
driver.get("https://www.saucedemo.com/")

print("Page Title: ", driver.title)
driver.implicitly_wait(10)
time.sleep(4)
list_cred=driver.find_elements(By.ID,'login_credentials')


wait = WebDriverWait(driver, 30)
wait.until(ec.presence_of_element_located(By.ID,'user_name'))
# element = wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))

driver.quit()