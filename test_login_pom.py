import logging
import time

from setup.basetest import BaseTest
from page_objects.loginpage import LoginPage

class TestLogs(BaseTest):  # Inherit from BaseTest
    def test_first(self):
        url = self.creds["base_url"]
        self.driver.get( url)  # Ensure correct URL format
        logging.info("Opened the site")

        login_page = LoginPage(self.driver)
        uname = self.creds["standard_username"]
        pwd = self.creds["Password_for_all_users"]
        login_page.login(uname, pwd)

        time.sleep(5)  # Just for testing (remove in real automation)
