X,K,D = map(int,input().split())

X = abs(X)
S = X//D

if K>S:
    Y = X-S*D
    if (K-S)%2==0:
        print(Y)
    else:
        print(D-Y)
else:
    Y = X-K*D
    print(Y)
