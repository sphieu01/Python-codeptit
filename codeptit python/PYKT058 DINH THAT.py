t = int(input())

for _ in range (t):
    n, canh , u , v = map(int, input().split())
    adj = []
    for i in range (n+1):
        adj.append([])

    for c in range(canh):
        temp1 , temp2 = map(int, input().split())
        adj[temp1].append(temp2)

    isused = [0]*(n+1)
    res = []
    arrres = [0]*(n+1)
    
    cnt = 0

    def dfsfindpath(start, end):
        global cnt
        isused[start] = 1 
        res.append(start)

        if start == end:
            #print(res)
            cnt = cnt + 1
            for i in res:
                arrres[i] += 1
            
        for i in adj[start]:
            if isused[i] == 0:
                dfsfindpath(i,end)
   
        res.pop()
        isused[start] = 0

    dfsfindpath(u,v)
    # print(arrres)
    cntres = 0
    for i in arrres:
        if i == cnt:
            cntres += 1
    print(cntres-2)
        

    

