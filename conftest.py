import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    driver_path = r"D:\Users\nidwija.bhatta\Documents\PYTHON\python_automation_nidwija_trainee2025\bin\chromedriver.exe"

    ser = Service(driver_path)
    driver = webdriver.Chrome(service=ser)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver  #this instance of webdriver will be used by the test

    # Teardown
    driver.quit()
