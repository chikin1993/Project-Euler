NUMBERS = list(range(1000))
sumList = []
for i in NUMBERS:
    if i % 3 == 0 or i % 5 == 0:
        sumList.append(i)
print(sum(sumList))
