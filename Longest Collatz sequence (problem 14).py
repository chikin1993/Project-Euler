def collatz(n):
    if n == 1:
        n = 0
        return n
    elif n % 2 == 0:
        n = n/2
        n = int(n)
        return n
    elif n % 2 == 1:
        n = 3*n + 1
        n = int(n)
        return n

def collSeq(n):
    seq = [n]
    while n > 0:
        seq.append(collatz(n))
        n = collatz(n)
    return len(seq)-1

colList = []

#for i in range(1000000):
#    colList.append(collSeq(i))
    
#print(max(colList))
#print(colList.index(max(colList)))

print(collSeq(837799))
