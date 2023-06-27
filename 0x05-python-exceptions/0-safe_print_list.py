#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        my_list = []

    try:
        for i in range(x):
            print(my_list[i], end="")
    except IndexError:
        i -= 1
        pass

    print()
    return (i + 1)
