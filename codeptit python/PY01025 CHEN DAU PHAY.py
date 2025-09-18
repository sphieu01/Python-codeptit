s = input()
s = s[::-1]
res = ""
for i in range(len(s)):
    if (i % 3 == 0 and i != 0):
        res += ","
    res += s[i] 
res = res[::-1]
print(res) 