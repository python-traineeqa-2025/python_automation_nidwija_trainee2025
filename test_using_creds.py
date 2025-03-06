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
        list_cred = self.driver.find_elements(By.ID, 'login_credentials')

        login_cred_list = []
        for i in list_cred:
            logging.info(i.text)
            login_cred_list.append(i.text)
        logging.info(login_cred_list)

        username_input=self.driver.find_element(By.ID, 'user-name')
        username_input.click()
        username_input.send_keys(self.creds['standard_username'])
        password_input=self.driver.find_element(By.ID, 'password')
        password_input.click()
        password_input.send_keys(self.creds['Password_for_all_users'])
        submit_btn=self.driver.find_element(By.ID, 'login-button')
        submit_btn.click()
        time.sleep(5)




