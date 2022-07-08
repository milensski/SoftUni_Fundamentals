line_products = input().split(" ")

searched_products = input().split()

product_dict = {line_products[i]: line_products[i + 1] for i in range(0, len(line_products), 2)}

for element in searched_products:
    if element in product_dict:
        print(f'We have {product_dict[element]} of {element} left')
    else:
        print(f'Sorry, we don\'t have {element}')
