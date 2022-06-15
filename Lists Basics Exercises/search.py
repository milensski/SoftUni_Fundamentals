n = int(input())
key_word = input()

lst_of_strings = []
filtered_list = []

for _ in range(n):
    some_string = input()
    lst_of_strings.append(some_string)

print(lst_of_strings)

for i in range(len(lst_of_strings)):
    if key_word in lst_of_strings[i]:
        filtered_list.append(lst_of_strings[i])

print(filtered_list)
