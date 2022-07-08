from collections import defaultdict

sequence = input().lower().split()

d = defaultdict(int)

for element in sequence:
    d[element] += 1

[print(key, end=" ") for key in d if d[key] % 2 != 0]
