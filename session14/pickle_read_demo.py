import pickle

with open('saved.p', 'rb') as p:
    t = pickle.load(p)

print(t)
print(type(t))