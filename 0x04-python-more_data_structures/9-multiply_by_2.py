#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict()
    for i in list(a_dictionary.keys()):
        new[i] = a_dictionary[i] * 2
    return (new)
