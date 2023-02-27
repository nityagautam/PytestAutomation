import os
from src.utilities.Utility import Utility
from src.utilities.Logger import Logger


# get the logger first
log = Logger().get_logger()


# ===================================================================
# Place all the common data
# related to the application and framework in this class
# ===================================================================
class Config:
    # ------------------------------------------------------------
    # Default Configuration data for the application
    # ------------------------------------------------------------
    APP_REPORT_TITLE = "AMISHRA AUTOMATION REPORT"   # This is just for the Report title
    ENV_URL = "https://google.co.in"
    ENV_TYPE = "TEST"
    ENV_CREDENTIALS = {
        "DEV": {"USERNAME": "username", "PASSWORD": "password"},
        "TEST": {"USERNAME": "username", "PASSWORD": "password"},
        "STAGING": {"USERNAME": "username", "PASSWORD": "password"},
        "PRODUCTION": {"USERNAME": "username", "PASSWORD": "password"}
    }
    BROWSER = "firefox"         # Browser name for the automation
    WAIT_TIMEOUT = 10           # Wait timeout in Seconds
    RETRY_COUNT = 1             # As loop/Iteration of tries
    TEST_DATA = None            # None, If external test_data.json is not loaded else entire json object

    # Screenshots path
    SCREENSHOT_LOC = os.path.abspath('./out/screenshots/')

    # External test data file path
    ALL_LOCATORS_JSON_FILE_PATH = os.path.abspath("./src/pages/locators.json")

    # External test data file path
    TEST_DATA_FILE_PATH = os.path.abspath("./resources/test_data/test_data.json")

    # ------------------------------------------------------------
    # Initiation of above properties if test_data.json is found
    # ------------------------------------------------------------
    def __init__(self):
        # Test data expected path
        td_path = os.path.abspath("./resources/test_data/test_data.json")

        # Debug Log
        log.debug(f"Checking for the external test_data.json file from: {td_path}")

        try:
            # If config file is there then,
            if os.path.exists(td_path):
                # TODO:
                log.debug(f"Configuration file found ...")
                # Read the JSON file
                json_data = Utility.read_json(json_file_path=td_path)
                self.TEST_DATA = json_data
                log.debug(f" FROM config.TEST_DATA: {self.TEST_DATA['TEST_DATA']}")
                # Search for the keyword "IN_USE": true/false, if true then use
                if json_data['TEST_DATA']["IN_USE"]:
                    # Load the test data and override the class properties
                    # set the values now
                    log.debug(f"Overriding the values now")
                else:
                    log.debug(f"Will not be using the values, as the 'IN_USE' flag is False")
            else:
                log.debug(f"'test_data.json' file not found, will use default values ...")
        except Exception as e:
            log.debug(f"Some error occurred while opening test_data.json file. \nError: \n", e)
