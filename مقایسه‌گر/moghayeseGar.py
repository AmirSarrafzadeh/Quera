def compare(string1, string2):
    if string1[0] < string2[0]:
        string1 = string1[::-1][:-1]
        string2 = string2[::-1][:]
    elif string1[0] > string2[0]:
        string2 = string2[::-1][:-1]
        string1 = string1[::-1][:]
    else:
        string1 = string1[::-1][:-1]
        string2 = string2[::-1][:-1]

    if len(string1) == 0 and len(string2) != 0:
        return string2[::-1][:]
    elif len(string2) == 0 and len(string1) != 0:
        return string1[::-1][:]
    elif len(string1) == 0 and len(string2) == 0:
        return "Both strings are empty!"
    else:
        return compare(string1, string2)


