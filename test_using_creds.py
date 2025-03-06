# import logging
import logging
import time

from setup.basetest import BaseTest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class TestLogs(BaseTest):
    def test_first(self):
        url=self.creds['base_url']
        self.driver.get(url)
        logging.info("opened the site")
        title=self.driver.title
        logging.info("site opened. ")
        users_pwd=self.creds["users"]
        logging.info(users_pwd)

        #loop for key value, sendkeys garda username is key pwd is value


        username_input=self.driver.find_element(By.ID, 'user-name')
        username_input.click()
        uname=self.creds['standard_username']
        username_input.send_keys(uname )
        password_input=self.driver.find_element(By.ID, 'password')
        password_input.click()
        password_input.send_keys(self.creds['Password_for_all_users'])
        submit_btn=self.driver.find_element(By.ID, 'login-button')
        submit_btn.click()
        time.sleep(5)




