def checkPrime(n):
    n = int(n)
    if n< 2: return False
    for i in range (2,int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True
    


t = int(input())
for _ in range (t):
    s = input()
    l = len(s)
    if (checkPrime(s[l-4:l])):
        print("YES")
    else:
        print("NO")
        
    