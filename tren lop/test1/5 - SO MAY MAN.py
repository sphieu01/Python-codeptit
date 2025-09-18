s = input()

def check(s):
    cnt4 = 0
    cnt7 = 0
    for c in s:
        if c == '7':
            cnt7 += 1
        if c == '4':
            cnt4 += 1
    return cnt4 + cnt7 == 7 or cnt4 + cnt7 == 4

if check(s):
    print("YES")
else:
    print("NO")