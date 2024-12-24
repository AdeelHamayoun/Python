# # 1. Calculate string length.
#
# a = 'w3resource.com'
# print(len(a))
# count = 0
# for i in a:
#     count = count+1
# print('loop count:' + str(count))

#
# # 2. Count character frequency in a string.
# # Sample String : google.com'
# # Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
#
# result = {}
# s = 'google.com'
# for i in s:
#     if i in result.keys():
#         result[i] += 1
#     else:
#         result[i] = 1
# print(result)

# 3. Get string of first and last 2 chars.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'

# s = 'w3resource'
# print(s[:2] + s[-2:])
# s2 = 'w3'
# print(s2[:2] + s2[-2:])

# #
# # 4. Replace first char occurrences with $.
# # Sample String : 'restart'
# # Expected Result : 'resta$t'
#
# s = 'restart'
# first_char = s[0]
# s1 = s[1:]
# s1 = s1.replace(first_char,'$')
# print(first_char + s1)

# # 5. Swap first 2 chars of 2 strings.
# #
# # Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# # Sample String : 'abc', 'xyz'
# # Expected Result : 'xyc abz'
#
# s = 'abc', 'xyz'
# first_string = s[0]
# second_string = s[1]
# first = second_string[:2] + first_string[2]
# second = first_string[:2] + second_string[2]
# print (first +" "+ second)
#

# # 6. Add ing or ly to a string.
# #
# # Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# # If the given string already ends with 'ing', add 'ly' instead.
# # If the string length of the given string is less than 3, leave it unchanged.
# # Sample String : 'abc'
# # Expected Result : 'abcing'
# # Sample String : 'string'
# # Expected Result : 'stringly'
#
# def add_char(a):
#     if len(a)>2:
#         if a[len(a)-3:] == 'ing':
#             a = a + 'ly'
#         elif a[len(a)-3:] != 'ing':
#             a = a + 'ing'
#     return a
# print(add_char('string'))


# 7. Replace 'not'...'poor' with 'good'.
#
# Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
#
# def find_repalce(a):
#     not_place = a.find('not')
#     poor_place = a.find('poor')
#     if poor_place > not_place & not_place != -1:
#         part = a[not_place:poor_place+4]
#         a = a.replace(part,'good')
#     return a
#
# print(find_repalce('The lyrics is not that poor!'))
# print(find_repalce('The lyrics is poor!'))

# #
# #8. Find longest word in a list.
# #
# # Write a Python function that takes a list of words and return the longest word
# # and the length of the longest one.
# # input = ["PHP", "Exercises", "Backend"]
# # Sample Output:
# # Longest word: Exercises
# # Length of the longest word: 9
#
# input = ["PHP", "Exercises", "Backend"]
#
# l_word = ''
# l_length = 0
# for i in input:
#     if len(i) > l_length:
#         l_word = i
#         l_length = len(i)
# print(f"""
# Longest word: {l_word}
# Length of the longest word: {l_length}
# """)


# # 9. Remove nth character from a string.
# # Write a Python program to remove the nth index character from a nonempty string.
#
# def remove_char(s,a):
#     part1 = s[:a-1]
#     part2 = s[a:]
#     return part1 + part2
#
# x = print(remove_char("Backend" , 5))


a = 'a quick brown fox jumps over the lazy dog'
print(a.split())





































