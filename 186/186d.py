# N = int(input())
# A = list(map(int,input().split()))
# import numpy as np
# l = []
# for i in range(1,N):
#     l.append(A[i]-A[0])
# result = 0
#
# for i in range(len(l)):
#     new_l = abs(np.array(l)+(A[0]-A[i]))
#     result += sum(new_l[i:])
#
#
# print(result)


# N = int(input())
# A = list(map(int,input().split()))
# import numpy as np
# A.sort()
# plus_list = list(range(N))[::-1]
# minas_list = list(range(N))
# result = np.array(A)*plus_list-np.array(A)*minas_list
# print(abs(sum(result)))


N = int(input())
A = list(map(int,input().split()))
import itertools

A = sorted(A)
ruiseki_A = ([0]+list(itertools.accumulate(A)))
result = 0
for i in range(N):
  result += A[i]*i-ruiseki_A[i]
print(result)

