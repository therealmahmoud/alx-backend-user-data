#!/usr/bin/env python3
""" Task 0."""
import re
from typing import List


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
