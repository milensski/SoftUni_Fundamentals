def add_and_subtract(a, b, c):
    def sum_numbers(a, b):
        result = a + b
        return result

    def subtract(c):
        return sum_numbers(a, b) - c

    return subtract(c)


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))
