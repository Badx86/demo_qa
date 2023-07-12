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
    EXPAND_ALL_BUTTON = By.XPATH, "//button[@title='Expand all']//*[name()='svg']"
    COLLAPSE_ALL_BUTTON = By.XPATH, "//button[@title='Collapse all']//*[name()='svg']"
    HOME_TOGGLE = By.XPATH, "(//button[@title='Toggle'])[1]"
    DESKTOP_TOGGLE = By.XPATH, "(//button[@title='Toggle'])[2]"
    DOCUMENTS_TOGGLE = By.XPATH, "(//button[@title='Toggle'])[3]"
    WORKSPACE_TOGGLE = By.XPATH, "(//button[@title='Toggle'])[4]"
    OFFICE_TOGGLE = By.XPATH, "(//button[@title='Toggle'])[5]"
    DOWNLOADS_TOGGLE = By.XPATH, "(//button[@title='Toggle'])[6]"

    # Checkboxes
    HOME_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[1]"
    DESKTOP_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[2]"
    NOTES_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[3]"
    COMMANDS_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[4]"
    DOCUMENTS_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[5]"
    WORKSPACE_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[6]"
    REACT_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[7]"
    ANGULAR_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[8]"
    VEU_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[9]"
    OFFICE_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[10]"
    PUBLIC_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[11]"
    PRIVATE_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[12]"
    CLASSIFIED_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[13]"
    GENERAL_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[14]"
    DOWNLOADS_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[15]"
    WORD_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[16]"
    EXCEL_CHECKBOX = By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[17]"

    # Checkbox Result Notes
    RESULT_HOME = By.XPATH, "//div[@id='result']"

