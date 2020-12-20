N = int(input())
l = list(map(int,input().split()))

import itertools

l_sum = list(itertools.accumulate(l))

ans = 0
for i in range(1,len(l)):
    ans += l_sum[i-1]*l[i]

print(ans%(10**9+7))

# print(list(itertools.accumulate(l)))
