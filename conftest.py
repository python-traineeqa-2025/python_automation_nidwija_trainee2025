import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    # Setup
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver  #this instance of webdriver will be used by the test

    # Teardown
    driver.quit()
