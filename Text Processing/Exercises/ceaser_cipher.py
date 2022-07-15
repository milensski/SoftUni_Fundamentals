password = input()

new_password = ''

for char in password:
    new_char = ord(char)+3
    new_password += chr(new_char)

print(new_password)