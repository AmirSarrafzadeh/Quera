def separator(ls):
    """Separate even and odd numbers in a list"""
    even = []
    odd = []
    for item in ls:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)

    return even, odd

