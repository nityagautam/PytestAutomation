# PyTest Automation Framework
An automation framework using pytest, pytest-html  
<hr/>


### Pre-Requisite:
<pre>
    1. python3
    2. Updated web drivers in (./resources/drivers/)
    3. Consider adding driver location into system path
</pre>

### Setup
<pre>
    1. Clone the repo
        ~ git clone {this_repo_link}
        ~ cd ./PytestAutomation
    2. Run the requirement (You can also create virtualenv first before installing modules)
        ~ pip install -r requirements.txt
</pre>


### Execution
> python -m pytest {runs the entire framework test}

> python -m pytest <PATH_TO_TEST_FILE> {runs the specific test file}


### Results / Reports
<pre>
    After an execution, We can find the test results in form of html/xml reports in 
    - `out/test_result.xml`
    - `out/test_report.xml`

Note: These location can be easily modified in `./pytest.ini`
</pre>


### Folder Structure
<pre>
      root
        |____ out
                |____ reports
                |____ screenshots
                |____ automation.log
                |____ report.html
                |____ test_result.xml

        |____ resources
                |____ drivers
                |____ test_data
                        |____ test_data.json (Contains test data along with configuration values)

        |____ src
                |____ config
                        |____ config.py (Contains the configuration for entire framework)[HP]
                |____ pages
                        |____ xyz_page (Page Object Classes)
                        |____ locators.py (Contains all the locators)[HP]
                        |____ locators.json (Contains all the locators)[LP]
                |____ tests
                        |____ sanity
                        |____ etc
                |____ utilities
                        |____ basepage.py (Base class for PageObject classes)
                        |____ basetest.py (Base class for Test classes)
                        |____ Logger (Custom Logger)
                        |____ SD.py (SeleniumDriver)
                        |____ Utility.py (Common Utility)
                        |____ WDF.py (WebDriverFactory)
                |____ __init__.py
                |____ conftest.py (Contains pytest common fixtures)

        |____ pytest.ini (Contains pytest configuration)
        |____ README.md
        |____ LICENSE
        |____ requirements.txt (Python lib/modules requirements)

:>
HP = High presidency
LP = Low presidency
</pre>


<br/><br/><hr/>
## Development
<hr/>

### Adding New Page Object class
<pre>
You can add new page object classes under the `src/pages/`
which inherits the `BasePage` class from `src/utilities/basepage.py` 
</pre>


### Adding New Test class
<pre>
You can add new Test classes under the `src/tests/`
which inherits the `BaseTest` class from `src/utilities/basetest.py` 
[
consider under an suite like `src/tests/{suite_name}/{Test_file}`; 
Example: `src/tests/sanity/test_one.py`
]
</pre>


### Adding locators for Page Object
<pre>
You can add new locators for any page object classes under the `src/pages/locators.py`
And from the constructor of 'BasePage' we will be loading all the locators 
for that specific page object class and will attach them to 'self' of chile page object class.

EXAMPLE:

locators.py:
    ALL_LOCATORS = {
        "Page_Object_Class_Name": {
            "LOCATOR_NAME": "{LOCATOR_TYPE}={LOCATOR_VALUE}",
            "SUBMIT_BTN": "xpath=//.*[@type='submit']",
        },
        ...
    }

Any_page_object_class.py:
    class Page_Object_Class_Name(BasePage):
        def __init__(self, driver):
            # Init and load from super/parent class
            super().__init__(driver)
            self.driver = driver

        def click_on_some_button_step(self):
            self.click(locator=self.SUBMIT_BTN)

        ...

Note: You can also refer to the existing demo test classes and page object classes for implementations.

            
</pre>

