import logging

import pytest
import datetime
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from common.data.credentials import get_credentials
from common.config.config import Config
# from pages.admin.user_management_page import UserManagementPage
# from pages.menu.firstlevelmenu import FirstLevelMenu

from pages.login_page import LoginPage
from pages.header_page import Header
from datetime import datetime
from py.xml import html

# TODO find a better way to store results/screenshots/logs directories, consider also getting them from cmd
RESULTS_DIR = 'results'
SCREENSHOTS_DIR = 'screenshots'

# TODO remove duplicated code for logging
timestamp = datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
filename = os.path.join(Config().get('results_dir'), f"{timestamp}.log")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename, mode='a')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@pytest.fixture(scope="session")
def config():
    return Config()


@pytest.fixture(autouse=True)
def log_test_case(request):
    logger.info(f"---  {request.node.cls.__name__}:   {request.node.own_markers[0].args[0]}  ---")
    yield
    logger.info('')


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
def driver(browser, url, headless, config):
    global driver_  # declare global to access from _capture_screenshot() function, no better way to pass driver to pytest_runtest_makereport()
    if browser == 'chrome':
        options = ChromeOptions()
        options.headless = True if headless else False
        driver_ = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.headless = True if headless else False
        driver_ = webdriver.Firefox(options=options)
    elif browser == 'safari':
        driver_ = webdriver.Safari()
    driver_.get(url)
    driver_.set_window_size(*config.get('screen_size'))
    logger.info("Driver created")

    yield driver_

    driver_.close()
    logger.info("Driver closed")


# region html report
# source: http://www.automationtesting.co.in/2017/02/pytest-with-selenium-html-report-with.html
def _create_results_dir():
    Path(os.path.join(RESULTS_DIR, SCREENSHOTS_DIR)).mkdir(parents=True, exist_ok=True)


def _reorder_columns(cells):
    new_order = {2: 'Test', 3: 'Description', 0: 'Result', 4: 'Duration', 1: 'Time'}
    cells[:] = [cells[i] for i in list(new_order.keys())]


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description', class_='sortable time'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()  # remove links column
    _reorder_columns(cells)


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()
    _reorder_columns(cells)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    _create_results_dir()
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    test_description, = item.own_markers[0].args
    report.description = test_description

    if report.when == 'call' or report.when == "setup":

        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_path_in_report = os.path.join(SCREENSHOTS_DIR, f"{report.head_line.replace('.', '-')}.png")
            file_path = os.path.join(RESULTS_DIR, file_path_in_report)
            _capture_screenshot(file_path)
            if file_path_in_report:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_path_in_report
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver_.get_screenshot_as_file(name)


# endregion

# region page fixtures
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

# @pytest.fixture()
# def user_management(driver, header_page):
#     # TODO replace with proper page objects for menu navigation
#     menu = FirstLevelMenu(header_page.driver)
#     menu.select_menu_item('Admin')
#     menu.click_element((By.ID, 'menu_admin_UserManagement'))
#
#     user_management_page = UserManagementPage(menu.driver)
#
#     return user_management_page

# endregion
