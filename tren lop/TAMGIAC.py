n = int(input())
for i in range (n):
    if i == 0:
        for i in range(n-1):
            print(" ", end = "")
        print("*")
    elif i == n-1:
        for i in range(2*n- 1):
            if i % 2 == 0:
                print("*", end = "")
            else:
                print(" ", end = "")
    else:
        k1 = n-i-1
        for i in range(k1):
            print(" ", end = "")
        print("*",end ="")
        k2 = 2*n - 1 - 2*k1-2
        for i in range(k2):
            print(" ", end = "")
        print("*")

#     *
#    * *


# * * * * *

# 3 va 6
# 4 va 7
# 5 va 8