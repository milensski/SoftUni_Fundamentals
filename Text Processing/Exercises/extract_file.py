
file_path = input()
file_name = ""
file_extension = ""

root = file_path.split("\\")

for name in root:
    if "." in name:
        name = name.split(".")

        file_extension = name[1]
        file_name = name[0]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")