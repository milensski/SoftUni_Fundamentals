from collections import defaultdict
n = int(input())

synonyms = defaultdict(list)

for _ in range(n):
    key = input()
    value = input()

    synonyms[key].append(value)


[print(f'{word} - {", ".join(synonym)}') for word,synonym in synonyms.items()]