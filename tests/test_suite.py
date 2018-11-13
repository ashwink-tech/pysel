import unittest

from tests.home.login_test import TestLogin
from tests.home.register_course_test import TestRegisterCourse


tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestRegisterCourse)

smoke_test = unittest.TestSuite([tc1, tc2])


unittest.TextTestRunner(verbosity=2).run(smoke_test)
