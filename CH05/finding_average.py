numbers = [9,41,12,3,74,15]
sum = 0
sr = 0

for i in numbers:
    sum = sum + i
    sr = sr + 1
    avg = sum / sr
    print(sr,i,sum, avg)
print("final average", avg)