from utils.capturescreenshot import CaptureScreenShot


class AssertStatus():

    def __init__(self, driver):
        self.result_list = []
        self.driver = driver
        self.css = CaptureScreenShot(driver)

    def set_result(self, result, result_message):
        self.result_list.append(result)

    # This method should be used while adding assertion in any test method
    def mark(self, result, result_message):
        self.set_result(result, result_message)

    # This method should be used while adding last assertion in any test method
    def mark_final(self, test_name, result, result_message):
        print('The result is '+str(result))
        self.set_result(result, result_message)

        if False in self.result_list:
            self.css.capture_screen_shoot(test_name)
            assert True == False
        else:
            assert True == True

        self.result_list.clear()


