"""
@package base

WebDriver Factory class implementation
It creates a web-driver instance based on browser configurations

"""
import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from src.utilities.Logger import Logger


class WebDriverFactory:

    def __init__(self, config_obj):
        """
        Inits WebDriverFactory class
        :Returns None:
        """
        # Extract the info from config
        if config_obj is not None:
            self.config = config_obj
            self.browser = self.config.BROWSER
            self.baseUrl = self.config.ENV_URL
            # Get the logger and configuration
            self.log = Logger(self.config).get_logger()
        else:
            self.log.error(f"Please provide the correct instance of config to WDF(WebDriverFactory)")
            pytest.exit(f"[ERROR] >>> Some error occurred, Check the log {self.config.LOG_FILE_PATH}")

    def get_web_driver_instance(self):
        """
        Get WebDriver Instance based on the browser configuration
        :return 'WebDriver Instance':
        """
        driver = None

        try:
            if self.browser.lower() == "firefox":
                # Set firefox driver
                driver_location = os.path.abspath(self.config.FIREFOX_DRIVER_PATH)
                # TODO: Write a function which searches the bin files from the system installation paths and ENV paths
                options = Options()
                options.binary_location = driver_location
                os.environ["webdriver.gecko.driver"] = driver_location
                # driver = webdriver.Firefox(options=options)
                driver = webdriver.Firefox()

            #elif self.browser.lower() == "chrome":
            else:
                # Set Chrome driver
                driver_location = os.path.abspath(self.config.CHROME_DRIVER_PATH)
                os.environ["webdriver.chrome.driver"] = driver_location
                driver = webdriver.Chrome(driver_location)
                # driver.set_window_size(1366, 768)

            # Setting Driver Implicit Time out for An Element
            driver.implicitly_wait(15)
            # Maximize the window
            driver.maximize_window()
            # Loading browser with App URL
            driver.get(self.baseUrl)

            # now, return the web driver
            return driver

        except Exception as e:
            self.log.debug(f"While creating {self.browser} webdriver instance, Following Error occurred")
            self.log.error(e)
            self.log.debug(f"Exiting now...")
            pytest.exit(f"[ERROR] >>> Some error occurred, Check the log {self.config.LOG_FILE_PATH}")




