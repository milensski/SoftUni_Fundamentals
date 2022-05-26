n = int(input())
banned = [",", ".", "_"]

for i in range(n):
    word = input()
    if any(c in banned for c in word):
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")