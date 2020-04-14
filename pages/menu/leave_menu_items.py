from selenium.webdriver.common.by import By

from pages.leave.add_leave_entitlements_page import AddLeaveEntitlementMPage
from pages.leave.holidays_page import HolidaysPage
from pages.leave.leave_entitlements_and_usage_report_page import LeaveEntitlementsAndUsageReportPage
from pages.leave.leave_entitlements_page import LeaveEntitlementsMPage
from pages.leave.leave_period_page import LivePeriodPage
from pages.leave.leave_types_page import LiveTypesPage
from pages.leave.work_week_page import WorkWeekPage
from pages.menu.base_menu import MenuItem, BaseMenu


class EntitlementsMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_leave_Entitlements+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Add Entitlements', (By.ID, 'menu_leave_addLeaveEntitlement'), None, AddLeaveEntitlementMPage),
        MenuItem('Employee Entitlements', (By.ID, 'menu_leave_viewLeaveEntitlements'), None, LeaveEntitlementsMPage)
    }


class LeaveReportsMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_leave_Reports+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Leave Entitlements and Usage Report', (By.ID, 'menu_leave_viewLeaveBalanceReport'), None,
                 LeaveEntitlementsAndUsageReportPage)
    }


class LeaveConfigureMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_leave_Configure+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Leave Period', (By.ID, 'menu_leave_defineLeavePeriod'), None, LivePeriodPage),
        MenuItem('Leave Types', (By.ID, 'menu_leave_leaveTypeList'), None, LiveTypesPage),
        MenuItem('Work Week', (By.ID, 'menu_leave_defineWorkWeek'), None, WorkWeekPage),
        MenuItem('Holidays', (By.ID, 'menu_leave_viewHolidayList'), None, HolidaysPage),
    }
