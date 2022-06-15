def grade_to_word(value):

    result = ''
    if 2 <= value < 3:
        result = "Fail"
    elif 3 <= value < 3.50:
        result = "Poor"
    elif 3.50 <= value < 4.50:
        result = "Good"
    elif 4.50 <= value < 5.50:
        result = "Very Good"
    elif 5.50 <= value <= 6:
        result = "Excellent"
    return result


grade = float(input())


print(grade_to_word(grade))

