import re


n = int(input())

pattern = r'^(.+)\>([0-9]+)\|([a-z]+)\|([A-Z]+)\|([^\<\>]+)\<(\1)$'

for _ in range(n):

    password = input()

    result = re.search(pattern,password)

    if result:

        password = result.group(2)+result.group(3)+result.group(4)+result.group(5)
        print(f'Password: {password}')

    else:
        print('Try another password!')