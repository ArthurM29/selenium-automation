from selenium.webdriver.common.by import By

from pages.menu.base_menu import BaseMenu, MenuItem
from pages.pim.configuration.configure_pim_page import ConfigurePIMPage
from pages.pim.configuration.custom_fields_page import CustomFieldsPage
from pages.pim.configuration.data_import_page import DataImportPage
from pages.pim.configuration.reporting_methods_page import ReportingMethodsPage
from pages.pim.configuration.termination_reasons_page import TerminationReasonsPage


class PIMConfigurationMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_pim_viewPimModule+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Optional Fields', (By.ID, 'menu_pim_configurePim'), None, ConfigurePIMPage),
        MenuItem('Custom Fields', (By.ID, 'menu_pim_listCustomFields'), None, CustomFieldsPage),
        MenuItem('Data Import', (By.ID, 'menu_admin_pimCsvImport'), None, DataImportPage),
        MenuItem('Reporting Methods', (By.ID, 'menu_pim_viewReportingMethods'), None, ReportingMethodsPage),
        MenuItem('Termination Reasons', (By.ID, 'menu_pim_viewTerminationReasons'), None, TerminationReasonsPage),
    }