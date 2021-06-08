N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

import itertools

L = list(range(1,N+1))

p = list(itertools.permutations(L))

index_P = [i for i in range(len(p)) if p[i]==P]
index_Q = [i for i in range(len(p)) if p[i]==Q]
print(abs(index_P[0]-index_Q[0]))