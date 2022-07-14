def repeat_string(words):

    return ["".join(word*len(word)) for word in words ]




words = input(). split()

print(*repeat_string(words),sep="")