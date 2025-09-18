t = int(input())

def check(s):
    for c in s:
        if c != '7' and c != '4':
            return False
    return True
            

for _ in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")




