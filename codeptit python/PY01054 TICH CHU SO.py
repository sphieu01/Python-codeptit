def checkPrime(n):
    n = int(n)
    if n < 2: return False
    for i in range (2,int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True
    
def check(n):
    tich = 1
    for c in n:
        if c != "0":
            tich *= int(c)
    return tich
    




t = int(input())
for _ in range (t):
    s = input()
    print(check(s))
        
    