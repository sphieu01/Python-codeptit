import math

def checkPrime(n):
    n = int(n)
    if n < 2: return False
    else:
        for i in range(2, int(n**0.5)+ 1):
            if n % i == 0:
                return False
    return True

t = int(input())

for _ in range(t):
    s = input()
    # print( s[0:3] , s[-3:] ,end = " ")
    if (checkPrime(s[0:3]) and checkPrime(s[-3:])):
        
        print("YES")
    else:
        print("NO")

