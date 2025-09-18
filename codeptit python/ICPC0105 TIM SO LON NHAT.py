test = int(input())
for t in range(test):
    s = input()
    maxmax = -99999
    maxso = 0

    for i in range(len(s)):
        if (i == len(s)-1 and s[i].isdigit()):
            maxso *= 10
            maxso += int(s[i])
            maxmax = max(maxmax, maxso)
            maxso = 0 
        elif(s[i].isdigit() and s[i+1].isdigit()):
            maxso *= 10
            maxso += int(s[i])
        elif (s[i].isdigit() and not(s[i+1].isdigit())):
            maxso *= 10
            maxso += int(s[i])
            maxmax = max(maxmax, maxso)
            maxso = 0   
        
        
        #print(maxso)
    maxmax = max(maxmax, maxso)
    print(maxmax)
    #print()


    
    

