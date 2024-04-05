from collections import Counter

employees = int(input())
names_list = []

for i in range(employees):
    employee = input().split()
    name = employee[0]
    names_list.append(name)

string_counts = Counter(names_list)

most_common_string, count = string_counts.most_common(1)[0]
print(count)
