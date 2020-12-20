N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

flug = 0
for i in range(N):
    for j in range(i):
        for k in range(j):
            x1,y1 = l[i]
            x2,y2 = l[j]
            x3,y3 = l[k]

            x1 -= x3
            x2 -= x3
            y1 -= y3
            y2 -= y3

            if y1*x2 == y2*x1:
                flug = 1
if flug:
    print("Yes")
else:
    print("No")
