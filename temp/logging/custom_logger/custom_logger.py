import inspect
import logging


def custom_logger(log_level):
    # gets the name of the class/method from where it is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("{}.log".format(logger_name), mode='w')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s: %(name)s %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

    # by default, log all messages
