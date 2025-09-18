def checkPrime(n):
    n = int(n)
    if n < 2: return False
    for i in range (2,int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True

arr = [0]
for i in range (1,100005):
    arr.append(arr[i-1]) 
    if checkPrime(i):
        if checkPrime(i-6) and checkPrime(i-4):
            arr[i] += 1
        if checkPrime(i-6) and checkPrime(i-2):
            arr[i] += 1
            

t = int(input())

for _ in range(t):
    n = int(input())
    print(arr[n])
