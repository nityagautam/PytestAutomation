ALL_LOCATORS = {

    # -----------------------------------------------------------------------------------------------------------
    # Each entry demote the Page object class, with its name
    # -----------------------------------------------------------------------------------------------------------
    "DEMO_PAGE_CLASS_NAME": {
        "PAGE_CLASS_ELEMENT_1": "<LOCATOR_TYPE>=<LOCATOR_VALUE>",
        "PAGE_SUBMIT_BTN_1": "xpath=//*[@role='button' and @type='submit']",
        "PAGE_SUBMIT_BTN_2": "id=submit_btn",
        "PAGE_SUBMIT_BTN_3": "name=submit_btn",
        "PAGE_SUBMIT_BTN_4": "css=.btn > submit",
        "PAGE_SUBMIT_BTN_5": "class=submit_btn_class",
        "PAGE_SUBMIT_BTN_6": "link=submit_btn_link",
    },

    # -----------------------------------------------------------------------------------------------------------
    # Start adding yours below this line [You may refer above demo/sample]
    # -----------------------------------------------------------------------------------------------------------
    "GoogleSearchPage": {
        "SEARCH_BOX": "xpath=//input[@name='q']",
        "SEARCH_SUBMIT_BTN": "xpath=//*[@name='btnK' and @type='submit']",
        "SEARCH_RESULT_FIRST_LINK": "xpath=(//*[@id='rso']//a)[1]",
    }
}
