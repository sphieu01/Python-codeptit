import math

def isprime(n):
    if n < 2:
        return False
    for i in range (2, int(n**0.5)+1):
        if n % i == 0: 
            return False
    return True

test = int(input())
for t in range(test):
    cnt = 0
    n = int( input())
    for i in range (1, n):
        if(math.gcd(n, i) == 1):
            cnt+=1
    if isprime(cnt): print("YES")
    else: print("NO")      


