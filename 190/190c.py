N,M = map(int,input().split())
X = [tuple(map(int,input().split())) for i in range(M)]
K = int(input())
Y = [list(map(int,input().split())) for i in range(K)]

import itertools
import collections

x = set(X)
a = list(itertools.chain.from_iterable(x))
c = collections.Counter(a)
print(x)
print(a)

values, counts = zip(*c.most_common())
values = list(values)
print(values)

s = set()
for i in range(K):
    if values.index(Y[i][0]) > values.index(Y[i][1]):
        if not Y[i][1] in s:
            s.add(Y[i][1])
        else:
            s.add(Y[i][0])

    else :
        if not Y[i][0] in s:
            s.add(Y[i][0])
        else:
            s.add(Y[i][1])

count = 0
for i in range(M):
    if set(X[i]) <= s:
        count += 1
print(count)
print(s)