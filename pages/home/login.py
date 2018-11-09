from base.BasePage import BasePage
from genericmethods.BrowserMethods import BrowserMethods
from genericmethods.WaitMethods import WaitMethods
from genericmethods.BrowserActionMethods import BrowserActionMethods


class LoginPage(BasePage):

    def __init__(self, driver):

        super().__init__(driver)
        self.driver = driver

    _login_link = "//a[contains(@href,'sign_in')]"
    _email_field = "//input[@id='user_email']"
    _password_field = "//input[@id='user_password']"
    _login_button = "//input[@value='Log In']"
    _account_icon = "//img[@alt='ashu271989@gmail.com']"
    _login_error_msg = "//div[contains(text(),'Invalid email or password.')]"

    def click_on_login_link(self):
        BrowserActionMethods.click(self.driver, self._login_link)

    def login(self, username="", password=""):
        WaitMethods.wait_for_element(self.driver, self._email_field)
        BrowserActionMethods.input(self.driver, self._email_field, username)
        BrowserActionMethods.input(self.driver, self._password_field, password)
        BrowserActionMethods.click(self.driver, self._login_button)

    def verify_login_sucess(self):
        element = BrowserActionMethods.get_element(self.driver, self._account_icon)
        return element.is_displayed()

    def verify_title(self):
        self.verifyPageTitle("Let's Kode Its")

    def verify_login_not_success(self):
        element = BrowserActionMethods.get_element(self.driver, self._login_error_msg)
        return element.is_displayed()

