# //////////////////////////////
# # conditional statements
# //////////////////////////////
#
# x = 11
# if x<5:
#     print("Value of x is less than 5")
# if x>=5:
#     if x==5:
#         print("Value of x is equal to 5")
#     elif x<=10:
#         print("Value of x is less equal than 10")
#     else:
#         print("Value of x is greater than 10")


# //////////////////////////////
# # try catch
# //////////////////////////////
# # calculate salary and overtime
#
# hour = input("Please enter the total hours:")
# rate = input("Please enter the per hour rate:")
#
# try:
#     hour = float(hour)
#     rate = float(rate)
# except:
#     input("Please enter numeric values, exiting.....")
#     quit()
#
# if hour>40:
#     rg = 40 * rate
#     ot = (hour - 40) * (rate * 0.5)
#     salary = rg + ot
# else:
#     salary= hour * rate
#
# print("Your salary would be:", salary)


# # //////////////////////////////
# # # function
# # //////////////////////////////
# # # calculate salary and overtime
#
# def sal_cal(hour,rate):
#     if hour>40:
#         rg = 40 * rate
#         ot = (hour - 40) * (rate * 0.5)
#         salary = rg + ot
#     else:
#         salary= hour * rate
#     return salary
#
#
# hour = input("Please enter the total hours:")
# rate = input("Please enter the per hour rate:")
#
# try:
#     hour = float(hour)
#     rate = float(rate)
# except:
#     input("Please enter numeric values, exiting.....")
#     quit()
#
# print("Your salary is:",sal_cal(hour,rate))


# # //////////////////////////////
# # # while loop
# # //////////////////////////////

#
# input_values = []
# x = ''
# while x != 'done':
#     x = input("Please enter the value:")
#     if x != 'done':
#         try:
#             x = float(x)
#             input_values.append(x)
#             continue
#         except:
#             print("Please enter numeric value")
#             break
#     print('your enterred values:',input_values )


# # //////////////////////////////
# # # For loop ---- find the largest number
# # //////////////////////////////
#
# values = [1,2,3,4,5,6,7,8,99,0,-1,-2,-3,-4]
# max_number = 0
# for i in values:
#     if i > max_number:
#         max_number = i
# print(max_number)

# # //////////////////////////////
# # # For loop ---- running total of numbers in array
# # //////////////////////////////

# values = [1,2,3,4,5,6,7,8,99,0,-1,-2,-3,-4,-5,-6,-7]
# total = 0
# for i in values:
#     total = total + i
# print(total)

# # //////////////////////////////
# # # For loop ---- Filtering
# print if values are larger than 20
# # //////////////////////////////

# print("Before")
# values = [9,41,12,3,74,15]
# for i in values:
#     if i >20:
#         print("Larger  number", i)
# print("After")


# # //////////////////////////////
# # # For loop ---- searching
# Boolean value to true if we found 3 in array
# # //////////////////////////////

# found = False
# print("Before",found )
# values = [9,41,12,3,74,15]
# for i in values:
#     if i == 3:
#         found = True
#     print(found, i)
#     found = False
# print("After",found)


# # //////////////////////////////
# # # For loop ---- searching
# find the samallest
# # //////////////////////////////

# small_number = None
# values = [9,41,12,3,1,15]
# for i in values:
#     if small_number == None:
#         small_number = i
#     elif i < small_number:
#         small_number = i
#
# print("Small Number",small_number)


# # //////////////////////////////
# # # For loop
# write a program which repeatedly reads number until user enters done
# once done is entered then print total, count and average of numbers
# if user enters any other than number, detect mistake
# # //////////////////////////////
#
# def take_input():
#     input_values = []
#     x = ''
#     while x != 'done':
#         x = input("Please enter the value:")
#         if x != 'done':
#             try:
#                 x = float(x)
#                 input_values.append(x)
#                 continue
#             except:
#                 print("Please enter numeric value")
#                 break
#     return input_values
#
# def math_operations(input_values):
#     sum = 0
#     count = 0
#     avg = 0
#
#     for value in input_values:
#         sum = sum + value
#         count = count + 1
#         avg = sum/count
#     print('Sum of entered values are', sum)
#     print('count of entered values are', count)
#     print('Average of entered values are', avg)
#
# values = take_input()
# print('your entered values:', values)
# math_operations(values)


# # //////////////////////////////
# # # string
# find letter a count in string
# # //////////////////////////////
#
# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count+1
# print(count)

# # //////////////////////////////
# # # string
# string slicing
# # //////////////////////////////
#
# word = 'Monthly Python'
# length = len(word)
# print(word[0:4])
# print(word[6:7])
# print(word[8:14])
# print(word[8:length])
#
# print(word[:4]) # from start till end
# print(word[5:]) # from index 5 till end
# print(word[:]) # whole string



# # //////////////////////////////
# # # string
# using in as a logical operator
# # //////////////////////////////

# word = 'Monthly Python'
# print('M' in word)
# if 'M' in word:
#     print("found it!")
# else:
#     print("No such word")


# # //////////////////////////////
# # # string
# string functions
# # //////////////////////////////


# word = ' Monthly Python '
# print(word.lower())
# print(word.upper())
# print(word.find('P'))
# print(word.replace('P','M'))
# print(word.lstrip())
# print(word.rstrip())
# print(word.strip())

# print(type(word)) # print type of variable
# print(dir(word))  # print all available function


# # //////////////////////////////
# # # string
# string parsing and extracting
# find the host using find function
# # //////////////////////////////
#
# data = 'From adeel.hamayoun@gmail.com Sat Dec 7 11:25:16 2024'
#
# a_post = data.find('@')
# space_post = data.find(' ',a_post)
#
# host = data[a_post+1:space_post]
# print(host)

# # # //////////////////////////////
# # # # Reading a text file
# # # //////////////////////////////
#
# fhand = open('mbox.txt')
#
# for line in fhand:
#     print(line)

# # //////////////////////////////
# # # Reading a text file
# count number of line
# # //////////////////////////////

# count = 0
# fhand = open('mbox.txt')
# for line in fhand:
#     count = count+1
# print("line count:", count)



# # //////////////////////////////
# # # Reading a text file
# read function to read files into a string
# # //////////////////////////////

# fhand = open('mbox.txt')
# fstring = fhand.read()
# print (len(fstring))
# print (fstring[:100])



# # //////////////////////////////
# # # Reading a text file
# search through a file (search line starts with from )
# # //////////////////////////////

# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip() #to remove the \n at the start of new line to minimise the extra space
#     if line.startswith("From:"):
#         print(line)

#
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip() #to remove the \n at the start of new line to minimise the extra space
#     if not '@uct.ac.za' in line:
#         continue
#     print(line)


# # //////////////////////////////
# # # Reading a text file and word counts using dictionary
# # //////////////////////////////
#
# counts = dict()
# xbox = open("mbox.txt")
# for line in xbox:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0)+1
# print(counts)
#
# print(list(counts))
# print(counts.keys())
# print(counts.values())
# print(counts.items())
#
# for aaa,bbb in counts.items():
#     print(aaa,bbb)


# # //////////////////////////////
# Tuples
# # # Reading a text file and word counts using dictionary and using tuples count top 10
# # //////////////////////////////


counts = dict()
xbox = open("mbox.txt")
for line in xbox:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
# print(counts)
list = list()
for key, val in counts.items():
    newtup = (val,key)
    list.append(newtup)
# print(list)
list = sorted(list, reverse=True)

for val, key in list[:10]:
    print(key,val)


























