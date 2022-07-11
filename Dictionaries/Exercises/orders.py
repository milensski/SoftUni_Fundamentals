products = {}

while True:
    command = input()

    if command == "buy":
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name in products:
        products[name] = [price, quantity + products[name][1]]
    else:

        products[name] = [price, quantity]

for element in products:
    total_sum = products[element][0] * products[element][1]
    print(f"{element} -> {total_sum:.2f}")
