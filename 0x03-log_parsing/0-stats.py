#!/usr/bin/python3
""" This script reads stdin line by line and computes metrics """
import sys
import re


# Global variables for counting log entries and storing information
log_entry_count = 0
metrics = {}


def print_metrics() -> None:
    """ Prints the accumulated log metrics. """
    print("File size: {}".format(metrics.get('size', 0)))
    for key in sorted(metrics.keys()):
        if key == 'size':
            continue
        print("{}: {}".format(key, metrics[key]))


try:
    # Read lines from standard input
    for line in sys.stdin:
        log_entry_count += 1
        line_pattern = (
            r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'   # IP address
            r'[ ]?-[ ]?'                                   # Space-dash-space
            r'\[\d{4}-\d{2}-\d{2} '                  # Date (YYYY-MM-DD)
            r'\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?\]'     # Time (HH:MM:SS)
            r' "GET /projects/260 HTTP/1\.1"'        # Request method and path
            r' (\d{3})'                              # Status code (3 digits)
            r' (\d{1,4})$')                          # Size (1-4 digits)

        match = re.match(line_pattern, line)
        if match:
            status_code = match.group(1)
            size = match.group(2)

            # Update metrics dictionary
            metrics['size'] = metrics.get('size', 0) + int(size)
            metrics[status_code] = metrics.get(status_code, 0) + 1
        # Print metrics after every 10 entries
        if log_entry_count % 10 == 0:
            print_metrics()
except KeyboardInterrupt:
    # Handle keyboard interruption
    sys.exit(1)
finally:
    print_metrics()
