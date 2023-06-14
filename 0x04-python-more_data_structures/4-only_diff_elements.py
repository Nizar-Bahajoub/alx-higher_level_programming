#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = set_1.difference(set_2)
    new = new.union(set_2.difference(set_1))
    return (new)
