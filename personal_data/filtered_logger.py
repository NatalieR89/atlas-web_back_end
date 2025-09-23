#!/usr/bin/env python3
"""
filtered_logger module.

Provides the RedactingFormatter class that redacts sensitive fields in logs.
"""

import logging
from typing import List
from filtered_logger import filter_datum  # import the function you already wrote


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class that obfuscates sensitive fields in log messages. """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to redact."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Redact sensitive fields in the log record’s message before formatting."""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)
