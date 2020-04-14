from selenium.webdriver.common.by import By

from pages.leave.leave_entitlements_page import LeaveEntitlementsMPage
from pages.leave.timesheets_page import TimesheetsPage
from pages.menu.base_menu import BaseMenu, MenuItem
from pages.time.attendance_configuraton_page import AttendanceConfigurationPage
from pages.time.attendance_summary_page import AttendanceSummaryPage
from pages.time.customers_page import CustomersPage
from pages.time.project_reports_page import ProjectReportsPage
from pages.time.projects_page import ProjectsPage
from pages.time.view_attendance_record_page import ViewAttendanceRecordPage
from pages.time.employee_reports_page import EmployeeReportsPage


class TimesheetsMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_time_Timesheets+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Employee Timesheets', (By.ID, 'menu_time_viewEmployeeTimesheet'), None, TimesheetsPage)
    }


class AttendanceMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_attendance_Attendance+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Employee Records', (By.ID, 'menu_attendance_viewAttendanceRecord'), None, ViewAttendanceRecordPage),
        MenuItem('Configuration', (By.ID, 'menu_attendance_configure'), None, AttendanceConfigurationPage)
    }


class TimeReportsMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_time_Reports+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Project Reports', (By.ID, 'menu_time_displayProjectReportCriteria'), None, ProjectReportsPage),
        MenuItem('Employee Reports', (By.ID, 'menu_time_displayEmployeeReportCriteria'), None, EmployeeReportsPage),
        MenuItem('Attendance Summary', (By.ID, 'menu_time_displayAttendanceSummaryReportCriteria'), None,
                 AttendanceSummaryPage)
    }


class ProjectInfoMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_admin_ProjectInfo+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Customers', (By.ID, 'menu_admin_viewCustomers'), None, CustomersPage),
        MenuItem('Projects', (By.ID, 'menu_admin_viewProjects'), None, ProjectsPage)
    }
