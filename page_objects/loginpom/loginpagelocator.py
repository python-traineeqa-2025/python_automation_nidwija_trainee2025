from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME =(By.ID, "user-name")
    PASSWORD =(By.ID,"password")
    SUBMIT_BTN=(By.ID, "login-button")
