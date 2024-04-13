#!/usr/bin/env python3
""" This function returns and obfuscated log messages
"""
import re
import logging


def filter_datum(fields, redaction, message, separator):
    """ Return an obfuscated message
    """
    for field in fields:
        patterns = re.sub(f'{field}=.*?{separator}',
                          f'{field}={redaction}{separator}', message)
    return patterns


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Implement the filter datum as the formatter
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
