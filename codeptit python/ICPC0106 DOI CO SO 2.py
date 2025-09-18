import math

def chuyen(s):
    sum = 0
    # s = s[::-1]
    for i in range (len(s)):
        sum += int(s[i])*int(pow(2,i))
    if sum < 10:
        return str(sum)
    else:
        if (sum == 10): return 'A'
        elif (sum == 11): return 'B'
        elif (sum == 12): return 'C'
        elif (sum == 13): return 'D'
        elif (sum == 14): return 'E'
        elif (sum == 15): return 'F'
    

test = int(input())
for t in range(test):
    coso = int(input())
    s = input()
    doan = int(math.log(coso, 2))
    res = ""
    # if (len(s) % doan != 0):
    #     can = len(s) % doan
    #     for i in range (int(can)):
    #         s = '0' + s
    # print(s)
    s = s[::-1]
    for i in range(math.ceil(len(s) / doan)):
        #print(s[i*doan:i*doan+doan])
        res += chuyen(s[i*doan:i*doan+doan])
    print(res[::-1])

# 10010100010010101
# 012 345 678
# 0   1   2
# 012 012 012