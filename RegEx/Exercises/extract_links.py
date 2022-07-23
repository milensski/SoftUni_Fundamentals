import re


search_pattern = r'(www)\.([A-Za-z][A-Za-z0-9-]+)(\.[a-z]+)+'


while True:

    text = input()

    if not text:
        break

    result = re.finditer(search_pattern,text)


    for match in result:
        print(match.group())