import math

t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(2, int(math.sqrt(n)+1)):
        while(n % i == 0):
            n /= i
            if(i % 2 == 0): cnt +=1
    print(cnt)        