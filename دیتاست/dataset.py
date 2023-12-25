n, q, l = map(int, input().split())

if 1 <= n <= 10**5 and 1 <= q <= 10**5 and 1 <= l <= 10**2:
    first_dict = {}
    for _ in range(n):
        m, char = input().split()
        first_dict[m] = char

    q_list = []
    for _ in range(q):
        s = input()
        q_list.append(s)

    matching_keys = [first_dict[key] if key in first_dict else 'Unknown' for key in q_list]
    for item in matching_keys:
        print(item)







