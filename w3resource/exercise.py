# # Write a Python program to sum all the items in a list.
#
# a = [3,5,7,9]
#
# result = 0
# for i in a:
#     result = result + i
# print(result)



# # Get the largest number from a list
#
# a = [1, 2, -8, 0]
# largest_num = 0
#
# for i in a:
#     if i>largest_num:
#         larget_num = i
# print(larget_num)



# # Get the lowest number from a list
#
# a = [1, 2, -8, -10]
# lowest_num = a[0]
#
# for i in a:
#     if i<=lowest_num:
#         lowest_num = i
# print(lowest_num)

#
# Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2


# a = ['abc', 'xyz', 'aba', '1221']
# result = list()
# count = 0
# for i in a:
#     if i[0] == i[len(i)-1]:
#         result.append(i)
# for i in result:
#     count = count+1
# print(count)


# Write a Python program to get a list, sorted in increasing order by the
# # last element in each tuple from a given list of non-empty tuples.
# # Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#
# a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# def last(n):
#     return n[-1]
#
# def tuple_sort(x):
#     return sorted(x, key = last)
#
# print(tuple_sort(a))

#
# # Write a Python program to remove duplicates from a list.
#
# a = [10,20,30,20,10,50,60,40,80,50,40]
# result = list()
#
# for i in a:
#     if i not in result:
#         result.append(i)
# print(result)

# # Write a Python program to check if a list is empty or not.
#
# l = []
# count = 0
# for i in l:
#     count +=1
# if count<1:
#     print("empty")
# else:
#     print("not empty")
#



# # Write a Python program to clone or copy a list.
#
# original_list = [10, 22, 44, 23, 4]
# new_list  = list(original_list)
#
# print(new_list)
#
#



# Write a Python program to find the list of words that are longer than n from a given list of words.
# result = list()
# processing = list()
# word_length = 3
# a = "The quick brown fox jumps over the lazy dog"
# processing = a.split(' ')
#
# for i in processing:
#     if len(i) > word_length:
#         result.append(i)
#
# print(result)

#
# # 11. Write a Python function that takes two lists and returns True if they have at least one common member.
#
# a = [1,3,5,7,9,10,'adeel']
# b = [2,4,5,8,10,'adeel']
# ind = False
# for x in a:
#     for y in b:
#         if x == y:
#             Ind = 'True'
#
# print(ind)
#

#
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# a = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# skip_list = [0,4,5]
# new_list = [x for (i,x) in enumerate(a) if i not in skip_list]
#
# print(new_list)





# class Solution:
#     def solution(self,S):
#         stack = []
#         for char in S:
#             print(stack,char)
#             if stack and self.transform(stack[-1],char):
#                 stack.pop()
#             else:
#                 stack.append(char)
#         return "".join(stack)
#
#     def transform(self,char1,char2):
#         return (char1 == 'A' and char2 == 'B') or (char1 == 'B' and char2 == 'A' ) or \
#                (char1 == 'C'and char2==  'D') or (char1 == 'D' and char2 == 'C')
#
# s = Solution()
# print(s.solution("CBACD"))
# # print(s.solution("CABABD"))
# # print(s.solution("ACBDACBD"))


import datetime
def solution(E, L):
    # Implement your solution here

    start = datetime.datetime(E)
    end = datetime.datetime(L)

    duration = end - start


    return duration


print(solution('10:00', '13:21'))















































