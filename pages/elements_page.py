import allure
from locators.elements_page_locators import TextBoxLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    @allure.step('Fill all fields and submit form')
    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Test_Name')
        self.element_is_visible(self.locators.EMAIL).send_keys("Test@Email.com")
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys("Test_Current_Address")
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys("Test_Permanent_Address")
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return self.element_is_visible(self.locators.CREATED_FORM)




