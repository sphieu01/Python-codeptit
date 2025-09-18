primearr = [1]*100005
def sang():
    primearr[0] = 0
    primearr[1] = 0 
    for i in range(2, int(100005*0.5) + 1):
        if primearr[i] == 1:
            for j in range (i*i, 100005,i):
                primearr[j] = 0

            
sang()

arr = []
# for i in range (11,100001):
#     if i not in arr and int(str(i)[::-1]) not in arr:
        
#             arr.append(i)
                    
            
t = int(input())

for _ in range(t):
    n = int(input())
    for i in range (n):
        k = int(str(i)[::-1])
        if primearr[i] == 1 and i != k and primearr[k] and i < k and k < n:
            print(i, end = " ")
            print(k, end = " ")
    print()
