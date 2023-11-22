#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        sys.stderr.write("Exception: {}\n".format(ve))
    except TypeError as ve:
        sys.stderr.write("Exception: {}\n".format(ve))
        return False
    else:
        return True
