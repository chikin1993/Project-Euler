def factorial(n):
    num = 1
    while n > 1:
        num *= n
        n -= 1
    return num

gridSize = 20
paths = factorial(2*gridSize)/(factorial(gridSize)*factorial(gridSize))
print(int(paths))
