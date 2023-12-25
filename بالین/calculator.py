def calculate_floor(string):
    floor = 0
    string = string.upper()
    for c in string:
        if c == 'U':
            floor += 1
        elif c == 'D':
            floor -= 1
    return floor
