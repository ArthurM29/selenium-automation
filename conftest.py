import pytest
from selenium import webdriver

from pages.login_page import LoginPage

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