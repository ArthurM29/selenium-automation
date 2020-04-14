import logging

from common.utils import random_string

pretty_logger = logging.getLogger('pretty_logger')


class User:
    def __init__(self,
                 user_role='ESS',
                 employee_name='Hannah Flores',
                 username=f'hflores_{random_string(3)}',
                 status='Enabled',
                 password='Password_jan_123!',
                 confirm_password='Password_jan_123!'):
        self.user_role = user_role
        self.employee_name = employee_name
        self.username = username
        self.status = status
        self.password = password
        self.confirm_password = confirm_password
        pretty_logger.info(f"Created user: {self}")

    def __str__(self):
        return str(self.__class__.__name__) + ": " + str(self.__dict__)
