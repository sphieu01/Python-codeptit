test = int(input())

for t in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    #print(arr)
    cnt = 0
    for i in range(n):
        r = len(arr)-1
        l = i + 1
        while (l < r and l != i and r != i):
            if arr[l] + arr[r] + arr[i] == 0:
                cnt += 1
                l += 1
            else:
                if arr[l] + arr[r]  + arr[i] < 0:
                    l += 1
                else:
                    r -= 1
    print(cnt)   

# 1 -2 1 0 5  
# -2 0 1 1 5       
# l r