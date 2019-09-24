#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # To facilitate debug I'm setting the default value to Dev
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'confs.settings.dev')

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
