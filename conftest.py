import pytest
from selenium import webdriver
from common.data.credentials import get_credentials

from pages.login_page import LoginPage
from pages.header_page import Header

url = 'https://opensource-demo.orangehrmlive.com/'


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")
    parser.addoption("--headless")
    parser.addoption("--env")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


# @pytest.fixture(scope="session")
# def headless(request):
#     return request.config.getoption("--headless")
#
#
# @pytest.fixture(scope="session")
# def url(request):
#     return request.config.getoption("--url")
#
# @pytest.fixture(scope="session")
# def env(request):
#     return request.config.getoption("--env")


def create_driver(browser):
    print("Driver created")
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    driver.get(url)
    return driver


def close_driver(driver):
    print("Driver closed")
    driver.close()


@pytest.fixture()
def login_page(browser):
    driver = create_driver(browser)
    yield LoginPage(driver)
    close_driver(driver)


@pytest.fixture()
def header_page():
    driver = create_driver(browser)
    login_page = LoginPage(driver)
    login_page.login(*get_credentials('valid_credentials'))
    header_page = Header(driver)
    yield header_page
    close_driver(driver)


@pytest.fixture()
def about_modal():
    driver = create_driver(browser)
    login_page = LoginPage(driver)
    login_page.login(*get_credentials('valid_credentials'))
    header_page = Header(driver)
    about_modal = header_page.open_about_modal()
    yield about_modal
    close_driver(driver)
