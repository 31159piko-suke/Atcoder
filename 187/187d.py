N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

import numpy as np
A = np.sum(l,axis=0)[0]
B = np.sum(l,axis=0)[1]

a = []
for i in range(N):
    a.append(l[i][0])

yoko = np.sum(l,axis=1)

tokushitu = yoko + a
tokushitu = sorted(tokushitu,reverse=True)

count = 0
tokusitu_ = A
for i in range(N):
    tokusitu_ -= tokushitu[i]
    count += 1
    if tokusitu_<0:
        print(count)
        break
