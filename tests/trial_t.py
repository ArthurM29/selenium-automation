from pytest import mark as m
import pytest_check as check
from common.data.credentials import get_credentials


@m.describe("Login")
class TestLogin:

    # @m.it("Try --browser command line argument")
    # def test_browser_cmd_argument(self, browser):
    #     print(f"\nbrowser: {browser}")
    #
    # @m.it("Try --headless command line argument")
    # def test_headless_cmd_argument(self, headless):
    #     if headless:
    #         print("Browser is headless")
    #     else:
    #         print("Browser is not headless")
    #     print(f"\nheadless: {headless}")
    #     print(f"headless type: {type(headless)}")
    #
    # @m.it("Try --url command line argument")
    # def test_url_cmd_argument(self, url):
    #     print(f"\nurl: {url}")
    #
    # @m.it("Try --env command line argument")
    # def test_env_cmd_argument(self, env):
    #     print(f"\nenv: {env}")


    @m.it("Multiple assertions")
    def test_multi_assert(self):
        name1 = 'Babo'
        name2 = 'Rubo'
        check.equal(name1, 'Kabo')
        check.is_true(2 == 2)
        check.equal('Dubo',  name2)
