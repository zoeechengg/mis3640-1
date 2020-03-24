# with open('new_file_2.txt', 'w') as f:
#     for _ in range(10):
#         f.write('something\n')

# context manager 
# 
# Same as
# 

# f = open('new_file.txt', 'w')
# f.write('something')
# f.close()    


import pickle

t = [1, 2, 3, 'Alvie', 'Nathan', ('a', 'b')]

# context manager
with open('saved.p', 'wb') as p:
    pickle.dump(t, p)


    