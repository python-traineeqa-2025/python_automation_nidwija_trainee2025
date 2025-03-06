from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):  # Accept driver from test class
        self.driver = driver

    def login(self, username, pwd):
        username_input = self.driver.find_element(By.ID, "user-name")
        username_input.click()
        username_input.send_keys(username)

        password_input = self.driver.find_element(By.ID, "password")
        password_input.click()
        password_input.send_keys(pwd)

        submit_btn = self.driver.find_element(By.ID, "login-button")
        submit_btn.click()
