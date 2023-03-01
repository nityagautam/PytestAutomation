import pytest
from src.utilities.basetest import BaseTest
from src.pages.google_search.google_search_page import GoogleSearchPage


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
