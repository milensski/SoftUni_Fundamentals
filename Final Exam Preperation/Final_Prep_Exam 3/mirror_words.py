import re


def mirror_words(word, second_word):
    if word == second_word[-1::-1]:
        return True
    return False


pattern = r'([\#|\@])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

text = input()

result = re.findall(pattern, text)
count = 0
mirrors = []
for match in result:

    if match:
        word = match[1]
        second_word = match[2]
        if mirror_words(word, second_word):
            mirrors.append(word + " <=> " + second_word)

        count += 1

if count > 0:

    print(f'{count} word pairs found!')

else:

    print('No word pairs found!')

if len(mirrors) > 0:

    print('The mirror words are:')
    print(*mirrors, sep=', ')
else:

    print('No mirror words!')
