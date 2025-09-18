def check(s):
    s= s.lower()
    if s[-3:] != ".py" : return False
    
    for c in s:
        ok = 0
        if (c >= 'a' and c <= 'z') or c == '.' or c == '_':
            ok = 1
        if ok == 0 :
            return False
    return True

s = input()
if check(s):
    print("yes")
else:
    print("no")
