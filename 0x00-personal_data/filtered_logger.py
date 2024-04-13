#!/usr/bin/env python3
""" This function returns and obfuscated log messages
"""
import re
import logging
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """ Get a logger from a csv
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(list(PII_IELDS)))
    logger.addHandler(stream)
    return logger


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Return an obfuscated message
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


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
        """ Implement the filter datum as the formatter
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
