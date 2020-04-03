import logging


class CustomLogger:
    def __init__(self, name=__name__, log_level=logging.INFO, formatter=logging.Formatter('')):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)
        self.formatter = formatter

    def set_file_handler(self, file_path, mode='w'):
        if self.logger.hasHandlers():
            self.logger.handlers.clear()
        file_handler = logging.FileHandler(file_path, mode=mode)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)

    @staticmethod
    def get_logger(name):
        return logging.getLogger(name)

    def set_formatter(self, format_='%(asctime)s - %(levelname)s - %(message)s'):
        self.formatter = logging.Formatter(format_)
        # file_handler = self.logger.handlers[0]
        # file_handler.setFormatter(formatter)
        self.set_file_handler('results/automation.log')
