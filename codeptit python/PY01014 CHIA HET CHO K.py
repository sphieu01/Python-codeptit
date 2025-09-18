inp = input().split()
a = int(inp[0])
k = int(inp[1])
n = int(inp[2])

cnt= 0
b = n + a + 1
for i in range (0,n+1):
    if (i*k >= a):
        
        b = i*k - a
        #print(b)
        break

if (b == 0):
    b+=k

while b + a <= n:
    print(b, "", end = "")
    cnt = 1
    b += k

if (cnt == 0 or a > n):
    print(-1)