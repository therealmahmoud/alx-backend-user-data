#!/usr/bin/env python3
""" Task 0."""
import os
import re
import logging
import mysql.connector
from typing import List


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
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.propagate = False
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to a secure holberton database to read a users table."""
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', "localhost"),
    db_pass = os.getenv('PERSONAL_DATA_DB_PASSWORD', ""),
    db_user = os.getenv('PERSONAL_DATA_DB_USERNAME', "root"),
    db_name = os.getenv('PERSONAL_DATA_DB_NAME', "")
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        port=3306,
        password=db_pass,
        database=db_name,
    )
    return connection
