from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://127.0.0.1:5000")
        self.wait_until_loaded()

    def wait_until_loaded(self):
        WebDriverWait(self.driver, timeout=10).until(
            expected_conditions.visibility_of_element_located(self.get_input_username()))

    def get_input_username(self):
        return By.ID, "username"

    def get_input_password(self):
        return By.ID, "password"

    def get_submit_button(self):
        return By.ID, "submit"

    def write_username(self, value):
        input_username_element = self.driver.find_element(*self.get_input_username())
        input_username_element.send_keys(value)

    def write_password(self, value):
        input_password_element = self.driver.find_element(*self.get_input_password())
        input_password_element.send_keys(value)

    def click_submit(self):
        submit_button = self.driver.find_element(*self.get_submit_button())
        submit_button.click()
