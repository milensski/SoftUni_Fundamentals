import re

text = input()

search_pattern = fr'\b{input()}\b'

result = re.findall(search_pattern, text, re.IGNORECASE)

print(len(result))
