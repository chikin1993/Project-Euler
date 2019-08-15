def pallCheck10(n):
    forward = list(str(n))
    backward = forward[::-1]
    if forward == backward:
        return True
    else:
        return False
    
def pallCheck2(n):
    forward = bin(n)[2:]
    backward = forward[::-1]
    if forward == backward:
        return True
    else:
        return False

def doublePallCheck(n):
    if pallCheck10(n) == True:
        if pallCheck2(n) == True:
            return True
        else:
            return False
    else:
        return False

doublePallList = []    

for i in range(1,10**6):
    if doublePallCheck(i) == True:
        doublePallList.append(i)

print(sum(doublePallList))
