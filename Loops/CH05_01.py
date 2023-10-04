# write a program which repeattedly reads number untill user enters done
# once done is entered then print total, count and average of numbers
# if user enters any thing other than number, detect mistake

def get_input():
    val = ""
    values = []
    while val != "done":
            val = input("print a number: ",)
            if val != "done":
                try:
                    fval = int(val)
                    values.append(fval)
                except:
                    print("Invalid Input")
                    continue
    return values

def calculation(values):
    sum = 0
    sr = 0
    avg = 0
    for i in values:
        sum = sum+i
        sr = sr+1
        avg = sum/sr
    print(sum,sr,avg)


val = get_input()
calculation(val)