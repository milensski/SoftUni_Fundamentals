start_char = int(input())
final_char = int(input())

for i in range(start_char, final_char + 1):
    print(f"{chr(i)}", end=" ")

