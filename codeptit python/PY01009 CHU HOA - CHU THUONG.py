s = input()
cntupper = 0
cntlower = 0
for c in s:
    if c.isupper(): cntupper += 1
    else: cntlower += 1
if (cntupper <= cntlower):
    s = s.lower()
else: s = s.upper()
print(s)