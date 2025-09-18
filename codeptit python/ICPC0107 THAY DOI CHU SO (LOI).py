test = int(input())
for t in range(test):
    inp = input().split()
    a = inp[0]
    b = inp[1]
    maxv = str(max(int(a),int(b)))
    minv = str(min(int(a),int(b)))
    # x = input()
    # y = input()

    x = input().strip()
    if(x.count(' ')) : 
        x, y = x.split()
    else : y = input()

    print(int(x.replace(maxv, minv)) + int(y.replace(maxv, minv)), end = " ")
    print(int(x.replace(minv, maxv)) + int(y.replace(minv, maxv)))