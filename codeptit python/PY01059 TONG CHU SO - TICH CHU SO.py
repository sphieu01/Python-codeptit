import math
t = int(input())

for _ in range(t):
    s = input()
    sumchan = 0
    mulle = 1
    cnt0le = 0
    for i in range(len(s)):
        c = s[i]
        if (i % 2 == 0):
            sumchan += int(c)
        else:
            if c == '0':
                cnt0le += 1
            else:
                mulle *= int(c)
    print(sumchan, end = " ")
    if (cnt0le == (math.floor(len(s)/2) )):
        print(0)
    else: print(mulle)

