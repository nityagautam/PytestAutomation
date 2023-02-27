"""
@package base

WebDriver Factory class implementation
It creates a web-driver instance based on browser configurations

"""
import os
from selenium import webdriver
from src.config.config import Config


class WebDriverFactory:

    def __init__(self):
        """
        Inits WebDriverFactory class
        :Returns None:
        """
        # Extract the info from config
        self.browser = Config().BROWSER       # td.testData("browser")
        self.baseUrl = Config().ENV_URL   # td.testData("environment")

    def get_web_driver_instance(self):
        """
        Get WebDriver Instance based on the browser configuration
        :return 'WebDriver Instance':
        """
        # TODO: Apply system/Platform

        if self.browser == "firefox":
            driver_location = "/Users/nityagautam/work/coding/prototype_projects/AutomationProjects" \
                              "/PytestAutomation/resources/geckodriver"
            os.environ["webdriver.gecko.driver"] = driver_location
            driver = webdriver.Firefox()

        elif self.browser == "chrome":
            # Set Chrome driver
            driver_location = "/Users/nityagautam/work/coding/prototype_projects/AutomationProjects" \
                             "/PytestAutomation/resources/chromedriver"
            os.environ["webdriver.chrome.driver"] = driver_location
            driver = webdriver.Chrome(driver_location)
            driver.set_window_size(1366, 768)

        else:
            driver = webdriver.Firefox()

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(15)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(self.baseUrl)

        return driver


