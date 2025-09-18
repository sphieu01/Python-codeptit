m = int(input())
n = int(input())
h = int((n-m)/2 + 1)

for i in range (h):
    if i == 0:
        k = int((n-m)/2)
        print("  "*k + "* "*m)
    elif i == h-1:
        print("* " * n)
    else:
        k = int((n-m)/2- i)
        print("  "*k + "* " + "  "*int(n-2*k-2) + "* ")

