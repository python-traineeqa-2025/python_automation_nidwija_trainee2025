# import logging
import logging
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from setup.basetest import BaseTest


class TestLogs(BaseTest):

    def test_first(self):
        self.driver.get("https://demoqa.com/alerts")
        logging.info("opened the site")
        title = self.driver.title
        logging.info(title)
        alert_element=self.driver.find_element(By.ID , "alertButton")
        alert_element.click()
        # self.driver.switch_to.
        alert = self.driver.switch_to.alert
        time.sleep(4)
        logging.info(f"Alert text: {alert.text} ")

        alert.accept()
        # alert.dismiss()
        # time.sleep(4)
        # prompt = self.driver.find_element(By.ID, "promtButton")
        # prompt.click()
        # #
        # # Wait for the prompt alert to appear
        #
        # # Switch to prompt alert and send keys
        # prompt_alert = self.driver.switch_to.alert
        # time.sleep(2)  # Small delay to ensure input field is interactive
        # prompt_alert.send_keys("Hello Selenium!")
        #
        # # Accept the prompt
        # prompt_alert.accept()
        # logging.info("Prompt accepted successfully!")