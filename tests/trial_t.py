from pytest import mark as m
from common.data.credentials import get_credentials


@m.describe("Login")
class TestLogin:

    @m.it("Try --browser command line argument")
    def test_browser_cmd_argument(self, browser):
        print(f"\nbrowser: {browser}")

    @m.it("Try --headless command line argument")
    def test_headless_cmd_argument(self, headless):
        if headless:
            print("Browser is headless")
        else:
            print("Browser is not headless")
        print(f"\nheadless: {headless}")
        print(f"headless type: {type(headless)}")

    @m.it("Try --url command line argument")
    def test_url_cmd_argument(self, url):
        print(f"\nurl: {url}")

    @m.it("Try --env command line argument")
    def test_env_cmd_argument(self, env):
        print(f"\nenv: {env}")
