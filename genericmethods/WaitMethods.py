from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WaitMethods():

    @staticmethod
    def wait_for_element(driver, locator):
        wait = WebDriverWait(driver, 120, poll_frequency=2)
        element_present = expected_conditions.presence_of_element_located((By.XPATH, locator))
        wait.until(element_present)
        element_clickable = expected_conditions.element_to_be_clickable((By.XPATH, locator))
        wait.until(element_clickable)

    @staticmethod
    def wait_for_element_invisible(driver, locator):
        wait = WebDriverWait(driver, 120, poll_frequency=2)
        element_invisible = expected_conditions.invisibility_of_element_located((By.XPATH, locator))
        wait.until(element_invisible)