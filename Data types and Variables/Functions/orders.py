def order(product, quantity):
    product_dict = {"coffee": 1.50, "coke": 1.40, "water": 1, "snacks": 2}
    return f'{(product_dict[product] * quantity):.2f}'


product = input()
quantity = int(input())

print(order(product, quantity))

