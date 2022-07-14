def filter_substring(first, second):
    while first in second:
        second = second.replace(first, "")

    return second


print(filter_substring(input(), input()))
