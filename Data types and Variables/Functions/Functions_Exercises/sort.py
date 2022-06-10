numbers = input().split()
numbers = [int(number) for number in numbers]
print(list(map(int, (sorted(numbers)))))
