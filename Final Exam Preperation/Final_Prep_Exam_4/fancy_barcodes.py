import re

n = int(input())
pattern = '\@\#+([A-Z][A-Za-z0-9]{4,}[A-Z])\@\#+'

for _ in range(n):

    barcode = input()

    result = re.search(pattern,barcode)

    if result:
        digits = ''

        for char in result.group(1):
            if char.isdigit():
                digits += char
        if not digits:
            digits = '00'
        print(f'Product group: {digits}')

    else:
        print('Invalid barcode')


