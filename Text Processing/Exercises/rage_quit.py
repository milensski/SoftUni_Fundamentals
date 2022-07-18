message = input()

symbols = {}

current_symbols = ''
n = ''

unique_symbols = set()

for i in range(len(message)):

    if message[i].isdigit():
        n += message[i]
        if i + 1 < len(message):
            if message[i + 1].isdigit():
                continue

        if current_symbols not in symbols:
            symbols[current_symbols] = int(n)
        else:
            symbols[current_symbols] += int(n)


        current_symbols = ''

        n = ''

    else:
        current_symbols += message[i]
        unique_symbols.add(message[i].lower())

print(f"Unique symbols used: {len(unique_symbols)}")

for symbol, number in symbols.items():
    if number == 0:
        continue
    print(symbol.upper() * number, end='')
