def palindrome(num):
    return str(num) == str(num)[::-1]

theRange = list(range(900,1000))
#print(theRange)
numbers = []
for i in theRange:
    for j in theRange:
        numbers.append(i*j)
numbers = sorted(list(set(numbers)))
#print(numbers)
palindromes = []
for i in numbers:
    if palindrome(i) == True:
        print(i)
