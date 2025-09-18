t = int(input())

myset = {""}
myset.remove("")

for _ in range (t):
    s = input()
    myset.add(s)

print(len(myset))