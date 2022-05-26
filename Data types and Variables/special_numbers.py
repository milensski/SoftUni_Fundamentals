n = int(input())

for i in range(1, n+1):
    first_digit = i // 10
    second_digit = i % 10
    sum_of_digits = first_digit + second_digit
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")

