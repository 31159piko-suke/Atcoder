N = int(input())
s = input()


l = []
for i in range(N):
    l.append(s[i])
    a = "".join(l)

    if len(a)>=3 and a[-3:]=="fox":
        l.pop()
        l.pop()
        l.pop()
print(len(l))