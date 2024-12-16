

# fhand = open('mbox.txt')

#
# count = 0
#
# for line in fhand:
#     count = count+1
# print(count)

 # --- read funciton
# inp = fhand.read()

# print(inp[:500])

# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From: '):
#         print(line)


# #  startswith function
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print(line)

# for line in fhand:
#      line = line.rstrip()
#      if line.find('@uct.ac.za') == -1:
#          continue
#      print(line)

#  input a file name and read
# fname = input("Please input file name:")
# fhand = open(fname)
# iput = fhand.read()
#
# print(iput[:500])

#  input a file name and read and convert into upper character
# fname = input("Please input file name:")
# fhand = open(fname)
# iput = fhand.read()
# iput = iput.upper()
#
#
# print(iput[:500])


#  input a file name and read and search for line X-DSPAM-Confidence: 0.8475
# fname = input("Please input file name:")
# fhand = open(fname)
# for line in fhand:
#     if line.find('X-DSPAM-Confidence: 0.8475') == -1: continue
#     print(line)


#  input a file name and message if wrong file name entered
count = 0
fname = input("Please input file name:")
try:
    fhand = open(fname)
except:
    print("file cannot be opend",fname)
    exit()

for line in fhand:
    count = count + 1
print("There were " + str(count) + " lines in ", fname)





