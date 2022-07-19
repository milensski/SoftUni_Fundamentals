message = input()


def move(number_of_letters, message):

    message = message[number_of_letters:] + message[:number_of_letters]

    return message


def insert(index, letter, message):

    to_list = []
    [to_list.append(char) for char in message]

    to_list.insert(index,letter)

    message = "".join(to_list)


    return message


def changeall(substring, replace_letter, message):

    while substring in message:
        message = message.replace(substring,replace_letter)

    return message


while True:

    command = input()

    if "Decode" in command:
        break

    if "Move" in command:
        action, number_of_letters = command.split("|")
        number_of_letters = int(number_of_letters)
        message = (move(number_of_letters, message))
    elif "Insert" in command:
        action, index, letter = command.split("|")
        index = int(index)
        message = (insert(index, letter, message))
    elif "ChangeAll" in command:
        action, substring, replace_letter = command.split("|")
        message = (changeall(substring,replace_letter,message))

print(f"The decrypted message is: {message}")
