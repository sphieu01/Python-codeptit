t = int(input())

arr =[0,1,1] + [0]*93
for i in range(2,94):
    arr[i] = arr[i-1] + arr[i-2]

for _ in range (t):
    a,b = map(int, input().split())
    
    for i in range(a,b+1):
        print(arr[i] , end = " ")
    print()