'''
1. read the file, save the words into a list
2. (option 2) sort the word
'rumeer' -> 'eemrru' (signature of the word)
'reemur' -> 'eemrru' (signature of the word)
'kenzi' ->  'ekinz' (signature of the word)

create empty list for each signature

{signature: [words that have the same signature]} 
e.g.
{'eemrru' :['rumeer', 'reemur'], 'ekinz' : ['kenzi']}

3. get the values from the dict, probably only the lists with more than one word

expected: 
['rumeer', 'reemur']
['kenzi'], 
['retainers', 'ternaries']


4. create another dictionary, to store the data like
{2: [['rumeer', 'reemur'], ['retainers', 'ternaries']], 1: [['kenzi']]}

'''


def read_file_to_list(path_to_file):
    """
    reads all the words from the file,
    returns a list of words
    """


def list_to_dict(words):
    """
    words: a list of all the words

    returns a dictionary, the dictionary looks like
    {'eemrru' :['rumeer', 'reemur'], 'ekinz' : ['kenzi']}
    """


def print_anagrams(word_dict, n_words_in_anagram = 1):
    """
    prints all the anagrams with more than n words
    """


def create_another_dict(old_dict):
    """
    creates a new dict, key is number of words in the anagram list,
    value is a list of anagram lists
    {2: [['rumeer', 'reemur'], ['retainers', 'ternaries']], 1: [['kenzi']]}

    returns the new dict
    """

def prints_anagrams_by_number(words_dict):
    """
    prints the longest list of anagrams first, followed by the second longest, and so on
    """



def main():
    word_list = read_file_to_list('session09/words.txt')
    word_dict = list_to_dict(word_list)
    # ex-2
    print_anagrams(word_dict) 


if __name__ == "__main__":
    main()