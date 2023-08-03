import random
import allure
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxLocators, CheckBoxLocators, RadioButtonLocators, WebTableLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    @allure.step("Fill all fields and submit form")
    def fill_all_fields(self):
        info = next(generated_person())
        full_name = info.full_name
        email = info.email
        current_address = info.current_address
        permanent_address = info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return full_name, email, current_address, permanent_address

    @allure.step("Compare received data with expected data")
    def check_fill_form(self):
        full_name = self.element_is_visible(self.locators.CREATED_NAME).text.split(":")[1]
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address

    @allure.step('Check all fields activation style changes after clicking/tab on them')
    def activate_all_fields_and_check_style(self):
        css_property = 'box-shadow'
        locators = [
            self.locators.FULL_NAME,
            self.locators.EMAIL,
            self.locators.CURRENT_ADDRESS,
            self.locators.PERMANENT_ADDRESS
        ]
        styles = []
        for i in locators:
            initial_style, active_style = self.activate_and_check_field_style(i, css_property)
            styles.append((initial_style, active_style))
        return styles


class CheckBoxPage(BasePage):
    locators = CheckBoxLocators()

    @allure.step("Expand all elements")
    def expand_all(self):
        self.element_is_visible(self.locators.EXPAND_BUTTON).click()

    @allure.step("Click random element")
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = random.choice(item_list)
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step("Get checked box")
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        lst = []
        for i in checked_list:
            title_item = i.find_element("xpath", self.locators.TITLE_ITEM)
            lst.append(title_item.text)
        return str(lst).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.step("Get output result")
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT)
        lst = []
        for i in result_list:
            lst.append(i.text)
        return str(lst).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    @allure.step("Click on the radio buttons")
    def click_on_the_radio_button(self, item):
        choice = {
            'yes': self.locators.YES_BUTTON,
            'impressive': self.locators.IMPRESSIVE_BUTTON,
            'no': self.locators.NO_BUTTON
        }
        element = self.element_is_visible(choice[item])
        if not element.is_enabled():
            return 'disabled'
        element.click()

    @allure.step("Check get output result")
    def get_output_result(self):
        return self.element_is_present(self.locators.TEXT_OUTPUT).text


class WebTablePage(BasePage):
    locators = WebTableLocators()

    @allure.step("Create new person")
    def add_new_person(self, count=1):
        while count != 0:
            info = next(generated_person())
            first_name = info.firstname
            last_name = info.lastname
            email = info.email
            age = info.age
            salary = info.salary
            department = info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.AGE).send_keys(age)
            self.element_is_visible(self.locators.SALARY).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step("Check that added person added to the table")
    def check_added_person(self):
        peoples = self.elements_are_present(self.locators.FULL_TABLE_LIST)
        data = []
        for i in peoples:
            data.append(i.text.splitlines())
        return data

    @allure.step("Check created person search")
    def check_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return row.text.splitlines()
