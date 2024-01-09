#!/usr/bin/python3
""" module with methods to read line by line """

import signal
import sys


def print_statistics(total_size, status_codes):
    """
    Prints the computed statistics.
    """
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{:d}: {:d}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """
    Signal handler function.

    Args:
        sig: Signal number
        frame: Current stack frame

    Returns:
        None
    """
    print_statistics(total_size, status_codes)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

line_count = 0
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        line_count += 1
        try:
            tokens = line.split()
            total_size += int(tokens[-1])
            status_code = int(tokens[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except ValueError:
            pass

        if line_count % 10 == 0:
            print_statistics(total_size, status_codes)

except KeyboardInterrupt:
    print_statistics(total_size, status_codes)
    sys.exit(0)
