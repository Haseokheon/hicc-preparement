#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Django가 설치되어 있지 않습니다.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
