def check(n):
    sum = 0
    ncpy = n
    while(n > 0):
        sum += n%10
        n = int(n/10)
    #print(sum)
    if(sum % 10 != 0):
        return False
    n = str(ncpy)
    for i in range(len(n)-1):
        if(abs(int(n[i]) - int(n[i+1])) != 2):
            return False
    return True
    

t = int(input())

for _ in range(t):
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")