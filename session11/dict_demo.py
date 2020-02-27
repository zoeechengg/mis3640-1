def histogram(s):
    d = dict()

    for letter in s:
        # if letter not in d:
        #     d[letter] = 1
        # else:
        #     d[letter] += 1
        d[letter] = d.get(letter, 0) + 1

    return d

name = 'Queenie never quits.'
h = histogram(name)
print(h)