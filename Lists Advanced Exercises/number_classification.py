sequence = input().split(", ")

sequence = list(map(int, sequence))

positive = list(map(str, [num for num in sequence if num >= 0]))
negative = list(map(str, ([num for num in sequence if num < 0])))
even = list(map(str, ([num for num in sequence if num % 2 == 0])))
odd = list(map(str, ([num for num in sequence if num % 2 != 0])))

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
