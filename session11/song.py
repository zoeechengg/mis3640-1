def histogram(word_list):
    d = dict()
    for word in word_list:
        d[word] = d.get(word, 0) + 1
    return d


def print_hist(h):
    for c in h:
        print(c, h[c])

with  open('session11/hey_jude.txt') as f:
    lyrics = f.read().lower().replace(',', ' ').replace('-', ' ').replace('(', ' ').replace(')', ' ').replace('!', ' ').split()

h = histogram(lyrics)
print_hist(h)

with open('session11/result.txt', 'w') as out_file:
    for word, freq in h.items():
        out_file.write(f'{word}: {freq}\n')
