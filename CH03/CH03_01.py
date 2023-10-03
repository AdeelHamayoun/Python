# write a program to get two inputs from user
#  hours and rate per hour
# calculate the wage
# if hour is grater than 40 then rate per hour is increase by 1.5


hour = input("Please enter Hours: ")
rpo = input("Please enter Rate per Hour")
h = float(hour)
r = float(rpo)
if h > 40.0:
    # print("Overtime")
    reg = h * r
    otp = (h - 40) * (r * 0.5)
    pay = reg + otp

else:
    # print("Regular")
    pay = h*r
print("Pay: ",pay )

