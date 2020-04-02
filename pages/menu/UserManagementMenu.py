from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from common.selenium_lib import element_attribute_contains_value

from pages.base_page import BasePage


class FirstLevelMenu(BasePage):
    # region locators
    _menu_container_div = (By.CSS_SELECTOR, '.menu')
    _menu_item_li = [By.XPATH, "//a[@id='{id}']/parent::li"]

    _page_identifier_element = _menu_container_div

    menu_item_locators = {'Admin': (By.ID, 'menu_admin_viewAdminModule'),
                          'PIM': (By.ID, 'menu_pim_viewPimModule'),
                          'Leave': (By.ID, 'menu_leave_viewLeaveModule'),
                          'Time': (By.ID, 'menu_time_viewTimeModule'),
                          'Recruitment': (By.ID, 'menu_recruitment_viewRecruitmentModule'),
                          'Performance': (By.ID, 'menu__Performance'),
                          'Dashboard': (By.ID, 'menu_dashboard_index'),
                          'Directory': (By.ID, 'menu_directory_viewDirectory'),
                          'Maintenance': (By.ID, 'menu_maintenance_purgeEmployee')
                          }

    # endregion

    # region private methods
    def _verify_menu_item_selected(self, name):
        by, id_ = self.menu_item_locators[name]
        self._menu_item_li[1] = self._menu_item_li[1].format(id=id_)
        self.wait_until(element_attribute_contains_value(self._menu_item_li, 'class', 'current'))

    # endregion

    # region public interface
    def select_menu_item(self, name):
        self.click_element_with_JS(self.menu_item_locators[name])
        self._verify_menu_item_selected(name)

    # endregion

# menu.select_menu_item('Admin').select_menu_item('User Management').select_menu_item('Users')
