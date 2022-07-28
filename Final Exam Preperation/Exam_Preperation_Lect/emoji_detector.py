def emoji_threshold(emoji):
    threshold = 0
    for char in emoji:
        if char.isalpha():
            threshold += ord(char)
    return threshold


import re

text = input()

digit_pattern = r'\d'
words_pattern = r'\:{2}([A-Z][a-z]{2,})\:{2}|\*{2}([A-Z][a-z]{2,})\*{2}'
emojis = []

result = re.findall(digit_pattern, text)
cool_threshold = 1

for digit in result:
    cool_threshold *= int(digit)

result = re.finditer(words_pattern, text)
for match in result:
    emojis.append(match.group())
print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
[print(emoji) for emoji in emojis if emoji_threshold(emoji) >= cool_threshold]
