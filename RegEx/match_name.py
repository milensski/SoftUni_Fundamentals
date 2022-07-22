import re

text = input()

search_pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

result = re.findall(search_pattern,text)

for match in result:
    print(match,end= " ")