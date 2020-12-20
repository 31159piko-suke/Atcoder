N = int(input())
l = list(map(int, input().split()))

import collections
import itertools

def insuubunnkai(n):#因数分解したリストを返す関数
    b = 2
    fct = []
    while b*b<n:
        while n%b==0:
            n //= b
            fct.append(b)
        b += 1

    if n != 1:
        fct.append(n)

    return fct

list_a = []
for i in range(N):
    a = list(set(insuubunnkai(l[i])))
    list_a.append(a)

list_a = list(itertools.chain.from_iterable(list_a))

c = collections.Counter(list_a)
print(c.most_common()[0][0])
