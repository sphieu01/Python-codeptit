import math

t = int(input())

for _ in range(t):
    s = input()
    scheck = input()
    cnt = 0
    while (s.find(scheck) != -1):
        cnt += 1
        k = s.find(scheck)
        s = s[0:k] + " " + s[k+len(scheck):]
        # print(s)
    print(cnt)
    # print()
    
    

