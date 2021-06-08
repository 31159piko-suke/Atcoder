N = int(input())
s = input()
 
 
l = []
for i in range(N):
    l.append(s[i])
    if "".join(l[-3:]) == "fox":
        l.pop()
        l.pop()
        l.pop()
print(len(l))