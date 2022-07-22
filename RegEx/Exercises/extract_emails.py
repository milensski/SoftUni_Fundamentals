import re

user_pattern = r'( |^)[A-Za-z0-9]+((\.|\-|\_)[A-Za-z0-9]+)*'
host_pattern = r'[a-zA-Z]+(-([a-zA-z]+))*(\.[a-zA-Z]+(-([a-zA-z]+)\.[a-zA-Z]+)*)+'

search_pattern = fr'{user_pattern}@{host_pattern}'


text = input()

result = re.finditer(search_pattern,text)

for match in result:
    print(match.group())