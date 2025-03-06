# import logging
import logging
from setup.basetest import BaseTest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class TestLogs():


    def test_first(self,driver):
            self.driver=driver
            self.driver.get("https://www.saucedemo.com/")
            logging.info("opened the site")
            title=self.driver.title
            logging.info("site opened. ")
            list_cred = self.driver.find_elements(By.ID, 'login_credentials')

            login_cred_list = []
            for i in list_cred:
                logging.info(i.text)
                login_cred_list.append(i.text)
                # i.click()
            logging.info(login_cred_list)



