word = "103o"
string_digits = []
for char in word:
    if char.isdigit():
        string_digits.append(int(char))

digit = "".join(list(map(str,string_digits)))

print(chr(int(digit)))