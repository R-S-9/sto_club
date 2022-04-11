#!/usr/bin/env python

import os
import sys

from loguru import logger

from django.core.management.commands.runserver import Command as runserver


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    runserver.default_port = "8000"
    logger.info(
        f"'Manage' 'main' info:'Server start on {runserver.default_port}."
    )
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    logger.add(
        "logs/settings_logs.log",
        format="{time} {level} {message}",
        level="INFO",
        rotation="10MB",
        compression="zip"
    )

    main()
