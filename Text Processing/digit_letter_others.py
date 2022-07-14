def filter_digits(text):
    return [''.join(ch) for ch in text if ch.isdigit()]

def filter_letters(text):
    return [''.join(ch) for ch in text if ch.isalpha()]

def filter_signs(text):
    return [''.join(ch) for ch in text if not ch.isalnum()]


text = input()

print(*filter_digits(text),sep="")
print(*filter_letters(text),sep="")
print(*filter_signs(text),sep="")
