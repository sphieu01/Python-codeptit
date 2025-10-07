t = int(input())

def check(n):
    n = str(n)
    if len(n) % 2 == 1:
        return False
    if (n != n[::-1]):
        return False
    # cnt0, cnt2, cnt4, cnt6, cnt8 = 0,0,0,0,0
    # for c in n:
    #     if c == '0' : cnt0 = 1
    #     elif c == '2' : cnt2 = 1
    #     elif c == '4' : cnt4 = 1
    #     elif c == '6' : cnt6 = 1
    #     elif c == '8' : cnt8 = 1
    #     else:
    #         return False
        
    # cnt = cnt0+ cnt2+ cnt4+ cnt6+ cnt8
    # return cnt % 2 == 1
    for c in n:
        if c != '2' and c != '4' and c != '6' and c != '8' and c != '0':
            return False
    return True

for _ in range(t):
    k = int(input())
    for i in range (k):
        if check(i):
            print(i, end = " ")
    print()
    
    