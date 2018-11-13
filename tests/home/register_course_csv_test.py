import unittest
import pytest
from ddt import ddt, data, unpack

from definitions import ROOT_DIR
from pages.courses.register_course_page import RegisterCoursesPage
from utils.getcsvdata import get_csv_data


@pytest.mark.usefixtures("one_time_setup")
@ddt
class TestRegisterCourseCsv(unittest.TestCase):
    """
    objectSetup is used to create an instance of page classes.
    autouse=True helps to use the instance across the class.
    """
    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.rc = RegisterCoursesPage(self.driver)

    # use to enroll in the courses
    @pytest.mark.run(order=1)
    @data(*get_csv_data(ROOT_DIR + "/testdata.csv"))
    @unpack
    def test_enroll_course(self, course_name):
        self.rc.enroll_in_course(course_name)
