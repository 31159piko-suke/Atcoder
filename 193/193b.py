N = int(input())
l = [list(map(int,input().split())) for i in range(N)]

L = []
for i in l:
    if l[i][2]-l[i][0]>=1:
        L.append(l[i][1])
print(L)
print(min(L) if len(L)>=1 else -1)