numbers = input().split()

numbers = [int(number) for number in numbers]

print(list(filter(lambda x: x % 2 == 0, numbers)))

