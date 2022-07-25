

def valid_index(index,text):
    if 0 <= index and index < len(text):
        return True
    return False


def add(index, word, text):

    if valid_index(index,text):
        text = text[0:index] + word + text[index::]
        print(text)
        return text
    print(text)
    return text


def remove(start_index, end_index, text):
    if valid_index(start_index,text) and valid_index(end_index,text):
        text = text[:start_index] + text[end_index+1:]
        print(text)
        return text
    print(text)
    return text

def switch(old_string, new_string, text):
    if old_string in text:
        text = text.replace(old_string,new_string)
        print(text)
        return text
    print(text)
    return text

text = input()


while True:
    command = input()

    if command == 'Travel':
        break

    command = command.split(':')

    if 'Add Stop' in command:

        index = int(command[1])
        word = command[2]

        text = add(index,word,text)

    elif 'Remove Stop' in command:

        start_index = int(command[1])
        end_index = int(command[2])

        text = remove(start_index,end_index,text)

    elif 'Switch' in command:

        old_string = command[1]
        new_string = command[2]

        text = switch(old_string,new_string,text)


print(f'Ready for world tour! Planned stops: {text}')