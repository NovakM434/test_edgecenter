import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver

from page.registrations_page import RegistationPage


class TestRegistrationsField:
    @allure.title("Проверка поля email")
    @allure.description("Вводим не валидные данные и проверяем, что они не пройдут")
    @pytest.mark.email
    @pytest.mark.parametrize("email,expected_error", [
        ("фывфыв", "Введите правильный email."),
        ("email@", "Введите правильный email."),
        ("email@domain", "Введите правильный email."),
        ("email@.com", "Введите правильный email."),
    ])
    def test_not_valid_email_field(self, browser: WebDriver, email: str, expected_error: str):
        registration_page = RegistationPage(browser)
        registration_page.go_to_registration_page()
        response = registration_page.email_field(email)
        assert response == expected_error

    @allure.title("Проверка поля email")
    @allure.description("Проверяем, что пустое поле вызовет ошибку.")
    @pytest.mark.email
    def test_null_email_field(self, browser: WebDriver):
        registration_page = RegistationPage(browser)
        registration_page.go_to_registration_page()
        response = registration_page.email_field("")
        assert response == "Заполните это поле."

    @allure.title("Проверка поля password")
    @allure.description("Вводим не валидные данные, и ловим ошибку.")
    @pytest.mark.password
    @pytest.mark.parametrize("password,warning", [
        ("P", "Хотя бы одна буква должна быть строчной."),
        ("Pa", "Пароль должен содержать цифру."),
        ("1Pa", "Нужен минимум 1 специальный символ."),
        ("!1Pa", "Используйте хотя бы 8 символов."),
    ])
    def test_password(self, browser: WebDriver, password: str, warning: str):
        registration_page = RegistationPage(browser)
        registration_page.go_to_registration_page()
        response = registration_page.password_field(password)
        assert response == warning

    @allure.title("Проверка поле моб.номера")
    @allure.description("Проверяем, что пустое поле вызовет ошибку.")
    @pytest.mark.phonenumber
    def test_phone_field(self, browser: WebDriver):
        registration_page = RegistationPage(browser)
        registration_page.go_to_registration_page()
        response = registration_page.phone_field()
        assert response == "Заполните это поле"
