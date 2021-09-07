import copy
import logging.config
import traceback
from pythonjsonlogger import jsonlogger
import os

ENVIRONMENT = os.environ['ENVIRONMENT']

LOGGING_CONFIG = {
    'version': 1,  # required
    'disable_existing_loggers': True,  # this config overrides all other loggers
    'formatters': {
        'simple': {
            'format': '%(levelname)s [%(logId)s]: %(message)s -- %(metadata)s -- %(exc_info)s'
        },
        'json': {
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '%(asctime)s\t%(levelname)s -- %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_json': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'json'
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console_json']
        }
    }
}


class Logger:

    def __init__(self, logger_name, service_name):
        if ENVIRONMENT == 'dev' or ENVIRONMENT == 'test':
            LOGGING_CONFIG['loggers']['']['handlers'] = ['console']

        self.logId = None
        self.service_name = service_name
        self.environment = ENVIRONMENT
        logging.config.dictConfig(LOGGING_CONFIG)
        self.log = logging.getLogger(logger_name)

    def setLogId(self, logId):
        self.logId = logId

    def getLogId(self):
        return self.logId

    def buildExtra(self, metadata):
        extra = {
            'metadata': metadata,
            'service': self.service_name,
            'environment': self.environment,
            'logId': self.logId,
            'level': self.log.level
        }

        return extra

    def info(self, message, metadata=None):
        self.log.info(message, extra=self.buildExtra(metadata))

    def warning(self, message, metadata=None):
        self.log.warning(message, extra=self.buildExtra(metadata))

    def error(self, message, metadata=None):
        self.log.error(message, extra=self.buildExtra(metadata))

    def exception(self, message):
        if message:
            self.log.error(message)
        self.log.error("Uncaught exception: %s", traceback.format_exc())

    def debug(self, message, metadata=None):
        self.log.debug(message, extra=self.buildExtra(metadata))

    def critical(self, message, metadata=None):
        self.log.debug(message, extra=self.buildExtra(metadata))


def logger(logger_name, service_name):
    log = Logger(logger_name=logger_name, service_name=service_name)
    return log
