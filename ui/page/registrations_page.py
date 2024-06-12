from typing import Optional

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from .base_page import BasePage


class RegistationPage(BasePage):
    path = "/login/signup?lang=ru"

    email_field = (By.ID, "gc-input-0")
    warning_email_field = (By.CSS_SELECTOR, "gc-errors-outlet > gc-error")
    password_field = (By.ID, "gc-input-1")
    warning_password_field = (By.CSS_SELECTOR, "password-warnings div.mt-1")
    null_password_field = (By.CSS_SELECTOR, "gc-errors-outlet > gc-error")
    phone_field = (By.CSS_SELECTOR, "input[formcontrolname='phone']")
    warning_phone_field = (By.CSS_SELECTOR, "gc-errors-outlet > gc-error")
    check_box = (By.CSS_SELECTOR, "input[name=terms_agree]")
    submit_button = (By.CSS_SELECTOR, "gc-button[type='submit']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Переходим на страницу регистрации')
    def go_to_registration_page(self):
        self.driver.get(f"{self.base_url}{self.path}")

    @allure.step("Заполняем поле email")
    def fill_email_field(self, email: str):
        self._send_keys(self.email_field, email)

    @allure.step("Заполняем поле password")
    def fill_password_field(self, password: str):
        self._send_keys(self.password_field, password)

    @allure.step("Заполняем поле phone")
    def fill_phone_field(self, phone: str):
        self._send_keys(self.phone_field, phone)

    @allure.step("Ставим галочку в чекбоксе")
    def fill_checkbox(self):
        self._find_element(*self.check_box).click()

    @allure.step("Получение ошибки валидации email")
    def get_email_validation_error(self) -> Optional[str]:
        self._find_element(*self.password_field).send_keys(Keys.TAB)
        return self._find_element(*self.warning_email_field).text

    @allure.step("Получение ошибки валидации пароля")
    def get_password_validation_error(self) -> Optional[str]:
        self._find_element(*self.password_field).send_keys(Keys.TAB)
        return self._find_element(*self.warning_password_field).text

    @allure.step("Получение ошибки пустого поля пароля")
    def get_null_password_validation_error(self) -> Optional[str]:
        return self._find_element(*self.null_password_field).text

    @allure.step("Проверяем активна ли кнопка")
    def check_button_status(self) -> bool:
        self._find_element(*self.check_box).click()
        button_attr = self._find_element(*self.submit_button).get_attribute('class')
        is_enabled = "ng-star-inserted disabled" in button_attr
        return is_enabled

    @allure.step("Проверяем валидацию поля phone")
    def get_phone_error(self) -> Optional[str]:
        return self._find_element(*self.warning_phone_field).text

    @allure.step("Очищаем поле phone")
    def clear_phone(self):
        self._find_element(*self.phone_field).send_keys(Keys.BACK_SPACE)

    @allure.step("Очищаем поле password")
    def clear_password(self):
        self._find_element(*self.password_field).send_keys(Keys.BACK_SPACE)
