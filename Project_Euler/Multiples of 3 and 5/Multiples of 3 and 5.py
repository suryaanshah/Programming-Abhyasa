# Looping and finding the multiples of 3 or 5
MultiplesOf3n5=[]
for i in range(1001): # 1001 so it repeats 1000 times
    if i % 3 == 0 or i % 5 == 0:
        MultiplesOf3n5.append(i)
    else:
        None
 print(MultiplesOf3n5)
