from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WaitMethods():

    @staticmethod
    def wait_for_element(driver, locator):
        wait = WebDriverWait(driver, 60, poll_frequency=2)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, locator)))

