# import logging
import logging
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from setup.basetest import BaseTest


class TestLogs(BaseTest):

    def test_first(self):
        self.driver.get("https://www.jeevee.com/")
        logging.info("opened the site")
        title = self.driver.title
        logging.info(title)
        hover_element=self.driver.find_element(By.XPATH, "//div[text()='My Account']")
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()
        logging.info("opened dropdown")
        login_btn=self.driver.find_element(By.XPATH, "//div[text()='Login']")
        login_btn.click()
        logging.info("opened the dropdown and clicked on login")
        time.sleep(6)