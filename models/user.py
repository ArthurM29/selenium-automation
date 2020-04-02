class User:
    def __init__(self):
        self.user_role = 'ESS'
        self.employee_name = 'Hannah Flores'
        self.username = 'hflores'
        self.status = 'Enabled'
        self.password = 'Password_jan_123!'
        self.confirm_password = 'Password_jan_123!'

    def __str__(self):
        return str(self.__class__.__name__) + ": " + str(self.__dict__)
