t = int(input())

for _ in range(t):
    s = input()
    arr = []
    for c in s:
        arr.append(int(c)) 
    for i in range (len(arr)-1, 0,-1):
        if arr[i] >= 5:
            arr[i-1] += 1
            arr[i] = 0
        else:
            arr[i] = 0
        #print(arr)
    for x in arr: 
        print(x, end = "")
    print()

