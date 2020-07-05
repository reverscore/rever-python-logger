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
            'format': '%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s -- %(metadata)s -- %(exc_info)s'
        },
        'json': {
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s'
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

    def __init__(self, service_name, logger_name):
        if ENVIRONMENT == 'dev' or ENVIRONMENT == 'test':
            LOGGING_CONFIG['loggers']['']['handlers'] = ['console']

        self.service_name = service_name
        self.environment = ENVIRONMENT
        logging.config.dictConfig(LOGGING_CONFIG)
        self.log = logging.getLogger(logger_name)

    def info(self, message, metadata=None):
        self.log.info(message, extra={
                      'metadata': metadata, 'service': self.service_name, 'environment': self.environment})

    def warning(self, message, metadata=None):
        self.log.warning(message, extra={
                         'metadata': metadata, 'service': self.service_name, 'environment': self.environment})

    def error(self, message, metadata=None):
        self.log.error(message, extra={
                       'metadata': metadata, 'service': self.service_name, 'environment': self.environment})

    def exception(self, message):
        self.log.error("Uncaught exception: %s", traceback.format_exc())

    def debug(self, message, metadata=None):
        self.log.debug(message, extra={
                       'metadata': metadata, 'service': self.service_name, 'environment': self.environment})

    def critical(self, message, metadata=None):
        self.log.debug(message, extra={
                       'metadata': metadata, 'service': self.service_name, 'environment': self.environment})
