def checkPrime(n):
    n = int(n)
    if n < 2: return False
    for i in range (2,int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True
    
def check(n):
    if not checkPrime(n):
        return False
    if not checkPrime(n[::-1]):
        return False
    sum = 0
    for c in n:
        if not checkPrime(c):
            return False
        sum += int(c)
    if not checkPrime(sum):
        return False
    return True
    

t = int(input())
for _ in range (t):
    s = input()
    if check(s):
        print("Yes")
    else:
        print("No")
        
    