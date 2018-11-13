import pytest
from base.WebDriverFactory import WebDriverFactory
from pages.home.login import LoginPage



@pytest.yield_fixture(scope="class")
def one_time_setup(browser, request):
    """
    Here we get the webdriver instance from
    Webdriver factory class and returns the
    Webdriver
    """
    print('Running one_time_setup')
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()
    lp = LoginPage(driver)
    lp.click_on_login_link()
    lp.login("ashu271989@gmail.com", "test@123")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()


# Used to add browser as a command line argument
def pytest_addoption(parser):
    parser.addoption("--browser")


# Return the browser taken from command line
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
