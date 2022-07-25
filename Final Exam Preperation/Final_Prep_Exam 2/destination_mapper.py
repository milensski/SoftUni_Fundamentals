import re

pattern = r'([\=|\/])([A-Z][a-zA-Z]{2,})\1'

sequence = input()

destinations = []
total_sum = 0

result = re.findall(pattern,sequence)

for match in result:
    if match:
        destinations.append(match[1])
        total_sum += len(match[1])

print(f"Destinations: {', '.join(destinations)}")

print(f'Travel Points: {total_sum}')
