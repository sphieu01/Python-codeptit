# def checkPrime(n):
#     n = int(n)
#     if n < 2: return False
#     for i in range (2,int(n**0.5)+ 1):
#         if n % i == 0:
#             return False
#     return True
    
def check(n):
    if len(s) % 2 == 0: return False
    if s[0] == s[1]: return False
    temp = s[0]

    for i in range (0,len(s), 2):
        if temp != s[i]:
            return False
    return True
    

t = int(input())
for _ in range (t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
        
    