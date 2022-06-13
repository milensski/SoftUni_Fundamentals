def is_palindrome(numbers):
    if numbers == numbers[::-1]:
        return True
    else:
        return False


numbers = input().split(", ")

for number in numbers:
    print(is_palindrome(number))
