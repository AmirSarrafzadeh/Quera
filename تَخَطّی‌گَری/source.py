print(' '.join(sorted([item if (ord(item) - 97) % 2 == 0 else item.upper() for item in str(input())], reverse=True)))

