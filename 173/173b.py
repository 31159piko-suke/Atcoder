N = int(input())
l = [input() for _ in range(N)]


AC = 0
WA = 0
TLE = 0
RE = 0
for i in l:
    if i == "AC":
        AC += 1
    elif i == "WA":
        WA += 1
    elif i == "TLE":
        TLE += 1
    else:
        RE += 1

print("AC x "+str(AC))
print("WA x "+str(WA))
print("TLE x "+str(TLE))
print("RE x "+str(RE))
