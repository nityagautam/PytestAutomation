from src.utilities.SD import SeleniumDriver
from traceback import print_stack
from src.utilities.Utility import Utility, PageLocatorDict
from src.pages.locators import ALL_LOCATORS


class BasePage(SeleniumDriver, PageLocatorDict, Utility):

    # ---------------------------------------------------------
    # Note:
    # ---------------------------------------------------------
    # Since 'BasePage' class
    # - takes these args during instance creation
    #   - driver object
    #   - config object from Config()
    #   - logger object from Logger(config).get_logger()
    # And,
    #   Where ever we inherit this 'BasePage' [normally in Page Object Classes]
    #   - All the props and methods from Config will be attached to self
    #   - All the props and methods from Logger will be attached to self
    #   - All the methods from Selenium driver will be attached to self
    #   - All the methods from the Utility class will be attached to self
    #   - Locators from the 'locators.py' for this TestPage will be attached to self

    def __init__(self, driver, config_obj, logger_obj):
        # ---------------------------------------------------------
        # Init the various Class
        # ---------------------------------------------------------
        self.driver = driver            # Web driver
        self.config = config_obj        # Configuration instance
        self.log = logger_obj           # Logger instance

        # ---------------------------------------------------------
        # Load the page locators from the 'src > pages > locators.py'
        # ---------------------------------------------------------
        if self.__class__.__name__ in ALL_LOCATORS:
            PageLocatorDict.__init__(self, ALL_LOCATORS[self.__class__.__name__])

    def get_page_locators_from_external_json_file(self, page_name):
        """
        Read the locator data from JSON for specific page
        :param page_name: page class name
        :return: list of all locators in specific page
        """
        all_locators_from_json = self.readJson(self.ALL_LOCATORS_JSON_FILE_PATH)
        page_locators = all_locators_from_json[f'{page_name}'] if all_locators_from_json[f'{page_name}'] else {}
        return page_locators

    def override_page_locators_from_external_json_file(self, page_name):
        """
        Override the locator data from JSON for specific page
        :param page_name: page class name
        """
        all_locators_from_json = self.readJson(self.ALL_LOCATORS_JSON_FILE_PATH)
        page_locators = all_locators_from_json[f'{page_name}'] if all_locators_from_json[f'{page_name}'] else {}
        PageLocatorDict.__init__(self, page_locators)

    def verify_page_title(self, title_to_verify):
        """
        Verify the page Title
        :param title_to_verify: Title on the page that needs to be verified
        """
        try:
            actual_title = self.getTitle()
            return title_to_verify == actual_title
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
