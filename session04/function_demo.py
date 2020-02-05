def print_lyrics():
    print("Hey Jude. Don't make it bad.")
    print("Take a sad song and make it better.")


# print_lyrics()
# print(type(print_lyrics))

def repeat_lyrics():
    print_lyrics()
    print('Na - na - na - na - na, na - na - na - na')
    print_lyrics()


# repeat_lyrics()


def print_twice(w):
    print(w)
    print(w)


# print_twice('Babson')

# my_name = 'Andrew'
# print_twice(my_name)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)


# cat_twice('Babson', 'College')

# print(cat) 

# cat_twice(1, 2) 
# cat_twice('1', '2') 
# cat_twcie(1, '2')


def give_me_a_break():
    str1 = 'break'
    return str1


# give_me_a_break()
# print(give_me_a_break())

# print_twice(give_me_a_break()) 

def give_me_two_breaks():
    str1 = 'break'
    return str1
    print('another break')


print(give_me_two_breaks())
