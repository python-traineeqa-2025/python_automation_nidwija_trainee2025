import json
import logging

from selenium import webdriver

class BaseTest:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    logger = logging.getLogger(__name__)

    def setup_method(self, method):
        # driver_path = r"D:\Users\nidwija.bhatta\Documents\PYTHON\python_automation_nidwija_trainee2025\bin\chromedriver.exe"
        #
        # ser = Service(driver_path)
        # logging.info("set up driver")
        # driver = webdriver.Chrome(service=ser)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        creds_path = r"C:\Users\user\Documents\PYTHONPROJECTS\python_automation_nidwija_trainee2025\cred\creds.json"
        with open(creds_path, "r") as f:
            self.creds = json.load(f)

    def teardown_method(self, method):
        self.driver.quit()
