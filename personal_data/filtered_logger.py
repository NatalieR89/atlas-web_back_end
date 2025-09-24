#!/usr/bin/env python3
"""
filtered_logger module.

Provides utilities to redact sensitive fields in logs, create a logger with
redaction enabled, connect securely to a database using environment
variables, and a main function to display user records with sensitive data
redacted.
"""

import logging
import os
from typing import List
import mysql.connector
from mysql.connector.connection import MySQLConnection
from filtered_logger import filter_datum  # assume filter_datum is defined in same project


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class that obfuscates sensitive fields in log messages."""

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


def main() -> None:
    """Obtain a DB connection, retrieve all users, and log each row with redaction."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT name, email, phone, ssn, password, ip, last_login, user_agent FROM users;")

    logger = get_logger()
    for row in cursor:
        # format the row into a single log string
        message = (
            f"name={row[0]}; email={row[1]}; phone={row[2]}; "
            f"ssn={row[3]}; password={row[4]}; ip={row[5]}; "
            f"last_login={row[6]}; user_agent={row[7]};"
        )
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
