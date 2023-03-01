import os
from src.utilities.Utility import Utility
# Don't Import the Logger in the config;
# Otherwise it will get stuck in loop (as Logger uses/imports the Config)
#   from src.utilities.Logger import Logger
#   log = Logger().get_logger()


# ===================================================================
# Place all the common data
# related to the application and framework in this class
# ===================================================================
class Config:
    # ------------------------------------------------------------
    # Browser/Driver configs
    # ------------------------------------------------------------
    FIREFOX_BIN_PATH = ''
    FIREFOX_DRIVER_PATH = f"./resources/drivers/geckodriver{str('.exe') if Utility().is_windows() else str('')}"
    CHROME_BIN_PATH = ''
    CHROME_DRIVER_PATH = f"./resources/drivers/chromedriver{str('.exe') if Utility().is_windows() else str('')}"
    BROWSER = "firefox"  # Browser name for the automation
    WAIT_TIMEOUT = 10  # Wait timeout in Seconds

    # ------------------------------------------------------------
    # General configs
    # ------------------------------------------------------------
    # Log file name and location
    LOG_FILE_PATH = './out/automation.log'
    # Screenshots path
    SCREENSHOT_LOC = os.path.abspath('./out/screenshots/')
    # External test data file path
    ALL_LOCATORS_JSON_FILE_PATH = os.path.abspath("./src/pages/locators.json")

    # ------------------------------------------------------------
    # Test Data configs
    # ------------------------------------------------------------
    # External test data file path
    TEST_DATA_FILE_PATH = os.path.abspath("./resources/test_data/test_data.json")

    # ------------------------------------------------------------
    # [TEST_DATA]
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
    TEST_DATA = None            # None, If external test_data.json is not loaded else entire json object

    # ------------------------------------------------------------
    # Initiation of above properties if test_data.json is found
    # ------------------------------------------------------------
    def __init__(self):
        # Test data expected path
        td_path = self.TEST_DATA_FILE_PATH

        # Debug Log
        print(f"Checking for the external test_data.json file from: {td_path}")

        try:
            # If config file is there then,
            if os.path.exists(td_path):
                print(f"[Config] Configuration file found ...")
                # Read the JSON file
                json_data = Utility.read_json(json_file_path=td_path)
                self.TEST_DATA = json_data
                print(f"[Config] config.TEST_DATA: {self.TEST_DATA['TEST_DATA']}")
                # Search for the keyword "IN_USE": true/false, if true then use
                if json_data['TEST_DATA']["IN_USE"]:
                    # Load the test data and override the class properties
                    # set the values now
                    print(f"[Config] Overriding the values now")
                else:
                    print(f"[Config] Will not be using the values, as the 'IN_USE' flag is False")
            else:
                print(f"[Config] 'test_data.json' file not found, will use default values ...")
        except Exception as e:
            print(f"[Config] Some error occurred while opening test_data.json file. \nError: \n", e)
