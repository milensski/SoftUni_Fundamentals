import re

search_pattern = r'(?<=\_)\w+'


text = input()

result = re.findall(search_pattern,text)

for match in result:
    print(match.group(),end=",")