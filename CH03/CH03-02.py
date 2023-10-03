
hour = input("Please enter Hours: ")
rpo = input("Please enter Rate per Hour")
try:
    h = float(hour)
    r = float(rpo)
except:
    print("Please enter numeric values, exiting.....")
    quit()

if h > 40.0:
    # print("Overtime")
    reg = h * r
    otp = (h - 40) * (r * 0.5)
    pay = reg + otp

else:
    # print("Regular")
    pay = h*r
print("Pay: ",pay )
