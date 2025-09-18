d = int(input())
r = int(input())

for i in range(r):
    if i == 0 or i == r-1:
        for j in range(d):
            print("*", end = "")
    else : 
        print("*", end = "")
        for j in range(1,d-1):
            print(" ", end = "")
        print("*", end = "")
    print()