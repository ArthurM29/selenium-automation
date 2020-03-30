from pytest import mark as m
import time

from common.data.credentials import get_credentials
from pages.header_page import Header


@m.describe("Header")
class TestHeader:

    @m.it("Verify branding logo is displayed on header")
    def test_logo_is_displayed(self, header_page):
        assert header_page.is_logo_displayed()

    @m.it("Verify clicking on branding logo navigates to OrangeHRM production website")
    def test_logo_link_navigates_to_production_website(self, header_page):
        orange_hrm_prod_page = header_page.click_on_logo()
        assert orange_hrm_prod_page.get_url() == 'https://www.orangehrm.com/'
        assert orange_hrm_prod_page.is_loaded()

    @m.it("Verify welcome text is displayed with logged in username")
    def test_welcome_text_is_displayed(self, login_page):
        username, password = get_credentials(('valid_credentials'))
        login_page.login(username, password)
        header_page = Header(login_page.driver)  # TODO how can I get this from fixture and avoid creating in tests ?
        assert header_page.get_welcome_text() == f"Welcome {username}"

    @m.it("Verify user is able to logout")
    def test_able_to_logout(self, header_page):
        login_page = header_page.logout()
        assert login_page.is_loaded()

    @m.describe("About modal")
    @m.it("Verify dialog title is 'About'")
    def test_about_modal_title(self, about_modal):
        assert about_modal.get_title() == 'About'

    @m.describe("About modal")
    @m.it("Verify able to close modal with close icon")
    def test_close_icon(self, about_modal):
        about_modal.close()
        assert about_modal.is_not_loaded()

    # TODO add more tests
