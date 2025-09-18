inp = input().split()

k = int(inp[0])
p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while (k != 0):
    s = inp[1]
    res = ""

    for i in range(0, len(s)):
        pos = p.find(s[i])
        res +=  p[(pos+k)%28]
    
    res = res[::-1]
    print(res)

    inp = input().split()
    k = int(inp[0])