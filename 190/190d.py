N,M = map(int,input().split())
X = [tuple(map(int,input().split())) for i in range(M)]
K = int(input())
Y = [list(map(int,input().split())) for i in range(K)]
from itertools import combinations
for comb in combinations(Y, K):
    print(comb)
