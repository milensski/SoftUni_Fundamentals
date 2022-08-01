import re

text = input()

pattern = r'([\||\#])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'

result = re.finditer(pattern, text)
calories = 0
for match in result:
    if match:
        calories += int(match.group(4))


products = re.finditer(pattern,text)

print(f'You have food to last you for: {calories//2000} days!')

for matches in products:
     if matches:
          food = matches.group(2)
          date = matches.group(3)
          calorie = matches.group(4)

          print(f"Item: {food}, Best before: {date}, Nutrition: {calorie}")
