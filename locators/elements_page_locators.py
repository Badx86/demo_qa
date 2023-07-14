from selenium.webdriver.common.by import By


class TextBoxLocators:
    # Text Box(input)
    FULL_NAME = By.XPATH, "//input[@id='userName']"
    EMAIL = By.XPATH, "//input[@id='userEmail']"
    CURRENT_ADDRESS = By.XPATH, "//textarea[@id='currentAddress']"
    PERMANENT_ADDRESS = By.XPATH, "//textarea[@id='permanentAddress']"
    SUBMIT_BUTTON = By.XPATH, "//button[@id='submit']"

    # Output form
    CREATED_FORM = By.XPATH, "//div[@id='output']"
    CREATED_NAME = By.XPATH, "//p[@id='name']"
    CREATED_EMAIL = By.XPATH, "//p[@id='email']"
    CREATED_CURRENT_ADDRESS = By.XPATH, "//p[@id='currentAddress']"
    CREATED_PERMANENT_ADDRESS = By.XPATH, "//p[@id='permanentAddress']"


class CheckBoxLocators:
    # Buttons
    EXPAND_ALL_BUTTON = By.XPATH, "//button[@title='Expand all']"
    COLLAPSE_ALL_BUTTON = By.XPATH, "//button[@title='Collapse all']//*[name()='svg']"
    ITEMS_LIST = By.CSS_SELECTOR, "span[class='rct-title']"
    RESULT = By.CSS_SELECTOR, "#result"
    CHECKED_ITEMS = By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']"
    ITEMS_TITLE = By.CSS_SELECTOR, "span[class='rct-title']"