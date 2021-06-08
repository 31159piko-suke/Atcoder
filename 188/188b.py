N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

import numpy as np

C = np.dot(A,B)
if not C:
    print("Yes")
else:
    print("No")