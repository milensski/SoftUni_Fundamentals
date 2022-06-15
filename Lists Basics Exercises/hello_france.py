items_list = input().split("|")
budget = float(input())

budget_copy = budget

bough_items_prices = []
bough_items = 0
profit = 0

for items in items_list:
    item_values = items.split("->")
    item_type = item_values[0]
    item_price = float(item_values[1])

    if item_type == "Clothes" and item_price <= 50 and item_price <= budget:
        budget -= item_price
        item_new_price = (item_price + (item_price * 0.4))
        bough_items += item_new_price
        bough_items_prices.append(item_new_price)
        profit += item_new_price - item_price
    elif item_type == "Shoes" and item_price <= 35 and item_price <= budget:
        budget -= item_price
        item_new_price = (item_price + (item_price * 0.4))
        bough_items += item_new_price
        bough_items_prices.append(item_new_price)
        profit += item_new_price - item_price
    elif item_type == "Accessories" and item_price <= 20.50 and item_price <= budget:
        budget -= item_price
        item_new_price = (item_price + (item_price * 0.4))
        bough_items += item_new_price
        bough_items_prices.append(item_new_price)
        profit += item_new_price - item_price

new_budget = budget + bough_items


for i in bough_items_prices:
    print(f"{i:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
