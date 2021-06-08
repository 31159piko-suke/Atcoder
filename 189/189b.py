N,X = map(int,input().split())
l = [list(map(int,input().split())) for i in range(N)]

count = 0
for i in l:
    if i[1]!=0:
        count += 1
    X -= i[0]*(i[1]/100)
    if X<0:
        exit(print(count))
print(-1)