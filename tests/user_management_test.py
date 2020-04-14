from pytest import mark as m


@m.describe("User Management")
class TestUserManagement:

    @m.it("Verify able to add a new user")
    def test_add_user(self, user_management_page, user):
        #TODO how to organize teardown if user is added inside a test with test steps
        add_user_page = user_management_page.click_add_button()
        user_management_page = add_user_page.add_user(user)
        print()
