def check(s):
    for c in s:
        if (c != '0' and c!= '1' and c!= '2'):
            return False
    return True
    

t = int(input())
for _ in range (t):
    s = input()
    if (check(s)):
        print("YES")
    else:
        print("NO")
    