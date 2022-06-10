def sum_odd_even_digits(num):
    sum_even = 0
    sum_odd = 0
    for digit in num:
        digit = int(digit)
        if digit % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    return sum_even, sum_odd


numbers = input()

print(f"Odd sum = {sum_odd_even_digits(numbers)[1]}, Even sum = {sum_odd_even_digits(numbers)[0]}")
