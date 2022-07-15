first, second = input().split()
i = 0
result = 0
count = 0

while i < len(first) and i < len(second):
    result += ord(first[i]) * ord(second[i])
    i += 1

if len(first) >= len(second):
    count = len(first) - len(second)

    while i < len(first):
        result += ord(first[i])
        i += 1



else:
    count = len(second) - len(first)


    while i < len(second):
        result += ord(second[i])
        i += 1

print(result)
