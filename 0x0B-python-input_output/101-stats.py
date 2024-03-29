#!/usr/bin/python3
"""Reads from standard input"""


def print_stats(size, status):
    """Print accumulated metrics"""

    print("File size: {}".format(size))
    for key in sorted(status):
        print("{}: {}".format(key, status[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status.get(line[-2], -1) == -1:
                        status[line[-2]] = 1
                    else:
                        status[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status)

    except KeyboardInterrupt:
        print_stats(size, status)
        raise
