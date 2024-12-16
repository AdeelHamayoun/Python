
numbers = [10,80,30,12]
sample_list = ['abc', 'xyz', 'aba', '1221']
sample_string = "The quick brown fox"
sample_tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

str1 = [1,2,3,4,5]
str2 = [5,6,7,8,9]

def list_sum(numbers):
    sum = 0
    for number in numbers:
        sum = sum +number
    return sum

def list_greater_number(numbers):
    greater_number = 0
    for number in numbers:
        if number > greater_number:
            greater_number = number
    return greater_number

def list_smallest_number(numbers):
    smallest_number = None
    for number in numbers:
        if smallest_number == None:
            smallest_number = number
        elif number < smallest_number:
            smallest_number = number
    return smallest_number

def same_start_end(sample_list):
    result = []
    for item in sample_list:
        if item[0] == item[-1]:
            result.append(item)
    return result


def last_value(n):
    return n[-1]
def sort_tuple(sample_tuples):
    return sorted(sample_tuples, key=last_value )


def check_duplicate(a):
    result = []
    i_val = 1
    for item in a:
        for val in a[i_val:]:
            if item == val:
                dup_value = item
                result.append(dup_value)
        i_val = i_val+1
    return result

def remove_duplicate(a):
    result = []
    for item in a:
        if item in result:
            continue
        else:
            result.append(item)
    return sorted(result)


def copy_list(sample_list):
    new_result = []
    new_result = list(sample_list)
    return new_result, sample_list


def find_word(sample_string,n):

    nlist = []
    nlist = sample_string.split()
    for word in nlist:
        if len(word) >= n:
          print (word)
    return


def find_common(str1,str2):
    nlist = []
    for i1 in str1:
        for i2 in str2:
            if  i1 == i2:
                nlist.append(i1)
    return nlist


def remove_value(color):
    result = []
    for key,val in enumerate(color):
        if key not in (0,4,5):
            result.append(val)
    return result



sample_list2 = [1, 2, 3, 4, 4]

def largest_2nd (list):
    list.sort()


opportunity


# print(list_sum(numbers))
# print(list_greater_number(numbers))
# print(list_smallest_number(numbers))
# print(same_start_end(sample_list))
# print(sort_tuple(sample_tuples))
# print(check_duplicate(a))
# print(remove_duplicate(a))
# print(copy_list(sample_list))
# find_word(sample_string,4)
# print(find_common(str1,str2))
print(remove_value(color))

