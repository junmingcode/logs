# -*- coding:utf-8 -*-
import sys
import logging.handlers

DEFAULT_LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
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
        rotating_handler = logging.handlers.RotatingFileHandler(filename=filename, maxBytes=4194304, backupCount=5,
                                                                encoding="utf-8")
        rotating_handler.setFormatter(self.formatter)
        return rotating_handler

    def _debug(self):
        '''return a function that write debug message'''
        return self.log_set[logging.DEBUG].debug

    def _info(self):
        '''return a function that write info message'''
        return self.log_set[logging.INFO].info

    def _warning(self):
        '''return a function that write warning message'''
        return self.log_set[logging.WARNING].warning

    def _error(self):
        '''return a function that write error message'''
        return self.log_set[logging.ERROR].error


logger = Logger()

if __name__ == '__main__':
    # Function assignment must be made
    logger.debug = logger._debug()
    logger.info = logger._info()
    logger.warning = logger._warning()
    logger.error = logger._error()

    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
