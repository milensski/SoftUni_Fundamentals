def is_letters_digits(value):
    if str.isalnum(value):
        return True
    else:
        return False


def pass_length(value):
    if 6 <= len(value) <= 10:
        return True
    else:
        return False


def is_two_digits(value):
    count = 0
    for element in value:
        if element.isdigit():
            count += 1

    if count > 1:
        return True
    else:
        return False


def run(value):
    if is_letters_digits(value) and pass_length(value) and is_two_digits(value):
        print("Password is valid")
    else:
        if is_letters_digits(value) is False:
            print("Password must consist only of letters and digits")
        if pass_length(value) is False:
            print("Password must be between 6 and 10 characters")
        if is_two_digits(value) is False:
            print("Password must have at least 2 digits")


password = input()
run(password)
