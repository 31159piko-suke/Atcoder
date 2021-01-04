X,N = map(int,input().split())

if N == 0:
    print(X)
    exit()

l = list(map(int,input().split()))

for i in range(60):
    X_fu = X-i
    X_sei = X+i

    if not X_fu in l:
        print(X_fu)
        exit()
    if not X_sei in l:
        print(X_sei)
        exit()