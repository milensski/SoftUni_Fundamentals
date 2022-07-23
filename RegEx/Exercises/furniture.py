import re

pattern = r'>>([A-Za-z]+)<<(\d+|\d+\.\d+)!(\d+)'

furniture = []

total_sum = 0

while True:

    data = input()

    if data == 'Purchase':
        break

    result = re.match(pattern, data)

    if result is not None:
        furniture.append(result.group(1))

        price = float(result.group(2))

        quantity = int(result.group(3))

        total_sum += price * quantity

print("Bought furniture:")
[print(element) for element in furniture]
print(f"Total money spend: {total_sum:.2f}")
