def checkPrime(n):
    n = int(n)
    if n < 2: return False
    for i in range (2,int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True
    
def check(n):

    sum = 0
    for i in range (0,len(s)):
        if (i % 2 == 0):
            if int(s[i]) % 2 != 0 :return False
        else:
            if int(s[i]) % 2 != 1 :return False
        sum += int(s[i])
    if not checkPrime(sum): return False
    return True
    

t = int(input())
for _ in range (t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
        
    