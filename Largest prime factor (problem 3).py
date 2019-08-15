N = 600851475143
i = 2
factors = []
while i <= N:
    if N % i == 0:
        N /= i
        factors.append(i)
    else:
        i += 1
factors.sort(reverse=True)
print(factors[0])
