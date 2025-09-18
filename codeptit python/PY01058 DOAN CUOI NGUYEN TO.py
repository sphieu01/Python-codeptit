def checkPrime(n):
    n = int(n)
    if n < 2: return False
    for i in range (2,int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True
    
def check(n):
    if checkPrime(n[len(n)-4:len(n)]):
        return True
    else:
        return False

    
    

t = int(input())
for _ in range (t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
        
    