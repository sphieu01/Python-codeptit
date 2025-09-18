import math
t = int(input())

for _ in range(t):
    n = (input())
    nrev = n[::-1]
    if(math.gcd(int(n), int(nrev)) == 1):
        print("YES")
    else: 
        print("NO")