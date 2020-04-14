from selenium.webdriver.common.by import By

from pages.maintenance.purge_candidate_records_page import PurgeCandidateRecordsMPage
from pages.maintenance.purge_employee_records_page import PurgeEmployeeRecordsPage
from pages.menu.base_menu import BaseMenu, MenuItem


class PurgeRecordsMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_maintenance_PurgeRecords+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Employee Records', (By.ID, 'menu_maintenance_purgeEmployee'), None, PurgeEmployeeRecordsPage),
        MenuItem('Candidate Records', (By.ID, 'menu_maintenance_purgeCandidateData'), None, PurgeCandidateRecordsMPage)
    }
