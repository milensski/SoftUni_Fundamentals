numbers = input().split()

numbers = list(map(int, numbers))

print(list(filter(lambda x: x % 2 == 0, numbers)))
