import pytest
from selenium import webdriver
from common.data.credentials import get_credentials
from common.config.config import Config

from pages.login_page import LoginPage
from pages.header_page import Header

CONFIG_PATH = 'common/config/config.yaml'


@pytest.fixture(scope="session")
def config():
    return Config(CONFIG_PATH)


# region command line arguments
def pytest_addoption(parser):
    parser.addoption("--browser", type=str.lower,
                     help="one of the supported browsers")
    parser.addoption("--url", type=str.lower, help="website url")
    parser.addoption("--headless", action='store_true',
                     help="browser execution mode - return True if passed and False if not")
    parser.addoption("--env", type=str.lower, help="environment to run the tests against")


@pytest.fixture(scope="session")
def browser(request, config):
    cmd_browser = request.config.getoption("--browser")
    browser_ = cmd_browser if cmd_browser else config.get('browser').lower()
    if browser_ in config.get('supported_browsers'):
        return browser_
    else:
        raise Exception(f"'{browser_}' is not a supported browser.")


@pytest.fixture(scope="session")
def headless(request, config):
    cmd_headless = request.config.getoption("--headless")
    return cmd_headless if cmd_headless else config.get('headless')


@pytest.fixture(scope="session")
def url(request, config):
    cmd_url = request.config.getoption("--url")
    return cmd_url if cmd_url else config.get('url')


@pytest.fixture(scope="session")
def env(request, config):
    cmd_env = request.config.getoption("--env")
    return cmd_env if cmd_env else config.get('env')


# endregion

@pytest.fixture()
def driver(browser, url):
    print("Driver created")
    if browser == 'chrome':
        driver_ = webdriver.Chrome()
    elif browser == 'firefox':
        driver_ = webdriver.Firefox()
    driver_.get(url)
    yield driver_
    print("Driver closed")
    driver_.close()


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def header_page(driver):
    login_page = LoginPage(driver)
    login_page.login(*get_credentials('valid_credentials'))
    header_page = Header(driver)
    return header_page


@pytest.fixture()
def about_modal(driver):
    login_page = LoginPage(driver)
    login_page.login(*get_credentials('valid_credentials'))
    header_page = Header(driver)
    about_modal = header_page.open_about_modal()
    return about_modal
