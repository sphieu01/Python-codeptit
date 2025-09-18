def check(i):
    i = str(i)
    for c in i:
        if int(c) % 2 != 0:
            return False
    return True


t = int(input())
for _ in range (t):
    n = int(input())
    for i in range (2,1000,2):
        if (check(i)):
            s = int(str(i) + str(i)[::-1])
            if (s >= n): break   
            print(s, end = " ")

        
    print()
        
    