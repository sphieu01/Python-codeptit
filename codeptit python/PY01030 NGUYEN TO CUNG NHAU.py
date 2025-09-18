import math
inp = input().split()

n = int(inp[0])
k = int(inp[1])

cnt = 1
for i in range((10)**(k-1),10**k):
    if (math.gcd(n,i) == 1):
        print(i, end = " ")
        if cnt == 10:
            print()
            cnt = 1
        else:
            cnt += 1
