import pytest
from base.WebDriverFactory import WebDriverFactory


@pytest.yield_fixture(scope="class")
def one_time_setup(browser, request):

    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
