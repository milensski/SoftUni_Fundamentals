number = input()

largest = sorted(number, reverse=True)

result = str("".join(largest))

print(result)