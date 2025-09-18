
n,m,x = map(int, input().split()) # n dinh, m canh

arr = []
isused = [False]*(n+1)

def dfs(x1):
    for y in arr[x1]:
        if not isused[y]:
            isused[y] = True
            dfs(y)



for i in range(n+1):
    arr.append([])
for i in range (m):
    temp1 ,temp2 = map(int, input().split())
    arr[temp1].append(temp2)
    arr[temp2].append(temp1)

dfs(x)

found = False
for i in range (1,n+1):
    if not isused[i]:
        print(i)
        found = True

if not found:
    print(0)

