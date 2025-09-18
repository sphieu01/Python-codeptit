test = int(input())
for t in range(test):
    s = input()
    minv = 99999999999
    minso = 0

    for i in range(len(s)-1):
        if(s[i].isdigit() and s[i+1].isdigit()):
            minso *= 10
            minso += int(s[i])
        elif (s[i].isdigit() and s[i+1].isalpha()):
            minso *= 10
            minso += int(s[i])

            minv = min(minv, minso)

            #print(minv)
            minso = 0      
    print(minv)
    #print()


    
    

