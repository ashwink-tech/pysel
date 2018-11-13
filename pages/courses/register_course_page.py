import time

from base.BasePage import BasePage
from definitions import COURSE_PAGE
from genericmethods.BrowserActionMethods import BrowserActionMethods
from genericmethods.WaitMethods import WaitMethods


class RegisterCoursesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _find_course_field = "//input[@id='search-courses']"
    _course_link = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _course_enroll_button = "//button[@id='enroll-button-top']"
    _credit_card_field = "//input[@name='cardnumber']"
    _exp_date_field = "//input[@name='exp-date']"
    _cvc_field = "//input[@name='cvc']"
    _postal_field = "//input[@name='postal']"
    _terms_checkbox = "//*[(@id = 'agreed_to_terms_checkbox')]"
    _paypal_radio = "//div[@class='spc__tabs']//div[@id='paypal-radio']"
    _paypal_overlay = "//div[@class='spc is-loading']"
    _enroll_button = "//div[@class='spc__primary-submit']/button"

    def find_course(self, course_name):
        BrowserActionMethods.input(self.driver, self._find_course_field, course_name)

    def click_on_course(self, course_name):
        BrowserActionMethods.click(self.driver, self._course_link.format(course_name))

    def click_on_enroll_course(self):
        BrowserActionMethods.click(self.driver, self._course_enroll_button)

    def click_on_paypal(self):
        WaitMethods.wait_for_element_invisible(self.driver, self._paypal_overlay)
        BrowserActionMethods.click(self.driver, self._paypal_radio)

    def click_on_agreed_terms(self):
        BrowserActionMethods.scroll_down(self.driver)
        BrowserActionMethods.click_modified(self.driver, self._terms_checkbox)

    def click_on_enroll(self):
        BrowserActionMethods.click(self.driver, self._enroll_button)


    def enroll_in_course(self, course_name):

        self.find_course(course_name)
        self.click_on_course(course_name)
        self.click_on_enroll_course()
        self.click_on_paypal()
        self.click_on_agreed_terms()
        self.click_on_enroll()
        self.navigate_to_url(COURSE_PAGE)

