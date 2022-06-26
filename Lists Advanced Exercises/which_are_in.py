first_string = input().split(", ")
second_string = input().split(", ")

lst = []

for word in first_string:
    for second_word in second_string:
        if word in second_word and not word in lst:
            lst.append(word)

print(lst)
