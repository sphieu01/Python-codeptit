# isused = [int(0)] * 25
arrres = [int(0)] * 25

inp = input().split()
n = int(inp[0])
k = int(inp[1])

def inkq():
    for i in range (1,k+1):
        print(arr[int(arrres[i])], "",end = "")
    print()

def tohop(pos):

    for i in range(arrres[pos-1]+ 1, n + k - pos + 1):
        arrres[pos] = i 
        if (pos == k): inkq()
        else: tohop(pos + 1)

arrtemp = input().split()
arr = []
for j in arrtemp:
    if int(j) not in arr:
        arr.append(int(j))

n = len(arr)
arr.sort() 
arr = [0] + arr
#print(arr)
tohop(int(1))




