from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#this installs and sets up chromedriver on its own
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")
print("Page Title:", driver.title)

driver.quit()
