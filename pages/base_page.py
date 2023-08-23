import allure
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step("Open a browser")
    def open(self):
        """This method opens a browser by the provided link"""
        self.driver.get(self.url)

    @allure.step("Find a visible element")
    def element_is_visible(self, locator, timeout=5):
        """
        This method expects to verify that the element is present in the DOM tree, visible, and displayed on the page.
        Visibility means that the element is not only displayed but also has a height and width greater than 0.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Find visible elements")
    def elements_are_visible(self, locator, timeout=5):
        """
        This method expects to verify that the elements are present in the DOM tree, visible and displayed on the page.
        Visibility means that the elements are not only displayed but also have a height and width greater than 0.
        Locator - is used to find the elements.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    @allure.step("Find a present element")
    def element_is_present(self, locator, timeout=5):
        """
        This method expects to verify that the element is present in the DOM tree,
        but not necessarily visible and displayed on the page.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Find present elements")
    def elements_are_present(self, locator, timeout=5):
        """
        This method expects to verify that the elements are present in the DOM tree,
        but not necessarily visible and displayed on the page.
        Locator - is used to find the elements.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step("Find a not visible element")
    def element_is_not_visible(self, locator, timeout=5):
        """
        This method expects to verify whether the element is invisible or not.
        The element is present in the DOM tree.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Find clickable elements")
    def element_is_clickable(self, locator, timeout=5):
        """
        This method expects to verify that the element is visible, displayed on the page, and enabled.
        The element is present in the DOM tree.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Go to specified element")
    def go_to_element(self, element):
        """
        This method scrolls the page to the selected element, making it visible to the user.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Move cursor to element")
    def action_move_to_element(self, element):
        """
        This method moves the mouse cursor to the center of the selected element, simulating a hover action.
        It can be used to test the interactivity of an element when the mouse cursor is hovering over it.
        """
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @allure.step('Double click on the element')
    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    @allure.step('Right click on the element')
    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    @allure.step("Find element by text")
    def find_element_by_text(self, locator, text, timeout=5):
        """
        This method attempts to find an element by its displayed text.
        It will wait until the element with the specified text is present or until the timeout expires.
        Locator - is used to find the elements.
        Text - the visible text of the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        elements = self.elements_are_present(locator, timeout)
        for element in elements:
            if element.text == text:
                return element
        raise NoSuchElementException(f"No element with text '{text}' found.")

    @allure.step("Check if element is present on the page")
    def element_with_text_is_present(self, element_name):
        try:
            self.driver.find_element(By.XPATH, f"//*[text()='{element_name}']")
            return True
        except NoSuchElementException:
            return False

    @allure.step('Check element hover style')
    def check_element_hover_style(self, locator, css_property, seconds=10):
        """
        This method finds a visible element using the provided locator,
        simulates a hover action by moving the cursor to it,
        and then returns the value of the specified CSS property of the element.
        Locator - is used to find the element.
        Css_property - the name of the CSS property whose value is to be returned.
        """
        element = self.element_is_visible(locator)  # Get the WebElement using locator
        wait(self.driver, seconds)
        self.action_move_to_element(element)  # Move to the element
        return element.value_of_css_property(css_property)

    @allure.step('Activate field and check its style')
    def activate_and_check_field_style(self, locator, css_property):
        initial_style = self.check_element_hover_style(locator, css_property)  # Get the initial style
        self.click_and_return_element(locator)  # Activate the field
        active_style = self.check_element_hover_style(locator, css_property)  # Check the active style
        return initial_style, active_style

    @allure.step('Click on element and return it')
    def click_and_return_element(self, locator, seconds=15):
        """
        This method finds a visible element using the provided locator,
        performs a click action on it, and then returns the element.
        Locator - is used to find the element.
        """
        element = self.element_is_visible(locator)
        wait(self.driver, seconds)
        element.click()
        return element

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
