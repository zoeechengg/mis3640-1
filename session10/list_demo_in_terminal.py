   1: >>> name = 'Andrew'
   2: >>> name[-2]
'e'
   3: >>> name[-2] = 'a'
   4: >>> a = []
   5: >>> type(a)
list
   6: >>> len(a)
0
   7: >>> a = list()
   8: >>> type(a)
list
   9: >>> a = [10, 20, 30, 40]
  10: >>> len(a)
4
  11: >>> b = ['spam', 2.0, 5, [10, 20]]
  12: >>> len(b)
4
  13: >>> b[0]
'spam'
  14: >>> b[4]
  15: >>> b[3]
[10, 20]
  16: >>> b[-1]
[10, 20]
  17: >>> len(b[3])
2
  18: >>> c = [10, 20]
  19: >>> c[1]
20
  20: >>> b
['spam', 2.0, 5, [10, 20]]
  21: >>> b[3][1]
20
  22:
>>> AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
... numbers = [42, 123]
... empty = []
... print(AFC_east, numbers, empty)
...
  23: >>> AFC_east
['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
  24: >>> AFC_east[3]
'New York Jets'
  25: >>> AFC_east[3] = 'New York Giants'
  26: >>> AFC_east
['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Giants']
  27: >>> b
['spam', 2.0, 5, [10, 20]]
  28: >>> b[3][1] = 30
  29: >>> b
['spam', 2.0, 5, [10, 30]]
  30: >>> b[3] = [10, 40]
  31: >>> b
['spam', 2.0, 5, [10, 40]]
  32: >>> b[0] = 'span'
  33: >>> b
['span', 2.0, 5, [10, 40]]
  34: >>> b[0][-1] = 'm'
  35: >>> b
['span', 2.0, 5, [10, 40]]
  36: >>> b[1+2]
[10, 40]
  37: >>> name
'Andrew'
  38: >>> 'e' in name
True
  39: >>> 'E' in name
False
  40: >>> 'New York Jets' in AFC_east
False
  41: >>> AFC_east
['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Giants']
  42: >>> 'New England' in AFC_east
False
  43:
>>> L = [
...     ['Apple', 'Google', 'Microsoft'],
...     ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
...     ['Adam', 'Bart', 'Lisa']    
... ]
...
  44: >>> L[0][0]
'Apple'
  45: >>> L[-1]
['Adam', 'Bart', 'Lisa']
  46: >>> L[-1][2]
'Lisa'
  47: >>> L[-1][-1]
'Lisa'
  48: >>> len(L)
3
  49: >>> L[2]
['Adam', 'Bart', 'Lisa']
  50: >>> L[2][2]
'Lisa'
  51: >>> L[1][2][1]
'On Rail'
  52: >>> L[1][2][0]
'Ruby'
  53: >>> L[len(L)][len(L[len(L)])]
  54: >>> L[len(L)-1][len(L[len(L)-1])-1]
'Lisa'
  55: >>> z = 'On Rail'
  56: >>> z[2]
' '
  57: >>> L[1][2][1][2]
' '
  58: >>> L[1][2][1]
'On Rail'
  59: >>> type(L[1][2][1])
str
  60: >>> type(L[1][2])
list
  61: >>> z
'On Rail'
  62: >>> z[2:3]
' '
  63: >>> name
'Andrew'
  64:
>>> for whatever in name:
...     print(whatever)
...
  65: >>> AFC_east
['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Giants']
  66:
>>> for whatever in AFC_east:
...     print(whatever)
...
  67:
>>> for letter in name:
...     print(letter)
...
  68:
>>> for team in AFC_east:
...     print(team)
...
  69:
>>> for team in AFC_east:
...     for letter in team:
...         print(letter)
...     print()
...
  70: >>> numbers = [2020, 2, 25, 3, 44]
  71:
>>> for i in range(len(numbers)):
...     print(i)
...
  72:
>>> for i in range(len(numbers)):
...     numbers[i] = numbers[i] * 2
...
  73: >>> numbers
[4040, 4, 50, 6, 88]
  74:
>>> for i in range(len(numbers)):
...     print(numbers[i])
...
  75:
>>> for number in numbers:
...     print(number)
...
  76:
>>> for number in numbers:
...     number = number / 2
...
  77: >>> numbers
[4040, 4, 50, 6, 88]
  78: >>> numbers/2
  79:
>>> for number in numbers:
...     print(number) 
...     numbers[number] = number / 2
...
  80: >>> numbers_2 = numbers[:]
  81: >>> numbers-2
  82: >>> numbers_2
[4040, 4, 50, 6, 88]
  83: >>> numbers
[4040, 4, 50, 6, 88]
  84: >>> numbers_2 == numbers
True
  85: >>> numbers_2 is numbers
False
  86:
>>> for i, number in enumerate(numbers):
...     print(i, number)
...
  87:
>>> for i, number in enumerate(numbers):
...     numbers_2[i] = number / 2
...
  88: >>> numbers
[4040, 4, 50, 6, 88]
  89: >>> numbers_2
[2020.0, 2.0, 25.0, 3.0, 44.0]
  90: >>> help(enumerate)
  91:
>>> for i, letter in name:
...     print(i, letter)
...
  92:
>>> for i, letter in enumerate(name):
...     print(i, letter)
...
  93: >>> b
['span', 2.0, 5, [10, 40]]
  94: >>> AFC_east
['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Giants']
  95: >>> b[2] = AFC_east
  96: >>> b
['span',
 2.0,
 ['New England Patriots',
  'Buffalo Bills',
  'Miami Dolphins',
  'New York Giants'],
 [10, 40]]
  97: >>> len(b)
4
  98: >>> a = [1, 2, 3]
  99: >>> b = [4, 5, 6]
 100: >>> c = a + b
 101: >>> c
[1, 2, 3, 4, 5, 6]
 102: >>> last_name = ' Fu'
 103: >>> name + last_name
'Andrew Fu'
 104: >>> a * 4
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
 105: >>> name * 4
'AndrewAndrewAndrewAndrew'
 106: >>> import numpy as np
 107: >>> d =[]
 108:
>>> for i, number in enumerate(a):
...     d.append(number + b[i])
...
 109: >>> d
[5, 7, 9]
 110: >>> array_a = np.array(a)
 111: >>> array_a
array([1, 2, 3])
 112: >>> array_b = np.array(b)
 113: >>> array_c =  array_a + array_b
 114: >>> array_c
array([5, 7, 9])
 115: >>> array_a * 3
array([3, 6, 9])
 116: >>> print(array_a)
 117: >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
 118: >>> t[1:1+2]
['b', 'c']
 119: >>> t[1:3]
['b', 'c']
 120: >>> t[0:3]
['a', 'b', 'c']
 121: >>> t[0:4]
['a', 'b', 'c', 'd']
 122: >>> t[:4]
['a', 'b', 'c', 'd']
 123: >>> t[4:]
['e', 'f']
 124: >>> t[3:]
['d', 'e', 'f']
 125: >>> t[-3:]
['d', 'e', 'f']
 126: >>> t[:]
['a', 'b', 'c', 'd', 'e', 'f']
 127: >>> t[ : :2]
['a', 'c', 'e']
 128: >>> t[ : : -1]
['f', 'e', 'd', 'c', 'b', 'a']
 129: >>> t[ : : -2]
['f', 'd', 'b']
 130: >>> t
['a', 'b', 'c', 'd', 'e', 'f']
 131: >>> t[1:3] = ['Daniel', 'Sean']
 132: >>> t
['a', 'Daniel', 'Sean', 'd', 'e', 'f']
 133: >>> t[1:3] = ['Rumeer', 'Kenzi', 'Zoe']
 134: >>> t
['a', 'Rumeer', 'Kenzi', 'Zoe', 'd', 'e', 'f']
 135: >>> t[1:3] = 'Catherine'
 136: >>> t
['a', 'C', 'a', 't', 'h', 'e', 'r', 'i', 'n', 'e', 'Zoe', 'd', 'e', 'f']
 137: >>> list('Catherine')
['C', 'a', 't', 'h', 'e', 'r', 'i', 'n', 'e']
 138: >>> type(t[1:3])
list
 139: >>> type(t[1])
str
 140: >>> a
[1, 2, 3]
 141: >>> a.append(4)
 142: >>> a
[1, 2, 3, 4]
 143:
>>> names = ['Ivy',
...                 'Lucas',
...                 'Ray',
...                 'Nathan',
...                 'Rumeer']
...
 144: >>> ladies = ['Angela', 'Queenie', 'Zoe']
 145: >>> gentlemen = ['Sean', 'Chris', 'Takaki']
 146: >>> names.append('Eli')
 147: >>> names
['Ivy', 'Lucas', 'Ray', 'Nathan', 'Rumeer', 'Eli']
 148: >>> names.extend(ladies)
 149: >>> names
['Ivy', 'Lucas', 'Ray', 'Nathan', 'Rumeer', 'Eli', 'Angela', 'Queenie', 'Zoe']
 150:
>>> names = ['Ivy',
...                 'Lucas',
...                 'Ray',
...                 'Nathan',
...                 'Rumeer']
...
 151: >>> names.append(ladies)
 152: >>> names
['Ivy', 'Lucas', 'Ray', 'Nathan', 'Rumeer', ['Angela', 'Queenie', 'Zoe']]
 153:
>>> names = ['Ivy',
...                 'Lucas',
...                 'Ray',
...                 'Nathan',
...                 'Rumeer']
...
 154: >>> names.reverse()
 155: >>> names
['Rumeer', 'Nathan', 'Ray', 'Lucas', 'Ivy']
 156: >>> names.sort()
 157: >>> names
['Ivy', 'Lucas', 'Nathan', 'Ray', 'Rumeer']
 158: >>> c
[1, 2, 3, 4, 5, 6]
 159: >>> numbers
[4040, 4, 50, 6, 88]
 160: >>> numbers.sort()
 161: >>> numbers
[4, 6, 50, 88, 4040]
 162: >>> numbers.sort(reverse=True)
 163: >>> numbers
[4040, 88, 50, 6, 4]
 164: >>> names
['Ivy', 'Lucas', 'Nathan', 'Ray', 'Rumeer']
 165: >>> names.sort(reverse=True)
 166: >>> names
['Rumeer', 'Ray', 'Nathan', 'Lucas', 'Ivy']
 167: >>> names.sort(key=len)
 168: >>> names
['Ray', 'Ivy', 'Lucas', 'Rumeer', 'Nathan']
