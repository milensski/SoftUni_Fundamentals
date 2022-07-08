import math
from math import ceil

budget = float(input())

students = int(input())

price_flour = float(input())

price_egg = float(input())

price_apron = float(input())

free_packages = students // 5


apron = price_apron * math.ceil(students + students * 0.2)

egg = price_egg * 10 * students

flour = price_flour * (students - students//5)

needed_price = apron + flour + egg


if needed_price <= budget:
    print(f"Items purchased for {needed_price:.2f}$.")
else:
    print(f"{needed_price-budget:.2f}$ more needed.")