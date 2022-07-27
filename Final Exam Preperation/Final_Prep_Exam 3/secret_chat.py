def insert_space(index, secret_text):
    secret_text = secret_text[:index] + ' ' + secret_text[index::]

    return secret_text


def reverse(substring, secret_text):
    if substring in secret_text:
        secret_text = secret_text.replace(substring, '', 1)
        secret_text = secret_text + substring[-1::-1]
        print(secret_text)
        return secret_text

    print('error')
    return secret_text


def change_all(substring, replacement, secret_text):
    secret_text = secret_text.replace(substring, replacement)
    return secret_text


secret_text = input()

while True:

    command = input()

    if command == 'Reveal':
        break

    command = command.split(':|:')

    if command[0] == 'InsertSpace':
        index = int(command[1])

        secret_text = insert_space(index, secret_text)
        print(secret_text)

    elif command[0] == 'Reverse':

        substring = command[1]
        secret_text = reverse(substring, secret_text)


    elif command[0] == 'ChangeAll':

        substring = command[1]
        replacement = command[2]

        secret_text = change_all(substring, replacement, secret_text)
        print(secret_text)

print(f'You have a new text message: {secret_text}')
