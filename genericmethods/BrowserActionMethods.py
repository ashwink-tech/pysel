from selenium.webdriver.common.by import By


class BrowserActionMethods:

    @staticmethod
    def click(driver, locator):
        BrowserActionMethods.get_element(driver, locator).click()

    @staticmethod
    def input(driver, locator, input_value):
        BrowserActionMethods.get_element(driver, locator).clear()
        BrowserActionMethods.get_element(driver, locator).send_keys(input_value)

    @staticmethod
    def get_element(driver, locator):
        return driver.find_element(By.XPATH, locator)



