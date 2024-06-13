import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from page.registrations_page import RegistationPage


class TestRegistrationsField:
    @allure.title("Проверка поля email")
    @allure.description("Вводим не валидные данные и проверяем, что они не пройдут")
    @pytest.mark.email
    @pytest.mark.parametrize(
        "email,expected_error",
        [
            ("фывфыв", "Введите правильный email."),
            ("email@", "Введите правильный email."),
            ("email@domain", "Введите правильный email."),
            ("email@.com", "Введите правильный email."),
            ("", "Заполните это поле.")
        ],
    )
    def test_not_valid_email_field(
        self, browser: WebDriver, email: str, expected_error: str
    ) -> None:
        registration_page = RegistationPage(browser)
        registration_page.go_to_registration_page()
        registration_page.fill_email_field(email)
        email_error_response = registration_page.get_email_validation_error()
        with allure.step("Проверка, что не валидные данные в email дадут ошибку"):
            assert email_error_response == expected_error

    @allure.title("Проверка поля password")
    @allure.description("Вводим не валидные данные, и ловим ошибку.")
    @pytest.mark.password
    @pytest.mark.parametrize(
        "password,warning",
        [
            ("P", "Хотя бы одна буква должна быть строчной."),
            ('a', "Хотя бы одна буква должна быть ПРОПИСНОЙ."),
            ("Pa", "Пароль должен содержать цифру."),
            ("1Pa", "Нужен минимум 1 специальный символ."),
            ("!1Pa", "Используйте хотя бы 8 символов."),
        ],
    )
    def test_password(self, browser: WebDriver, password: str, warning: str) -> None:
        registration_page = RegistationPage(browser)
        registration_page.go_to_registration_page()
        registration_page.fill_password_field(password)
        password_error_response = registration_page.get_password_validation_error()
        with allure.step("Проверка, что не валидные данные в пароле дадут ошибку ошибку"):
            assert password_error_response == warning

    @allure.title("Проверка пустого поля пароля")
    @allure.description("Проверяем, что пустое поле так же вызовет ошибку")
    @pytest.mark.password2
    def test_null_password(self, browser: WebDriver) -> None:
        registration_page = RegistationPage(browser)
        registration_page.go_to_registration_page()
        registration_page.fill_password_field("1")
        registration_page.clear_password()
        password_error_response = registration_page.get_null_password_validation_error()
        print(password_error_response)
        with allure.step("Проверка, что не валидные данные в пароле дадут ошибку ошибку"):
            assert password_error_response == "Заполните это поле."

    @allure.title("Проверка поле моб.номера")
    @allure.description("Проверяем, заполняя все поля и указав короткий номер.")
    @pytest.mark.shortphonenumber
    def test_phone_short_field(self, browser: WebDriver) -> None:
        registration_page = RegistationPage(browser)
        registration_page.go_to_registration_page()
        registration_page.fill_email_field("1@mail.ru")
        registration_page.fill_password_field("Password@1")
        registration_page.fill_phone_field("902458965")
        registration_page.fill_checkbox()
        check_button_response = registration_page.check_button_status()
        with allure.step("Проверка статуса кнопки"):
            assert check_button_response

    @allure.title("Проверка поле моб.номера")
    @allure.description("Проверяем, что пустое поле вызовет ошибку.")
    @pytest.mark.nullphonenumber
    def test_phone_null_field(self, browser: WebDriver) -> None:
        registration_page = RegistationPage(browser)
        registration_page.go_to_registration_page()
        registration_page.fill_email_field('1@mail.ru')
        registration_page.fill_password_field('1')
        registration_page.clear_phone()
        get_phone_error_response = registration_page.get_phone_error()
        with allure.step("Проверяем что пустое поле даст ошибку"):
            assert get_phone_error_response == "Заполните это поле."
