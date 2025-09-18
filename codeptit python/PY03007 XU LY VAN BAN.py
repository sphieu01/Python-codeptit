import re

s = ""
regex = r'[\w\s,:]+'

while True:
    try: s += input()
    except EOFError: break
s = re.findall(regex, s) # mang

for cau in s: # cau la string cau
    cau = cau.lower()
    cau = cau.split() # cau la mang 
    for j in range(len(cau)):
        if j == 0:
            print(cau[j][0].upper(), end = "")
            print(cau[j][1:], end = " ")
        else:
            print(cau[j], end = " ")
    print() 
    

    
