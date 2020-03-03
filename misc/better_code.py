# 1
def f():
    if two_adjacent(word): 
        if xyx_substring(word):
            return True
    else:
        return False


# better code
def f(word):
    if two_adjacent(word) and xyx_substring(word):
        return True
    else:
        return False

# better better code
def f(word):
    return two_adjacent(word) and xyx_substring(word)



# 2
a = int(10)

# better code

a = 10







# 3
word[i] + word[i+1] 

# better code
word[i:i+2] 








# 4
if (a + b) > 4:
    pass

if isinstance(number, int) == True:
    pass 


# better code
if a + b > 4:
    pass

if isinstance(number, int):
    pass 



# 5
def not_allowed(word): #function will return true if the word does not contain the letter pairs 'ab', 'cd', or 'xy'
    pass


# better code
def not_allowed(word): 
    """
    returns True if the word does not contain the letter pairs 'ab', 'cd', or 'xy'
    """
    pass









# 6
def adjacent(word):
    count = 0 
    for i in range(len(word)-1):
        if word[i] == word[i+1]: 
            return True


# better code

def adjacent(word):
    count = 0 
    for i in range(len(word)-1):
        if word[i] == word[i+1]: 
            return True
    
    return False








# 7

if(char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or
                    char.lower() == "o" or char.lower() == "u"):


# better code
if char.lower() in ['a', 'e', 'i', 'o', 'u']:

# or 

if char.lower() in 'aeiou':

# char -> 'ae' 