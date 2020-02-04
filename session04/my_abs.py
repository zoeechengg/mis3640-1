def my_abs(number):
    """
    number: an integer or a floating number
    return the absolute value of a number
    """
    if isinstance(number, (int, float)) :
        if number >= 0:
            return number
        else:
            return -number
    else:
        return 'I don\'t know'

# my_abs(10)
# my_abs(-10)
# my_abs(0)
print(my_abs(-4.2))
print(my_abs(10))
print(my_abs('-1'))