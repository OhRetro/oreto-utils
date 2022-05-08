#Logger

import logging
import time

class Logger:
    def __init__(self, log_file_name=f"{time.strftime('%Y-%m-%d')}.log", log_level=logging.INFO):
        self.log_file_name = log_file_name
        self.log_level = log_level
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(self.gethandler())

    def gethandler(self):
        handler = logging.FileHandler(self.log_file_name)
        handler.setLevel(self.log_level)
        handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        return handler

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
        
    def exception(self, message):
        self.logger.exception(message)