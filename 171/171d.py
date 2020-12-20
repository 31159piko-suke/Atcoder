N = int(input())
A = list(map(int,input().split()))
Q = int(input())
l = [list(map(int,input().split())) for i in range(Q)]

import numpy as np

num = np.zeros(10**5+10000)
sum_ = 0

for i in range(len(A)):
    num[A[i]] += 1
    sum_ += A[i]

for i in range(len(l)):
    sum_ += (l[i][1]-l[i][0])*num[l[i][0]]
    tem = num[l[i][0]]
    num[l[i][1]] +=  tem
    num[l[i][0]] = 0

    print(int(sum_))
