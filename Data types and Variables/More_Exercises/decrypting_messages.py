key = int(input())

n = int(input())

value = ""
decrypted_message = ""

for i in range(n):
    value = input()
    decrypted_message += chr(ord(value) + key)

print(decrypted_message)