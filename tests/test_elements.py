import allure
import pytest

from data.elements import expected_elements
from data.urls import TEXT_BOX_URL, CHECK_BOX_URL, RADIO_BUTTON_URL
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


@allure.epic("Test Elements")
class TestElements:
    @allure.feature("Test Text Box")
    class TestTextBox:
        @allure.title("Check input == output")
        @allure.severity(allure.severity_level.NORMAL)
        def test_text_box_output(self, driver):
            page = TextBoxPage(driver, TEXT_BOX_URL)
            page.open()
            person_info = page.fill_all_fields()
            output_info = page.check_fill_form()
            assert (person_info == output_info), f"Expected info {person_info}, but got {output_info}"

        @allure.title('Interactivity of the fields')
        @allure.severity(allure.severity_level.NORMAL)
        def test_interactivity_of_the_fields(self, driver):
            page = TextBoxPage(driver, TEXT_BOX_URL)
            page.open()
            styles = page.activate_all_fields_and_check_style()
            for i, style in enumerate(styles):
                initial_style, active_style = style
                assert initial_style != active_style, f"Error: Field style at index {i} doesn't change on activation"

    @allure.feature("Test Check Box")
    class TestCheckBox:
        @allure.title("Test expanding all elements and check their presence")
        @allure.severity(allure.severity_level.NORMAL)
        def test_check_elements(self, driver):
            page = CheckBoxPage(driver, CHECK_BOX_URL)
            page.open()
            page.expand_all()
            for element_name in expected_elements:
                assert page.element_with_text_is_present(element_name), \
                    f"Element {element_name} is not present on the page"

        @allure.title("Test checkboxes: random click and output")
        @allure.severity(allure.severity_level.NORMAL)
        def test_check_box_random(self, driver):
            page = CheckBoxPage(driver, CHECK_BOX_URL)
            page.open()
            page.expand_all()
            page.click_random_checkbox()
            input_checkbox = page.get_checked_checkboxes()
            output_result = page.get_output_result()
            assert input_checkbox == output_result, "Input text and output checkbox is not equal"

    @allure.feature("Test Radio Button")
    class TestRadioButton:
        @allure.title("Test radio buttons")
        @allure.severity(allure.severity_level.NORMAL)
        @pytest.mark.parametrize("button,expected", [
            ("yes", "You have selected Yes"),
            ("impressive", "You have selected Impressive"),
            ("no", "disabled")])
        def test_radio_buttons(self, driver, button, expected):
            page = RadioButtonPage(driver, RADIO_BUTTON_URL)
            page.open()
            button_result = page.click_on_the_radio_button(button)
            if button_result == "disabled":
                assert expected == "disabled", "Button should be disabled but it's not"
            elif button_result == "enabled":
                output_text = page.get_output_result()
                assert output_text == expected, f"Expected {expected}, but got {output_text}"



