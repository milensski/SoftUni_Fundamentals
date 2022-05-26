orders = int(input())

current_order = 0
total_orders = 0

for order in range(orders):
    price_per_capsule = float(input())  # [0.01...100.00]
    days = int(input())  # range [1..31]
    capsules_per_day = int(input())  # range [1...2000]


    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    else:
        current_order = price_per_capsule * days * capsules_per_day
        print(f"The price for the coffee is: ${current_order:.2f}")
        total_orders += current_order

print(f"Total: ${total_orders:.2f}")