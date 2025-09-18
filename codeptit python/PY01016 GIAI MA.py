t = int(input())
for test in range(t):
    s = input()
    res = ""
    for i in range(0,len(s),2):
        for j in range(int(s[i+1])):
            res += s[i]
    print(res)