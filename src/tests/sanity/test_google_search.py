# from utilities.teststatus import TestStatus
# from navigation.homeNavigation import HomeNavigation
# from pages.loggedin_page import LoggedInPage
# import test_data.testData as td
# @pytest.fixture(autouse=True) sd
# Allure:
#   @allure.story('epic_1')  # epic/story of the test case
#   @allure.severity(allure.severity_level.MINOR)  # severity of the test case
#
# def classSetup(self):
#     self.loginPage = LoginPage(self.driver)

import pytest
import sys
import allure
from src.utilities.basetest import BaseTest
from src.pages.google_search.google_search_page import GoogleSearchPage
from src.config.config import Config


@pytest.mark.sanity
@pytest.mark.first
class TestGoogleSearch(BaseTest):

    # ------------------------------------------------
    # Before each Test def,
    # we need to initialize some page objects
    # ------------------------------------------------
    # @pytest.fixture(autouse=True)
    # def class_setup(self):
    #     self.loginPage = LoginPage(self.driver)
    #     self.config = Config()
    # -[END]-----------------------------------------------
    loginPage = None

    # -[TESTs STARTS FROM HERE]-----------------------------------------------

    def test_search_google_and_browse_first_result(self):
        # Create object for page(s)
        self.loginPage = GoogleSearchPage(self.driver)

        # Steps
        self.loginPage.search('EARTH')
        self.loginPage.extract_and_verify_for_results()
        self.loginPage.browse_first_result_link()

    def test_sample(self):
        assert True, "All good"
