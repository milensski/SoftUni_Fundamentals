def min_number(self):
    result = min(list(map(int, self)))
    return result


def max_number(self):
    return max(list(map(int, self)))


def sum_numbers(self):
    return sum(list(map(int, self)))


numbers = input().split()
numbers = [int(number) for number in numbers]

print(f"The minimum number is {min_number(numbers)}")
print(f"The maximum number is {max_number(numbers)}")
print(f"The sum number is: {sum_numbers(numbers)}")
