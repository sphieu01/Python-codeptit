def checkPrime(n):
    n = int(n)
    if n < 2: return False
    else:
        for i in range(2, int(n**0.5)+ 1):
            if n % i == 0:
                return False
    return True

n = int(input())

temp = 2
for i in range(n):
    for j in range(i+1):
        while not checkPrime(temp):
            temp += 1
        print(temp, end = " ")  
        temp += 1  
    print()

