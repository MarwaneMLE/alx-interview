#!/usr/bin/python3
"""
Tasks 0. UTF- Validation
"""


def validUTF8(data):
    """
    Method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    num_bytes = 0
    for byte in data:
        mask = 1 << 7

        #If w're not expecting additional bytes,determine the num of leading 1s
        if num_bytes == 0:
            while byte & mask:
                num_bytes += 1
                mask >>= 1

            # If no leading 1s, it's a single-byte character
            if num_bytes == 0:
                continue

            # Invalid cases for UTF-8
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if byte >> 6 != 0b10:
                return False

        num_bytes -= 1

    return num_bytes == 0
