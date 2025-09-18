
def isPrime(x):
    if x < 2: return False
    else:
        for i in range (2, int(x**0.5)+1):
            if x % i == 0:
                return False
    return True

inp = input().split()
n = int(inp[0])
m = int(inp[1])


arr = [[0] * 20 for _ in range(20)]
for i in range(n):
    inp = input().split()
    for j in range(m):
        arr[i][j] = int(inp[j])

        if isPrime(arr[i][j]):
            arr[i][j] = 1
        else:
            arr[i][j] = 0

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()