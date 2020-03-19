class PageNotLoadedException(Exception):
    """ Raised when the page identifier element does not get visible during specified time"""
    pass


class InvalidCredentialsException(Exception):
    """Raised when the credentials do not exist"""
    pass
