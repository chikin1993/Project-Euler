n = 1
for i in range(1,101):
    n = i*n
facList = list(str(n))
m = 0
for i in facList:
    m += int(i)
print(m)
