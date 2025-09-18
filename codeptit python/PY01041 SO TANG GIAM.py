def check(s):
    idx = 0
    if (len(s) < 3): return False
    while (int(s[idx]) < int(s[idx+1])):
        idx += 1
        if idx == len(s)-1:
            return False
    
    for  i in range (idx,len(s)-1):
        if int(s[i]) <= int(s[i+1]):
            return False
    return True

t = int(input())
for _ in range (t):
    s = input()
    if (check(s)):
        print("YES")
    else:
        print("NO")
    # print(check(s))