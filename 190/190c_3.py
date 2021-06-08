N,M = map(int,input().split())
X = [tuple(map(int,input().split())) for i in range(M)]
K = int(input())
Y = [list(map(int,input().split())) for i in range(K)]

result = 0
for i in range(2**K):
    d = []
    for j in range(K):
        if (i>>j)&1:
            d.append(Y[j][0])
        else:
            d.append(Y[j][1])
    
    result = max(sum([1 for k in range(M) if set(X[k])<=set(d)]),result)
    # ans = 0
    # for k in range(M):
    #     if X[k][0] in d and X[k][1] in d:
    #         ans += 1
    # result = max(result,ans)

print(result)