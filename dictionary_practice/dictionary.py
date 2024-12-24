# # 1. Write a Python script to sort (ascending and descending) a dictionary by value.
#
# k = []
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# k = list(d.keys())
# k.sort()
# print(d)
# for i in k:
#    print(i,d.get(i,0))

# # simple way
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print(dict(sorted(d.items())))


# # create a dictionary from two lists
#
# a = [1,3,4,2,0]
# b = [2,4,3,1,0]
#
# print(list(zip(a,b)))

# #
# # 2. Write a Python script to add a key to a dictionary.
# #
# # Sample Dictionary : {0: 10, 1: 20}
# # Expected Result : {0: 10, 1: 20, 2: 30}
#
# new_key = 0
# new_val = 0
# d = {0: 10, 1: 20}
# for index,v in d.items():
#         index += index
#         new_val += v
# d[index] = new_val
# print(d)

# #
# # 3. Write a Python script to concatenate the following dictionaries to create a new one.
# #
# # Sample Dictionary :
# # dic1={1:10, 2:20}
# # dic2={3:30, 4:40}
# # dic3={5:50,6:60}
# # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50,6:60}
#
# merged = {**dic1, **dic2, **dic3}
# print(merged)


# 4. Write a Python script to check whether a given key already exists in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# # 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# # Sample Dictionary ( n = 5) :
# # Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#
# # ---- i need to generte number from i to 5
#
# k = []
# v = []
# for i in range(1,6):
#     k.append(i)
#     v.append(i*i)
# print(dict(zip(k,v)))











