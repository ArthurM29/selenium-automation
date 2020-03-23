class PageNotLoadedException(Exception):
    """ Raised when the page identifier element does not get visible during specified time"""
    pass


class InvalidCredentialsException(Exception):
    """Raised when the credentials do not exist"""
    pass


class NotImplementedException(Exception):
    """Raised when the feature is not implemented yet"""
    pass


class ElementNotDisplayedException(Exception):
    """Raised when the element is not displayed"""
    pass


class ElementNotClickableException(Exception):
    """Raised when the element is not clickable"""
    pass
