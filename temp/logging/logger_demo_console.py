import logging

class LoggerDemoConsole:

    def test_log(self):
        # create logger
        logger = logging.getLogger('sample_log')
        logger.setLevel(logging.INFO)

        # create console logger and set loglevel
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter('%(asctime)s: %(name)s %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

        # add formatter to console handler
        console_handler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(console_handler)

        logger.info("Everything is good!")
        logger.warning("Hello")
        logger.error("PAhoo")



lg = LoggerDemoConsole()
lg.test_log()