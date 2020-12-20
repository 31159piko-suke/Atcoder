N,M,K = map(int,input().split())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))

import numpy as np
import itertools
import bisect

A = [0]+list(itertools.accumulate(A_list))
B = [0]+list(itertools.accumulate(B_list))

result = [0]
for i in range(N+1):
    index = bisect.bisect_right(B, K-A[i])-1

    if index>=0:
        result.append(i+index)

print(max(result))
