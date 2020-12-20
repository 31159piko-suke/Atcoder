N,K = list(map(int,input().split()))

import itertools

l = [list(map(int, input().split())) for _ in range(N)]

nums = list(range(2,N+1))

flug = 0
for root in itertools.permutations(nums):
    root = list(root)
    root.insert(0, 1)#前後に1挿入する
    root.insert(len(root), 1)
    sum_ = 0
    for j in range(N):
        x,y = root[j],root[j+1]
        sum_ += l[x-1][y-1]
    if sum_ == K:
        flug += 1
print(flug)
