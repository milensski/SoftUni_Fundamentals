n = int(input())
opening_bracket = 0
for i in range(n):
    curr_char = input()
    if curr_char == '(':
        opening_bracket += 1
        if opening_bracket == 2:
            print("UNBALANCED")
            exit()
    if curr_char == ')':
        opening_bracket -= 1
        if opening_bracket < 0:
            print("UNBALANCED")
            exit()
print("BALANCED")