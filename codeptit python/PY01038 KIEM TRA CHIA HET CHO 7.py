def check(n):
    cnt = 0
    found = 1
    while (n % 7 != 0 or cnt != 1000):
        if(n % 7 == 0):
            found = 1
            return n
        else:
            n += int(str(n)[::-1])
        cnt+=1
    if found == 0:
        return -1

t = int(input())
for _ in range (t):
    n = int(input())
    print(check(n))
