# -*- coding:utf-8 -*-
import sys
import logging.handlers
from concurrent_log_handler import ConcurrentRotatingFileHandler

DEFAULT_LOG_FMT = '%(asctime)s  [process: %(process)s]  [thread: %(thread)s]  %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
DEFUALT_LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'
Handlers = {
    # logging.NOTSET : "./log/NOTSET.log",
    logging.DEBUG: "./log/DEBUG.log",
    logging.INFO: "./log/INFO.log",
    logging.WARNING: "./log/WARNING.log",
    logging.ERROR: "./log/ERROR.log",
    # logging.CRITICAL : "./log/CRITICAL.log"
}
class Logger(object):

    def __init__(self):
        # set formatter ,the log will print like this formatter

        self.formatter = logging.Formatter(fmt=DEFAULT_LOG_FMT, datefmt=DEFUALT_LOG_DATEFMT)
        self.log_set = {}
        # get logger and set handler
        for level in Handlers.keys():
            logger = logging.getLogger(str(Handlers[level]))
            if not logger.handlers:
                logger.addHandler(self._get_rotating_file_handler(Handlers[level]))
                logger.addHandler(self._get_console_handler())
                logger.setLevel(level)
                self.log_set[level] = logger
            else:
                self.log_set[level] = logger

    def _get_console_handler(self):
        '''get console handler,will print log on console'''
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    def _get_rotating_file_handler(self, filename):
        '''get a file handler,will write log in file'''
        # rotating_handler = logging.handlers.RotatingFileHandler(filename=filename, maxBytes=41943040, backupCount=5,
        #                                                         encoding="utf-8")
        # Multi process support
        rotating_handler = ConcurrentRotatingFileHandler(filename=filename, maxBytes=41943040, backupCount=5,
                                                         encoding="utf-8")
        rotating_handler.setFormatter(self.formatter)
        return rotating_handler

    @property
    def debug(self):
        return self.log_set[logging.DEBUG].debug

    @property
    def info(self):
        return self.log_set[logging.INFO].info

    @property
    def warning(self):
        return self.log_set[logging.WARNING].warning

    @property
    def error(self):
        return self.log_set[logging.ERROR].error


logger = Logger()

if __name__ == '__main__':
    # Function assignment must be made
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
