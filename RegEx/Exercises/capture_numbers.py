import re

search_pattern = r'(\d+)'

while True:

    text = input()

    if not text:
        break

    result = re.findall(search_pattern, text)

    if len(result) > 0:
        print(' '.join(result), end=' ')
