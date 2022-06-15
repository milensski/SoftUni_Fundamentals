def factorial(a):
    if a == 1:
        return a
    else:
        return a * factorial(a-1)


number_a = int(input())
number_b = int(input())

result = factorial(number_a)/factorial(number_b)

print(f"{result:.2f}")

