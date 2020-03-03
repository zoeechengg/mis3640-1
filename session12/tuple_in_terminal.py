     1: >>> name = 'Andrew'
     2: >>> name[3: 3+2]
     3: >>> d = {'a': 20, 'b': 10}
     4:
>>> for k, v in d.items():
...     print(f'{k}: {v}')
...
     5:
>>> for i, letter in enumerate(name):
...     print(f'{i}: {letter}')
...
     6:
>>> for _, v in d.items():
...     print(v)
...
     7:
>>> for _ in range(10):
...     print('a')
...
     8: >>> a = [1, 2, 3]
     9: >>> a[0] = 'Rachel'
     10: >>> a
     11: >>> name
     12: >>> name[-2] = 'a'
     13: >>> t = 'a', 'b', 'c'
     14: >>> type(t)
     15: >>> t[0]
     16: >>> t[0] = 'd'
     17: >>> t1 = 'a'
     18: >>> type(t1)
     19: >>> t1 = 'a',
     20: >>> type(t1)
     21: >>> len(t1)
     22: >>> t1
     23: >>> t = tuple('Babson')
     24: >>> t
     25: >>> a
     26: >>> t = tuple(a)
     27: >>> t
     28: >>> t
     29: >>> t = (1, ) + t[1:]
     30: >>> t
     31: >>> a = 10
     32: >>> b = 90
     33: >>> b, a = a, b
     34: >>> b
     35: >>> a
     36: >>> email = 'zli@babson.edu'
     37: >>> email.split('@')
     38: >>> id, domain = email.split('@')
     39: >>> id
     40: >>> domain
     41: >>> tel = '123-456-7890'
     42: >>> area, _, local = tel.split('-')
     43: >>> area
     44: >>> local
     45: >>> *a, local = tel.splilt('-')
     46: >>> *a, local = tel.split('-')
     47: >>> local
     48: >>> a
     49: >>> tel = '+1-123-456-7890'
     50: >>> tel.split('-')
     51: >>> *a, local = tel.split('-')
     52: >>> local
     53: >>> a
     54: >>> country, *_, local = tel.split('-')
     55: >>> country
     56: >>> local
     57: >>> help(divmod)
     58: >>> divmod(7, 3)
     59:
>>> def f():
...     return 1, 2
...
     60: >>> f()
     61: >>> type(f())
     62: >>> type(f)
     63:
>>> def f():
...     return 1, 2
...
     64: >>> humidity, temp = f()
     65: >>> humidity
     66: >>> temp
     67:
>>> def sumall(*nums):
...     result = 0
...     for num in nums:
...         result += num
...     return result
...
     68: >>> sumall(1)
     69: >>> sumall(1, 2, 3)
     70: >>> sumall(1, 2, 3, 54325,4,643,6536,43,5,435,4325,4325,2)
