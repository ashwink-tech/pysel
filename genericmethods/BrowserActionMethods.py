import selenium
from selenium.webdriver.common.by import By

from genericmethods.WaitMethods import WaitMethods


class BrowserActionMethods:

    @staticmethod
    def click(driver, locator):
        WaitMethods.wait_for_element(driver, locator)
        BrowserActionMethods.get_element(driver, locator).click()

    @staticmethod
    def click_modified(driver, locator):
        BrowserActionMethods.get_element(driver, locator).send_keys(selenium.webdriver.common.keys.Keys.SPACE)

    @staticmethod
    def submit(driver, locator):
        BrowserActionMethods.get_element(driver, locator).submit()

    @staticmethod
    def input(driver, locator, input_value):
        WaitMethods.wait_for_element(driver, locator)
        element = BrowserActionMethods.get_element(driver, locator)
        element.clear()
        element.send_keys(input_value)

    @staticmethod
    def get_element(driver, locator):
        return driver.find_element(By.XPATH, locator)

    @staticmethod
    def scroll_down(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")







