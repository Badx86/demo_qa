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
