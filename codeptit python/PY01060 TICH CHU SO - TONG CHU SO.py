import math
t = int(input())

for _ in range(t):
    s = input()
    mulchan = 1
    sumle = 0
    for i in range(len(s)):
        c = s[i]
        if (i % 2 == 0):
            if c != '0':
                mulchan *= int(c)
        else:
            sumle += int(c)
                
    print(mulchan, end = " ")
    print(sumle)

