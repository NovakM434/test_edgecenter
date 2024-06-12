from selenium.webdriver.chrome.webdriver import ChromiumDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver) -> None:
        self.driver: ChromiumDriver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "https://auth.edgecenter.ru"

    def _find_element(self, by, locator):
        self.wait.until(EC.visibility_of_element_located((by, locator)))
        with allure.step(f"Поиск элемента по {by} {locator}"):
            return self.driver.find_element(by, locator)

    def _find_elements(self, by, locator):
        self.wait.until(EC.visibility_of_element_located((by, locator)))
        with allure.step(f"Поиск элементов по {by} {locator}"):
            return self.driver.find_elements(by, locator)

    def _click(self, by, locator, timeout=10):
        self.wait.until(EC.visibility_of_element_located((by, locator)))
        with allure.step(f"Клик по элементу {by} {locator}"):
            self._find_element(by, locator).click()

    def _send_keys(self, field, value):
        self._find_element(*field).send_keys(value)
