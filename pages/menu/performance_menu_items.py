from selenium.webdriver.common.by import By

from pages.menu.base_menu import BaseMenu, MenuItem
from pages.performance.kpis_page import KPIsPage
from pages.performance.performance_trackers_page import PerformanceTrackersPage
from pages.performance.search_performance_reviews_page import SearchPerformanceReviewsPage


class PerformanceConfigureMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_performance_Configure+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('KPIs', (By.ID, 'menu_time_viewEmployeeTimesheet'), None, KPIsPage),
        MenuItem('Trackers', (By.ID, 'menu_performance_addPerformanceTracker'), None, PerformanceTrackersPage)
    }


class ManageReviewsMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_performance_ManageReviews+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Manage Reviews', (By.ID, 'menu_performance_searchPerformancReview'), None,
                 SearchPerformanceReviewsPage)
    }
