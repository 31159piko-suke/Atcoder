H,W = map(int,input().split())
l = [list(map(int, input().split())) for _ in range(H)]

import collections
import itertools


l_ = list(itertools.chain.from_iterable(l))


result = 0
for i in range(H):
    for j in range(W):
        result += l[i][j]-min(l_)

print(result)
