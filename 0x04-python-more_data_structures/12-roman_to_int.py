#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return (0)
    else:
        rom = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        total = 0
        for i in range(len(roman_string) - 1):
            if rom[roman_string[i]] < rom[roman_string[i + 1]]:
                total -= rom[roman_string[i]]
            else:
                total += rom[roman_string[i]]
        total += rom[roman_string[-1]]
        return (total)
