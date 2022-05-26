divisor = int(input())
boundary = int(input())

for i in range(boundary, divisor, -1):
    if i % divisor == 0:
        print(i)
        break