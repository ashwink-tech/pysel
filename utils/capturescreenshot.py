import datetime
import os
from definitions import ROOT_DIR


class CaptureScreenShot:

    def __init__(self, driver):
        self.driver = driver

    def capture_screen_shoot(self, test_name):

        screen_shot_path = ROOT_DIR +\
                           "/screenshots/" + "Shot_" + datetime.datetime.now().strftime("%m_%d_%Y_%H:%M:%S")
        # Creates a directory
        os.makedirs(screen_shot_path)
        self.driver.save_screenshot(screen_shot_path + "/"+ test_name + ".png")
