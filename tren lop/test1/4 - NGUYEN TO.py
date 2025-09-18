def checkPrime(n):
    if n < 2:
        return False
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def ucln(a,b):
    while (b != 0):
        r = a % b
        
        a = b
        b = r
    return a

t = int(input())

for _ in range(t):
    n = int(input()) ; cnt = 0
    for i in range (1, n):
        if (ucln(i,n) == 1):
            cnt += 1
    if (checkPrime(cnt)):
        print("YES")
    else:
        print("NO")