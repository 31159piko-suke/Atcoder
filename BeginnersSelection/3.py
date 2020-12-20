N = int(input())
l = list(map(int,input().split()))

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

import collections

num_list = []
for i in range(N):
    num_list.append(collections.Counter(insuubunnkai(l[i]))[2])
print(min(num_list))
