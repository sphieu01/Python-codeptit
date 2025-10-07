m = {1 : 1}

while True :
    ok = 0
    a = []
    for i in m :
        for v in [2,3,5]:
            mul = i*v
            if mul <= 10**18 and mul not in m:
                a.append(mul)
    
    for i in a :
        ok = 1
        m[i] = 1

    if ok == 0 : break

# print(m)

p = 1
a = sorted(list(m))
for i in a :
    m[i] = p
    p += 1

t = int(input())
for i in range(t) :
    n = int(input())
    if n in m : print(m[n])
    else : print("Not in sequence")