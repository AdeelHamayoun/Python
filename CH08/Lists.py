

# cheese = ['cheddar','Edam','Gouda']
# numbers = [17,123]
# empty = []
#
# print(cheese,numbers,empty)
#
# print(cheese[1])
#
# # Lists are mutable
# numbers = [17,123]
# numbers[1] = 5
#
# print(numbers)


# cheese = ['cheddar','Edam','Gouda']
# z = 'Edam' in cheese
# print (z)

# Traversing a list

# cheese = ['cheddar','Edam','Gouda']
# for i in cheese:
#     print(i)
#
# for i in range(len(cheese)):
#     print(cheese[i])

# List operations
#
# a = [1,2,3]
# b= [4,5,6]
# c = a+b
# print (c)

# List slices
#
# t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[3:3])
# print(t[:])
# print(t[:5])
# print(t[3:])

#
# # List methods
# t = ['a', 'b', 'c']
# t.append('adeel')
# print(t)


# t = ['d', 'c', 'e', 'b', 'a']
# t.sort()
# print(t)


# Lists and functions

# nums = [3, 41, 12, 9, 74, 15]
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(sum(nums)/len(nums))

# take input from user and calculate average

# iput_list = list()
# while True:
#     iput = input("Please enter number:")
#     if iput == 'done':
#         break
#     else:
#         iput = float(iput)
#         iput_list.append(iput)
# avg = sum(iput_list)/len(iput_list)
# print("Your input numbers are ", iput_list)
# print("Avg: ", avg)

# List and string

# a = list()
# s = 'pining for the fjords'
# a= s.split()
# print(a)
# print(a[2])

# Write a Program to get the consecutive character counts
# Description:
# Input =  'aaaabbbcca'
# Output: [[“a”, 4], [“b”, 3], [“c”, 2], [“a”, 1]]


# Input =  'aaaabbbcca'
# fresult = list()
# count = 1
# current_char = Input[0]
# for i in range(1, len(Input)):
#     if current_char == Input[i]:
#         count = count+1
#     else:
#         fresult.append([current_char,count])
#         current_char = Input[i]
#         count = 1
# fresult.append([current_char,count])
#
# print(fresult)


# Write a program to read through the mail box data and when you find line that starts with “From”,
# you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.
#
# mylist = list()
# fhand = open('mbox.txt')
# for i in fhand:
#     i = i.rstrip()
#     if i.startswith('From: '):
#         mylist.append(i.split())
# for x in mylist:
#      print(x[1])
#



# How would you produce the list of all the words that Shakespeare used?
# www.py4e.com / code3 / romeo.txt.

#
# word_list = list()
# fhand = open('py4e.com_code3_romeo.txt')
# for line in fhand:
#     line = line.rstrip()
#     line = line.split()
#     for i in line:
#
#         if i in word_list:
#              continue
#         else:
#              word_list.append(i)
# print(word_list)



# he program that prompts the user for a list of numbers and prints out the maximum and minimum of
# the numbers at the end when the user enters “done”. Write the program to store the numbers the user
# enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after

#
# ilist = list()
# while True:
#     ival = input("Please enter number: ")
#     if ival == 'done':
#         break
#     else:
#         ilist.append(float(ival))
#
# print("MAX: ",max(ilist))
# print("MIN: ",min(ilist))
# print("SUM: ",sum(ilist))
# print("count: ",len(ilist))
# print("Average: ",sum(ilist)/len(ilist))

# Write a Python program to count the number of strings from
# a given list of strings. The string length is 2 or more and the first and last characters are the same.
# # Sample List : ['abc', 'xyz', 'aba', '1221']
# # Expected Result : 2
result = list()
count = 0
sample = ['abc', 'xyz', 'aba', '1221']

for i in sample:

    if i[0] == i[len(i)-1]:
        result.append(i)
        count +=1
print(count,"words")
print(result)


































































