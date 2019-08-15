FIBONACCI = [0]
i = 0
j = 1
while i+j < 4000000:
    i,j = j,i+j
    if j % 2 == 0:
        FIBONACCI.append(j)
print(sum(FIBONACCI))
