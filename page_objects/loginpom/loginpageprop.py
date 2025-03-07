from selenium.webdriver.support.wait import WebDriverWait

from page_objects.loginpom.loginpagelocator import LoginPageLocators


class LoginPageProperties(LoginPageLocators):

    @property
    def username_input(self):
        return self.driver.find_element(*LoginPageLocators.USERNAME)

    @property
    def pwd_input(self):
        # self.wait=WebDriverWait(self.driver,20)
        # self.wait.until()
        return self.driver.find_element(*LoginPageLocators.PASSWORD)

    @property
    def submit_button(self):
        return self.driver.find_element(*LoginPageLocators.SUBMIT_BTN)