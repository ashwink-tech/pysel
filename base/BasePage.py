from genericmethods.BrowserMethods import BrowserMethods


class BasePage():

    def __init__(self, driver):

        self.driver = driver

    def verify_page_title(self, title_to_verify):

        actual_title = BrowserMethods.get_title(self.driver)

        if actual_title in title_to_verify:
            return True
        else:
            return False

    def navigate_to_url(self, url):
        BrowserMethods.navigate_to_url(self.driver, url)

