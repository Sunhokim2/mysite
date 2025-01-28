#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Check database connection'

    def handle(self, *args, **kwargs):
        db_conn = connections['default']
        try:
            db_conn.cursor()
            self.stdout.write(self.style.SUCCESS('Database connection is OK'))
        except OperationalError:
            self.stdout.write(self.style.ERROR('Database connection failed'))


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
