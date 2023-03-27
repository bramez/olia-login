from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_until_loaded()

    def wait_until_loaded(self):
        WebDriverWait(self.driver, timeout=10).until(
            expected_conditions.visibility_of_element_located(self.get_user_profile_name()))

    def get_user_profile_name(self):
        return By.ID, "userprofile_name"

    def is_user_profile_name_displayed(self):
        element = self.driver.find_element(*self.get_user_profile_name())
        return element.is_displayed()
