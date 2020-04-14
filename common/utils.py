from random import choice, randint
from string import ascii_lowercase


def random_string(length, charset=None):
    """Return random string of given length from elements of charset, which defaults to lowercase ascii characters"""
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Invalid value: '{}'. Length must be a positive integer.".format(length))

    alphabet = charset if charset else ascii_lowercase
    new_str = ''.join(choice(alphabet) for s in range(length))
    assert len(new_str) == length, "Generated string does not match specified length"
    return new_str


def random_integer(start, stop):
    """Return a random integer in range [start, stop]"""
    return randint(int(start), int(stop))
