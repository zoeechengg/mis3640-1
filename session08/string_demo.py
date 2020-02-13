# built-in functions that take string(s) as parameter
# input()
# print()
# int()/float()/bool() 
# type()
# help()
# len()


# team = 'New England Patriots'
# letter = team[1]
# print(letter) 
# print(team[0])

# # print(team[1.5]) 

# print(len(team))
# print(team[19])
# print(team[-2]) 

# for whatever in team:
#     print(whatever)


# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     # if letter == 'O' or letter == 'Q':
#     if letter in 'OQ':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix) 


team = 'New England Patriots'
print(team[:11])
print(team[11:])
print(team[4:3])

print(team[:]) 

print(team[::2])
print(team[::-1]) 
print(team[::-2])



team = 'New England Patriots'
# team[12:20] ='Seahawks'

new_team = team[:12] + 'Seahawks'
print(new_team)
print(team)



def find(word, letter):
    for i, c in enumerate(word):
        if c == letter:
            return i
    return -1

print(find(team, 'E'))
print(find(team, 'z'))

