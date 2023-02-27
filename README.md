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