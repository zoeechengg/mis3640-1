# age = int(input('What is your age? >> '))

# if age >= 12:
#     print(f'Your age is {age}.')
#     print('You are a teenager.')
# elif age >= 18:
#     print(f'You are an adult.')
# else:
#     print('Kid!')

x = 1
y = 2

# if x == y:
#     print("x and y are equal.")
# else:
#     if x < y:
#         print("x is less than y.")
#     else:
#         print("x is greater than y")

# if x == y:
#     print("x and y are equal.")
# elif x < y:
#     print("x is less than y.")
# else:
#     print("x is greater than y")


def BMI_calculate(weight, height):
    """
    calculates BMI based on weight (lb) and height (inch) and prints the category.
    """
    bmi = 703 * weight / (height * height)
    if bmi <= 18.5:
        print("You are underwight")
    elif 18.5 < bmi < 25:
        print("Your weight is normal.")


# BMI_calculate(311, 89)
# expected: "You are underweighted."


def compare(a, b):
    if isinstance(a, str) or isinstance(b, str):
        print("String involved")
    else:
        if a > b:
            print("bigger")
        elif a == b:
            print("equal")
        else:
            print("smaller")


# compare("1", 2)
# compare(1, 2)
# compare(1, 1)


def diff21(n):
    """
    Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
    """
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2


# print(diff21(19))
# # 2
# print(diff21(21))
# # 0
# print(diff21(23))
# # 4


def cigar_party(cigars, is_weekend):
    """    
    When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
    """
    if is_weekend and cigars >= 40:
        return True
    else:
        if 40 <= cigars <= 60:
            return True
        else:
            return False


# print(cigar_party(30, False))
# # False
# print(cigar_party(50, False))
# # True
# print(cigar_party(70, False))
# # False
# print(cigar_party(70, True))
# # True
# print(cigar_party(30, True))
# # False


def countdown(n):
    import time

    # time.sleep(.1)

    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)


# countdown(5)


def fibonacci(n):
    """
    return the nth fibonacci number
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(1))
# 1
print(fibonacci(2))
# 1
print(fibonacci(3))
# 2
# ...
print(fibonacci(10))
# fibonacci(8) + fibonacci(9)
print(fibonacci(11))
# fibonacci(9) + fibonacci(10)
