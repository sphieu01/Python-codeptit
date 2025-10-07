small = int(-1e8 - 1)
t = int(input())

for test in range(t):
     
    n = int(input())
    arr = list(map(int, input().split()))
    a, b, c = small, small, small # 3 5 6
                                #     4
                                # 4 5 6
    
    for i in arr:
        if i < a:
            continue
        if i > c:
            a, b ,c = b , c , i
        elif i > b:
            a , b = b , i
        elif i > a:
            a = i 
        
    print(a + b + c)






