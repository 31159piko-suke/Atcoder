N,S,D = map(int,input().split())
l = [list(map(int,input().split())) for i in range(N)]

for i in range(N):
    if l[i][0]<S and l[i][1]>D:
        exit(print("Yes"))
print("No")


