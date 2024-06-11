from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Optional

from .base_page import BasePage


class RegistationPage(BasePage):
    path = "/"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def email_field(self, email: str) -> Optional[str]:
        email_field = self._find_element(By.ID, "gc-input-0")
        email_field.send_keys(email)
        email_field.send_keys(Keys.TAB)
        error_email = self._find_element(By.CSS_SELECTOR,
                                         "gc-errors-outlet > gc-error")
        return error_email.text

    def password_field(self, password: str) -> Optional[str]:
        password_field = self._find_element(By.ID, "gc-input-1")
        password_field.send_keys(password)
        password_field.send_keys(Keys.TAB)
        warning_password = self._find_element(By.CSS_SELECTOR,
                                              "password-warnings div.mt-1")
        return warning_password.text

    def phone_field(self) -> Optional[str]:
        phone_field = self._find_element(By.CSS_SELECTOR,
                                         'input[formcontrolname="phone"]')
        phone_field.clear()
        error_phone = self._find_element(By.CSS_SELECTOR,
                                         "gc-errors-outlet > gc-error")
        return error_phone.text
