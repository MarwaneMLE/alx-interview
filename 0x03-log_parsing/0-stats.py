#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys


# Initialize counters
i = 0

sum_file_size = 0  # Total size of files
# Dictionary to hold counts of different HTTP status codes
status_code = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
try:
    # Read lines from standard input
    for line in sys.stdin:
        args = line.split(' ')  # Split the line into parts
        # Ensure there are enough parts to process status and file size
        if len(args) > 2:
            status_line = args[-2]  # Get the HTTP status code
            file_size = args[-1]    # Get the file size

            # Increment the count for the status code if it's recognized
            if status_line in status_code:
                status_code[status_line] += 1

            # Add the file size to the total
            sum_file_size += int(file_size)
            i += 1  # Increment the line counter

            # Every 10 lines, print metrics
            if i == 10:
                print('File size: {:d}'.format(sum_file_size))
                sorted_keys = sorted(status_code.keys())  # Sort the status codes
                for key in sorted_keys:
                    value = status_code[key]
                    # Print the count of each status code if it is not zero
                    if value != 0:
                        print('{}: {}'.format(key, value))
                i = 0  # Reset the line counter for the next batch

except Exception:
    # Handle exceptions silently (consider logging for debugging)
    pass
finally:
    # Print final metrics after reading all lines
    print('File size: {:d}'.format(sum_file_size))
    sorted_keys = sorted(status_code.keys())  # Sort the status codes
    for key in sorted_keys:
        value = status_code[key]
        # Print the count of each status code if it is not zero
        if value != 0:
            print('{}: {}'.format(key, value))
