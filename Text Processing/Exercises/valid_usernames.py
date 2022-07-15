import re


def is_lenght_valid(user):
    if 3 <= len(user) <= 16:
        return True
    return False


def is_valid(user):
    for char in user:
        if not char.isalnum() and "-" not in char and "_" not in char:
            return False
    return True




username = input().split(", ")


for user in username:
    if is_lenght_valid(user) and is_valid(user):
        print(user)

