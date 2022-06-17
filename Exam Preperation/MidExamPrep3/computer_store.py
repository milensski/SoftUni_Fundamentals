price = 0
while True:
    command = input()

    if command == "special" or command == "regular":
        break

    if float(command) < 0:
        print("Invalid price!")
        continue
    else:
        price += float(command)


taxes = price * 0.2
total_price = price + taxes

if command == "special":
    total_price = total_price - total_price*0.1
else:
    total_price = price + taxes

if price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price:.2f}$")
    print(f"Taxes: {(price * 0.2):.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")

