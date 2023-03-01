# Standard Imports
# ===================
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import time
import os

# Custom Imports
# ================
from src.utilities.Logger import Logger
from src.config.config import Config


class SeleniumDriver(Config):

    # ---------------------------------------------------------
    # Note:
    # ---------------------------------------------------------
    # Since we've inherited the 'Config', hence
    # - All the props and methods from Config class will be attached to self

    def __init__(self, driver):
        self.driver = driver
        self.log = Logger().get_logger()    # Get the custom logger

    def get_title(self):
        return self.driver.title

    def parse_locator(self, locator, locator_type='id'):
        # Extract the type and value
        locator_type = locator[:locator.find("=")].lower()
        locator_value = locator[locator.find("=") + 1:]

        # Find and return the type
        if locator_type == "id":
            return By.ID, locator_value
        elif locator_type == "name":
            return By.NAME, locator_value
        elif locator_type == "xpath":
            return By.XPATH, locator_value
        elif locator_type == "css":
            return By.CSS_SELECTOR, locator_value
        elif locator_type == "class":
            return By.CLASS_NAME, locator_value
        elif locator_type == "link":
            return By.LINK_TEXT, locator_value
        else:
            self.log.info(f"Please follow the pattern: <LOCATOR_TYPE>=<LOCATOR_VALUE>")
            self.log.info("[PARSE LOCATOR] Locator type" + locator_type + "not correct/supported")
        return None, None

    def get_element(self, locator):
        element = None
        try:
            # Extract the locator type and value
            by_type, locator_value = self.parse_locator(locator)
            element = self.driver.find_element(by_type, locator_value)

            self.log.debug("Element found with locator: " + locator_value + " and By Type: " + by_type)
        except Exception as e:
            self.log.error("Element not found with locator: " + locator_value + " and By Type: " + by_type)
            self.log.error(e)

        # and, Return the collected element
        return element

    def get_element_with_wait(self, locator):
        element = None
        try:
            # Extract the locator type and value
            by_type, locator_value = self.parse_locator(locator)

            # Apply wait first
            self.log.debug(f"Applying wait with {self.WAIT_TIMEOUT} secs...")
            # wait = WebDriverWait(self.driver, self.timeout, ignored_exceptions=StaleElementReferenceException)
            wait = WebDriverWait(self.driver, self.WAIT_TIMEOUT)

            # Fetch the element with Expected condition of until clickable as default
            # element = wait.until(EC.visibility_of_element_located((by_type, locator_value)))
            element = wait.until(EC.element_to_be_clickable((by_type, locator_value)))

            self.log.debug("Element found with locator: " + locator_value + " and By Type: " + by_type)
        except Exception as e:
            self.log.debug("Element not found with locator: " + locator_value + " and By Type: " + by_type)
            self.log.error(e)

        # and, Return the collected element
        return element

    def click(self, locator):
        try:
            element = self.get_element_with_wait(locator=locator)
            if element:
                element.click()
        except Exception as e:
            self.log.debug(f"Unable to click.")
            self.log.debug(e)

    def type(self, locator, value):
        try:
            element = self.get_element_with_wait(locator=locator)
            if element:
                element.send_keys(value)
        except Exception as e:
            self.log.debug(f"Unable to type on given element.")
            self.log.debug(e)

    def clear(self, locator):
        try:
            element = self.get_element_with_wait(locator=locator)
            if element:
                element.clear()
        except Exception as e:
            self.log.debug(f"Unable to clear the value of given element.")
            self.log.debug(e)

    def take_screenshot(self, sc_path):
        try:
            # This 'sc_path' is being taken care of from 'conftest.py' module
            # Take the screenshot now
            self.driver.get_screenshot_as_file(sc_path)

            # return the screenshot file name
            self.log.debug(f"Screenshot taken at: {sc_path}")
        except Exception as e:
            self.log.debug(f"Something went wrong while taking screenshot.")
            self.log.debug(e)

    # --------------------------------------------------------
    # Further Custom definitions
    # --------------------------------------------------------
    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.get_by_type(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator +
                          " and locatorType: " + locatorType)
        return element

    def dropdown_select_element(self, locator, locatorType="id", selector="", selectorType="value"):
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            if selectorType == "value":
                sel.select_by_value(selector)
                time.sleep(1)
            elif selectorType == "index":
                sel.select_by_index(selector)
                time.sleep(1)
            elif selectorType == "text":
                sel.select_by_visible_text(selector)
                time.sleep(1)
            self.log.info("Element selected with selector: " + str(selector) +
                          " and selectorType: " + selectorType)

        except:
            self.log.error("Element not selected with selector: " + str(selector) +
                       " and selectorType: " + selectorType)
            print_stack()

    def get_dropdown_options_count(self, locator, locatorType="id"):
        '''
        get the number of options of drop down list
        :return: number of Options of drop down list
        '''
        options = None
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            options = sel.options
            self.log.info("Element found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator +
                       " and locatorType: " + locatorType)

        return options

    def getDropdownSelectedOptionText(self, locator, locatorType="id"):
        '''
        get the text of selected option in drop down list
        :return: the text of selected option in drop down list
        '''
        selectedOption_text = None
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            selectedOption_text = sel.first_selected_option.text
            self.log.info("Return the selected option of drop down list with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.error("Can not return the selected option of drop down list with locator: " + locator +
                       " and locatorType: " + locatorType)

        return selectedOption_text

    def getDropdownSelectedOptionValue(self, locator, locatorType="id"):
        '''
        get the value of selected option in drop down list
        :return: the value of selected option in drop down list
        '''
        selectedOption_value = None
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            selectedOption_value = sel.first_selected_option.get_attribute("value")
            self.log.info("Return the selected option of drop down list with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.error("Can not return the selected option of drop down list with locator: " + locator +
                       " and locatorType: " + locatorType)

        return selectedOption_value

    def isElementSelected(self, locator, locatorType):
        isSelected = None
        try:
            element = self.getElement(locator, locatorType)
            isSelected = element.is_selected()
            self.log.info("Element found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator +
                           " and locatorType: " + locatorType)

        return isSelected

    def getElementList(self, locator, locatorType="id"):
        """
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.get_by_type(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.error("Element list not found with locator: " + locator +
                           " and locatorType: " + locatorType)

        return element



    def elementClick(self, locator="", locatorType="id", element=None):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def elementHover(self, locator="", locatorType="id", element=None):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            time.sleep(2)
            self.log.info("hover to element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("cannot hover to the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("send data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("cannot send data on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def clearKeys(self, locator="", locatorType="id", element=None):
        """
        Clear keys of an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.clear()
            self.log.info("Clear data of element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("cannot clear data of the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) !=0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element found with locator: " + locator +
                              " and locatorType: " + locatorType)
                return True
            else:
                self.log.error("Element not found with locator: " + locator +
                              " and locatorType: " + locatorType)
                return False
        except:
            self.log.error("Element not found with locator: " + locator +
                              " and locatorType: " + locatorType)
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " and locatorType: " + locatorType)
            else:
                self.log.error("Element is not displayed with locator: " + locator +
                              " and locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.error("Element is not displayed with locator: " + locator +
                              " and locatorType: " + locatorType)
            return False

    def elementPresenceCheck(self, locator="", locatorType="id"):
        try:
            locatorType = locatorType.lower()
            byType = self.get_by_type(locatorType)
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType = 'id', timeout = 10, pollFrequency = 0.5 ):
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            ByType = self.get_by_type(locatorType)
            element = wait.until(EC.element_to_be_clickable((ByType,locator)))

            self.log.info("Element appeared on the web page")

        except:
            self.log.info("Element not appeared on the web page")
            print_stack()

        return element

    def webScroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def getURL(self):
        '''
        Get the current URL
        :return: current URL
        '''
        currentURL = self.driver.current_url

        return currentURL

    def pageBack(self):
        '''
        page back the browser
        '''
        self.driver.execute_script("window.history.go(-1)")

    def getAttributeValue(self, locator="", locatorType="id", element=None, attribute=""):
        '''
        get attribute value
        '''
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            attribute_value = element.get_attribute(attribute)
        except:
            self.log.error("Failed to get " + attribute + " in element with locator: " +
                           locator + " and locatorType: " + locatorType)
            print_stack()
            attribute_value = None
        return attribute_value

    def refresh(self):
        self.driver.get(self.driver.current_url)

    def page_has_loaded(self):
        try:
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return document.readyState == "complete";'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return jQuery.active == 0'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return typeof jQuery != "undefined"'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return angular.element(document).injector().get("$http").pendingRequests.length === 0'))
        except:
            return False

    def screenShot(self, resultMessage):
        """
        Take a screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        if len(fileName) >= 200:
            fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            allure.attach(self.driver.get_screenshot_as_png(),
                          name=fileName,
                          attachment_type=allure.attachment_type.PNG)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()


