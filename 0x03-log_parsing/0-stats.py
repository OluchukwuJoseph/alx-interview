#!/usr/bin/python3
""" This script reads stdin line by line and computes metrics """
import sys
import re
import signal


# Global variables for counting log entries and storing information
log_entry_count = 0
metrics = {}


def print_metrics() -> None:
    """ Prints the accumulated log metrics. """
    print(f"File size: {metrics['size']}")
    for key, value in metrics.items():
        if key == 'size':
            continue
        print(f"{key}: {value}")


def handle_sigint(signal_number: int, frame: int) -> None:
    """ Handles SIGINT signal to print metrics before exiting. """
    print_metrics()


# Register the SIGINT signal handler
signal.signal(signal.SIGINT, handle_sigint)

# Read lines from standard input
for line in sys.stdin:
    line_pattern = (
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'   # IP address
        r' - '                                   # Space-dash-space
        r'\[\d{4}-\d{2}-\d{2} '                  # Date (YYYY-MM-DD)
        r'\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?\]'     # Time (HH:MM:SS)
        r' "GET /projects/260 HTTP/1\.1"'        # Request method and path
        r' (\d{3})'                              # Status code (3 digits)
        r' (\d{1,4})$')                          # Size (1-4 digits)

    match = re.match(line_pattern, line)
    if match:
        log_entry_count += 1
        status_code = match.group(1)
        size = match.group(2)

        # Update metrics dictionary
        metrics['size'] = metrics.get('size', 0) + int(size)
        metrics[status_code] = metrics.get(status_code, 0) + 1
        # Print metrics every 10 entries
        if log_entry_count % 10 == 0:
            print_metrics()
