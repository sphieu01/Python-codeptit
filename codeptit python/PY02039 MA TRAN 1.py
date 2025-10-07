arr =[]

n = int(input())
for i in range (n): arr.append([])

for i in range (n):
    arr[i] = list(map(int,input().split()))

sum1 = 0
for i in range(0,n):
    for j in range(i+1, n):
        # print(arr[i][j])
        sum1 += arr[i][j]

sum2 = 0
for i in range(0,n):
    for j in range (0,i):
        sum2 += arr[i][j]
        #print(arr[i][j])
chenh = abs(sum1 - sum2)
db = int(input())
if (chenh <= db):
    print("YES")
else:
    print("NO")

print(chenh)