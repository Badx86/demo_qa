import allure
from data.elements import expected_elements
from data.urls import TEXT_BOX_URL, CHECK_BOX_URL
from pages.elements_page import TextBoxPage, CheckBoxPage


@allure.epic("Test Elements")
class TestElements:
    @allure.feature("Test Text Box")
    class TestTextBox:
        @allure.story("")
        @allure.severity(allure.severity_level.NORMAL)
        def test_text_box(self, driver):
            page = TextBoxPage(driver, TEXT_BOX_URL)
            page.open()
            person_info = page.fill_all_fields()
            output_info = page.check_fill_form()
            assert (person_info == output_info), f"Expected info {person_info}, but got {output_info}"

    @allure.feature("Test Check Box")
    class TestCheckBox:
        @allure.story("Test expanding all elements and check their presence")
        @allure.severity(allure.severity_level.NORMAL)
        def test_check_elements(self, driver):
            page = CheckBoxPage(driver, CHECK_BOX_URL)
            page.open()
            page.expand_all()
            for element_name in expected_elements:
                assert page.element_with_text_is_present(element_name), \
                    f"Element {element_name} is not present on the page"

