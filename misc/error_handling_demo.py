# try:
#     number = int(input('Please enter a number:'))
#     result = 2019 / number
#     print(result)
#     name = 'Babson'
#     print(name[number])
# except ZeroDivisionError as e:
#     print('Something is wrong:', e)
# except ValueError as e:
#     print(e)
# except IndexError as e:
#     print('Index Error:', e)
# else:
#     print('This is in else.')
# finally:
#     print('This is finally')

# print('After something is wrong, we still can get here!')


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()


name_dict = {"John": 90, "Paul": 80, "George": 85}
try:
    print(reverse_lookup(d=name_dict, v=100))
except LookupError as e:
    print('There is no such value.')
