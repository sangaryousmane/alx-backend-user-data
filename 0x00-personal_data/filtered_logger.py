#!/usr/bin/env python3
""" This function returns and obfuscated log messages
"""
import re


def filter_datum(fields, redaction, message, separator):
    pattern = "(" + "|".join(fields) + ")=[^" + separator + "]*"
    return re.sub(pattern, lambda x: x.group(1) + "=" + redaction, message)
