import random
import allure
import pytest
from data.elements import expected_elements
from data.urls import TEXT_BOX_URL, CHECK_BOX_URL, RADIO_BUTTON_URL, WEB_TABLES_URL, BUTTONS_URL, LINKS_URL, \
    BROKEN_LINKS_URL
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    BrokenLinksImagesPage


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

    @allure.feature("Test Web Table")
    class TestWebTable:
        @allure.title("Create new person")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_web_table_add_person(self, driver):
            page = WebTablePage(driver, WEB_TABLES_URL)
            page.open()
            for i in range(random.randint(1, 7)):
                new_person = page.add_new_person()
                result = page.check_new_added_person()
                assert new_person in result, "Where is a f*cking person?"

        @allure.title("Search person")
        @allure.severity(allure.severity_level.NORMAL)
        def test_web_table_search_person(self, driver):
            page = WebTablePage(driver, WEB_TABLES_URL)
            page.open()
            key_word = page.add_new_person()[random.randint(0, 5)]
            page.check_some_person(key_word)
            table_result = page.check_search_person()
            assert key_word in table_result, "The person was not found in the table"

        @allure.title("Edit person")
        @allure.severity(allure.severity_level.NORMAL)
        def test_web_table_update_person(self, driver):
            page = WebTablePage(driver, WEB_TABLES_URL)
            page.open()
            last_name = page.add_new_person()[1]
            page.check_some_person(last_name)
            age = page.update_person_info()
            row = page.check_search_person()
            assert age in row, "The person`s age has not been changed"

        @allure.title("Delete person")
        @allure.severity(allure.severity_level.NORMAL)
        def test_web_table_delete_person(self, driver):
            page = WebTablePage(driver, WEB_TABLES_URL)
            page.open()
            email = page.add_new_person()[3]
            page.check_some_person(email)
            page.delete_person()
            text = page.check_deleted_person()
            assert text == "No rows found", "The person card hasn`t been deleted"

        @pytest.mark.xfail
        @allure.title("Check count of rows")
        @allure.severity(allure.severity_level.NORMAL)
        def test_web_table_change_rows(self, driver):
            page = WebTablePage(driver, WEB_TABLES_URL)
            page.open()
            count = page.select_up_to_rows()
            assert count == [5, 10, 20, 25, 50,
                            100], 'The number of rows in the table has not been changed or has changed incorrectly'

    @allure.feature("Test click buttons")
    class TestButtons:
        @allure.title("Different clicks on buttons")
        @allure.severity(allure.severity_level.NORMAL)
        def test_different_clicks_on_buttons(self, driver):
            page = ButtonsPage(driver, BUTTONS_URL)
            page.open()
            double = page.double_click()
            right = page.right_click()
            standard = page.standard_click()
            assert double == 'You have done a double click'
            assert right == 'You have done a right click'
            assert standard == 'You have done a dynamic click'

    @allure.feature("Test link clicks")
    class TestLinks:
        @allure.title("Check links")
        @allure.severity(allure.severity_level.NORMAL)
        def test_check_link(self, driver):
            page = LinksPage(driver, LINKS_URL)
            page.open()
            href_link, current_url = page.check_new_tab_simple_link()
            assert href_link == current_url

        @pytest.mark.parametrize("link_locator, expected_response", LinksPage.LINKS_RESPONSES.items())
        @allure.title("Check link responses")
        @allure.severity(allure.severity_level.NORMAL)
        def test_check_link_responses(self, driver, link_locator, expected_response):
            page = LinksPage(driver, LINKS_URL)
            page.open()
            actual_response = page.check_link_response(link_locator)
            assert expected_response in actual_response, f"Expected '{expected_response}', Actual '{actual_response}'"

    @allure.feature("Test Broken Links-Images")
    class TestBrokenLinksImages:
        @allure.title("Check Images Size")
        @allure.severity(allure.severity_level.NORMAL)
        def test_images(self, driver):
            page = BrokenLinksImagesPage(driver, BROKEN_LINKS_URL)
            page.open()
            valid_image_size, broken_image_size = page.check_images()
            assert valid_image_size == (347, 100), f"Valid image size is not as expected: {valid_image_size}"
            assert broken_image_size == (16, 16), f"Broken image size is not as expected: {broken_image_size}"

        @allure.title("Check Links")
        @allure.severity(allure.severity_level.NORMAL)
        def test_links(self, driver):
            page = BrokenLinksImagesPage(driver, BROKEN_LINKS_URL)
            page.open()
            invalid_link_page_text = page.check_links()
            assert "This page returned a 500 status code" in invalid_link_page_text,\
                "Invalid link page text is not as expected"
