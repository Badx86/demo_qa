import allure
from data.urls import TEXT_BOX_URL
from pages.elements_page import TextBoxPage


@allure.epic("Test Elements")
class TestElements:
    @allure.feature("Test Text Box")
    class TestTextBox:
        @allure.story("Test Text Box Form Submission")
        @allure.severity(allure.severity_level.NORMAL)
        def test_text_box(self, driver):
            page = TextBoxPage(driver, TEXT_BOX_URL)
            page.open()
            person_info = page.fill_all_fields()
            output_info = page.check_fill_form()
            assert (
                person_info == output_info
            ), f"Expected info {person_info}, but got {output_info}"
