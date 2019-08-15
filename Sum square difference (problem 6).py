n = 100
numList = list(range(1,n+1))
#print(numList)

sumOfSquares = []
for i in numList:
    sumOfSquares.append(i*i)
sumOfSquares = sum(sumOfSquares)
#print(sumOfSquares)

squareOfSums = sum(numList)*sum(numList)

print(squareOfSums - sumOfSquares)
