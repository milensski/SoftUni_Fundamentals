statistics_dict = {}

while True:
    command = input()

    if command == "statistics":
        break

    key, value = command.split(": ")

    if key in statistics_dict:
        statistics_dict[key] += int(value)
    else:
        statistics_dict[key] = int(value)

print("Products in stock:")
[print(f'- {key}: {value}') for key, value in statistics_dict.items()]
print(f'Total Products: {len(statistics_dict)}')
print(f'Total Quantity: {sum(statistics_dict.values())}')
