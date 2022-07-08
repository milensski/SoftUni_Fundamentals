list_characters = input().split(", ")
char_dict = {}
char_dict = {list_characters[i]: ord(list_characters[i]) for i in range(0,len(list_characters))}

print(char_dict)