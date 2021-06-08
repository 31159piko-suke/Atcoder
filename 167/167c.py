N,M,X = map(int,input().split())
l = [list(map(int,input().split())) for i in range(N)]


money_list = []
for i in range(2**N):
    money = 0
    A = [-X]*M

    for j in range(N):
        if (i>>j) & 1:
            A = [A[k] + l[j][1:][k] for k in range(M)]
            money += l[j][0]

    result = all([a>=0 for a in A])
    if result:
        money_list.append(money)

print(min(money_list) if money_list else -1)


