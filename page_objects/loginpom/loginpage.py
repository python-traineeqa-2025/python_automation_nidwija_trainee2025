
from page_objects.loginpom.loginpageprop import LoginPageProperties


class LoginPage(LoginPageProperties):

    def __init__(self,driver):
        self.driver=driver
        # self.wait=WebDriverWait(self.driver,20)



    def login(self, username, pwd):
        uname= self.username_input

        uname.click()
        # self.wait.until()
        uname.send_keys(username)
        password=self.pwd_input
        password.click()
        password.send_keys(pwd)
        submit=self.submit_button
        submit.click()
