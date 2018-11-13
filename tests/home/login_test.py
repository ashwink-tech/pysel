import inspect
import unittest
import pytest
from pages.home.login import LoginPage
from utils.assertstatus import AssertStatus


@pytest.mark.usefixtures("one_time_setup")
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, one_time_setup):
        self.lp = LoginPage(self.driver)
        self.ats = AssertStatus(self.driver)

    # inspect.stack is used to pass the testname i.e test_valid_login
    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("ashu271989@gmail.com", "test@123")
        self.ats.mark(self.lp.verify_login_sucess(), "Login not successful")
        self.ats.mark_final(inspect.stack()[0][3], self.lp.verify_title(), "Login not successful")

    @pytest.mark.run(order=1)
    def test_invalid__login(self):
        self.lp.logout()
        self.lp.click_on_login_link()
        self.lp.login("ashu271988@gmail.com", "test@123")
        self.ats.mark_final(inspect.stack()[0][3], self.lp.verify_login_not_success(), "Login successful")
