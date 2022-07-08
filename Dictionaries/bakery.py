line_products = input().split(" ")

table_bakery = {line_products[i]: int(line_products[i + 1]) for i in range(0, len(line_products), 2)}

print(table_bakery)
