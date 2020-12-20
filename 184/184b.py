N,X = map(int,input().split())
S = input()


for i in S:
    if i == "o":
        X += 1
    else:
        X -= 1
        if X<0:
            X = 0
print(X)
