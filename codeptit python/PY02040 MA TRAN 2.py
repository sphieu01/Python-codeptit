arr =[]

n = int(input())
for i in range (n): arr.append([])

for i in range (n):
    arr[i] = list(map(int,input().split()))

sum1 = 0
for i in range(0,n):
    for j in range(0, n):
            if (i + j < n-1):
                #print(arr[i][j])
                sum1 += arr[i][j]
    

sum2 = 0
for i in range(0,n):
    for j in range (0,n):
        if (i + j >= n):
            #print(arr[i][j])
            sum2 += arr[i][j]
    #print()

#print(sum1, sum2)
chenh = abs(sum1 - sum2)
db = int(input())
if (chenh <= db):
    print("YES")
else:
    print("NO")

print(chenh)