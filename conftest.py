import pytest
from selenium import webdriver
from common.data.credentials import get_credentials

from pages.login_page import LoginPage
from pages.header_page import Header

url = 'https://opensource-demo.orangehrmlive.com/'


def create_driver():
    print("Driver created")
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def close_driver(driver):
    print("Driver closed")
    driver.close()


@pytest.fixture()
def login_page():
    driver = create_driver()
    yield LoginPage(driver)
    close_driver(driver)


@pytest.fixture()
def header_page():
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.login(*get_credentials('valid_credentials'))
    header_page = Header(driver)
    yield header_page
    close_driver(driver)


@pytest.fixture()
def about_modal():
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.login(*get_credentials('valid_credentials'))
    header_page = Header(driver)
    about_modal = header_page.open_about_modal()
    yield about_modal
    close_driver(driver)
