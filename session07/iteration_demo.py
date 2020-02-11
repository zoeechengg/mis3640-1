# current_sum = 0

# for i in range(1001):
#     if i % 2 == 0:
#         print(f'The value of i is {i}')
#         current_sum = current_sum + i
#         print(f'Currently, the sum is {current_sum}.')
#         print()

# print(current_sum)


# iteration = 0

# while iteration < 5:
#     count = 0
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world": 
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 



i = 0
current_sum = 0

while i <= 10:
    print(f'current value of i is {i}')
    current_sum += i
    print(f'after adding i, the current sum is {current_sum}.')
    i += 2
    print()

print(current_sum)