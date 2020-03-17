import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.DEBUG, datefmt='%d/%m/%Y %I:%M:%S %p')

logging.info("Everything is good!")
logging.warning("Hello")
logging.error("PAhoo")