from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import ChromiumDriver
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver) -> None:
        self.driver: ChromiumDriver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "https://auth.edgecenter.ru/login/signup?lang=ru"

    def _find_element(self, by, locator):
        self.wait.until(EC.visibility_of_element_located((by, locator)))
        return self.driver.find_element(by, locator)

    def _find_elements(self, by, locator):
        self.wait.until(EC.visibility_of_element_located((by, locator)))
        return self.driver.find_elements(by, locator)

    def _click(self, by, locator, timeout=10):
        self.wait.until(EC.visibility_of_element_located((by, locator)))
        self._find_element(by, locator).click()

    def go_to_registration_page(self):
        self.driver.get(self.base_url)
