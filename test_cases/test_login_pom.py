import logging
import time

from setup.basetest import BaseTest

from page_objects.loginpom.loginpage import LoginPage

class TestLogs(BaseTest):  # Inherit from BaseTest
    def test_login(self):
        url = self.creds["base_url"]
        self.driver.get( url)  # Ensure correct URL format
        logging.info("Opened the site")

        login_page = LoginPage(self.driver)
        logging.info("getting the credentials")

        uname = self.creds["standard_username"]
        pwd = self.creds["Password_for_all_users"]
        logging.info("got the credentials now logging in")
        login_page.login(uname,pwd)
        logging.info("logged in")

        time.sleep(5)
