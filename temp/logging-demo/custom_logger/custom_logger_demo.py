import logging
from temp.logging.custom_logger.custom_logger import custom_logger


class LoggingDemo2():
    log = custom_logger(logging.DEBUG)

    def method1(self):
        self.log.info("Everything is good!")
        self.log.warning("Hello")
        self.log.error("PAhoo")

    def method2(self):
        m2_log = custom_logger(logging.INFO)
        m2_log.info("Everything is good!")
        m2_log.warning("Hello")
        m2_log.error("PAhoo")

    def method3(self):
        self.log.info("Everything is good!")
        self.log.warning("Hello")
        self.log.error("PAhoo")


ld = LoggingDemo2()
ld.method1()
ld.method2()
ld.method3()