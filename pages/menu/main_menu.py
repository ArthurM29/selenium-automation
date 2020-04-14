from pages.maintenance.purge_employee_records_page import PurgeEmployeeRecordsPage
from pages.leave.timesheets_page import TimesheetsPage
from pages.dashboard_page import DashboardPage
from pages.menu.main_menu_items import *
from pages.search_directory_page import SearchDirectoryPage


class MainMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, '.menu>ul')
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Admin', (By.ID, 'menu_admin_viewAdminModule'), AdminMenu, UserManagementPage),
        MenuItem('PIM', (By.ID, 'menu_pim_viewPimModule'), PIMMenu, EmployeeListPage),
        MenuItem('Leave', (By.ID, 'menu_leave_viewLeaveModule'), LeaveMenu, LeaveListPage),
        MenuItem('Time', (By.ID, 'menu_time_viewTimeModule'), TimeMenu, TimesheetsPage),
        MenuItem('Recruitment', (By.ID, 'menu_recruitment_viewRecruitmentModule'), RecruitmentMenu, CandidatesPage),
        MenuItem('Performance', (By.ID, 'menu__Performance'), PerformanceMenu, None),
        MenuItem('Dashboard', (By.ID, 'menu_dashboard_index'), None, DashboardPage),
        MenuItem('Directory', (By.ID, 'menu_directory_viewDirectory'), None, SearchDirectoryPage),
        MenuItem('Maintenance', (By.ID, 'menu_maintenance_purgeEmployee'), MaintenanceMenu, PurgeEmployeeRecordsPage)
    }


