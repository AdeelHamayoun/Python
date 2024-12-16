fhand = open('py4e.com_code3_intro.txt')

di = dict()
for line in fhand:
    line = line.rstrip()
    # print(line)
    wds= line.split()
    # print(wds)
    for w in wds:
        if w in di:
            di[w] = di[w]+1
        else:
            di[w] = 1
        # print(w,di[w])
print(di)
largest = -1
word = ''
for k,v in di.items():
    if v > largest:
        largest = v
        word = k

print(word, "Larget count number :", largest)
