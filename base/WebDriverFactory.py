"""
   Return the webdriver based on the browser
   passed via command line
   """
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverFactory():


    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):

        site_url = "https://letskodeit.teachable.com"

        if self.browser == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(site_url)

        return driver
