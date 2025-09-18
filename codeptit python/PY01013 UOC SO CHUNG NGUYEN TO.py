import math

def isPrime(n):
    if (n < 2): return False
    for i in range (2,int(n**0.5)+1):
        if n % i == 0: return False
    return True

def tongchuso(n):
    sum = 0
    for c in str(n):
        sum+=int(c)
    return sum

t = int(input())
for test in range(t):
    x = input().split()
    a = int(x[0]) 
    b = int(x[1])
    ucln = math.gcd(a,b)
    
    if isPrime(tongchuso(ucln)):
        print("YES")
    else:
        print("NO")
