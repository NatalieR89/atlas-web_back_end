#!/usr/bin/env python3
"""
filtered_logger module.

Provides utilities to redact sensitive fields in logs, create a logger with
redaction enabled, and connect securely to a database using environment
variables.
"""

import logging
import os
from typing import List
import mysql.connector
from mysql.connector.connection import MySQLConnection
from filtered_logger import filter_datum  # reuse your earlier function


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class that obfuscates sensitive fields in log messages. """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to redact."""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Redact sensitive fields in the log record’s message before formatting."""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)


# Define sensitive fields from user_data.csv
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """Return a configured logger for user data with redaction enabled."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    """Return a MySQL database connection using environment variables."""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )
