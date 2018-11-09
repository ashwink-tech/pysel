import datetime
import os
import time


class CaptureScreenShot():

    def __init__(self, driver):
        self.driver = driver

    def capture_screen_shoot(self, test_name):

        screen_shot_path = os.path.dirname(os.path.dirname(__file__)) +\
                           "/screenshots/" + "Shot_" + datetime.datetime.now().strftime("%m_%d_%Y_%H:%M:%S")
        os.makedirs(screen_shot_path)
        self.driver.save_screenshot(screen_shot_path + "/"+ test_name + ".png")
