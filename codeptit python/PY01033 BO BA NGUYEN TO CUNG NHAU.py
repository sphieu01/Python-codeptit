import math
inp = input().split()

l = int(inp[0])
r = int(inp[1])
lgoc = l
for i in range(l, r + 1):
    for j in range (i, r+1):
        for k in range(j, r+ 1):
            if (math.gcd(i,j) == 1 and math.gcd(j,k) == 1 and math.gcd(i,k)==1):
                print("(",i,", " , j,", ", k, ")", sep = "")
