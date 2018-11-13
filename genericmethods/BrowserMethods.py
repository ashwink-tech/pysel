
class BrowserMethods:

    @staticmethod
    def get_title(driver):
        return driver.title

    @staticmethod
    def navigate_to_url(driver, url):
        driver.get(url)
