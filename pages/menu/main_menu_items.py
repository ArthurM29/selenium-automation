from pages.admin.nationalities_page import NationalitiesPage
from pages.pim.employee_list_page import EmployeeListPage
from pages.leave.assign_leave_page import AssignLeavePage
from pages.leave.time_menu_items import TimesheetsMenu, AttendanceMenu, TimeReportsMenu, ProjectInfoMenu
from pages.leave.leave_list_page import LeaveListPage
from pages.maintenance.download_personal_data_page import DownloadPersonalDataPage
from pages.menu.admin_menu_items import *
from pages.menu.maintenance_menu_items import PurgeRecordsMenu
from pages.menu.performance_menu_items import PerformanceConfigureMenu, ManageReviewsMenu
from pages.menu.pim_menu_items import *
from pages.menu.leave_menu_items import *
from pages.performance.employee_trackers_page import PerformanceTrackersPage
from pages.pim.add_employee_page import AddEmployeePage
from pages.pim.employee_reports_page import EmployeeReportsPage
from pages.recruitement.candidates_page import CandidatesPage
from pages.recruitement.vacancies_page import VacanciesPage


class AdminMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_admin_viewAdminModule+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('UserManagement', (By.ID, 'menu_admin_UserManagement'), UserManagementMenu, None),
        MenuItem('Job', (By.ID, 'menu_admin_Job'), JobMenu, None),
        MenuItem('Organization', (By.ID, 'menu_admin_Organization'), OrganizationMenu, None),
        MenuItem('Qualifications', (By.ID, 'menu_admin_Qualifications'), QualificationsMenu, None),
        MenuItem('Nationalities', (By.ID, 'menu_admin_nationality'), None, NationalitiesPage),
        MenuItem('Configuration', (By.ID, 'menu_admin_Configuration'), AdminConfigurationMenu, None)
    }


class PIMMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_pim_viewPimModule+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Configuration', (By.ID, 'menu_pim_Configuration'), PIMConfigurationMenu, None),
        MenuItem('Employee List', (By.ID, 'menu_pim_viewEmployeeList'), None, EmployeeListPage),
        MenuItem('Add Employee', (By.ID, 'menu_pim_addEmployee'), None, AddEmployeePage),
        MenuItem('Reports', (By.ID, 'menu_core_viewDefinedPredefinedReports'), None, EmployeeReportsPage),
    }


class LeaveMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_leave_viewLeaveModule+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Entitlements', (By.ID, 'menu_leave_Entitlements'), EntitlementsMenu, None),
        MenuItem('Reports', (By.ID, 'menu_leave_Reports'), LeaveReportsMenu, None),
        MenuItem('Configure', (By.ID, 'menu_leave_Configure'), LeaveConfigureMenu, None),
        MenuItem('Leave List', (By.ID, 'menu_leave_viewLeaveList'), None, LeaveListPage),
        MenuItem('Assign Leave', (By.ID, 'menu_leave_assignLeave'), None, AssignLeavePage),
    }


class TimeMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_time_viewTimeModule+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Timesheets', (By.ID, 'menu_time_Timesheets'), TimesheetsMenu, None),
        MenuItem('Attendance', (By.ID, 'menu_attendance_Attendance'), AttendanceMenu, None),
        MenuItem('Reports', (By.ID, 'menu_time_Reports'), TimeReportsMenu, None),
        MenuItem('ProjectInfo', (By.ID, 'menu_admin_ProjectInfo'), ProjectInfoMenu, None)
    }


class RecruitmentMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_recruitment_viewRecruitmentModule+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Candidates', (By.ID, 'menu_recruitment_viewCandidates'), None, CandidatesPage),
        MenuItem('Vacancies', (By.ID, 'menu_recruitment_viewJobVacancy'), None, VacanciesPage)
    }


class PerformanceMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu__Performance+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Configure', (By.ID, 'menu_performance_Configure'), PerformanceConfigureMenu, None),
        MenuItem('ManageReviews', (By.ID, 'menu_performance_ManageReviews'), ManageReviewsMenu, None),
        MenuItem('Employee Trackers', (By.ID, 'menu_performance_viewEmployeePerformanceTrackerList'), None,
                 PerformanceTrackersPage)
    }


class MaintenanceMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_maintenance_purgeEmployee+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Purge Records', (By.ID, 'menu_maintenance_PurgeRecords'), PurgeRecordsMenu, None),
        MenuItem('Access Records', (By.ID, 'menu_maintenance_accessEmployeeData'), None, DownloadPersonalDataPage)
    }
