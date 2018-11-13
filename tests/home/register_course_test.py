import pytest
import unittest
from pages.courses.register_course_page import RegisterCoursesPage


@pytest.mark.usefixtures("one_time_setup")
class TestRegisterCourse(unittest.TestCase):
    """
    objectSetup is used to create an instance of page classes.
    autouse=True helps to use the instance across the class.
    """
    @pytest.fixture(autouse=True)
    def objectSetup(self, one_time_setup):
        self.rc = RegisterCoursesPage(self.driver)

    # use to enroll in the courses
    @pytest.mark.run(order=1)
    def test_enroll_course(self):
        self.rc.enroll_in_course("JavaScript for beginners")
