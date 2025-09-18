import math
import sys

t = int(input())

for _ in range(t):
    n = int(input())
    if(n == 0):
        print(0, end = "")
    else:
        print("1 ", end = "")
        for i in range(2,int(math.sqrt(n)) + 1):
            cnt = 0
            change = 0
            while(n % i == 0):
                n /= i
                cnt += 1
                change = 1
            if (change == 1):
                print("* ",i, "^", cnt,sep = "" ,end=" ")
        if (n > 1):
            print("* ",i, "^", 1,sep = "" ,end=" ")
    print()