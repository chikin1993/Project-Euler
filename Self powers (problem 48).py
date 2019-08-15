seq = []
for i in range(1,1001):
    seq.append(i**i)
bigNum = sum(seq)
bigList = list(str(bigNum))
bigList = bigList[::-1]
bigList = bigList[:10]
bigList = bigList[::-1]
bigList = ''.join(bigList)
print(bigList)
