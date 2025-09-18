test = int(input())
for t in range (test):
    s = input()
    cnt = 0
    ok = 1
    for c in s:
        if (c != '4' and c != '7'): 
            ok = 0
            break
    if (ok == 1): print('YES')
    else: print("NO")
