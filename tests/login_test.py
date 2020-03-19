from pytest import mark as m
from common.data.credentials import get_credentials


@m.describe("Login")
class TestLogin:

    @m.it("Verify able to login with valid credentials")
    def test_valid_login(self, login_page):
        dashboard = login_page.login(*get_credentials(('valid_credentials')))
        assert dashboard.get_title() == 'Dashboard'

    @m.it("Verify error message is displayed if trying to login with empty username")
    def test_login_with_empty_username(self, login_page):
        login_page.invalid_login(*get_credentials(('empty_username')))
        assert login_page.get_invalid_login_error() == 'Username cannot be empty'

    @m.it("Verify error message is displayed if trying to login with empty password")
    def test_login_with_empty_password(self, login_page):
        login_page.invalid_login(*get_credentials(('empty_password')))
        assert login_page.get_invalid_login_error() == 'Password cannot be empty'

    @m.it("Verify error message is displayed if trying to login with empty username and password")
    def test_login_with_empty_username_and_password(self, login_page):
        login_page.invalid_login(*get_credentials(('empty_username_and_password')))
        assert login_page.get_invalid_login_error() == 'Username cannot be empty'

    @m.it("Verify error message is displayed if trying to login with invalid username")
    def test_login_with_invalid_username(self, login_page):
        login_page.invalid_login(*get_credentials(('invalid_username')))
        assert login_page.get_invalid_login_error() == 'Invalid credentials'

    @m.it("Verify error message is displayed if trying to login with invalid password")
    def test_login_with_invalid_password(self, login_page):
        login_page.invalid_login(*get_credentials(('invalid_password')))
        assert login_page.get_invalid_login_error() == 'Invalid credentials'

    @m.it("Verify error message is displayed if trying to login with invalid username and password")
    def test_login_with_invalid_username_and_password(self, login_page):
        login_page.invalid_login(*get_credentials(('invalid_username_and_password')))
        assert login_page.get_invalid_login_error() == 'Invalid credentials'
