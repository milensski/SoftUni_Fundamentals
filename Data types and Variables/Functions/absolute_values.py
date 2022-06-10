values_input = list(map(str, input().split()))


def absolute_value(values):
    result = [float(value) for value in values]
    return result


print([abs(values) for values in list(absolute_value(values_input))])

