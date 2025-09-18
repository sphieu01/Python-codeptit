x = input()
n = len(x) #

isused = [0]*(n+1)

def hoanvi(s, pos):
    if pos == n: 
        print(s)
        return
    for i in range (n):
        if isused[i] == 0:
            isused[i] = 1
            hoanvi(s + x[i], pos + 1)
            isused[i] = 0

hoanvi("", 0)