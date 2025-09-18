import math
n = int(input())

arr = [[0 for j in range(105)] for i in range(105)]

for i in range (n):
    s = input()
    for j in range (n):
        arr[i][j] = s[j]

res = 0

for i in range (n):
    sum = 0
    for j in range (n):
        if arr[i][j] == 'C':
            sum += 1
    res += math.comb(sum,2)

for i in range (n):
    sum = 0
    for j in range (n):
        if arr[j][i] == 'C':
            sum += 1
    res += math.comb(sum,2)

print(res)