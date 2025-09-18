t = int(input())

for _ in range(t):
    inp = input().split()
    n = int(inp[0])
    k = int(inp[1])
    arr = input().split()
    for i in range(k,n):
        print(arr[i], end = " ")
    for i in range (k):
        print(arr[i], end = " ")
    print()
