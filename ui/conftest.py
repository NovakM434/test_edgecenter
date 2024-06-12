import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="local",
                     help="browser option: local or remote")


@pytest.fixture(scope="function")
def browser(request):
    browser_option = request.config.getoption("--browser")

    if browser_option == "remote":
        chrome_options = Options()
        driver = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            options=chrome_options
        )
    else:
        driver = webdriver.Chrome()

    yield driver
    driver.quit()
