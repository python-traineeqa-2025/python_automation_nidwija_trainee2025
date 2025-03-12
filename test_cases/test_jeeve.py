# import logging
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from setup.basetest import BaseTest


class TestLogs(BaseTest):

    def test_first(self):
        self.driver.get("https://www.jeevee.com/")
        logging.info("opened the site")
        title = self.driver.title
        logging.info(title)