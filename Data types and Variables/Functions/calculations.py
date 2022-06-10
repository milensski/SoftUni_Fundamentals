import operator

operation = input()
a = int(input())
b = int(input())


def calc(a, b, operation):
    operations_dict = {"multiply": operator.mul(a, b), "divide": operator.truediv(a, b), "add": operator.add(a, b),
                       "subtract": operator.sub(a, b)}
    return int(operations_dict[operation])


print(calc(a, b, operation))
