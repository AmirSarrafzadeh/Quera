print(' '.join(map(str, sorted([int(x) for i, x in enumerate(input().split()) if (i+1) % 6 == 0 and int(x) % 6 == 0]))))
