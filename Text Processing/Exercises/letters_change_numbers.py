import string

alphabet = string.ascii_uppercase
alpha_dict = {}

i = 1

for letter in alphabet:
    alpha_dict[letter] = i
    i += 1


def alphabet_number(char, alpha_dict):
    char = char.upper()

    return alpha_dict[char]


text = input().split()
total_sum = 0

for word in text:
    num_from_word = ''

    for char in word:
        if char.isdigit():
            num_from_word += char

    num_from_word = int(num_from_word)

    if word[0].isupper():
        num_from_word /= alphabet_number(word[0], alpha_dict)
    else:
        num_from_word *= alphabet_number(word[0], alpha_dict)

    if word[-1].isupper():
        num_from_word -= alphabet_number(word[-1], alpha_dict)
    else:
        num_from_word += alphabet_number(word[-1], alpha_dict)

    total_sum += num_from_word

print(f"{total_sum:.2f}")

