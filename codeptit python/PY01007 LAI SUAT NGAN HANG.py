import math

t = int(input())
for test in range (t):
    a = input().split()
    n = float(a[0])
    x = float(a[1])
    m = float(a[2])

    res = math.log(m/n, 1+x/100)
    print(math.ceil(res))

    
