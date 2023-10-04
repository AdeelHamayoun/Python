numbers = [3,41,12,9,74,15]
smallest= None
for i in numbers:
    if smallest is None:
        smallest = i
    if i < smallest:
        smallest = i
    print("so far smallest",smallest )
print("Final",smallest)