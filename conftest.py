import pytest
from selenium import webdriver

url = 'https://opensource-demo.orangehrmlive.com/'


@pytest.fixture
def create_driver():
    print("Driver created")
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


@pytest.fixture
def close_file(create_driver):
    print("Driver closed")
    create_driver.close()
