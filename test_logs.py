# import logging
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class TestLogs:
    def test_first(self):
            driver_path = r"D:\Users\nidwija.bhatta\Documents\PYTHON\python_automation_nidwija_trainee2025\bin\chromedriver.exe"

            ser = Service(driver_path)
            logging.info("set up driver")
            driver = webdriver.Chrome(service=ser)
            # driver=webdriver.Chrome()
            driver.get("https://www.saucedemo.com/")
            logging.info("opened the site")
            title=driver.title
            logging.info("site opened. ")
            list_cred = driver.find_elements(By.ID, 'login_credentials')

            # logging.info(list_cred)
            login_cred_list = []
            for i in list_cred:
                # print(i.text)
                logging.info(i.text)
                login_cred_list.append(i.text)
                # i.click()
            logging.info(login_cred_list)
            driver.quit()



