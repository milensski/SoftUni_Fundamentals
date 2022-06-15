def perfect_number(value):

    divisible_nums = []
    for i in range(1, (value // 2) + 1):
        if value % i == 0:
            divisible_nums.append(i)
    if sum(divisible_nums) == value:
        return True
    else:
        return False


number = int(input())

if number > 0 and perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
