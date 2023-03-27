from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ErrorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_until_loaded()

    def wait_until_loaded(self):
        WebDriverWait(self.driver, timeout=10).until(
            expected_conditions.visibility_of_element_located(self.get_error_title()))

    def get_error_title(self):
        return By.ID, "error-title"

    def is_error_title_displayed(self):
        element = self.driver.find_element(*self.get_error_title())
        return element.is_displayed()

    def get_link_go_back(self):
        return By.ID, "link-go-back"

    def is_link_go_back_displayed(self):
        element = self.driver.find_element(*self.get_link_go_back())
        return element.is_displayed()