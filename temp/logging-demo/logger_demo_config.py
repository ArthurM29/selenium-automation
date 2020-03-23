import logging
import logging.config

class LoggerDemoConfig:

    def test_log(self):

        # create logger
        logging.config.fileConfig('logging-demo.conf')
        logger = logging.getLogger(LoggerDemoConfig.__name__)


        logger.info("Everything is good!")
        logger.warning("Hello")
        logger.error("PAhoo")



lg = LoggerDemoConfig()
lg.test_log()