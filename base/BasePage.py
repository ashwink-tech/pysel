from genericmethods.BrowserMethods import BrowserMethods


class BasePage():

    def __init__(self, driver):

        self.driver = driver

    def verifyPageTitle(self, title_to_verify):

        actual_title = BrowserMethods.get_title(self.driver)

        if actual_title in title_to_verify:
            return True
        else:
            return False

