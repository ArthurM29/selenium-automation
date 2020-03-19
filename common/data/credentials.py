from common.exceptions import InvalidCredentialsException

credential_types = [
    {"valid_credentials": ("Admin", "admin123")},
    {"empty_username": ("", "admin123")},
    {"empty_password": ("Admin", "")},
    {"empty_username_and_password": ("", "")},
    {"invalid_username": ("Admin_INVALID", "admin123")},
    {"invalid_password": ("Admin", "admin123_INVALID")},
    {"invalid_username_and_password": ("Admin_INVALID", "admin123_INVALID")}
]


def get_credentials(name):
    name = name.lower()
    for credentials in credential_types:
        if credentials.get(name.lower()):
            username, password = credentials[name]
            return username, password
    raise InvalidCredentialsException(f"{name} is not a valid credentials type")
