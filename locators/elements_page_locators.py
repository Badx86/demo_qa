from selenium.webdriver.common.by import By


class TextBoxLocators:
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")
    # Text Box(input)
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    # Output form
    CREATED_FORM = By.XPATH, "//div[@id='output']"
    CREATED_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxLocators:
    EXPAND_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")
    OUTPUT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonLocators:
    YES_BUTTON = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_BUTTON = (By.CSS_SELECTOR, "label[for='noRadio']")
    TEXT_OUTPUT = (By.CSS_SELECTOR, ".mt-3")
    BTN_OUTPUT = (By.CSS_SELECTOR, ".text-success")


class WebTableLocators:
    # Registration Form (buttons)
    ADD_BUTTON = (By.CSS_SELECTOR, "#addNewRecordButton")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    # Search bar
    SEARCH_FIELD = (By.CSS_SELECTOR, "#searchBox")
    # Registration Form (fields)
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    AGE = (By.CSS_SELECTOR, "#age")
    SALARY = (By.CSS_SELECTOR, "#salary")
    DEPARTMENT = (By.CSS_SELECTOR, "#department")
    # Table
    FULL_TABLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    EDIT_PERSON_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    NO_ROWS_FOUND = (By.XPATH, "//div[@class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")


class ButtonsLocators:
    # Buttons
    DOUBLE_CLICK_BTN = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BTN = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_BTN = (By.CSS_SELECTOR, "div[class='mt-4']:nth-child(3n) button")
    # Output text
    DOUBLE_CLICK_MSG = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_MSG = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    CLICK_MSG = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")
