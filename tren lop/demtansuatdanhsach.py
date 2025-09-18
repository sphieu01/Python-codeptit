arr = input().split()

thisdict = {}

for i in arr:
    try:
        thisdict[i] += (1)
    except:
        thisdict[i] = 1
for x,y in thisdict.items():
    print (x , y)
