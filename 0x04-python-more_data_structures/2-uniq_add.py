#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    add = set()
    for i in my_list:
        add.add(i)
    for j in add:
        s += j
    return (s)
