import allure
from data.urls import TEXT_BOX_URL
from pages.elements_page import TextBoxPage


@allure.epic('Test Elements')
class TestElements:
    @allure.feature('Test TextBox')
    class TestTextBox:
        @allure.story('Test Text Box Form Submission')
        @allure.severity(allure.severity_level.NORMAL)
        def test_text_box(self, driver):
            page = TextBoxPage(driver, TEXT_BOX_URL)
            page.open()
            created_form = page.fill_all_fields()
            assert created_form, "The form was not created"