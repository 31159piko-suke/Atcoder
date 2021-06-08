N,M= map(int,input().split())
A = [-int(i) for i in input().split()]

from heapq import heapify, heappop, heappush

heapify(A)

for i in range(M):
    heappush(A,heappop(A)/2)

print(-sum(int(i) for i in A))