import logging
import time

from selenium.webdriver.common.by import By
from setup.basetest import BaseTest
from page_objects.loginpom.loginpage import LoginPage

class TestLogin(BaseTest):

    def test(self):
        url = self.creds["base_url"]
        uname = self.creds["standard_username"]
        pwd = self.creds["Password_for_all_users"]


        self.driver.get(url)
        logging.info("opened the site")
        login=LoginPage(self.driver)
        login.login(uname,pwd)




        product = self.driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Onesie']")
        product.click()

        description = self.driver.find_element(By.XPATH, "//div[@class='inventory_details_desc large_size']")
        logging.info(description.text)

        price = self.driver.find_element(By.XPATH, "//div[@class='inventory_details_price']")
        logging.info(price.text)

        time.sleep(6)


