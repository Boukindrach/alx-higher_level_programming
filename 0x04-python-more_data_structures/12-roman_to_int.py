#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or (not isinstance(roman_string, str)):
        return 0

    x = list(roman_string)
    y = len(x)
    roman_n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    p = 0

    for a in range(y):
        if x[a] not in list(roman_n):
            return 0
        if (a != y - 1) and roman_n.get(x[a]) >= roman_n.get(x[a + 1]):
            p += roman_n.get(x[a])
        elif a == y - 1:
            p += roman_n.get(x[a])
        else:
            p -= roman_n.get(x[a])

    return p
