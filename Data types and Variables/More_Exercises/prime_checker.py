number = int(input())

is_prime = True
count = 0
if number == 0 or number == 1:
    is_prime = False
    print(is_prime)
else:
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            count += 1
    if count > 1:
        is_prime = False
        print(is_prime)
        exit()
    else:
        is_prime = True
        print(is_prime)
        exit()