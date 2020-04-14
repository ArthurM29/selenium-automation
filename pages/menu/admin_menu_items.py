from pages.admin.configuration.email_configuration_page import EmailConfigurationPage
from pages.admin.configuration.email_subscription_page import EmailSubscriptionsPage
from pages.admin.configuration.localization_page import LocalizationPage
from pages.admin.configuration.modules_page import ModulesPage
from pages.admin.configuration.register_oauth_client_page import RegisterOAuthClientPage
from pages.admin.configuration.social_media_authentication_page import SocialMediaAuthenticationPage
from pages.admin.organization.organization_structure_page import OrganizationStructurePage
from pages.admin.qualifications.education_page import EducationPage
from pages.admin.job.employment_status_page import EmploymentStatusPage
from pages.admin.organization.general_information_page import GeneralInformationPage
from pages.admin.job.job_categories_page import JobCategoriesPage
from pages.admin.job.job_titles_page import JobTitlesPage
from pages.admin.qualifications.languages_page import LanguagesPage
from pages.admin.qualifications.licenses_page import LicensesPage
from pages.admin.organization.locations_page import LocationsPage
from pages.admin.qualifications.memberships_page import MembershipsPage
from pages.admin.job.pay_grades_page import PayGradesPage
from pages.admin.qualifications.skills_page import SkillsPage
from pages.admin.user_management_page import UserManagementPage
from pages.admin.job.work_shifts_page import WorkShiftsPage
from pages.menu.base_menu import BaseMenu, MenuItem
from selenium.webdriver.common.by import By


class UserManagementMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_admin_UserManagement+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Users', (By.ID, 'menu_admin_viewSystemUsers'), None, UserManagementPage)
    }


class JobMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_admin_Job+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Job Titles', (By.ID, 'menu_admin_viewJobTitleList'), None, JobTitlesPage),
        MenuItem('Pay Grades', (By.ID, 'menu_admin_viewPayGrades'), None, PayGradesPage),
        MenuItem('Employment Status', (By.ID, 'menu_admin_employmentStatus'), None, EmploymentStatusPage),
        MenuItem('Job Categories', (By.ID, 'menu_admin_jobCategory'), None, JobCategoriesPage),
        MenuItem('Work Shifts', (By.ID, 'menu_admin_workShift'), None, WorkShiftsPage)
    }


class OrganizationMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_admin_Organization+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('General Information', (By.ID, 'menu_admin_viewOrganizationGeneralInformation'), None,
                 GeneralInformationPage),
        MenuItem('Locations', (By.ID, 'menu_admin_viewLocations'), None,
                 LocationsPage),
        MenuItem('Structure', (By.ID, 'menu_admin_viewCompanyStructure'), None,
                 OrganizationStructurePage),
    }


class QualificationsMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_admin_Qualifications+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Skills', (By.ID, 'menu_admin_viewSkills'), None, SkillsPage),
        MenuItem('Education', (By.ID, 'menu_admin_viewEducation'), None, EducationPage),
        MenuItem('Licenses', (By.ID, 'menu_admin_viewLicenses'), None, LicensesPage),
        MenuItem('Languages', (By.ID, 'menu_admin_viewLanguages'), None, LanguagesPage),
        MenuItem('Memberships', (By.ID, 'menu_admin_membership'), None, MembershipsPage)
    }


class AdminConfigurationMenu(BaseMenu):
    _menu_container_locator = (By.CSS_SELECTOR, "#menu_admin_Configuration+ul")
    _page_identifier_element = _menu_container_locator

    menu_items = {
        MenuItem('Email Configuration', (By.ID, 'menu_admin_listMailConfiguration'), None, EmailConfigurationPage),
        MenuItem('Email Subscriptions', (By.ID, 'menu_admin_viewEmailNotification'), None, EmailSubscriptionsPage),
        MenuItem('Localization', (By.ID, 'menu_admin_localization'), None, LocalizationPage),
        MenuItem('Modules', (By.ID, 'menu_admin_viewModules'), None, ModulesPage),
        MenuItem('Social Media Authentication', (By.ID, 'menu_admin_openIdProvider'), None,
                 SocialMediaAuthenticationPage),
        MenuItem('Register OAuth Client', (By.ID, 'menu_admin_registerOAuthClient'), None,
                 RegisterOAuthClientPage),
    }
