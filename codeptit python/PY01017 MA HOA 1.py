t = int(input())
for test in range(t):
    s = input()
    res = ""
    chartemp = s[0]
    charcnt = 0
    for c in s:
        if chartemp == c:
            charcnt += 1
        else:
            res += str(charcnt)
            res += chartemp
            chartemp = c
            charcnt = 1
    res += str(charcnt)
    res += chartemp
    print(res)