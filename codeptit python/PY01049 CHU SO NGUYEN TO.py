def checkPrime(n):
    n = int(n)
    if n < 2: return False
    for i in range (2,int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True
    
def check(n):
    if (not checkPrime(len(s))):
        #print("owo")
        return False
    cntPrime = 0
    cntnonPrime = 0
    for c in n:
        if c == '2' or c == '3' or c == '5' or c == '7' :
            cntPrime += 1
        else:
            cntnonPrime += 1
    if cntPrime > cntnonPrime:
        return True
    else: 
        return False  



t = int(input())
for _ in range (t):
    s = input()
    if (check(s)):
        print("YES")
    else:
        print("NO")
        
    