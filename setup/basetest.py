# import json
# import logging
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
#
# class BaseTest:
#     logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
#     logger = logging.getLogger(__name__)
#
#     def setup_method(self, method):
#         # driver_path = r"D:\Users\nidwija.bhatta\Documents\PYTHON\python_automation_nidwija_trainee2025\bin\chromedriver.exe"
#         #
#         # ser = Service(driver_path)
#         # logging.info("set up driver")
#         # driver = webdriver.Chrome(service=ser)
#         # self.driver=driver
#         self.driver = webdriver.Chrome()
#
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#
#         # creds_path = r"D:\Users\nidwija.bhatta\Documents\PYTHON\python_automation_nidwija_trainee2025\cred\creds.json"
#         creds_path = r"C:\Users\user\Documents\PYTHONPROJECTS\python_automation_nidwija_trainee2025\cred\creds.json"
#         with open(creds_path, "r") as f:
#             # x=json.load(f)
#             self.creds = json.load(f)
#
#     def teardown_method(self, method):
#         self.driver.quit()
import json
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BaseTest:
    """Base test class to handle WebDriver setup & credentials loading."""

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)

    @pytest.fixture(autouse=True, scope="class")
    def setup(self, request):
        """Automatically initializes WebDriver and credentials for tests."""

        driver_path = r"D:\Users\nidwija.bhatta\Documents\PYTHON\python_automation_nidwija_trainee2025\bin\chromedriver.exe"

        ser = Service(driver_path)
        logging.info("set up driver")
        driver = webdriver.Chrome(service=ser)
        self.driver=driver

        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # Load credentials
        creds_path = r"D:\Users\nidwija.bhatta\Documents\PYTHON\python_automation_nidwija_trainee2025\cred\creds.json"

        # creds_path = r"C:\Users\user\Documents\PYTHONPROJECTS\python_automation_nidwija_trainee2025\cred\creds.json"
        with open(creds_path, "r") as f:
            self.creds = json.load(f)

        # Attach driver to the test class instance
        request.cls.driver = self.driver
        request.cls.creds = self.creds

        yield

        self.driver.quit()
