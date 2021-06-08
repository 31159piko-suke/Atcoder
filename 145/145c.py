import itertools

N = int(input())
l = [list(map(int,input().split())) for i in range(N)]

L = list(range(N))

p = list(itertools.permutations(L))
sum_ = 0
for i in p:
    keiro = 0
    for j in range(N-1):
        x_1 = l[i[j]][0]
        y_1 = l[i[j]][1]
        x_2 = l[i[j+1]][0]
        y_2 = l[i[j+1]][1]

        s = ((x_1-x_2)**2 + (y_1-y_2)**2)**0.5
        keiro += s
    sum_ += keiro
print(sum_/len(p))