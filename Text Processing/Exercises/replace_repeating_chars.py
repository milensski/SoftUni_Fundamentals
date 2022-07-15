text = input()

modified = ''
last_char = ''

for i in range(len(text)):
    count = 0
    current_char = text[i]


    if current_char == last_char:
        continue

    modified += current_char
    last_char = current_char

print(modified)