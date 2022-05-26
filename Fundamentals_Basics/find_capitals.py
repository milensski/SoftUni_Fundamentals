text = input()
res = []

for index, char in enumerate(text):
    if char.isupper():
        res.append(index)

print(res)