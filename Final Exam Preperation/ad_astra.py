import re

text = input()


pattern = r'([?<=#|\|])([a-zA-Z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'

result = re.finditer(pattern,text)

calories = 0

for match in result:
    if match.group() is not None and match.group(2).strip() != "":
        calories += int(match.group(4))


days = calories // 2000

print(f"You have food to last you for: {days} days!")

if days == 0:
    exit()

result = re.finditer(pattern,text)

for match in result:
    products = match.group(2)
    date = match.group(3)
    calories = int(match.group(4))
    print(f"Item: {products}, Best before: {date}, Nutrition: {calories}")