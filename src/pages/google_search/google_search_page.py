import time
from src.utilities.basepage import BasePage
from src.utilities.Logger import Logger


class GoogleSearchPage(BasePage):

    def __init__(self, driver, config_obj, logger_obj):
        # Init and load from super/parent class
        super().__init__(driver, config_obj, logger_obj)
        self.driver = driver
        # Since we have inherited the 'BasePage'
        # - All the props and methods from Config will be attached to self
        # - All the props and methods from Logger will be attached to self
        # - All the methods from Selenium driver will be attached to self
        # - All the methods from the Utility class will be attached to self
        # - Locators from the 'locators.py' for 'LoginPage' will be attached to self

    def search(self, keyword):
        self.log.debug(f"Initiating google search with keyword: {keyword} ...")
        # self.type(locator="xpath=//input[@name='q']", value=keyword + "\n")
        self.type(locator=self.SEARCH_BOX, value=keyword + "\n")
        # self.click(locator="xpath=//*[@name='btnK' and @type='submit']")
        self.click(locator=self.SEARCH_SUBMIT_BTN)
        # Sleep time
        time.sleep(5)

    def extract_and_verify_for_results(self):
        self.log.debug(f"Initiating extraction of first element on the result page ...")
        # first_link = self.get_element_with_wait(locator="xpath=(//*[@id='rso']//a)[1]")
        first_link = self.get_element_with_wait(locator=self.SEARCH_RESULT_FIRST_LINK)
        self.log.debug(f"First result for the keyword: {first_link.text} ...")
        assert len(first_link.text) > 0, "Zero result found after search"

    def browse_first_result_link(self):
        # first_link = self.get_element_with_wait(locator="xpath=(//*[@id='rso']//a)[1]")
        first_link = self.get_element_with_wait(locator=self.SEARCH_RESULT_FIRST_LINK)
        self.log.debug(f"Browsing First result for the keyword: {first_link.text} ...")
        self.click(locator=self.SEARCH_RESULT_FIRST_LINK)

