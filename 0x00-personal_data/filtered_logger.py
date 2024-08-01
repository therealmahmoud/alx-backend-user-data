#!/usr/bin/env python3
""" Task 0."""
import re
from typing import List
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Formats a LogRecord."""
        message = super(RedactingFormatter, self).format(record)
        filterd = filter_datum(self.fields, self.REDACTION,
                               message, self.SEPARATOR)
        return filterd


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """ Returns the log message obfuscated. """
    pattern = '|'.join([f'{field}=.*?{separator}' for field in fields])
    return re.sub(pattern, lambda x: x.group().split('=')[0] + '=' +
                  redaction + separator, message)


def get_logger() -> logging.Logger:
    """ Returns a logging.Logger object. """
    logger = logging.getLogger('user_data')
    level = logger.setLevel(logging.INFO)
    return level.addHandler(RedactingFormatter(PII_FIELDS))
