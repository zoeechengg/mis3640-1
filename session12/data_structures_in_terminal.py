   1: >>> # variable length of arguments
   2: >>> # create a function that multiply all the arguments together
   3:
>>> def multiply(*args):
...     result = 1
...     for arg in args:
...         result *= arg
...     return result
...
   4: >>> multiply(2)
2
   5: >>> multiply(2, 3, 4, 5)
120
   6: >>> multiply([2, 3, 4, 5])
[2, 3, 4, 5]
   7: >>> # try to find out how many unique letters there are in one word
   8: >>> # get all the unique letters from one word
   9: >>> word = 'bookkeeper'
  10: >>> unique_lettes = []
  11:
>>> for letter in word:
...     if letter not in unique_lettes:
...         unique_lettes.append(letter)
...
  12: >>> unique_lettes
['b', 'o', 'k', 'e', 'p', 'r']
  13: >>> set(word)
{'b', 'e', 'k', 'o', 'p', 'r'}
  14: >>> nums = [ 1, 1, 2, 2, 2, 2, 3, 3]
  15: >>> set(nums)
{1, 2, 3}
  16: >>> s = set(nums)
  17: >>> type(s)
set
  18: >>> s.add(4)
  19: >>> s
{1, 2, 3, 4}
  20: >>> s1 = {1, 2, 3}
  21: >>> s2 = {2, 3, 4}
  22: >>> s1 & s2
{2, 3}
  23: >>> s1 | s2 # union
{1, 2, 3, 4}
  24: >>> s1.difference(s2)
{1}
  25: >>> s2.difference(s1)
{4}
  26: >>> # string and list
  27: >>> s = 'Daniel'
  28: >>> s.split()
['Daniel']
  29: >>> list(s)
['D', 'a', 'n', 'i', 'e', 'l']
  30: >>> college = 'Babson College'
  31: >>> college.split()
['Babson', 'College']
  32: >>> words = college.split()
  33: >>> words
['Babson', 'College']
  34: >>> ' '.join(words)
'Babson College'
  35: >>> letters = list(s)
  36: >>> letters
['D', 'a', 'n', 'i', 'e', 'l']
  37: >>> ''.join()
  38: >>> ''.join(letters)
'Daniel'
  39: >>> # list and dict
  40: >>> letters
['D', 'a', 'n', 'i', 'e', 'l']
  41: >>> hist = {}
  42:
>>> for letter in letters:
...     hist[letter] = letters.get(letter, 0) + 1
...
  43:
>>> for letter in letters:
...     hist[letter] = hist.get(letter, 0) + 1
...
  44: >>> hist
{'D': 1, 'a': 1, 'n': 1, 'i': 1, 'e': 1, 'l': 1}
  45: >>> letters
['D', 'a', 'n', 'i', 'e', 'l']
  46: >>> dict(letters)
  47: >>> hist
{'D': 1, 'a': 1, 'n': 1, 'i': 1, 'e': 1, 'l': 1}
  48: >>> hist['D'] = 5
  49: >>> hist
{'D': 5, 'a': 1, 'n': 1, 'i': 1, 'e': 1, 'l': 1}
  50: >>> new_letters = []
  51:
>>> for letter, freq in hist.items():
...     new_letters.extend([letter] * freq)
...
  52: >>> new_letters
['D', 'D', 'D', 'D', 'D', 'a', 'n', 'i', 'e', 'l']
  53: >>> # list and tuple
  54: >>> new_letters
['D', 'D', 'D', 'D', 'D', 'a', 'n', 'i', 'e', 'l']
  55: >>> (new_letters, )
(['D', 'D', 'D', 'D', 'D', 'a', 'n', 'i', 'e', 'l'],)
  56: >>> tuple(new_letters)
('D', 'D', 'D', 'D', 'D', 'a', 'n', 'i', 'e', 'l')
  57: >>> list(tuple(new_letters))
['D', 'D', 'D', 'D', 'D', 'a', 'n', 'i', 'e', 'l']
  58: >>> # list and set
  59: >>> new_letters
['D', 'D', 'D', 'D', 'D', 'a', 'n', 'i', 'e', 'l']
  60: >>> set(new_letters)
{'D', 'a', 'e', 'i', 'l', 'n'}
  61: >>> list(set(new_letters))
['D', 'a', 'n', 'e', 'i', 'l']
  62: >>> # string and set
  63: >>> s
'Daniel'
  64: >>> name = 'Queenie'
  65: >>> set(name)
{'Q', 'e', 'i', 'n', 'u'}
  66: >>> list(set(name))
['n', 'e', 'Q', 'i', 'u']
  67: >>> sorted(list(set(name)))
['Q', 'e', 'i', 'n', 'u']
  68: >>> sorted(set(name))
['Q', 'e', 'i', 'n', 'u']
  69: >>> set(name)
{'Q', 'e', 'i', 'n', 'u'}
  70: >>> hist
{'D': 5, 'a': 1, 'n': 1, 'i': 1, 'e': 1, 'l': 1}
  71: >>> sorted(hist)
['D', 'a', 'e', 'i', 'l', 'n']
  72: >>> sorted(hist.keys())
['D', 'a', 'e', 'i', 'l', 'n']
  73: >>> sorted(hist.values())
[1, 1, 1, 1, 1, 5]
  74: >>> # string and dict
  75: >>> s
'Daniel'
  76: >>> dict(s)
  77: >>> d = {}
  78:
>>> for letter in s:
...     d[letter] = d.get(letter, 0) + 1
...
  79: >>> d
{'D': 1, 'a': 1, 'n': 1, 'i': 1, 'e': 1, 'l': 1}
  80: >>> new_s =''
  81:
>>> for letter, freq in d.items():
...     new_s += letter * freq
...
  82: >>> new_s
'Daniel'
  83: >>> # string and tuple
  84: >>> s
'Daniel'
  85: >>> name
'Queenie'
  86: >>> tuple(name)
('Q', 'u', 'e', 'e', 'n', 'i', 'e')
  87: >>> str(tuple(name))
"('Q', 'u', 'e', 'e', 'n', 'i', 'e')"
  88: >>> ''.join(tuple(name))
'Queenie'
  89: >>> # tuple and set
  90: >>> t = tuple(name)
  91: >>> t
('Q', 'u', 'e', 'e', 'n', 'i', 'e')
  92: >>> set(t)
{'Q', 'e', 'i', 'n', 'u'}
  93: >>> tuple(set(t))
('n', 'e', 'Q', 'i', 'u')
  94: >>> help(set)
  95: >>> # dict and tuple
  96: >>> d
{'D': 1, 'a': 1, 'n': 1, 'i': 1, 'e': 1, 'l': 1}
  97: >>> tuple(d.keys())
('D', 'a', 'n', 'i', 'e', 'l')
  98: >>> tuple(d.values())
(1, 1, 1, 1, 1, 1)
  99: >>> tuple(d.items())
(('D', 1), ('a', 1), ('n', 1), ('i', 1), ('e', 1), ('l', 1))
 100: >>> # dict and set
 101: >>> set(d.keys())
{'D', 'a', 'e', 'i', 'l', 'n'}
 102: >>> set(d.values())
{1}
 103: >>> set(d.items())
{('D', 1), ('a', 1), ('e', 1), ('i', 1), ('l', 1), ('n', 1)}
 104: >>> # string, list and dict
 105: >>> s
'Daniel'
 106: >>> a = [1, 2, 3, 4, 5, 6]
 107: >>> zip(s, a)
<zip at 0x1c56a00e408>
 108:
>>> for i in zip(s, a):
...     print(i)
...
 109: >>> list(zip(s,a))
[('D', 1), ('a', 2), ('n', 3), ('i', 4), ('e', 5), ('l', 6)]
 110: >>> dict(zip(s,a))
{'D': 1, 'a': 2, 'n': 3, 'i': 4, 'e': 5, 'l': 6}
 111: >>> type(zip(s, a))
zip
 112: >>> s
'Daniel'
 113: >>> a = [1, 2, 3, 4]
 114: >>> list(zip(s, a))
[('D', 1), ('a', 2), ('n', 3), ('i', 4)]
