crypted_message = input().split()
decipher_message = []
for word in crypted_message:
    new_char = ""
    for char in word:
        if char.isdigit():
            new_char += char


    word = word.replace(new_char,"")

    if len(word) >= 2:
        word = word[-1] + word[1:-1] + word[0]

    new_word = chr(int(new_char)) + word

    decipher_message.append(new_word)

print(*decipher_message, sep=' ')