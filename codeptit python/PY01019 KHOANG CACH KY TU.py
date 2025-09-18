def check(s):
    srev = s[::-1]
    for i in range(0,len(s)-1):
        if (abs(ord(s[i]) - ord(s[i-1])) != abs(ord(srev[i]) - ord(srev[i-1]))):
            return False
    return True

test = int(input())
for t in range(test):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
    
    

