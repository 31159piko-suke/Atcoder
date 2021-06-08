X = input()
M = int(input())

d = int(max(X))

if len(X)==1:
    if int(X)<=M:
        print(1)
        exit()
    else:
        print(0)
        exit()


def summan(X,n):
    num = 0
    for i in range(len(X)):
        num += int(X[i])*(n**i)
    return num

X = X[::-1]
count = 0
while True:
    a = summan(X, d+1)
    if a>M:
        break
    count += 1
    d += 1

print(count)